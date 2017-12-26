'''
https://ru.wikibooks.org/wiki/GUI_Help/Tkinter_book
https://metanit.com/python/tutorial/9.1.php
https://ru.wikiversity.org/wiki/%D0%9A%D1%83%D1%80%D1%81_%D0%BF%D0%BE_%D0%B1%D0%B8%D0%B1%D0%BB%D0%B8%D0%BE%D1%82%D0%B5%D0%BA%D0%B5_Tkinter_%D1%8F%D0%B7%D1%8B%D0%BA%D0%B0_Python
'''
from tkinter import *
import main


def get_url_entry(event):
    """enter click"""
    global h, w, padx, pady, start_x, start_y
    url = url_entry.get()
    number_page = number_page_entry.get()
    url_lbl = Label(root, text=url, font='12', bg='grey')
    url_lbl.place(height=h, relwidth=0.8, relx=0.5, y=3*h+start_y+4*pady, anchor='c')
    url_entry.delete(0, END)
    main.start(url, number_page)


def get_url_button():
    """button START click"""
    url = url_entry.get()
    number_page = number_page_entry.get()
    url_lbl = Label(root, text=url, font='12', bg='grey')
    url_lbl.place(height=h, relwidth=0.8, relx=0.5, y=3*h+start_y+4*pady, anchor='c')
    url_entry.delete(0, END)
    main.start(url, number_page)


root = Tk()
root.title('Scrape olx.ua')
root.geometry('800x600')
root['bg'] = 'grey'

url_label = Label(root, text='Enter URL', font='16', bg='grey')
url_entry = Entry(root, width=50, font='14')
url_entry.focus()
url_entry.bind('<Return>', get_url_entry)
number_page_label = Label(root, text='Enter the number of pages', font='16', bg='grey')
number_page_entry = Entry(root, width=10, font='14')
number_page_entry.insert(0, '1')
number_page_entry.bind('<Return>', get_url_entry)
start_button = Button(root, text="Start", command=get_url_button, font='16')

'''
# use grid()
url_label.grid(row=0, column=0, sticky="w", padx=10, pady=10)
url_entry.grid(row=0, column=1, sticky="w") # columnspan=2
number_page_label.grid(row=1, column=0, sticky="w", padx=10, pady=10)
number_page_entry.grid(row=1, column=1, sticky="w")
start_button.grid(row=2, column=1, sticky="w")
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


root.mainloop()
