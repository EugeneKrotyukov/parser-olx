import sqlite3


def create_bd(bd_name):
    """create table"""
    conn = sqlite3.connect(bd_name)
    with conn:
        cursor = conn.cursor()
        cursor.execute('''DROP TABLE IF EXISTS olx_parsing''') # удаляет таблицу, если она существует
        cursor.execute('''CREATE TABLE olx_parsing (
        number,
        title,
        price,
        date,
        time,
        phone,
        place,
        content)''')


def insert_bd(bd_name, number, title, price, date, time, phone, place, content):
    """insert in table"""
    conn = sqlite3.connect(bd_name)
    with conn:
        cursor = conn.cursor()
        cursor.execute('''INSERT INTO olx_parsing (number, title, price, date, time, phone, place, content)
                         VALUES (?, ?, ?, ?, ?, ?, ?, ?)''', (number, title, price, date, time, phone, place, content))