import quandl
import pandas as pd
import datetime
import matplotlib.pyplot as plt
from matplotlib import style
style.use('ggplot')

api_key = "*******"

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

    #print(main_df.head())
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

if __name__ == '__main__':
    #fetch_initial_state_data()
    load_serialied_data()


