"""
https://ru.wikibooks.org/wiki/GUI_Help/Tkinter_book
https://metanit.com/python/tutorial/9.1.php
https://ru.wikiversity.org/wiki/%D0%9A%D1%83%D1%80%D1%81_%D0%BF%D0%BE_%D0%B1%D0%B8%D0%B1%D0%BB%D0%B8%D0%BE%D1%82%D0%B5%D0%BA%D0%B5_Tkinter_%D1%8F%D0%B7%D1%8B%D0%BA%D0%B0_Python
"""
from tkinter import *
import tkinter.ttk as ttk
import main
import plot

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
    """plotting in Frame2"""
    plot.plotting(frame2)


def get_discounts():
    get_url_button()


def _quit():
    """quit"""
    root.quit()
    root.destroy()


root = Tk()
root.title('Scrape olx.ua')
root.geometry('800x600')

nb = ttk.Notebook(root)
nb.pack()

button = Button(master=root, text='Quit', command=_quit, font='16')
button.pack(side=BOTTOM)

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
pb = ttk.Progressbar(frame1, orient=HORIZONTAL, length=750, mode='determinate')

main.set_pb(pb, root)

# use grid()
url_label.grid(row=0, column=0, sticky="w", padx=10, pady=10)
url_entry.grid(row=0, column=1, sticky="w")  # columnspan=2
number_page_label.grid(row=1, column=0, sticky="w", padx=10, pady=10)
number_page_entry.grid(row=1, column=1, sticky="w")
start_button.grid(row=2, column=1, sticky="w")

# Frame 2
statistic_button = Button(frame2, text="Plotting", command=get_statistics, font='16')
statistic_button.pack()

# Frame 4
statistic_button = Button(frame4, text="Discounts", command=get_discounts, font='16')
statistic_button.grid()
pb = ttk.Progressbar(frame4, orient=HORIZONTAL, length=750, mode='determinate')

root.mainloop()
