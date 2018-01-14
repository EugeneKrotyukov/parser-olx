import bd_sqlite
import re


prices = bd_sqlite.select_from_bd('olx_sqlite')
print(prices)
list_prices = []
for element in prices:
    '''
    digit = ''
    for symbol in element[0]:
        if '0' <= symbol <= '9':
            digit += symbol
        else:
            break
    # digit = element[0].isdigit()
    '''
    # digit = re.search(r'\d', element[0])
    # digit = str(digit.group(0))
    print(type(element[0]))
    # list_prices.append(digit)
# print(list_prices)
