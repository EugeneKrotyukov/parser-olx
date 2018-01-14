"""
https://ru.wikibooks.org/wiki/GUI_Help/Tkinter_book
https://metanit.com/python/tutorial/9.1.php
https://ru.wikiversity.org/wiki/%D0%9A%D1%83%D1%80%D1%81_%D0%BF%D0%BE_%D0%B1%D0%B8%D0%B1%D0%BB%D0%B8%D0%BE%D1%82%D0%B5%D0%BA%D0%B5_Tkinter_%D1%8F%D0%B7%D1%8B%D0%BA%D0%B0_Python
"""
from tkinter import *
import tkinter.ttk as ttk
# import threading
# import time
import main





def get_url_button():
    """button START click"""
    start_button['state'] = 'disabled'
    url = url_entry.get()
    number_page = number_page_entry.get()
    # url_lbl = Label(root, text=url, font='12', bg='grey')
    # url_lbl.place(height=h, relwidth=0.8, relx=0.5, y=3*h+start_y+4*pady, anchor='c')
    # url_entry.delete(0, END)
    main.get_list_product(url, number_page)
    start_button['state'] = 'normal'


def get_url_entry(event):
    """enter click"""
    get_url_button()


# def progress(maximum, current):
#    """progress bar"""
#    pb['maximum'] = maximum
#    pb['value'] = current


WIDTH = 800
HEIGHT = 600


root = Tk()
root.title('Scrape olx.ua')
root.geometry('800x600')
# root['bg'] = 'grey'

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

url_label = Label(frame1, text='Enter URL', font='16', bg='grey')
url_entry = Entry(frame1, width=50, font='14')
url_entry.focus()
url_entry.bind('<Return>', get_url_entry)
number_page_label = Label(frame1, text='Enter the number of pages', font='16', bg='grey')
number_page_entry = Entry(frame1, width=10, font='14')
number_page_entry.insert(0, '1')
number_page_entry.bind('<Return>', get_url_entry)
start_button = Button(frame1, text="Start", command=get_url_button, font='16')
pb = ttk.Progressbar(frame1, orient=HORIZONTAL, length=800, mode='determinate')

main.set_pb(pb, root)

#threading.Thread(target=progress, args=(100, 50)).start()

# МАСШТАБИРОВАНИЕ перед выводом на график
# для маштабирования цены на график необходимо
# разделить long_x на max_price и
# затем каждое значение умножать на полученый коэф
# с кол-вом объявлений необходимо проделать туже операцию
x_start, y_end = 50, 50
x_end = WIDTH - x_start # 750
y_start = HEIGHT - y_end # 550
long_x = x_end - x_start # 700
long_y = y_start - y_end # 500
min_price = 10
max_price = 100
number_ads = 20
step_price = long_x // (max_price - min_price) # 7
step_ads = long_y // number_ads # 25

# список из цен
# отсортировать по возростанию
# подсчитать кол-во одинаковых элементов

canvas = Canvas(frame2, width=WIDTH, height=HEIGHT, bg="white")
canvas.create_line(x_start, y_start, x_end, y_start, width=2, arrow=LAST)
canvas.create_line(x_start, y_start, x_start, y_end, width=2, arrow=LAST)
for x in range(100, 750, 50):
    canvas.create_text(x, y_start+10, text=x)
for y in range(0, 500, 50):
    canvas.create_text(x_start-20, y_start-y, text=y)



# use grid()
url_label.grid(row=0, column=0, sticky="w", padx=10, pady=10)
url_entry.grid(row=0, column=1, sticky="w") # columnspan=2
number_page_label.grid(row=1, column=0, sticky="w", padx=10, pady=10)
number_page_entry.grid(row=1, column=1, sticky="w")
start_button.grid(row=2, column=1, sticky="w")
pb.grid(row=7, column=0, columnspan=2, sticky="w")
canvas.pack()
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
