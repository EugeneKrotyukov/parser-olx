import sqlite3


def create_bd(bd_name):
    conn = sqlite3.connect(bd_name)
    with conn:
        cursor = conn.cursor()
        cursor.execute('''DROP TABLE IF EXISTS olx_parsing''') # удаляет таблицу, если она существует
        cursor.execute('''CREATE TABLE olx_parsing ad_number real, title text, price real, date text, place text, phone text, context text''')

def insert_bd(bd_name, ad_number, title, price, date, place, phone, context):
    conn = sqlite3.connect(bd_name)
    with conn:
        cursor = conn.cursor()
        cursor.executemany('''INSERT INTO olx_parsing (order, ad_number, title, price, date, place, person, condition, phone, context)
                            VALUE(?, ?, ?, ?, ?, ?, ?)''',
                           (ad_number, title, price, date, place, phone, context))

