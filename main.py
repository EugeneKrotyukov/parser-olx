import bd_sqlite
import re
import urllib.request
import urllib.error
from bs4 import BeautifulSoup
# from numpy import mean, std

"""
crawling - переход по страницам и ссылкам
scraping - сбор информации
parsing - crawling + scraping
"""

def get_response(url):
    """get html"""
    user_agent = 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Ubuntu Chromium/53.0.2785.143 Chrome/53.0.2785.143 Safari/537.36'
    r = urllib.request.Request(url, headers={'user-agent': user_agent})
    response = urllib.request.urlopen(r)
    return response


def get_max_page(html):
    """get the last page"""
    max_page = re.search(r'(?<="page_count":").*?(?=")', html)
    return str(max_page.group(0))


def get_link_for_product(html):
    """get list of products on page"""
    link_products = []
    soup = BeautifulSoup(html, 'html.parser')
    for result in soup.findAll('table', attrs={'summary': 'Объявление'}):
        product = result.find('a').get('href')
        link_products.append(product)
    return link_products


def get_cookie(response):
    """get cookie"""
    return response.getheader('Set-Cookie')


def token_and_id(html):
    """get token_phone and id_product"""
    token = re.search(r"(?<=phoneToken\ =\ ')[\w\W]*?(?=';)", html)
    id_product = re.search(r'(?<=ID)[\w\W]*?(?=\.html)', html)
    return str(token.group(0)), str(id_product.group(0))


def get_phone(id_product, token, cookie):
    """get phone"""
    # 295659644
    url = 'https://www.olx.ua/ajax/misc/contact/phone/' + id_product +'/?pt=' + token
    user_agent = 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Ubuntu Chromium/53.0.2785.143 Chrome/53.0.2785.143 Safari/537.36'
    r = urllib.request.Request(url, headers={'user-agent': user_agent, 'Cookie': cookie})
    try:
        phone_response = urllib.request.urlopen(r)
        str_phone_response = str(phone_response.read().decode("utf-8"))
        if len(str_phone_response) > 30:
            phone = re.search(r'(?<=">)[\w\W]*?(?=<)', str_phone_response)
        else:
            phone = re.search(r'(?<=":")[\w\W]*?(?=")', str_phone_response)
        phone = str(phone.group(0))
    except urllib.error.URLError as e:
        phone = e.reason
    return phone


def parse_details(html):
    """get number, title, price, date, time, place, content"""
    b_soup = BeautifulSoup(html, 'html.parser')
    soup = b_soup.find('div', attrs={'class': 'offer-titlebox'})
    title = soup.find('h1').text.strip()  # title
    place = soup.find('strong').text.strip()  # place
    time_date = soup.find('em').text  # time and date
    time = re.search(r"(\d{2}:\d{2})", time_date)
    time = str(time.group(0))
    date = re.search(r"(\d{1,2}\s\w{3,9}\s\d{4})", time_date)
    date = str(date.group(0))
    number = soup.find('small').text[18:]  # number
    try:
        price = b_soup.find('div', attrs={'class': 'price-label'}).text.strip()  # price
    except AttributeError:
        price = None
    try:
        content = b_soup.find('div', attrs={'id': 'textContent'}).text.strip()  # content
    except AttributeError:
        content = None
    # link_img = b_soup.find('div', attrs={'id': 'offerdescription'}
    return number, title, price, date, time, place, content

def set_pb( a_pb, a_root):
    """set progressbar, root for GUI"""
    global pb, root
    pb = a_pb
    root = a_root

def scrape(list_product):
    """scrape data and write to base"""
    bd_sqlite.create_bd('olx_sqlite')
    pb['maximum'] = len(list_product)
    for link in list_product:

        pb.step()
        root.update()

        r = get_response(link)
        cookie = get_cookie(r)
        html = str(r.read().decode("utf-8"))
        token, id_product = token_and_id(html)
        number, title, price, date, time, place, content = parse_details(html)
        phone = get_phone(id_product, token, cookie)

        # numbers = bd_sqlite.select_from_bd_column('olx_sqlite', 'number')
        # if number in numbers:
        #    price = bd_sqlite.select_from_bd_value('olx_sqlite', 'price', number)
        #    print(price)

        bd_sqlite.insert_into_bd('olx_sqlite', number, title, price, date, time, phone, place, content)


def get_list_product(url, number_page):
    """get list links"""
    list_product = []
    count_page = 1  # start page
    # response = get_response(url)
    # max_page = int(get_max_page(str(response.read().decode("utf-8"))))

    while int(number_page) >= count_page:
        url_page = url + '?page=' + str(count_page)
        response_page = get_response(url_page)
        link = get_link_for_product(str(response_page.read().decode("utf-8")))
        list_product.extend(link)
        # parse_product(list_product)
        count_page += 1

    scrape(list_product)


def select_prices():
    """get list of prices"""
    prices = bd_sqlite.select_from_bd_column('olx_sqlite', 'price')
    print(prices)
    list_prices = []
    for element in prices:
        if element[0] is not None:
            digit = re.search(r'[0-9| ]+', element[0])  # finds all the digits
            digit = str(digit.group(0))
            digit = re.sub(r'\s', '', digit)  # removes all spaces
            list_prices.append(int(digit))
    list_prices.sort()
    print(list_prices)
    return list_prices


# def filter_prices(prices):
#    """filters prices for standard deviation"""
#    filter_list = []
#    # mean_price = mean(prices)
#    std_price = std(prices)
#    for e, price in enumerate(prices, -1):
#        if price <= std_price:
#            filter_list.append(price)
#        else:
#            if price <= prices[e] + std_price:
#                filter_list.append(price)
#    # filter_list = [price for price in prices if price < (mean_price+std_price)]
#    return filter_list


def calculate_statistics(list_prices):
    """dict: key - price, value - number of ads with this price"""
    price_count = {}
    for price in list_prices:
        if price in price_count:
            price_count[price] += 1
        else:
            price_count[price] = 1
    return price_count


# def filter_statistics(statistics):
#    """filter by values less than 1%"""
#    value = list(statistics.values())
#    threshold = max(value) // 10  # 10%
#    price_count_filter = {price: count for price, count in statistics.items() if count > threshold}
#    return price_count_filter




