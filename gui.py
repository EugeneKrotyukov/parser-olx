"""
https://ru.wikibooks.org/wiki/GUI_Help/Tkinter_book
https://metanit.com/python/tutorial/9.1.php
http://effbot.org/tkinterbook/
https://ru.wikiversity.org/wiki/%D0%9A%D1%83%D1%80%D1%81_%D0%BF%D0%BE_%D0%B1%D0%B8%D0%B1%D0%BB%D0%B8%D0%BE%D1%82%D0%B5%D0%BA%D0%B5_Tkinter_%D1%8F%D0%B7%D1%8B%D0%BA%D0%B0_Python
"""
from tkinter import *
import tkinter.ttk as ttk
import bd_sqlite
import parser
import plot
import new_ad
import change
import export_exls
import utility


def parsing():
    """button PARSING click"""
    global pb
    parsing_btn['state'] = 'disabled'
    url = url_entry.get()
    number_page = number_page_entry.get()
    query_name = query_name_entry.get()
    parser.set_lstbox(frame11, query_lstbox)
    parser.set_pb(frame5, pb)
    parser.check(url, number_page, query_name)
    parsing_btn['state'] = 'normal'


def parsing_entry(event):
    """ENTER click"""
    parsing()


def del_query():
    """delete row from Query_table and TableID"""
    utility.set_lstbox(frame11, query_lstbox)
    id_query = del_entry.get()
    utility.del_query(id_query)


def statistics():
    """displays bar in Frame2"""
    id_query = query_entry.get()
    # plot.set_fig(frame22, fig)
    plot.plotting(frame22, id_query)


def new_ads():
    """displays new ads in Frame3 """
    new_btn['state'] = 'disabled'
    id_query = new_entry.get()
    new_lstbox.delete(0, END)
    new_ad.set_lstbox(frame32, new_lstbox)
    new_ad.set_pb(frame5, pb)
    new_ad.get_new_ad(frame32, id_query)
    new_btn['state'] = 'normal'


def price_changes():
    """displays ads at a price changes in Frame4 """
    changes_btn['state'] = 'disabled'
    id_query = changes_entry.get()
    changes_lstbox.delete(0, END)
    change.set_lstbox(frame42, changes_lstbox)
    change.set_pb(frame5, pb)
    change.get_change(frame42, id_query)
    changes_btn['state'] = 'normal'


def preview():
    """display content TableID in Frame5"""
    export_btn['state'] = 'disabled'
    id_query = export_entry.get()
    export_lstbox.delete(0, END)
    export_exls.set_lstbox(frame52, export_lstbox)
    export_exls.preview_tableID(id_query)
    export_btn['state'] = 'normal'


def export_excel():
    exl_btn['state'] = 'disabled'
    id_query = export_entry.get()
    file_name = exl_entry.get()
    export_exls.export_exl(id_query, file_name)
    exl_btn['state'] = 'normal'


def _quit():
    """quit"""
    root.quit()
    root.destroy()


root = Tk()
root.title('Scrape olx.ua')
root.geometry('800x600')
root.resizable(width=False, height=False)

nb = ttk.Notebook(root)  # закладки
nb.pack()

frame1 = Frame(root)
frame11 = Frame(frame1)
frame12 = Frame(frame1)
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
frame51 = Frame(frame5)
frame52 = Frame(frame5)
frame53 = Frame(frame5)
frame9 = Frame(root)
frame9.pack()


pb = ttk.Progressbar(frame9, orient=HORIZONTAL, length=792, mode='determinate')
pb.pack()
quit_btn = Button(frame9, text='Quit', command=_quit, font=16)
quit_btn.pack(side=BOTTOM, pady=5)

nb.add(frame1, text='Parser')
nb.add(frame2, text='Statistics')
nb.add(frame3, text='New ads')
nb.add(frame4, text='Price Changes')
nb.add(frame5, text='Export to Excel')

# Frame 1
frame11.pack()
url_lbl = Label(frame11, text='URL', font=16)
url_lbl.grid(row=0, column=0, sticky='w', padx=10, pady=5)
url_entry = Entry(frame11, width=62, font=14)
url_entry.focus()
url_entry.bind('<Return>', parsing_entry)
url_entry.grid(row=0, column=1, columnspan=4, sticky='w')

number_page_lbl = Label(frame11, text='Number of Pages', font=16)
number_page_lbl.grid(row=1, column=0, sticky='w', padx=10, pady=5)
number_page_entry = Entry(frame11, width=10, font=14)
number_page_entry.insert(0, 1)
number_page_entry.bind('<Return>', parsing_entry)
number_page_entry.grid(row=1, column=1, sticky='w')

query_name_lbl = Label(frame11, text='Query Name', font=16)
query_name_lbl.grid(row=2, column=0, sticky='w', padx=10, pady=5)
query_name_entry = Entry(frame11, width=62, font=14)
query_name_entry.bind('<Return>', parsing_entry)
query_name_entry.grid(row=2, column=1, columnspan=4, sticky='w')

parsing_btn = Button(frame11, text="Parsing", command=parsing, font=16)
parsing_btn.grid(row=3, column=2, sticky='w')

query_lstbox = Listbox(frame11, height=18, font='monospace 10')
query_lstbox.grid(row=4, column=0, columnspan=5, sticky='we', pady=5)
data_from_query_table = bd_sqlite.select_from_query_table_all()

header = ' {} {} {} {} '.format('ID'.center(4, ' '),
                                'Query Name'.center(30, ' '),
                                'Url'.center(50, ' '),
                                'N Ads'.center(8, ' '))
query_lstbox.insert(0, header)
for line, row in enumerate(data_from_query_table, 1):
    id_q = str(row[0]).center(4, ' ')
    table_name = 'table{}'.format(row[0])
    n_ads = bd_sqlite.select_number_rows(table_name)
    n_ads = str(n_ads).center(8, ' ')
    name_q = utility.format_string(row[1], 30)
    url_q = utility.format_string(row[2], 50)
    # page_q = str(row[3]).center(8, ' ')
    output = ' {} {} {} {} '.format(id_q, name_q, url_q, n_ads)
    query_lstbox.insert(line, output)

frame12.pack()
del_lbl = Label(frame12, text='Enter ID', font=16)
del_lbl.grid(row=0, column=0, sticky='we', padx=5, pady=5)
del_entry = Entry(frame12, width=10, font=14)
del_entry.grid(row=0, column=1, sticky='we', padx=5, pady=5)
del_btn = Button(frame12, text="Delete Query", command=del_query, font=16)
del_btn.grid(row=0, column=2, sticky='we', padx=5, pady=5)

# Frame 2
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
frame31.pack()
new_lbl = Label(frame31, text='Enter ID', font=16)
new_lbl.grid(row=0, column=0, sticky='we', padx=5, pady=5)
new_entry = Entry(frame31, width=10, font=14)
new_entry.focus()
new_entry.insert(0, 1)
new_entry.grid(row=0, column=1, sticky='we', padx=5, pady=5)
new_btn = Button(frame31, text="New Ads", command=new_ads, font=16)
new_btn.grid(row=0, column=2, sticky='we', padx=5, pady=5)
frame32.pack()
new_lstbox = Listbox(frame32, width=750, height=26, font='monospace 10')
new_lstbox.pack()

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
changes_lstbox = Listbox(frame42, width=750,	height=26,	font='monospace 10')
changes_lstbox.pack()

# Frame 5
frame51.pack()
export_lbl = Label(frame51, text='Enter ID', font=16)
export_lbl.grid(row=0, column=0, sticky='we', padx=5, pady=5)
export_entry = Entry(frame51, width=10, font=14)
export_entry.focus()
export_entry.insert(0, 1)
export_entry.grid(row=0, column=1, sticky='we', padx=5, pady=5)
export_btn = Button(frame51, text="Preview", command=preview, font=16)
export_btn.grid(row=0, column=2, sticky='we', padx=5, pady=5)

frame52.pack()
export_lstbox = Listbox(frame52, width=750,	height=23,	font='monospace 10')
export_lstbox.pack()

frame53.pack()
exl_lbl = Label(frame53, text='Enter File Name', font=16)
exl_lbl.grid(row=0, column=0, sticky='we', padx=5, pady=5)
exl_entry = Entry(frame53, width=10, font=14)
exl_entry.grid(row=0, column=1, sticky='we', padx=5, pady=5)
exl_btn = Button(frame53, text="Export to Excel", command=export_excel, font=16)
exl_btn.grid(row=0, column=2, sticky='we', padx=5, pady=5)


root.mainloop()
