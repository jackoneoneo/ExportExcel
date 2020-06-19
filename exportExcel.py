'''
 把sqlite文件导入成excel
'''

from openpyxl import Workbook
import sqlite3





conn = sqlite3.connect(
    r"C:\Users\Administrator\Desktop\d2e9eb00db2020-06-02\d2e9eb00db2020-06-02\hdd\db\d2e9eb00db2020-06-02\01bcms1.db")
c = conn.cursor()

table_name_list = c.execute("SELECT name FROM sqlite_master where type='table' order by name")
table_list = []
for item in table_name_list:
    table_list.append(item[0])
# 创建excel
for item in table_list:
    wb = Workbook()
    ws = wb.active
    print(item)
    field_data_list = c.execute("PRAGMA table_info(" + item + ")")
    field_list = []
    for field in field_data_list:
        field_list.append(field[1])
    ws.append(field_list)
    sql = 'select * from %s' % (item)
    data_result_list = conn.execute(sql)
    for data in data_result_list:
        ws.append(list(data))
    wb.save(item + ".xlsx")

c.close()
conn.close()
