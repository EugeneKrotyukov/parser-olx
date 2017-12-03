import sqlite3


conn = sqlite3.connect('olx_scrape.db')
with conn:
    cursor = conn.cursor()
    cursor.execute('''DROP TABLE IF EXISTS olx_parsing''') # удаляет таблицу, если она существует
    cursor.execute('''CREATE TABLE olx_parsing
            (order int,
            ad_number real,
            title text,
            price real,
            date text,
            place text,
            person text,
            condition text,
            phone text,
            context text)
        '''
    cursor.executemany('''INSERT INTO olx_parsing VALUE(?, ?, ?, ?, ?, ?, ?, ?, ?, ?, )''', detailes)

