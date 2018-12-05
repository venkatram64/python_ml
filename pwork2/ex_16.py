import quandl
import pandas as pd
import datetime
import matplotlib.pyplot as plt
from matplotlib import style
style.use('ggplot')

api_key = "*********"

def fetch_initial_state_data():

    query = "FMAC/HPI_TX"
    df = quandl.get(query, authtoken=api_key)
    df.to_pickle('hpi_data.tx.pickle')


def load_serialied_data():
    fig = plt.figure()
    ax1 = plt.subplot2grid((1, 1), (0, 0))
    pickle_data = pd.read_pickle('hpi_data.tx.pickle')
    tx_one_year = pickle_data.resample('A').mean()
    tx_one_year.plot(ax=ax1, label='Monthly TX HPI')
    plt.show()

if __name__ == '__main__':
    fetch_initial_state_data()
    load_serialied_data()


