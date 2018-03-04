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


def display_query_table():
    header = ' {} {} {} {} '.format('ID'.center(4, ' '),
                                    'Query Name'.center(30, ' '),
                                    'Url'.center(50, ' '),
                                    'N Ads'.center(8, ' '))
    lstbox.insert(0, header)
    content = bd_sqlite.select_from_query_table_all()
    for line, row in enumerate(content, 1):
        id_q = str(row[0]).center(4, ' ')
        table_name = 'table{}'.format(row[0])
        n_ads = bd_sqlite.select_number_rows(table_name)
        n_ads = str(n_ads).center(8, ' ')
        name_q = format_string(row[1], 30)
        url_q = format_string(row[2], 50)
        output = ' {} {} {} {} '.format(id_q, name_q, url_q, n_ads)
        lstbox.insert(line, output)


def del_query(id_table):
    table_name = 'table{}'.format(id_table)
    bd_sqlite.drop_parsing_table(table_name)
    bd_sqlite.del_from_query_table_row(id_table)
    display_query_table()
