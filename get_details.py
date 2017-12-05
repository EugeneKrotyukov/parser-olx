# -*- coding: utf-8 -*-
import re
import urllib.request
from bs4 import BeautifulSoup


def get_response_phone(id_product, cookie, token):
    url = 'https://www.olx.ua/ajax/misc/contact/phone/' + id_product +'/?pt=' + token
    r = urllib.request.Request(url, headers={'Cookie': cookie})
    phone = urllib.request.urlopen(r)
    return str(phone.read().decode("utf-8"))

def parse_token(html):
    token = re.search(r"(?<=phoneToken\ =\ ')[\w\W]*?(?=';)", html)
    return str(token.group(0))

def parse_id_product(html):
    id_product = re.search(r'(?<=ID)[\w\W]*?(?=\.html)', html)
    return str(id_product.group(0))

def parse_details(html):
    '''детали'''
    b_soup = BeautifulSoup(html, 'html.parser')
    soup = b_soup.find('div', attrs={'class': 'offer-titlebox'})
    title = soup.find('h1').text.strip() # название
    place = soup.find('strong').text.strip() # город
    time_date = soup.find('em').text.strip()[52:72] # дата, время размещения
    time, date = time_date.split(',')
    ad_number = soup.find('small').text[18:] # номер объявления
    price = b_soup.find('div', attrs={'class': 'price-label'}).text.strip() # цена
    content = b_soup.find('div', attrs={'id': 'textContent'}).text.strip() # описание
    # link_img = b_soup.find('div', attrs={'id': 'offerdescription'})
    return ad_number, title, price, date, place, content


def scrab_number(phone_response):
    if 'block' in phone_response:
        phone = re.search(r'(?<=">)[\w\W]*?(?=<)', phone_response)
    else:
        phone = re.search(r'(?<=":")[\w\W]*?(?=")', phone_response)
    return str(phone.group(0))


def get_cookie(response):
    """get cookie """
    return response.getheader('Set-Cookie')
