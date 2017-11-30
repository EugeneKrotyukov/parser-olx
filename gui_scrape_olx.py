from tkinter import *


def get_url_entry(event):
    print(query.get())
    return query.get()


def get_url_button():
    print(query.get())
    return query.get()


root = Tk()
root.title('Parser olx.ua')
root.geometry('800x600')

query_label = Label(root, text='Enter the Query')
query_label.grid(row=0, column=0, sticky="w", padx=10, pady=10)

query = Entry(root, width=50)
query.grid(row=0, column=1)
query.focus()

start_button = Button(text="Start", command=get_url_button)
start_button.grid(row=0, column=2, padx=10, pady=10, sticky="e")

query.bind('<Return>', get_url_entry)

root.mainloop()