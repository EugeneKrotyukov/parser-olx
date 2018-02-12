"""
https://ru.wikibooks.org/wiki/GUI_Help/Tkinter_book
https://metanit.com/python/tutorial/9.1.php
https://ru.wikiversity.org/wiki/%D0%9A%D1%83%D1%80%D1%81_%D0%BF%D0%BE_%D0%B1%D0%B8%D0%B1%D0%BB%D0%B8%D0%BE%D1%82%D0%B5%D0%BA%D0%B5_Tkinter_%D1%8F%D0%B7%D1%8B%D0%BA%D0%B0_Python
"""
from tkinter import *
import tkinter.ttk as ttk
import parser
import plot
import change


def parsing():
    """button PARSING click"""
    global pb
    parsing_btn['state'] = 'disabled'
    url = url_entry.get()
    number_page = number_page_entry.get()
    query_name = query_name_entry.get()
    pb.grid(row=4, column=0, columnspan=4, sticky="w", padx=10, pady=10)
    parser.check(url, number_page, query_name)
    parsing_btn['state'] = 'normal'
    pb.grid_remove()


def parsing_entry(event):
    """ENTER click"""
    parsing()


def statistics():
    """displays bar in Frame2"""
    plot.plotting(frame2)


def price_changes():
    """displays ads at a price changes in Frame4 """
    url = url_entry.get()
    number_page = number_page_entry.get()
    change.get_change(url, number_page)


def _quit():
    """quit"""
    root.quit()
    root.destroy()


root = Tk()
root.title('Scrape olx.ua')
root.geometry('800x600')
root.resizable(width=False, height=False)

nb = ttk.Notebook(root)
nb.pack()

quit_btn = Button(master=root, text='Quit', command=_quit, font=16).pack(side=BOTTOM)

frame1 = Frame(root)
frame2 = Frame(root)
frame3 = Frame(root)
frame4 = Frame(root)

nb.add(frame1, text='Parser')
nb.add(frame2, text='Statistics')
nb.add(frame3, text='New ads')
nb.add(frame4, text='Price Changes')

# Frame 1
url_lbl = Label(frame1, text='URL', font=16)
url_lbl.grid(row=0, column=0, sticky='w', padx=10, pady=10)
url_entry = Entry(frame1, width=62, font=14)
url_entry.focus()
url_entry.bind('<Return>', parsing_entry)
url_entry.grid(row=0, column=1, columnspan=4, sticky='w')

number_page_lbl = Label(frame1, text='Number of Pages', font=16)
number_page_lbl.grid(row=1, column=0, sticky='w', padx=10, pady=10)
number_page_entry = Entry(frame1, width=10, font=14)
number_page_entry.insert(0, 1)
number_page_entry.bind('<Return>', parsing_entry)
number_page_entry.grid(row=1, column=1, sticky='w')

query_name_lbl = Label(frame1, text='Query Name', font=16)
query_name_lbl.grid(row=2, column=0, sticky='w', padx=10, pady=10)
query_name_entry = Entry(frame1, width=62, font=14)
query_name_entry.bind('<Return>', parsing_entry)
query_name_entry.grid(row=2, column=1, columnspan=4, sticky='w')

parsing_btn = Button(frame1, text="Parsing", command=parsing, font=16)
parsing_btn.grid(row=3, column=2, sticky='w')

pb = ttk.Progressbar(frame1, orient=HORIZONTAL, length=750, mode='determinate')
parser.set_pb(root, pb)

# Frame 2
statistic_btn = Button(frame2, text="Plotting", command=statistics, font=16)
statistic_btn.pack()

# Frame 3

# Frame 4
changes_btn = Button(frame4, text="Price Changes", command=price_changes, font=16)
changes_btn.pack()
changes_lstbox = Listbox(frame4, width=750,	height=25,	font=10)
changes_lstbox.pack()
change.set_lstbox(frame4, changes_lstbox)


root.mainloop()
