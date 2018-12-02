import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import matplotlib.ticker as mticker
from mpl_finance import candlestick_ohlc
import numpy as np
import urllib
from matplotlib import style


style.use('classic')

MA1 = 10
MA2 = 30

def moving_average(values, window):
    weights = np.repeat(1.0, window)/window
    smas = np.convolve(values, weights, 'valid')
    return smas

def high_minus_low(highs, lows):
    return highs - lows


def bytespdate2num(fmt, encoding='utf-8'):
    str_converter = mdates.strpdate2num(fmt)
    def bytesconverter(b):
        s = b.decode(encoding)
        return str_converter(s)
    return bytesconverter


def graph_data(stock):
    fig = plt.figure()
    ax1 = plt.subplot2grid((6, 1), (0, 0), rowspan=1, colspan=1)
    plt.title(stock)
    plt.ylabel('H-L')

    ax2 = plt.subplot2grid((6, 1), (1, 0), rowspan=4, colspan=1, sharex=ax1)
    #plt.xlabel('Date')
    plt.ylabel('Price')
    ax2v = ax2.twinx()

    ax3 = plt.subplot2grid((6, 1), (5, 0), rowspan=1, colspan=1, sharex=ax1)
    plt.ylabel("MA")

    stock_price_url = 'https://pythonprogramming.net/yahoo_finance_replacement'
    source_code = urllib.request.urlopen(stock_price_url).read().decode()

    stock_data = []
    split_source = source_code.split('\n')

    for line in split_source:
        split_source = line.split(',')
        if len(split_source) == 7:
            if 'Date' not in line and 'Volume' not in line:
                stock_data.append(line)


    date, openp, closep, lowp, highp, adjusted_close, volume = np.loadtxt(stock_data,
                                                                          delimiter=',',
                                                                          unpack=True,
                                                                          converters={0: bytespdate2num('%Y-%m-%d')}
                                                                          )

    x = 0
    y = len(date)
    ohlc = []
    while x < y:
        """if x == 600:
            break"""
        append_me = date[x], openp[x], highp[x], lowp[x], closep[x], volume[x]
        ohlc.append(append_me)
        x += 1

    ma1 = moving_average(closep, MA1)
    ma2 = moving_average(closep, MA2)
    start = len(date[MA2-1:])
    h_l = list(map(high_minus_low, highp, lowp))
    ax1.plot_date(date[-start:], h_l[-start:], '-')
    ax1.yaxis.set_major_locator(mticker.MaxNLocator(nbins=4, prune='lower'))

    candlestick_ohlc(ax2, ohlc[-start:], width=0.4, colorup='g', colordown='r')

    ax2.yaxis.set_major_locator(mticker.MaxNLocator(nbins=4, prune='upper'))
    ax2.grid(True)
    bbox_props=dict(boxstyle='round', fc='w', ec='k', lw=1)
    ax2.annotate(str(closep[-1]), (date[-1], closep[-1]),
                 xytext=(date[-1]+4, closep[-1]), bbox=bbox_props)

    ax2v.fill_between(date[-start:], 0, volume[-start:], facecolor='b', alpha=0.4)
    ax2v.axes.yaxis.set_ticklabels([])
    ax2v.grid(False)
    ax2v.set_ylim(0, 3*volume.max())

    ax3.plot(date[-start:], ma1[-start:], linewidth=1)
    ax3.plot(date[-start:], ma2[-start:], linewidth=1)
    ax3.fill_between(date[-start:], ma2[-start:], ma1[-start:],
                     where=(ma1[-start:] < ma2[-start:]),
                     facecolor='r', edgecolor='r', alpha=0.5)

    ax3.fill_between(date[-start:], ma2[-start:], ma1[-start:],
                     where=(ma1[-start:] > ma2[-start:]),
                     facecolor='g', edgecolor='g', alpha=0.5)
    ax3.xaxis.set_major_formatter(mdates.DateFormatter('%Y-%m-%d'))
    ax3.xaxis.set_major_locator(mticker.MaxNLocator(10))
    ax3.yaxis.set_major_locator(mticker.MaxNLocator(nbins=4, prune='upper'))

    for label in ax3.xaxis.get_ticklabels():
        label.set_rotation(45)

    #plt.step(ax1.get_xticklabels(), visible=False)
    #plt.step(ax2.get_xticklabels(), visible=False)
    plt.subplots_adjust(left=0.12, bottom=0.30, right=0.90, top=0.80, wspace=0.2, hspace=0)
    plt.show()



if __name__ == '__main__':
    graph_data('TSLA')

