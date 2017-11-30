import requests
from bs4 import BeautifulSoup
import re

'''
url = 'https://www.olx.ua/list/q-%D0%91%D0%BE%D1%82%D0%B8%D0%BD%D0%BA%D0%B8-Zamberlan-Expert-Pro/'
response = requests.get(url)

#список всех объявлений
links = list()
soup = BeautifulSoup(response.text, 'html.parser')
for result in soup.findAll('table', attrs={'summary': 'Объявление'}):
    links.append(result.find('a', href=True))

for index, item in enumerate(links, start=1):
    print(index, item['href'])
'''

url = 'https://www.olx.ua/obyavlenie/botinki-zamberlan-expert-pro-alpinizm-IDtfBnU.html?sd=1#3e084819b6'

'''
# v1 без  использования сессии
response = requests.get(url)
print(response.status_code)
# идентификатор
identifier = re.findall('ID(.+?)\.', url)
id = identifier[0]
print(id)
# токен
token = re.findall('pt=(.+?) ', str(response.cookies))
pt = token[0]
print(pt)
print(response.headers)
print(response.cookies)

url = 'https://www.olx.ua/ajax/misc/contact/phone/{}/?pt={}'.format(id, pt)
print(url)

# headers in manual
# headers = {
#    'Accept': '*/*',
#    'Accept-Encoding': 'gzip, deflate, sdch, br',
#    'Accept-Language': 'en-US, en; q=0.8',
#    'Connection': 'keep-alive',
#    'Host': 'www.olx.ua',
#    'Referer': 'https://www.olx.ua/obyavlenie/botinki-zamberlan-expert-pro-alpinizm-IDtfBnU.html?sd=1',
#    'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Ubuntu Chromium/53.0.2785.143 Chrome/53.0.2785.143 Safari/537.36'
# }
# response2 = requests.get(url, headers=headers, cookies=response.cookies)

response2 = requests.get(url, headers=response.headers, cookies=response.cookies)
print(response2.status_code)
print(response2.text)
'''


# v2 с использованием сессии
with requests.Session() as session:

    response = requests.get(url)
    print(response.status_code)
    # идентификатор
    identifier = re.findall('ID(.+?)\.', url)
    id = identifier[0]
    print(id)
    # токен
    token = re.findall('pt=(.+?) ', str(response.cookies))
    pt = token[0]
    print(pt)
    print(response.headers)
    print(response.cookies)

    url = 'https://www.olx.ua/ajax/misc/contact/phone/{}/?pt={}'.format(id, pt)
    print(url)
    response2 = session.get(url, headers=response.headers, cookies=response.cookies)
    print(response2.status_code)
    print(response2.text)



'''
# парсинг страницы
content = list()
soup = BeautifulSoup(response.text, 'html.parser')
result = soup.find('div', attrs={'class': 'offer-titlebox'})
content.append(result.find('h1').text.strip())
content.append(result.find('strong').text.strip())
content.append('Добавлено: {}'.format(result.find('em').text.strip()[50:75]))
content.append(result.find('small').text)
result = soup.find('div', attrs={'id': 'textContent'}).text
content.append(result.strip())
result = soup.find('div', attrs={'class': 'price-label'}).text
content.append(result.strip())

for index, item in enumerate(content, start=1):
    print(index, item)
'''