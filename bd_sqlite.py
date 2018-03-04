"""
http://zametkinapolyah.ru/karta-sajta
http://www.sqlitetutorial.net/sqlite-delete/
"""
import sqlite3


def create_query_table(bd_name='olx.sqlite3'):
    """create query_table"""
    conn = sqlite3.connect(bd_name)
    with conn:
        cursor = conn.cursor()
        cursor.execute('''CREATE TABLE IF NOT EXISTS query_table (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            query_name,
            url,
            number_page)''')


def insert_into_query_table(query_name, url, number_page, bd_name='olx.sqlite3'):
    """insert into query_table"""
    conn = sqlite3.connect(bd_name)
    try:
        with conn:
            cursor = conn.cursor()
            cursor.execute('''INSERT INTO query_table (query_name, url, number_page)
            VALUES (?, ?, ?)''', (query_name, url, number_page))
    except sqlite3.Error as err:
        print('Error: ', err)
        print('Table Name: ', table_name)
        print('URL: ', url)


def select_from_query_table_all(bd_name='olx.sqlite3'):
    """select all from query_table"""
    conn = sqlite3.connect(bd_name)
    with conn:
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM query_table')
    return cursor.fetchall()


def select_last_insert(bd_name='olx.sqlite3'):
    """select last insert into query_table"""
    conn = sqlite3.connect(bd_name)
    with conn:
        cursor = conn.cursor()
        cursor.execute('''SELECT id FROM query_table ORDER BY id DESC LIMIT 1''')
    return cursor.fetchone()[0]


def select_number_rows(table_name, bd_name='olx.sqlite3'):
    """select number of rows in table"""
    query = "SELECT COUNT(*) FROM '{table_name}'".format(table_name=table_name)
    conn = sqlite3.connect(bd_name)
    with conn:
        cursor = conn.cursor()
        cursor.execute(query)
    return cursor.fetchone()[0]


def select_from_query_table_value(row, bd_name='olx.sqlite3'):
    """select url, number_page from query_table"""
    query = "SELECT * FROM query_table WHERE id='{row}'".format(row=row)
    conn = sqlite3.connect(bd_name)
    with conn:
        cursor = conn.cursor()
        cursor.execute(query)
    return [item for sublist in cursor.fetchall() for item in sublist]


def create_parsing_table(table_name, bd_name='olx.sqlite3'):
    """create parsing_table"""
    conn = sqlite3.connect(bd_name)
    with conn:
        cursor = conn.cursor()
        drop = 'DROP TABLE IF EXISTS {}'.format(table_name)
        cursor.execute(drop)
        create = 'CREATE TABLE IF NOT EXISTS {} (number PRIMARY KEY, title, price, date, time, phone, place, content)'.format(table_name)
        cursor.execute(create)


def insert_into_parsing_table(table_name, number, title, price, date, time, phone, place, content, bd_name='olx.sqlite3'):
    """insert into table"""
    conn = sqlite3.connect(bd_name)
    try:
        with conn:
            cursor = conn.cursor()
            cursor.execute("INSERT INTO {} VALUES (?,?,?,?,?,?,?,?)".format(table_name),
                           (number, title, price, date, time, phone, place, content))
            # cursor.execute('''INSERT INTO olx_parsing (number, title, price, date, time, phone, place, content)
            # VALUES (?, ?, ?, ?, ?, ?, ?, ?)''', (number, title, price, date, time, phone, place, content))
    except sqlite3.Error as err:
        print('Error: ', err)
        print('Ad Number: ', number)


def select_from_parsing_table_all(table_name, bd_name='olx.sqlite3'):
    """select all from table"""
    query = 'SELECT * FROM {table_name}'.format(table_name=table_name)
    conn = sqlite3.connect(bd_name)
    with conn:
        cursor = conn.cursor()
        cursor.execute(query)
    return cursor.execute(query)


def select_from_parsing_table_column(column, table_name, bd_name='olx.sqlite3'):
    """select column from table"""
    query = 'SELECT {column} FROM {table_name}'.format(column=column, table_name=table_name)
    conn = sqlite3.connect(bd_name)
    with conn:
        cursor = conn.cursor()
        cursor.execute(query)
    return [item for sublist in cursor.fetchall() for item in sublist]



def select_from_parsing_table_value(column, table_name, row, bd_name='olx.sqlite3'):
    """select value from table"""
    query = "SELECT {column} FROM {table_name} WHERE number='{row}'".format(column=column, table_name=table_name, row=row)
    conn = sqlite3.connect(bd_name)
    with conn:
        cursor = conn.cursor()
        cursor.execute(query)
    return cursor.fetchone()[0]


def drop_parsing_table(table_name, bd_name='olx.sqlite3'):
    """drop parsing_table"""
    conn = sqlite3.connect(bd_name)
    with conn:
        cursor = conn.cursor()
        drop = 'DROP TABLE IF EXISTS {}'.format(table_name)
        cursor.execute(drop)


def del_from_query_table_row(row, bd_name='olx.sqlite3'):
    """delete row from query_table"""
    conn = sqlite3.connect(bd_name)
    with conn:
        cursor = conn.cursor()
        delete = "DELETE FROM query_table WHERE id='{}'".format(row)
        cursor.execute(delete)