import requests
from bs4 import BeautifulSoup
import re
import urllib.request


# url_product = 'https://www.olx.ua/obyavlenie/botinki-zamberlan-expert-pro-gtx-rr-IDvHW6U.html#3e084819b6'
url_product = 'https://www.olx.ua/obyavlenie/mikrodvigatel-talka-tayfun-IDvVMHs.html#daa3b1175e'


'''
#use requests
header = {'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Ubuntu Chromium/53.0.2785.143 Chrome/53.0.2785.143 Safari/537.36'}

r = requests.get(url_product, headers=header)
# print(r.request.headers) #заголовок, который я отправил на сервер
h = r.headers
# print(h)
c = r.cookies
# dict_c = requests.utils.dict_from_cookiejar(r.cookies) #преобразует CookiesJar в Dict
# print(dict_c)
# pt = dict_c['pt']

html = r.text

token = re.search(r"(?<=phoneToken\ =\ ')[\w\W]*?(?=';)", html)
token = str(token.group(0))
# print(token)

id_product = re.search(r'(?<=ID)[\w\W]*?(?=\.html)', html)
id_product = str(id_product.group(0))
# print(id_product)

url_phone = 'https://www.olx.ua/ajax/misc/contact/phone/' + id_product + '/?pt=' + token
# print(url_phone)

response_phone = requests.get(url_phone, headers=h, cookies=c)
print(response_phone.text)
# print(response_phone.request.headers)
'''


'''
#use requests.Session()
session = requests.Session()
response = session.get(url_product)
header = response.headers
# print(headers)
cookie = response.cookies
# print(cookies)
# set_cookie = response.headers['set-cookie']
# print(set_cookie)
# token = re.search(r"(?<=pt=)(.+?);", set_cookie)
# token = str(token.group(0))
# print(token)

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
r = urllib.request.Request(url_product, headers={'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Ubuntu Chromium/53.0.2785.143 Chrome/53.0.2785.143 Safari/537.36'})
response = urllib.request.urlopen(r)
str_response = str(response.read().decode("utf-8"))

token = re.search(r"(?<=phoneToken\ =\ ')[\w\W]*?(?=';)", str_response)
token = str(token.group(0))
# print(token)

id_product = re.search(r'(?<=ID)[\w\W]*?(?=\.html)', str_response)
id_product = str(id_product.group(0))
# print(id_product)

cookie = response.getheader('Set-Cookie')
# print(cookie)

url = 'https://www.olx.ua/ajax/misc/contact/phone/' + id_product +'/?pt=' + token
r = urllib.request.Request(url, headers={'Cookie': cookie, 'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Ubuntu Chromium/53.0.2785.143 Chrome/53.0.2785.143 Safari/537.36'})
phone_response = urllib.request.urlopen(r)
str_phone_response = str(phone_response.read().decode("utf-8"))
# print(str_phone_response)

if 'block' in phone_response:
    phone = re.search(r'(?<=">)[\w\W]*?(?=<)', str_phone_response)
else:
    phone = re.search(r'(?<=":")[\w\W]*?(?=")', str_phone_response)
print(str(phone.group(0)))
