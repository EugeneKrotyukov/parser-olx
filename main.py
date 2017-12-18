import get_details
import bd_sqlite
import re
import requests
from bs4 import BeautifulSoup


# url = 'https://www.olx.ua/odessa/q-zamberlan/' #main page


def get_response(url):
    """get html"""
    response = requests.get(url)
    return response


def get_max_page(html):
    """get the last page"""
    max_page = re.search(r'(?<="page_count":").*?(?=")', html)
    return str(max_page.group(0))


def scrab_product(html):
    """get list of products on page"""
    products = list()
    soup = BeautifulSoup(html, 'html.parser')
    for result in soup.findAll('table', attrs={'summary': 'Объявление'}):
        product = result.find('a').get('href')
        products.append(product)
        # print(product)
    return products


def token_and_id_(html):
    token = re.search(r"(?<=phoneToken\ =\ ')[\w\W]*?(?=';)", html)
    # print(str(token.group(0)))
    id_product = re.search(r'(?<=ID)[\w\W]*?(?=\.html)', html)
    # print(str(id_product.group(0)))
    return str(token.group(0)), str(id_product.group(0))


# def parse_id_product(html):
#    id_product = re.search(r'(?<=ID)[\w\W]*?(?=\.html)', html)
#    # print(str(id_product.group(0)))
#    return str(id_product.group(0))


def parse_details(html):
    """get number, title, price, date, time, place, content"""
    b_soup = BeautifulSoup(html, 'html.parser')
    soup = b_soup.find('div', attrs={'class': 'offer-titlebox'})
    title = soup.find('h1').text.strip() # title
    place = soup.find('strong').text.strip() # place
    time_date = soup.find('em').text.strip()[52:73] # time and date
    time, date = time_date.split(',')
    number = soup.find('small').text[18:] # number
    price = b_soup.find('div', attrs={'class': 'price-label'}).text.strip() # price
    content = b_soup.find('div', attrs={'id': 'textContent'}).text.strip() # content
    # link_img = b_soup.find('div', attrs={'id': 'offerdescription'})
    # print(number, title, price, date, time, place)
    return number, title, price, date, time, place, content


def parse_product(links):
    """parsing product details and write in sqlite"""
    for link in links:
        r = get_response(link)
        number, title, price, date, time, place, content = parse_details(r.text)
        bd_sqlite.insert_bd(name_bd, number, title, price, date, time, place, content)


def start(url):
    bd_sqlite.create_bd(name_bd)
    count_page = 1 # start page
    response = get_response(url)
    max_page = int(get_max_page(response.text))
    # print(max_page)

    while max_page >= count_page:
        url_page = url + '?page=' + str(count_page)
        # print(url_page)
        response_page = get_response(url_page)
        list_product = scrab_product(response_page.text)
        parse_product(list_product)
        count_page += 1


name_bd = 'olx_sqlite'