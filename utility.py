def format_string(string, width):
    if len(string) <= width:
        string = string.ljust(width, ' ')
    else:
        string = '{}...'.format(string[:(width-3)])
    return string


'''
s_ru = 'ЙЦУКЕНГШЩЗ'
s_en = 'ZXCVBNMASD'
s_dg = '1234567890'
s_ii = 'iiiiiiiiii'
s___ = 'ШШШШШШШШШШ'
'''