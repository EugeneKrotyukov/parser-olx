import urllib.request
from bs4 import BeautifulSoup


def get_response(url):
    """get html"""
    user_agent = 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Ubuntu Chromium/53.0.2785.143 Chrome/53.0.2785.143 Safari/537.36'
    r = urllib.request.Request(url, headers={'user-agent': user_agent})
    return urllib.request.urlopen(r)


def get_links_to_ads(html):
    """get list of products on page"""
    links = []
    soup = BeautifulSoup(html, 'html.parser')
    for result in soup.findAll('table', attrs={'summary': 'Объявление'}):
    # for result in soup.findAll('h3', attrs={'class': 'x-large lheight20 margintop5'}):
        link = result.find('a').get('href')
        if link.startswith('https://www.olx.ua/obyavlenie/'):
            links.append(link)
    return links


url = 'https://www.olx.ua/dom-i-sad/mebel/odessa/q-%D0%BC%D0%B0%D1%82%D1%80%D0%B0%D1%86/?search%5Bfilter_enum_state%5D%5B0%5D=new'
number_page = 4

reference_list = []
count_page = 1

while int(number_page) >= count_page:
    print('page ', count_page)
    url_page = '{}?page={}'.format(url, str(count_page))
    response_page = get_response(url_page)
    link = get_links_to_ads(str(response_page.read().decode("utf-8")))
    reference_list.extend(link)
    count_page += 1
print('Numbers of Ads ', len(reference_list))