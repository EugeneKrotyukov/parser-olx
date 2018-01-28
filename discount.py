import bd_sqlite
import scraper


def get_discounted_ads(url, number_page):
    ad_numbers = bd_sqlite.select_from_bd_column('number')
    flat_list = [item for sublist in ad_numbers for item in sublist]
    print(flat_list)
    ad_number = '462255976'
    if ad_number in flat_list:
        print('YES')
    else:
        print('NO')