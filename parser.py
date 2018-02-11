import scraper
import bd_sqlite
import urllib.request


def set_pb(frame, widget):
    """set frame and progressbar for GUI"""
    global window, pb
    pb = widget
    window = frame


def parsing(url, number_page):
    if scraper.check_url(url):
        tested_number_page = scraper.check_number_page(url, number_page)
        if tested_number_page:
            reference_list = []
            count_page = 1  # start page

            # scrape reference from all pages
            while int(tested_number_page) >= count_page:
                url_page = '{}?page={}'.format(url, str(count_page))
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
                window.update()
                r = scraper.get_response(link)
                cookie = scraper.get_cookie(r)
                html = str(r.read().decode("utf-8"))
                token, id_product = scraper.token_and_id(html)
                number, title, price_ua, date, time, place, content = scraper.get_details(html)
                phone = scraper.get_phone(id_product, token, cookie)
                price = int(scraper.get_digits(price_ua))
                # write to bd
                bd_sqlite.insert_into_bd(number, title, price, date, time, phone, place, content)
