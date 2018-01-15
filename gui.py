"""
https://ru.wikibooks.org/wiki/GUI_Help/Tkinter_book
https://metanit.com/python/tutorial/9.1.php
https://ru.wikiversity.org/wiki/%D0%9A%D1%83%D1%80%D1%81_%D0%BF%D0%BE_%D0%B1%D0%B8%D0%B1%D0%BB%D0%B8%D0%BE%D1%82%D0%B5%D0%BA%D0%B5_Tkinter_%D1%8F%D0%B7%D1%8B%D0%BA%D0%B0_Python
"""
from tkinter import *
import tkinter.ttk as ttk
import main


def get_url_button():
    """button START click"""
    global pb
    start_button['state'] = 'disabled'
    url = url_entry.get()
    number_page = number_page_entry.get()
    pb.grid(row=3, column=0, columnspan=2, sticky="w", padx=10, pady=10)
    main.get_list_product(url, number_page)
    start_button['state'] = 'normal'
    pb.grid_remove()


def get_url_entry(event):
    """enter click"""
    get_url_button()


def get_statistics():
    """plotting"""
    WIDTH = 800
    HEIGHT = 550
    prices = main.select_prices()
    max_price = prices[-1]
    min_price = prices[0]
    # number_ads = len(prices)
    # number_ads_label = Label(frame2, text='Processed ads {}'.format(number_ads), font='16').pack()
    # min_price_label = Label(frame2, text='Minimum price {}'.format(min_price), font='16').pack()
    # max_price_label = Label(frame2, text='Maximum price {}'.format(max_price), font='16').pack()

    number_of_offers = main.calculate_statistics(prices)
    sort_numbers = sorted(number_of_offers.values())
    max_number = sort_numbers[-1]
    min_number = sort_numbers[0]

    x_start, y_end = 50, 50
    x_end = WIDTH - x_start  # 750
    y_start = HEIGHT - y_end  # 550
    long_x = x_end - x_start  # 700
    long_y = y_start - y_end  # 500
    scale_x = round(long_x / max_price, 1)
    scale_y = round(long_y / max_number, 1)
    step_x = int((max_price - min_price) / 10)
    if step_x < 1:
        step_x = 1
    step_y = int((max_number - min_number) / 10)
    if step_y < 1:
        step_y = 1

    canvas = Canvas(frame2, width=WIDTH, height=HEIGHT, bg="white")
    # grid of coordinates
    canvas.create_line(x_start, y_start, x_end+(step_x*scale_x//2), y_start, width=2, arrow=LAST)
    canvas.create_line(x_start, y_start, x_start, y_end-(step_y*scale_y//2), width=2, arrow=LAST)
    for x in range(min_price, max_price, step_x):
        canvas.create_text(x*scale_x+10, y_start+10, text=x)
    for y in range(min_number, max_number+step_y, step_y):
        canvas.create_text(x_start-20, y_start - y*scale_y, text=y)
    # output values
    for key, value in number_of_offers.items():
        # print(key, value, key*scale_x, value*scale_y)
        canvas.create_line(key*scale_x, y_start, key*scale_x, value*scale_y, width=1)
    canvas.pack()


root = Tk()
root.title('Scrape olx.ua')
root.geometry('800x600')

nb = ttk.Notebook(root)
nb.pack()

frame1 = Frame(root)
frame2 = Frame(root)
frame3 = Frame(root)
frame4 = Frame(root)

nb.add(frame1, text='Start')
nb.add(frame2, text='Statistics')
nb.add(frame3, text='New ads')
nb.add(frame4, text='Discounts')

# Frame 1
url_label = Label(frame1, text='Enter URL', font='16')
url_entry = Entry(frame1, width=50, font='14')
url_entry.focus()
url_entry.bind('<Return>', get_url_entry)
number_page_label = Label(frame1, text='Enter the number of pages', font='16')
number_page_entry = Entry(frame1, width=10, font='14')
number_page_entry.insert(0, '1')
number_page_entry.bind('<Return>', get_url_entry)
start_button = Button(frame1, text="Start", command=get_url_button, font='16')
pb = ttk.Progressbar(frame1, orient=HORIZONTAL, length=780, mode='determinate')

main.set_pb(pb, root)

# use grid()
url_label.grid(row=0, column=0, sticky="w", padx=10, pady=10)
url_entry.grid(row=0, column=1, sticky="w") # columnspan=2
number_page_label.grid(row=1, column=0, sticky="w", padx=10, pady=10)
number_page_entry.grid(row=1, column=1, sticky="w")
start_button.grid(row=2, column=1, sticky="w")


# Frame 2
statistic_button = Button(frame2, text="Statistics", command=get_statistics, font='16')
statistic_button.pack()



'''

h = 30
w = 90
padx = 15
pady = 15
start_x = 15
start_y = 15
url_label.place(height=h, width=w, x=start_x, y=start_y) # relx=0.01
url_entry.place(height=h, relwidth=0.8, relx=0.15, y=start_y, anchor='nw') # width=w*7  x=start_x+w+padx
number_page_label.place(height=h, width=2.5*w, x=start_x, y=h+start_y+pady) # relx=0.01
number_page_entry.place(height=h, width=w, x=2.5*w+start_x+padx, y=h+start_y+pady)
start_button.place(height=h, width=w, relx=0.5, y=2*h+start_y+3*pady, anchor='c')
pb.pack(side=BOTTOM)


'''

root.mainloop()
