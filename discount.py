import bd_sqlite
import parser


def get_discounted_ads(url, number_page):
    ad_numbers = bd_sqlite.select_from_bd_column('number')
    flat_list = [item for sublist in ad_numbers for item in sublist]
    print(flat_list)
    print(len(flat_list))
    print(sorted(flat_list))
    s = set(flat_list)
    print(s)
    print(len(s))
