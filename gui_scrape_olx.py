'''
https://ru.wikibooks.org/wiki/GUI_Help/Tkinter_book
https://metanit.com/python/tutorial/9.1.php
https://ru.wikiversity.org/wiki/%D0%9A%D1%83%D1%80%D1%81_%D0%BF%D0%BE_%D0%B1%D0%B8%D0%B1%D0%BB%D0%B8%D0%BE%D1%82%D0%B5%D0%BA%D0%B5_Tkinter_%D1%8F%D0%B7%D1%8B%D0%BA%D0%B0_Python
'''
from tkinter import *


def get_url_entry(event):
    print(query_entry.get())
    return query_entry.get()


def get_url_button():
    print(query_entry.get())
    return query_entry.get()


root = Tk()
root.title('Parser olx.ua')
root.geometry('800x600')

query = Frame(root)
query.pack()

query_label = Label(query, text='Enter the Query', font='14')
query_label.pack(side='left', padx=10, pady=10)
# query_label.grid(row=0, column=0, sticky="w", padx=10, pady=10)

query_entry = Entry(query, width=50, font='14')
query_entry.pack(side='left')
# query_entry.grid(row=0, column=1, columnspan=2)
query_entry.focus()
query_entry.bind('<Return>', get_url_entry)

start_button = Button(query, text="Start", command=get_url_button, font='14')
start_button.pack(side='left', padx=10, pady=10)
# start_button.grid(row=0, column=3, padx=10, pady=10, sticky="e")


answer = Frame(root)
answer.pack()


root.mainloop()
