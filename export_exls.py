"""
https://xlsxwriter.readthedocs.io/getting_started.html
"""
from xlsxwriter.workbook import Workbook
import bd_sqlite
import utility


def set_lstbox(frame, widget):
    """set frame and listbox for GUI"""
    global window, lstbox
    window = frame
    lstbox = widget


def preview_tableID(id_table):
    """preview content TableID and export to excel"""
    header = ' {} {} {} {} {} '.format('No'.center(4, ' '),
                                      'Ad Number'.center(13, ' '),
                                      'Title'.center(45, ' '),
                                      'Price, UAH'.center(14, ' '),
                                      'Date'.center(18, ' '))
    lstbox.insert(0, header)
    table_name = 'table{}'.format(id_table)
    content = bd_sqlite.select_from_parsing_table_all(table_name)
    for line, row in enumerate(content, 1):
        no = str(line).center(4, ' ')
        number = str(row[0]).center(13, ' ')
        title = utility.format_string(row[1], 45)
        price = str(row[2]).center(14, ' ')
        date = utility.format_string(row[3], 18)
        output = ' {} {} {} {} {} '.format(no, number, title, price, date)
        lstbox.insert(line, output)


def export_exl(id_table, name):
    """export TableID to Excel"""
    table_name = 'table{}'.format(id_table)
    file_name = '{}.xlsx'.format(name)

    workbook = Workbook(file_name)
    worksheet = workbook.add_worksheet()

    format_title = workbook.add_format()
    format_cell = workbook.add_format()
    format_title.set_font_name('Times New Roman')
    format_title.set_font_size(12)
    format_title.set_align('center')
    format_title.set_bold()
    format_cell.set_font_name('Times New Roman')
    format_cell.set_font_size(12)
    format_cell.set_align('left')

    header = ['No', 'Ad Number', 'Title', 'Price, UAH', 'Date', 'Time', 'Phone', 'Location', 'Description']
    for col, val in enumerate(header):
        worksheet.write(0, col, val, format_title)

    content = bd_sqlite.select_from_parsing_table_all(table_name)
    for i, row in enumerate(content, 1):
        worksheet.write(i, 0, i, format_cell)
        for j, value in enumerate(row, 1):
            worksheet.write(i, j, value, format_cell)
    workbook.close()