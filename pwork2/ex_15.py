import quandl
import pandas as pd
import datetime
import matplotlib.pyplot as plt
from matplotlib import style
style.use('ggplot')

api_key = "*********"

def hpi_bench_mark():
    df = quandl.get('FMAC/HPI_USA', authtoken=api_key)
    #print(df)
    df['NSA Value'] = (df['NSA Value'] - df['NSA Value'][0])/df['NSA Value'][0] * 100.0
    return df

def plot_graph():
    fig = plt.figure()
    ax1 = plt.subplot2grid((1, 1), (0, 0))
    pickle_data_all = pd.read_pickle('hpi_data2.pickle')
    pickle_data_all.plot(ax=ax1)
    pickle_data = hpi_bench_mark()
    pickle_data.plot(ax=ax1, color='k', linewidth=5)
    plt.legend().remove()
    plt.show()

def correlation_data():
    pickle_data_all = pd.read_pickle('hpi_data2.pickle')
    pickle_data_all_correlation = pickle_data_all.corr()
    #print(pickle_data_all_correlation)
    print(pickle_data_all.describe())


if __name__ == '__main__':
    #hpi_bench_mark()
    #plot_graph()
    correlation_data()


