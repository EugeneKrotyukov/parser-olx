import scraper
import bd_sqlite
import plot
import urllib.request


def set_pb( a_pb, a_root):
    """set progressbar and root for GUI"""
    global pb, root
    pb = a_pb
    root = a_root


def parsing(url, number_page):
    reference_list = []
    count_page = 1  # start page
    # response = get_response(url)
    # max_page = int(get_max_page(str(response.read().decode("utf-8"))))

    # scrape reference from all pages
    while int(number_page) >= count_page:
        url_page = url + '?page=' + str(count_page)
        response_page = scraper.get_response(url_page)
        link = scraper.get_links_to_ads(str(response_page.read().decode("utf-8")))
        reference_list.extend(link)
        count_page += 1

    # create table
    bd_sqlite.create_bd()

    pb['maximum'] = len(reference_list)
    # detailed information on the ads
    for link in reference_list:
        pb.step()
        root.update()
        r = scraper.get_response(link)
        cookie = scraper.get_cookie(r)
        html = str(r.read().decode("utf-8"))
        token, id_product = scraper.token_and_id(html)
        number, title, price, date, time, place, content = scraper.get_details(html)
        phone = scraper.get_phone(id_product, token, cookie)

        # write to bd
        bd_sqlite.insert_into_bd(number, title, price, date, time, phone, place, content)
