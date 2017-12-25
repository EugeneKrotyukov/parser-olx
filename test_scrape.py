import requests
from bs4 import BeautifulSoup
import re
import urllib.request
import urllib.error


# url_product = 'https://www.olx.ua/obyavlenie/botinki-zamberlan-expert-pro-gtx-rr-IDvHW6U.html#3e084819b6'
# url_product = 'https://www.olx.ua/obyavlenie/botinki-zamberlan-tofane-gtx-rr-IDvAANc.html#1f9e494dbf;promoted'
# url_product = 'https://www.olx.ua/obyavlenie/zamberlan-civetta-40-rozmrrealno-39-dovzhina-stelki-254mm-nov-IDvXlWV.html?sd=1#1f9e494dbf;promoted'
url_product = "https://www.olx.ua/obyavlenie/kabel-radiochastotnyy-koaksialnyy-rk50-4-11-IDqugUS.html#5550043ca5"

user_agent = 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Ubuntu Chromium/53.0.2785.143 Chrome/53.0.2785.143 Safari/537.36'

"""
#use requests
print('*' * 100)
print('*' * 100)
r = requests.get(url_product, headers={'user-agent': user_agent})
# print(r.request.headers) #заголовок, который я отправил на сервер
# print('URL: ', r.url)
# print('STATUS_CODE: ', r.status_code)
print('HEADERS: ', r.headers)
# print(r.headers['Content-Type'])
print('HEADERS Set-Cookie: ', r.headers['Set-Cookie'])
print('COOKIES: ', r.cookies)
# print('COOKIES_DICT: ', requests.utils.dict_from_cookiejar(r.cookies)) #преобразует CookiesJar в Dict

html = r.text

token = re.search(r"(?<=phoneToken\ =\ ')[\w\W]*?(?=';)", html)
token = str(token.group(0))
# print(token)

id_product = re.search(r'(?<=ID)[\w\W]*?(?=\.html)', html)
id_product = str(id_product.group(0))
# print(id_product)


url_phone = 'https://www.olx.ua/ajax/misc/contact/phone/' + id_product + '/?pt=' + token
# print(url_phone)

response_phone = requests.get(url_phone, headers=h)
print(response_phone.text)
# print(response_phone.request.headers)
"""


'''
#use requests.Session()
print('*' * 100)
print('*' * 100)
session = requests.Session()
response = session.get(url_product)
header = response.headers
# print(header)
cookie = response.cookies
# print(cookie)
set_cookie = response.headers['set-cookie']
# print(set_cookie)

html = response.text

token = re.search(r"(?<=phoneToken\ =\ ')[\w\W]*?(?=';)", html)
token = str(token.group(0))
print(token)

id_product = re.search(r'(?<=ID)[\w\W]*?(?=\.html)', html)
id_product = str(id_product.group(0))
print(id_product)

url_phone = 'https://www.olx.ua/ajax/misc/contact/phone/' + id_product + '/?pt=' + token
# print(url_phone)

response_phone = session.get(url_phone)
print(response_phone.text)
'''


#use urllib.request
print('*' * 100)
print('*' * 100)
r = urllib.request.Request(url_product, headers={'user-agent': user_agent})
response = urllib.request.urlopen(r)
str_response = str(response.read().decode("utf-8"))

b_soup = BeautifulSoup(str_response, 'html.parser')
soup = b_soup.find('div', attrs={'class': 'offer-titlebox'})
title = soup.find('h1').text.strip() # title
print(title)
place = soup.find('strong').text.strip() # place
print(place)
time_date = soup.find('em').text # time and date
time = re.search(r"(\d{1,2}:\d{1,2})", time_date)
time = str(time.group(0))
print(time)
date = re.search(r"(\d{1,2}\s\w{3,9}\s\d{4})", time_date)
date = str(date.group(0))
print(date)
number = soup.find('small').text[18:] # number
print(number)
price = b_soup.find('div', attrs={'class': 'price-label'}).text.strip() # price
print(price)
# content = b_soup.find('div', attrs={'id': 'textContent'}).text.strip() # content

token = re.search(r"(?<=phoneToken\ =\ ')[\w\W]*?(?=';)", str_response)
token = str(token.group(0))
# print(token)

id_product = re.search(r'(?<=ID)[\w\W]*?(?=\.html)', str_response)
id_product = str(id_product.group(0))
# print(id_product)

cookie = response.getheader('Set-Cookie')
# print('GET URL: ', response.geturl())
# print('GetCode : ', response.getcode())
# print('GetHeader Set-Cookie: ', cookie)

url = 'https://www.olx.ua/ajax/misc/contact/phone/' + id_product +'/?pt=' + token
r = urllib.request.Request(url, headers={'Cookie': cookie, 'user-agent': user_agent})


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
print(phone)