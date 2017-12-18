import sqlite3


def create_bd(bd_name):
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
        place,
        content)''')


def insert_bd(bd_name, number, title, price, date, time, place, content):
    conn = sqlite3.connect(bd_name)
    with conn:
        cursor = conn.cursor()
        cursor.execute('''INSERT INTO olx_parsing (number, title, price, date, time, place, content)
                         VALUES (?, ?, ?, ?, ?, ?, ?)''', (number, title, price, date, time, place, content))


'''
bd_name = 'test.sqlite'
ad_number = '1234567890987654321'
title = 'Супер заголовок'
price = '2345'
date = '12 декабря 2017'
place = 'Одесса МАлиновский р-н'
content = 'здесь должно находится описание товара'

create_bd(bd_name)

insert_bd(bd_name, ad_number, title, price, date, place, content)
'''