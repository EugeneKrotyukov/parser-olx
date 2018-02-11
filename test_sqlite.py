import sqlite3


def select_limit_from_bd(col1='number', col2='title', col3='price', table_name='olx_parsing', bd_name='olx_sqlite'):
    """select all from table"""
    print('select_limit_from_bd: ', col1, col2, col3, table_name, bd_name)
    query = 'SELECT {col1}, {col2}, {col3} FROM {table_name} LIMIT 3'.format(col1=col1, col2=col2, col3=col3, table_name=table_name)
    conn = sqlite3.connect(bd_name)
    with conn:
        cursor = conn.cursor()
        cursor.execute(query)
    return cursor.fetchall()



def select_from_bd_column(column, table_name='olx_parsing', bd_name='olx_sqlite'):
    """select column from table"""
    print('select_from_bd_column: ', column, table_name, bd_name)
    query = 'SELECT {column} FROM {table_name}'.format(column=column, table_name=table_name)
    conn = sqlite3.connect(bd_name)
    with conn:
        cursor = conn.cursor()
        cursor.execute(query)
    return cursor.fetchall()


def select_from_bd_value(column, row, table_name='olx_parsing', bd_name='olx_sqlite'):
    """select value from table"""
    print('select_from_bd_value: ', column, table_name, row, bd_name)
    query = "SELECT {column} FROM {table_name} WHERE number='{row}'".format(column=column, table_name=table_name, row=row)
    conn = sqlite3.connect(bd_name)
    with conn:
        cursor = conn.cursor()
        cursor.execute(query)
    return cursor.fetchone()


def format_string(lst):
    format_lst = []
    for string in lst:
        if len(string) < 45:
            string.ljust(48, " ")
        else:
            string = '{}...'.format(string[:46])
        format_lst.append(string)
    return format_lst


bd = select_limit_from_bd()
print(bd)
print('-' * 100)

ad_numbers_from_bd = select_from_bd_column('number')
# print(ad_numbers_from_bd)
ad_numbers = [item for sublist in ad_numbers_from_bd for item in sublist]
print(ad_numbers)
number = ad_numbers[2]
print(number, type(number))
print('-' * 100)

price_from_bd = select_from_bd_value('price', number)
print(price_from_bd)
print(price_from_bd[0], type(price_from_bd[0]))
print('-' * 100)

prices_from_bd = select_from_bd_column('price')
prices = [item for sublist in prices_from_bd for item in sublist]
print(prices)
price = prices[2]
print(price, type(price))
print('-' * 100)

titles_bd = select_from_bd_column('title')
titles = [item for sublist in titles_bd for item in sublist]
for string in format_string(titles):
    print(string)

