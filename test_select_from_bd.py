import bd_sqlite
import re


"""get list of prices"""
prices = bd_sqlite.select_from_bd('olx_sqlite')
print(prices)
list_prices = []
for element in prices:
    digit = re.search(r'[0-9| ]+', element[0])  # finds all the digits
    digit = str(digit.group(0))
    digit = re.sub(r'\s', '', digit)  # removes all spaces
    list_prices.append(int(digit))
# list_prices.sort()
print(list_prices)

"""dict: key - price, value - number of ads with this price"""
dict_count = {}
for price in list_prices:
    if price in dict_count:
        dict_count[price] += 1
    else:
        dict_count[price] = 1
print(dict_count.items())
