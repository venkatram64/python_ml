import quandl
import pandas as pd
import datetime
import matplotlib.pyplot as plt
from matplotlib import style
style.use('ggplot')

api_key = "**********"

def fetch_initial_state_data():

    query = "FMAC/HPI_TX"
    df = quandl.get(query, authtoken=api_key)
    df.to_pickle('hpi_data.tx.pickle')


def load_serialied_data():
    fig = plt.figure()
    ax1 = plt.subplot2grid((2, 1), (0, 0))
    ax2 = plt.subplot2grid((2, 1), (1, 0), sharex=ax1)
    pickle_data = pd.read_pickle('hpi_data.tx.pickle')
    tx_mean_year = pickle_data.rolling(window=12, min_periods=1).mean()
    tx_mean_year.plot(ax=ax1, label='Monthly TX HPI Mean')
    tx_std_year = pickle_data.rolling(window=12, min_periods=1).std()
    tx_std_year.plot(ax=ax2, label='Monthly TX HPI Std')
    plt.show()

if __name__ == '__main__':
    fetch_initial_state_data()
    load_serialied_data()


