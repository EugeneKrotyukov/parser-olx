"""
http://nbviewer.jupyter.org/github/whitehorn/Scientific_graphics_in_python/blob/master/P1%20Chapter%201%20Pyplot.ipynb
"""
import matplotlib.pyplot as plt
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg  # Рисует график на виджете tkinter
# from matplotlib.backends.backend_tkagg import NavigationToolbar2TkAgg  # Добавляет кнопки управления для canvas
import bd_sqlite


def set_fig(frame, widget):
    """set frame and figure for GUI"""
    global window, fig
    window = frame
    fig = widget


def calculate_statistics(list_prices):
    """dict: key - price, value - number of ads with this price"""
    price_count = {}
    for price in list_prices:
        if price in price_count:
            price_count[price] += 1
        else:
            price_count[price] = 1
    return price_count


def plotting(window, id_table):
    """plotting bar"""
    table_name = 'table{}'.format(id_table)
    prices = bd_sqlite.select_from_parsing_table_column('price', table_name)
    price_count = calculate_statistics(prices)
    x = list(price_count.keys())
    y = list(price_count.values())
    width_bar = len(x) * 2

    # bar
    # fig = plt.figure()
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
