"""
http://nbviewer.jupyter.org/github/whitehorn/Scientific_graphics_in_python/blob/master/P1%20Chapter%201%20Pyplot.ipynb
"""
import matplotlib.pyplot as plt
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg  # Рисует график на виджете tkinter
from matplotlib.backends.backend_tkagg import NavigationToolbar2TkAgg  # Добавляет кнопки управления для canvas
from tkinter import *
import bd_sqlite
import scraper


def select_prices():
    """get list of prices"""
    prices_bd = bd_sqlite.select_from_bd_column('price')
    prices = [item for sublist in prices_bd for item in sublist]
    return prices


# def filter_prices(prices):
#    """filters prices for standard deviation"""
#    filter_list = []
#    # mean_price = mean(prices)
#    std_price = std(prices)
#    for e, price in enumerate(prices, -1):
#        if price <= std_price:
#            filter_list.append(price)
#        else:
#            if price <= prices[e] + std_price:
#                filter_list.append(price)
#    # filter_list = [price for price in prices if price < (mean_price+std_price)]
#    return filter_list


def calculate_statistics(list_prices):
    """dict: key - price, value - number of ads with this price"""
    price_count = {}
    for price in list_prices:
        if price in price_count:
            price_count[price] += 1
        else:
            price_count[price] = 1
    return price_count


# def filter_statistics(statistics):
#    """filter by values less than 1%"""
#    value = list(statistics.values())
#    threshold = max(value) // 10  # 10%
#    price_count_filter = {price: count for price, count in statistics.items() if count > threshold}
#    return price_count_filter


def plotting(window, id_table):
    """plotting bar"""
    table_name = 'table{}'.format(id_table)
    prices_from_bd = bd_sqlite.select_from_parsing_table_column('price', table_name)
    prices = [item for sublist in prices_from_bd for item in sublist]
    print(prices)
    price_count = calculate_statistics(prices)
    print(price_count)
    x = list(price_count.keys())
    y = list(price_count.values())
    width_bar = len(x) * 2

    # bar
    fig = plt.figure()
    ax = fig.add_subplot(111)
    ax.bar(x, y, width=width_bar)
    # ax.set_title('Распределение цены')
    ax.set_xlabel('Price, UAH')
    ax.set_ylabel('Number of offers')

    # tk.DrawingArea
    canvas = FigureCanvasTkAgg(fig, master=window)
    canvas.show()
    canvas.get_tk_widget().pack()

    # adds control buttons for canvas
    # toolbar = NavigationToolbar2TkAgg(canvas, window)
    # toolbar.update()
    # canvas._tkcanvas.pack()
