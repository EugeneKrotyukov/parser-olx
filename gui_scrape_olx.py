from tkinter import *


def get_url():
    return query.get()


root = Tk()
root.title('Parser olx.ua')
root.geometry('1000x400')

query_label = Label(text='Enter the Query')
query_label.grid(row=0, column=0, sticky="w")

query = Entry()
query.grid(row=0, column=1, padx=10, pady=10)

start_button = Button(text="Start", command=get_url)
start_button.grid(row=0, column=2, padx=5, pady=5, sticky="e")


root.mainloop()