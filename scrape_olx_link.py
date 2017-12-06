# -*- coding: utf-8 -*-
import get_details
import bd_olx
import re
import urllib.request
import logging
import time
# logging.basicConfig(level = logging.DEBUG)


# url = 'https://www.olx.ua/odessa/q-zamberlan/' #main page


def get_response(url):
    """get html """
    response = urllib.request.urlopen(url)
    return response


def scrab_product(html):
    """get list of products on page """
    products = re.findall(r'(?<=<h3\ class="x-large)[\w\W]*?<div\ class="rel\ observelinkinfo', html)
    return products


def scrab_product_link(product):
    """get product link """
    link = re.search(r'(?<=a\ href=")[\w\W]*?\.html', product)
    return str(link.group(0))


def write_to_bd(name_bd, list_products):
    """write product details in sqlite """
    for pr in list_products:
        link = scrab_product_link(pr)
        response = get_response(link)
        # logging.debug('Work with page - ' + "[" + link + "]")
        str_response = str(response.read().decode("utf-8"))
        token = get_details.parse_token(str_response)
        id_post = get_details.parse_id_product(str_response)
        cookie = get_details.get_cookie(response)
        ad_number, title, price, date, place, content = get_details.parse_details(str_response)
        #time.sleep(2)
        bd_olx.insert_bd(name_bd, ad_number, title, price, date, place, content)
        # try:
        #    phone_response = get_details.get_response_phone(id_post, cookie, token)
        #    phone = get_details.scrab_number(phone_response)
        #    # logging.debug('Parse phone - ' + "[" + phone + "]")
        #    bd_olx.insert_bd(name_bd, ad_number, title, price, date, place, phone, content)
        # except:
        #    logging.warning("Product don't have number phone - " + "[" + link + "]")


def get_max_page(html):
    """get the last page """
    max_page = re.search(r'(?<="page_count":").*?(?=")', html)
    return str(max_page.group(0))


def start(url):
    name_bd = 'olx_sqlite'
    count_page = 1 # start page
    response = get_response(url)
    max_page = int(get_max_page(str(response.read().decode("utf-8"))))
    bd_olx.create_bd(name_bd)

    while max_page >= count_page:
        url_page = url + '?page=' + str(count_page)
        # print('url_page', url_page)
        logging.info('PAGE - [' + str(count_page) + ']')
        html = get_response(url_page)
        list_product = scrab_product(str(html.read().decode("utf-8")))
        logging.debug('Scrape list of products on page')
        write_to_bd(name_bd, list_product)
        count_page += 1

    logging.info('OK!')

