import quandl
import pandas as pd
import datetime
import matplotlib.pyplot as plt
from matplotlib import style
style.use('ggplot')

api_key = open('quandl_key.txt', 'r').read()

def state_list():
    states = pd.read_html('https://simple.wikipedia.org/wiki/List_of_U.S._states')
    return states[0][1][1:]

def fetch_initial_state_data():
    main_df = pd.DataFrame()
    states = state_list()

    for abbrv in states:
        query = "FMAC/HPI_" + str(abbrv)
        #print("*******************  " + query)
        df = quandl.get(query, authtoken=api_key)
        df['NSA Value'] = (df['NSA Value'] - df['NSA Value'][0]) / df['NSA Value'][0] * 100.0
        if main_df.empty:
            main_df = df
        else:
            main_df = main_df.join(df, lsuffix='_left', rsuffix='_right')
    """
        Serializing the data
    """
    main_df.to_pickle('hpi_data2.pickle')


def load_serialied_data():
    pickle_data = pd.read_pickle('hpi_data2.pickle')
    #print(pickle_data.head())
    pickle_data.plot()
    plt.legend().remove()
    plt.show()

def mortgage_30y():
    df = quandl.get('FMAC/MORTG', trim_start='1975-01-01', authtoken=api_key)
    df['Value'] = (df['Value'] - df['Value'][0]) / df['Value'][0] * 100.0
    df = df.resample('D').fillna(method='ffill')
    df = df.resample('M').fillna(method='ffill')
    df.columns = ['M30']
    return df

def sp500_data():
    df = quandl.get('YAHOO/INDEX_GSPC', trim_start='1975-01-01', authtoken=api_key)
    df['Adjusted Close'] = (df['Adjusted Close'] - df['Adjusted Close'][0]) / df['Adjusted Close'][0] * 100.0
    df = df.resample('M')
    df.rename(columns={'Adjusted Close': 'sp500'}, inplce=True)
    df = df['sp500']
    return df

def gdp_data():
    df = quandl.get('BCB/4305', trim_start='1975-01-01', authtoken=api_key)
    df['Value'] = (df['Value'] - df['Value'][0]) / df['Value'][0] * 100.0
    df = df.resample('M')
    df.rename(columns={'Value': 'GDP'}, inplce=True)
    df = df['GDP']
    return df

def un_employment():
    df = quandl.get('ECPI/JOB_G', trim_start='1975-01-01', authtoken=api_key)
    df['Unemployment Rate'] = (df['Unemployment Rate'] - df['Unemployment Rate'][0]) / df['Unemployment Rate'][0] * 100.0
    df = df.resample('1D')
    df = df.resample('M')
    return df


def load_serialied_data():
    pickle_data = pd.read_pickle('hpi_data2.pickle')
    #print(pickle_data.head())
    pickle_data.plot()
    plt.legend().remove()
    plt.show()

if __name__ == '__main__':
    m30y = mortgage_30y()
    pickle_data = pd.read_pickle('hpi_data2.pickle')
    #sp500 = sp500_data()
    #US_GDP = gdp_data()
    #US_Unemployment = un_employment()
    HPI = pickle_data.join(m30y)
    print(HPI)


