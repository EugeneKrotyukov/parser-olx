import bd_sqlite
import re
import urllib.request
import urllib.error
from bs4 import BeautifulSoup


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


def scrab_product(html):
    """get list of products on page"""
    products = []
    soup = BeautifulSoup(html, 'html.parser')
    for result in soup.findAll('table', attrs={'summary': 'Объявление'}):
        product = result.find('a').get('href')
        products.append(product)
    return products


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
    url = 'https://www.olx.ua/ajax/misc/contact/phone/' + id_product +'/?pt=' + token
    user_agent = 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Ubuntu Chromium/53.0.2785.143 Chrome/53.0.2785.143 Safari/537.36'
    r = urllib.request.Request(url, headers={'user-agent': user_agent, 'Cookie': cookie})
    try:
        phone_response = urllib.request.urlopen(r)
        str_phone_response = str(phone_response.read().decode("utf-8"))
        if 'block' in phone_response:
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
    title = soup.find('h1').text.strip() # title
    place = soup.find('strong').text.strip() # place
    time_date = soup.find('em').text # time and date
    time = re.search(r"(\d{2}:\d{2})", time_date)
    time = str(time.group(0))
    date = re.search(r"(\d{1,2}\s\w{3,9}\s\d{4})", time_date)
    date = str(date.group(0))
    number = soup.find('small').text[18:] # number
    price = b_soup.find('div', attrs={'class': 'price-label'}).text.strip() # price
    content = b_soup.find('div', attrs={'id': 'textContent'}).text.strip() # content
    # link_img = b_soup.find('div', attrs={'id': 'offerdescription'})
    return number, title, price, date, time, place, content


def start(url, number_page):
    bd_sqlite.create_bd(name_bd)
    count_page = 1 # start page
    response = get_response(url)
    # max_page = int(get_max_page(str(response.read().decode("utf-8"))))

    while int(number_page) >= count_page:
        url_page = url + '?page=' + str(count_page)
        response_page = get_response(url_page)
        list_product = scrab_product(str(response_page.read().decode("utf-8")))
        # parse_product(list_product)

        for link in list_product:
            r = get_response(link)
            cookie = get_cookie(r)
            html = str(r.read().decode("utf-8"))
            token, id_product = token_and_id(html)
            number, title, price, date, time, place, content = parse_details(html)
            phone = get_phone(id_product, token, cookie)
            bd_sqlite.insert_bd(name_bd, number, title, price, date, time, phone, place, content)

        count_page += 1


name_bd = 'olx_sqlite'