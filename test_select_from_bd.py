import bd_sqlite
import re


"""get list of prices"""
prices = bd_sqlite.select_from_bd('olx_sqlite')
# print(prices)
list_prices = []
for element in prices:
    digit = re.search(r'[0-9| ]+', element[0])  # finds all the digits
    digit = str(digit.group(0))
    digit = re.sub(r'\s', '', digit)  # removes all spaces
    list_prices.append(int(digit))
list_prices.sort()
print(list_prices)
print(list_prices[-1], list_prices[0])

"""dict: key - price, value - number of ads with this price"""
dict_count = {}
for price in list_prices:
    if price in dict_count:
        dict_count[price] += 1
    else:
        dict_count[price] = 1
print(dict_count.items())

# sort_dict_count = sorted(dict_count, key=dict_count.get)
count = sorted(dict_count.values())
print(count[-1], count[0])

long_x = 700
long_y = 500
# scale_x = round(long_x / list_prices[-1], 2)
# scale_y = round(long_y / count[-1], 2)
# print(scale_x, scale_y)



