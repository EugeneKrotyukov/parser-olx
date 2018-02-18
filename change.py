import bd_sqlite
import scraper
from bs4 import BeautifulSoup


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


def get_data(html):
    """get number, title, price"""
    b_soup = BeautifulSoup(html, 'html.parser')
    soup = b_soup.find('div', attrs={'class': 'offer-titlebox'})
    title = soup.find('h1').text.strip()  # title
    number = soup.find('small').text[18:]  # number
    try:
        price = b_soup.find('div', attrs={'class': 'price-label'}).text.strip()  # price
    except AttributeError:
        price = None
    return number, title, price


def format_string(string, width):
    if len(string) <= width:
        string = string.ljust(width, ' ')
    else:
        string = '{}...'.format(string[:46])
    return string


def get_change(window, id_table):
    """ads with a changed price"""
    table_name = 'table{}'.format(id_table)
    query_table_from_bd = bd_sqlite.select_from_query_table_value(id_table)
    query_table = [item for sublist in query_table_from_bd for item in sublist]
    url = query_table[2]
    number_page = query_table[3]
    ad_numbers_from_bd = bd_sqlite.select_from_parsing_table_column('number', table_name)
    ad_numbers = [item for sublist in ad_numbers_from_bd for item in sublist]

    reference_list = []
    count_page = 1  # start page
    line = 0  # position number to insert into in listbox
    lstbox.delete(0, 23)

    # scrape reference from all pages
    while int(number_page) >= count_page:
        url_page = '{}?page={}'.format(url, str(count_page))
        response_page = scraper.get_response(url_page)
        link = scraper.get_links_to_ads(str(response_page.read().decode("utf-8")))
        reference_list.extend(link)
        count_page += 1

    header = '|{}|{}|{}|{}|'.format('Ad Number'.center(13), 'Title'.center(77), 'Old Price, UAH'.center(16), 'New Price, UAH'.center(16))
    lstbox.insert(line, header)

    pb['maximum'] = len(reference_list)
    # detailed information on the ads
    for link in reference_list:
        pb.step()
        window.update()
        r = scraper.get_response(link)
        html = str(r.read().decode("utf-8"))
        number, title, new_price = get_data(html)
        new_price = int(scraper.get_digits(new_price))
        if number in ad_numbers:
            price_from_bd = bd_sqlite.select_from_parsing_table_value('price', table_name, number)
            old_price = price_from_bd[0]
            if new_price != old_price:
                number = str(number).center(11, ' ')
                title = format_string(title, 54)
                old_price = str(old_price).center(21, ' ')
                new_price = str(new_price).center(23, ' ')
                line += 1
                output = '| {} | {} | {} | {} |'.format(number, title, old_price, new_price)
                lstbox.insert(line, output)