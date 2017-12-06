import sqlite3


def create_bd(bd_name):
    conn = sqlite3.connect(bd_name)
    with conn:
        cursor = conn.cursor()
        cursor.execute('''DROP TABLE IF EXISTS olx_parsing''') # удаляет таблицу, если она существует
        cursor.execute('''CREATE TABLE olx_parsing (
        ad_number,
        title,
        price,
        date,
        place,
        content)''')


def insert_bd(bd_name, ad_number):
    conn = sqlite3.connect(bd_name)
    with conn:
        cursor = conn.cursor()
        cursor.executemany('''INSERT INTO olx_parsing (ad_number)
                            VALUES (?)''', ad_number)

bd_name = 'test.sqlite'
ad_number = '9999'
title = 'Заголовок'
price = '555''
date = '12 декабря'
place = 'Одесса'
content = 'описание описание описание'

create_bd(bd_name)

insert_bd(bd_name, ad_number)