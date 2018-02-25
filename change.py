from bs4 import BeautifulSoup
import bd_sqlite
import scraper
import utility


def set_pb(frame, widget):
    """set frame and progressbar for GUI"""
    global window, pb
    pb = widget
    window = frame


def set_lstbox(frame, widget):
    """set frame and listbox for GUI"""
    global window, lstbox
    window = frame
    lstbox = widget


def get_change(window, id_table):
    """ads with a changed price"""
    table_name = 'table{}'.format(id_table)
    query_table = bd_sqlite.select_from_query_table_value(id_table)
    url = query_table[2]
    number_page = query_table[3]
    ad_numbers = bd_sqlite.select_from_parsing_table_column('number', table_name)

    reference_list = []
    count_page = 1  # start page
    line = 0  # position number to insert into in listbox
    lstbox.delete(0, 26)

    # scrape reference from all pages
    while int(number_page) >= count_page:
        url_page = '{}?page={}'.format(url, str(count_page))
        response_page = scraper.get_response(url_page)
        link = scraper.get_links_to_ads(str(response_page.read().decode("utf-8")))
        reference_list.extend(link)
        count_page += 1

    header = ' {} {} {} {} '.format('Ad Number'.center(13),
                                    'Title'.center(45),
                                    'Old Price, UAH'.center(18),
                                    'New Price, UAH'.center(18))
    lstbox.insert(line, header)

    pb['maximum'] = len(reference_list)
    # detailed information on the ads
    for link in reference_list:
        pb.step()
        window.update()
        r = scraper.get_response(link)
        html = str(r.read().decode("utf-8"))
        new_number, new_title, new_price, new_date, new_time, new_place, new_content = scraper.get_details(html)
        new_price = int(scraper.get_digits(new_price))
        if new_number in ad_numbers:
            old_price = bd_sqlite.select_from_parsing_table_value('price', table_name, new_number)
            if new_price != old_price:
                number = str(new_number).center(13, ' ')
                title = utility.format_string(new_title, 45)
                old_price = str(old_price).center(18, ' ')
                new_price = str(new_price).center(18, ' ')
                line += 1
                output = ' {} {} {} {} '.format(number, title, old_price, new_price)
                lstbox.insert(line, output)