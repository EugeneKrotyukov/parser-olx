"""
http://zametkinapolyah.ru/karta-sajta
"""
import sqlite3


def create_bd(bd_name='olx_sqlite'):
    """create table"""
    conn = sqlite3.connect(bd_name)
    with conn:
        cursor = conn.cursor()
        cursor.execute('''DROP TABLE IF EXISTS olx_parsing''') # удаляет таблицу, если она существует
        cursor.execute('''CREATE TABLE olx_parsing (
        number PRIMARY KEY,
        title,
        price,
        date,
        time,
        phone,
        place,
        content)''')


def insert_into_bd(number, title, price, date, time, phone, place, content, bd_name='olx_sqlite'):
    """insert in table"""
    conn = sqlite3.connect(bd_name)
    try:
        with conn:
            cursor = conn.cursor()
            cursor.execute('''INSERT INTO olx_parsing (number, title, price, date, time, phone, place, content)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?)''', (number, title, price, date, time, phone, place, content))
    except sqlite3.DataBaseError as err:
        print('Error: ', err)
        print('Ad Number: ', number)


def select_from_bd_column(column, table_name='olx_parsing', bd_name='olx_sqlite'):
    """select column from table"""
    query = 'SELECT {column} FROM {table_name}'.format(column=column, table_name=table_name)
    conn = sqlite3.connect(bd_name)
    with conn:
        cursor = conn.cursor()
        cursor.execute(query)
    return cursor.fetchall()


def select_from_bd_value(column, row, table_name='olx_parsing', bd_name='olx_sqlite'):
    """select value from table"""
    query = "SELECT {column} FROM {table_name} WHERE number='{row}'".format(column=column, table_name=table_name, row=row)
    conn = sqlite3.connect(bd_name)
    with conn:
        cursor = conn.cursor()
        cursor.execute(query)
    return cursor.fetchone()
