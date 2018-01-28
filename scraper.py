import bd_sqlite
import re
import urllib.request
import urllib.error
from bs4 import BeautifulSoup

"""
crawling - переход по страницам и ссылкам
scraping - сбор информации
parsing - crawling + scraping
"""

def get_response(url):
    """get html"""
    user_agent = 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Ubuntu Chromium/53.0.2785.143 Chrome/53.0.2785.143 Safari/537.36'
    r = urllib.request.Request(url, headers={'user-agent': user_agent})
    return urllib.request.urlopen(r)


# def get_max_page(html):
#    """get the last page"""
#    max_page = re.search(r'(?<="page_count":").*?(?=")', html)
#    return str(max_page.group(0))


def get_links_to_ads(html):
    """get list of products on page"""
    links = []
    soup = BeautifulSoup(html, 'html.parser')
    for result in soup.findAll('table', attrs={'summary': 'Объявление'}):
        link = result.find('a').get('href')
        links.append(link)
    return links


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
        if len(str_phone_response) > 30:
            phone = re.search(r'(?<=">)[\w\W]*?(?=<)', str_phone_response)
        else:
            phone = re.search(r'(?<=":")[\w\W]*?(?=")', str_phone_response)
        phone = str(phone.group(0))
    except urllib.error.URLError as e:
        phone = e.reason
    return phone


def get_details(html):
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


def get_digits(string):
    """clear the value read from the database"""
    digit = re.search(r'[0-9| ]+', string)  # finds all the digits
    digit = str(digit.group(0))
    digit = re.sub(r'\s', '', digit)  # removes all spaces
    return digit


