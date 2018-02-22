import bd_sqlite


def set_lstbox(frame, widget):
    """set frame and listbox for GUI"""
    global window, lstbox
    window = frame
    lstbox = widget


def format_string(string, width):
    """formatting data from the DB before output to the frame ListBox"""
    if len(string) <= width:
        string = string.ljust(width, ' ')
    else:
        string = '{}...'.format(string[:(width - 3)])
    return string

'''
def format_string(string, width):
    """formatting data in BYTE from the DB before output to the frame ListBox"""
    byte = string.encode()
    if len(byte) <= width:
        string = string.ljust(width, ' ')
    else:
        try:
            b_try = byte[:(width - 3)]
            string = b_try.decode()
            string = '{}...'.format(string)
        except UnicodeDecodeError:
            b_exc = byte[:(width - 2)]
            string = b_exc.decode()
            string = '{}..'.format(string)
    return string
'''

def del_query(id_table):
    table_name = 'table{}'.format(id_table)
    bd_sqlite.drop_parsing_table(table_name)
    bd_sqlite.del_from_query_table_row(id_table)
    lstbox.delete(0, 16)
    data_from_query_table = bd_sqlite.select_from_query_table_all()

    header = ' {} {} {} {} '.format('ID'.center(8, ' '),
                                    'Query Name'.center(40, ' '),
                                    'Url'.center(40, ' '),
                                    'N page'.center(8, ' '))
    lstbox.insert(0, header)
    for line, row in enumerate(data_from_query_table, 1):
        id_q = str(row[0]).center(8, ' ')
        name_q = format_string(row[1], 40)
        url_q = format_string(row[2], 40)
        page_q = str(row[3]).center(8, ' ')
        output = ' {} {} {} {} '.format(id_q, name_q, url_q, page_q)
        lstbox.insert(line, output)