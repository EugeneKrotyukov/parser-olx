"""
http://zametkinapolyah.ru/karta-sajta
"""
import sqlite3


def create_query_table(bd_name='olx_sqlite'):
    """create query_table"""
    conn = sqlite3.connect(bd_name)
    with conn:
        cursor = conn.cursor()
        cursor.execute('''CREATE TABLE IF NOT EXISTS query_table (
            table_name PRIMARY KEY,
            url,
            number_page)''')


def insert_into_query_table(table_name, url, number_page, bd_name='olx_sqlite'):
    """insert in query table"""
    conn = sqlite3.connect(bd_name)
    try:
        with conn:
            cursor = conn.cursor()
            cursor.execute('''INSERT INTO query_table (table_name, url, number_page)
            VALUES (?, ?, ?)''', (table_name, url, number_page))
    except sqlite3.Error as err:
        print('Error: ', err)
        print('Table Name: ', table_name)
        print('URL: ', url)


def create_parsing_table(table_name, bd_name='olx_sqlite'):
    """create parsing_table"""
    conn = sqlite3.connect(bd_name)
    with conn:
        cursor = conn.cursor()
        drop = 'DROP TABLE IF EXISTS {}'.format(table_name)
        cursor.execute(drop)
        create = 'CREATE TABLE {} (number PRIMARY KEY, title, price, date, time, phone, place, content)'.format(table_name)
        cursor.execute(create)


def insert_into_parsing_table(table_name, number, title, price, date, time, phone, place, content, bd_name='olx_sqlite'):
    """insert in table"""
    conn = sqlite3.connect(bd_name)
    try:
        with conn:
            cursor = conn.cursor()
            insert = 'INSERT INTO {} (number, title, price, date, time, phone, place, content) VALUES ({} {} {} {} {} {} {} {})'.format(table_name, number, title, price, date, time, phone, place, content)
            cursor.execute(insert)
            # cursor.execute('''INSERT INTO olx_parsing (number, title, price, date, time, phone, place, content)
            # VALUES (?, ?, ?, ?, ?, ?, ?, ?)''', (number, title, price, date, time, phone, place, content))
    except sqlite3.Error as err:
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
