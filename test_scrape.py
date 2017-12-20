import requests
from bs4 import BeautifulSoup
import re
import urllib.request


url_product = 'https://www.olx.ua/obyavlenie/botinki-zamberlan-expert-pro-gtx-rr-IDvHW6U.html#3e084819b6'

'''
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

# response_phone = requests.get(url_phone, headers=cookie)
# print(response_phone.text)

response_phone = session.get(url_phone)
print(response_phone.text)
'''


response = urllib.request.urlopen(url_product)
str_response = str(response.read().decode("utf-8"))

token = re.search(r"(?<=phoneToken\ =\ ')[\w\W]*?(?=';)", str_response)
token = str(token.group(0))
print(token)

id_product = re.search(r'(?<=ID)[\w\W]*?(?=\.html)', str_response)
id_product = str(id_product.group(0))
print(id_product)

cookie = response.getheader('Set-Cookie')
print(cookie)

url = 'https://www.olx.ua/ajax/misc/contact/phone/' + id_product +'/?pt=' + token
r = urllib.request.Request(url, headers={'Cookie': cookie})
phone_response = urllib.request.urlopen(r)
phone_response = str(phone_response.read().decode("utf-8"))

if 'block' in phone_response:
    phone = re.search(r'(?<=">)[\w\W]*?(?=<)', phone_response)
else:
    phone = re.search(r'(?<=":")[\w\W]*?(?=")', phone_response)
print(str(phone.group(0)))
