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


def insert_into_bd(bd_name, number, title, price, date, time, phone, place, content):
    """insert in table"""
    conn = sqlite3.connect(bd_name)
    with conn:
        cursor = conn.cursor()
        cursor.execute('''INSERT INTO olx_parsing (number, title, price, date, time, phone, place, content)
                         VALUES (?, ?, ?, ?, ?, ?, ?, ?)''', (number, title, price, date, time, phone, place, content))


def select_from_bd_column(bd_name, column):
    """select column from table"""
    query = 'SELECT {} FROM olx_parsing'.format(column)
    conn = sqlite3.connect(bd_name)
    with conn:
        cursor = conn.cursor()
        cursor.execute(query)
    print(cursor.fetchall())
    return cursor.fetchall()


def select_from_bd_value(bd_name, column, number):
    """select value from table"""
    query = 'SELECT {} FROM olx_parsing WHERE number={}'.format(column, number)
    conn = sqlite3.connect(bd_name)
    with conn:
        cursor = conn.cursor()
        cursor.execute(query)
    return cursor.fetch()

