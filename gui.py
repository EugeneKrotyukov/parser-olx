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
import bd_sqlite


def parsing():
    """button PARSING click"""
    global pb
    parsing_btn['state'] = 'disabled'
    url = url_entry.get()
    number_page = number_page_entry.get()
    query_name = query_name_entry.get()
    # pb.grid(row=5, column=0, columnspan=4, sticky="w", padx=10, pady=10)
    parser.check(url, number_page, query_name)
    parsing_btn['state'] = 'normal'
    # pb.grid_remove()


def parsing_entry(event):
    """ENTER click"""
    parsing()


def statistics():
    """displays bar in Frame2"""
    id_query = query_entry.get()
    plot.plotting(frame22, id_query)


def price_changes():
    """displays ads at a price changes in Frame4 """
    changes_btn['state'] = 'disabled'
    id_query = query_entry.get()
    changes_lstbox = Listbox(frame42, width=750,	height=23,	font=10)
    changes_lstbox.pack()
    change.set_lstbox(frame42, changes_lstbox)
    change.get_change(frame42, id_query)
    changes_btn['state'] = 'normal'


def _quit():
    """quit"""
    root.quit()
    root.destroy()


root = Tk()
root.title('Scrape olx.ua')
root.geometry('800x600')
root.resizable(width=False, height=False)

nb = ttk.Notebook(root)  #закладки
nb.pack()



frame1 = Frame(root)
frame2 = Frame(root)
frame21 = Frame(frame2)
frame22 = Frame(frame2)
frame3 = Frame(root)
frame31 = Frame(frame3)
frame32 = Frame(frame3)
frame4 = Frame(root)
frame41 = Frame(frame4)
frame42 = Frame(frame4)

frame5 = Frame(root)
frame5.pack()
pb = ttk.Progressbar(frame5, orient=HORIZONTAL, length=792, mode='determinate')
pb.pack()
quit_btn = Button(frame5, text='Quit', command=_quit, font=16)
quit_btn.pack(side=BOTTOM)

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

query_lstbox = Listbox(frame1, height=17, font=10)
query_lstbox.grid(row=4, column=0, columnspan=5, sticky='we', pady=10)
parser.set_lstbox(frame1, query_lstbox)
query = bd_sqlite.select_from_query_table_all()
for e, row in enumerate(query):
    query_lstbox.insert(e, row)

# pb = ttk.Progressbar(frame1, orient=HORIZONTAL, length=750, mode='determinate')
parser.set_pb(frame5, pb)

# Frame 2
# frame21.place(relx=0.5, rely=0.04, anchor=CENTER)
frame21.pack()
query_lbl = Label(frame21, text='Enter ID', font=16)
query_lbl.grid(row=0, column=0, sticky='we', padx=5, pady=5)
query_entry = Entry(frame21, width=10, font=14)
query_entry.focus()
query_entry.insert(0, 1)
query_entry.grid(row=0, column=1, sticky='we', padx=5, pady=5)
query_btn = Button(frame21, text="Plotting", command=statistics, font=16)
query_btn.grid(row=0, column=2, sticky='we', padx=5, pady=5)
frame22.pack()

# Frame 3

# Frame 4
frame41.pack()
changes_lbl = Label(frame41, text='Enter ID', font=16)
changes_lbl.grid(row=0, column=0, sticky='we', padx=5, pady=5)
changes_entry = Entry(frame41, width=10, font=14)
changes_entry.focus()
changes_entry.insert(0, 1)
changes_entry.grid(row=0, column=1, sticky='we', padx=5, pady=5)
changes_btn = Button(frame41, text="Price Changes", command=price_changes, font=16)
changes_btn.grid(row=0, column=2, sticky='we', padx=5, pady=5)
frame42.pack()
change.set_pb(frame5, pb)
# changes_lstbox = Listbox(frame42, width=750,	height=25,	font=10)
# changes_lstbox.pack()
# change.set_lstbox(frame42, changes_lstbox)


root.mainloop()
