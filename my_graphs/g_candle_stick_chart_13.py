import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import matplotlib.ticker as mticker
from mpl_finance import candlestick_ohlc
import numpy as np
import urllib
from matplotlib import style

#style.use('ggplot')
style.use('fivethirtyeight')

"""
print(plt.__file__)
print(plt.style.available)  # which gives all the available styles
'bmh', 'classic', 'dark_background', 'fast', 'fivethirtyeight', 'ggplot', 
'grayscale', 'seaborn-bright', 'seaborn-colorblind', 'seaborn-dark-palette', 
'seaborn-dark', 'seaborn-darkgrid', 'seaborn-deep', 'seaborn-muted', 'seaborn-notebook', 
'seaborn-paper', 'seaborn-pastel', 'seaborn-poster', 'seaborn-talk', 'seaborn-ticks', 
'seaborn-white', 'seaborn-whitegrid', 'seaborn', 'Solarize_Light2', 
'tableau-colorblind10', '_classic_test'
"""
def bytespdate2num(fmt, encoding='utf-8'):
    str_converter = mdates.strpdate2num(fmt)
    def bytesconverter(b):
        s = b.decode(encoding)
        return str_converter(s)
    return bytesconverter


def graph_data(stock):
    fig = plt.figure()
    ax1 = plt.subplot2grid((1, 1), (0, 0))
    stock_price_url = 'https://pythonprogramming.net/yahoo_finance_replacement'
    source_code = urllib.request.urlopen(stock_price_url).read().decode()

    stock_data = []
    split_source = source_code.split('\n')

    for line in split_source:
        split_source = line.split(',')
        if len(split_source) == 7:
            if 'Date' not in line and 'Volume' not in line:
                stock_data.append(line)

    # %Y full year
    # %y partial year
    # %m number month
    # %d number day
    # %H hours
    # %M minutes
    # %S seconds
    date, openp, closep, lowp, highp, adjusted_close, volume = np.loadtxt(stock_data,
                                                                          delimiter=',',
                                                                          unpack=True,
                                                                          converters={0: bytespdate2num('%Y-%m-%d')}
                                                                          )

    x = 0
    y = len(date)
    ohlc = []
    while x < y:
        if x == 80:
            break
        append_me = date[x], openp[x], highp[x], lowp[x], closep[x], volume[x]
        ohlc.append(append_me)
        x += 1
    candlestick_ohlc(ax1, ohlc, width=0.4, colorup='g', colordown='r')

    for label in ax1.xaxis.get_ticklabels():
        label.set_rotation(45)

    ax1.xaxis.set_major_formatter(mdates.DateFormatter('%Y-%m-%d'))
    ax1.xaxis.set_major_locator(mticker.MaxNLocator(10))
    ax1.grid(True)
    ax1.annotate('Bad News!', (date[12], highp[13]),
                 xytext=(0.5, 0.4), textcoords='axes fraction',
                 arrowprops=dict(facecolor='red', color='red'))

    font_dict = {'family': 'serif', 'color': 'darkred', 'size': 12}
    ax1.text(date[10], closep[10], "Start Price", fontdict=font_dict)
    plt.xlabel('Date')
    plt.ylabel('Price')
    plt.title('Interesting Graph\nCheck it out')
    #plt.legend()
    plt.subplots_adjust(left=0.09, bottom=0.20, right=0.94, top=0.90, wspace=0.2, hspace=0)
    plt.show()


if __name__ == '__main__':
    graph_data('TSLA')

