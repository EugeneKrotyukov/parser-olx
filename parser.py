import urllib.request
import re
import scraper
import bd_sqlite
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


def parsing(url, number_page, query_name):
    bd_sqlite.create_query_table()
    bd_sqlite.insert_into_query_table(query_name, url, number_page)
    table_name = bd_sqlite.select_last_insert()
    table_name = 'table' + str(table_name[0])

    reference_list = []
    count_page = 1  # start page

    # scrape reference from all pages
    while int(number_page) >= count_page:
        url_page = '{}?page={}'.format(url, str(count_page))
        response_page = scraper.get_response(url_page)
        link = scraper.get_links_to_ads(str(response_page.read().decode("utf-8")))
        reference_list.extend(link)
        count_page += 1

    bd_sqlite.create_parsing_table(table_name)

    pb['maximum'] = len(reference_list)
    # detailed information on the ads
    for link in reference_list:
        pb.step()
        window.update()
        r = scraper.get_response(link)
        cookie = scraper.get_cookie(r)
        html = str(r.read().decode("utf-8"))
        token, id_product = scraper.token_and_id(html)
        number, title, price_ua, date, time, place, content = scraper.get_details(html)
        phone = scraper.get_phone(id_product, token, cookie)
        price = int(scraper.get_digits(price_ua))

        bd_sqlite.insert_into_parsing_table(table_name, number, title, price, date, time, phone, place, content)

        lstbox.delete(0, 16)
        header = ' {} {} {} {} '.format('ID'.center(4, ' '),
                                        'Query Name'.center(25, ' '),
                                        'Url'.center(40, ' '),
                                        'N page'.center(8, ' '))
        lstbox.insert(0, header)
        data_from_query_table = bd_sqlite.select_from_query_table_all()
        for line, row in enumerate(data_from_query_table, 1):
            id_q = str(row[0]).center(4, ' ')
            name_q = utility.format_string(row[1], 25)
            url_q = utility.format_string(row[2], 40)
            page_q = str(row[3]).center(8, ' ')
            output = ' {} {} {} {} '.format(id_q, name_q, url_q, page_q)
            lstbox.insert(line, output)


def check(url, number_page, query_name):
    """input validation"""
    if url.startswith('https://www.olx.ua/'):
        pass
    else:
        return False
    if len(query_name) > 0:
        pass
    else:
        return False
    if number_page.isdigit():
        # get the last page
        response = scraper.get_response(url)
        html = str(response.read().decode("utf-8"))
        max_page = re.search(r'(?<="page_count":").*?(?=")', html)
        max_page = str(max_page.group(0))
        if number_page > max_page:
            number_page = max_page
        parsing(url, number_page, query_name)
    else:
        return False