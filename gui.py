'''
https://ru.wikibooks.org/wiki/GUI_Help/Tkinter_book
https://metanit.com/python/tutorial/9.1.php
https://ru.wikiversity.org/wiki/%D0%9A%D1%83%D1%80%D1%81_%D0%BF%D0%BE_%D0%B1%D0%B8%D0%B1%D0%BB%D0%B8%D0%BE%D1%82%D0%B5%D0%BA%D0%B5_Tkinter_%D1%8F%D0%B7%D1%8B%D0%BA%D0%B0_Python
'''
from tkinter import *
import main


def get_url_entry(event):
    url = url_entry.get()
    url_lable = Label(root, text=url, font='12')
    url_lable.grid(row=1, column=1)
    url_entry.delete(0, END)
    scrape_olx_main.start(url)


def get_url_button():
    url = url_entry.get()
    url_lable = Label(root, text=url, font='12')
    url_lable.grid(row=1, column=1)
    query_entry.delete(0, END)
    scrape_olx_main.start(url)


root = Tk()
root.title('Scrape olx.ua')
root.geometry('800x600')

enter_url = Label(root, text='Enter url', font='14')
enter_url.grid(row=0, column=0, sticky="w", padx=10, pady=10)

url_entry = Entry(root, width=50, font='14')
url_entry.grid(row=0, column=1, columnspan=2)
url_entry.focus()
url_entry.bind('<Return>', get_url_entry)

start_button = Button(root, text="Start", command=get_url_button, font='14')
start_button.grid(row=0, column=3, padx=10, pady=10, sticky="e")


root.mainloop()
