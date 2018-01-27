"""
http://nbviewer.jupyter.org/github/whitehorn/Scientific_graphics_in_python/blob/master/P1%20Chapter%201%20Pyplot.ipynb
"""
import matplotlib.pyplot as plt
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg  # Рисует график на виджете tkinter
from matplotlib.backends.backend_tkagg import NavigationToolbar2TkAgg  # Добавляет кнопки управления для canvas
from tkinter import *
import main


def plotting(root):
    """plotting bar"""
    prices = main.select_prices()
    # filter_std = main.filter_prices(prices)
    price_count = main.calculate_statistics(prices)
    price_count_filter = main.filter_statistics(price_count)
    x = list(price_count_filter.keys())
    y = list(price_count_filter.values())
    width_bar = len(x) * 2

    # bar
    fig = plt.figure()
    ax = fig.add_subplot(111)
    ax.bar(x, y, width=width_bar)
    # ax.set_title('Распределение цены')
    ax.set_xlabel('Price, UAH')
    ax.set_ylabel('Number of offers')

    # tk.DrawingArea
    canvas = FigureCanvasTkAgg(fig, master=root)
    canvas.show()
    canvas.get_tk_widget().pack()

    # adds control buttons for canvas
    toolbar = NavigationToolbar2TkAgg(canvas, root)
    toolbar.update()
    canvas._tkcanvas.pack()