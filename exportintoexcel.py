import mysql.connector
from openpyxl import Workbook

db = mysql.connector.connect(
    host ='localhost',
    port = 3306,
    user = 'root',
    password = 'Bellic4825550100#',
    database = 'ink_want_to_buy'
)

cursor =db.cursor()
sql='''
    select *
    from products;
'''
cursor.execute(sql)
products = cursor.fetchall()

for p in products:
    print(p)

#Excel
workbook = Workbook()
sheet = workbook.active
sheet.append(
    ['ID','ชื่อสินค้า','ราคา','ความต้องการ','วันที่บันทึก']
)

for p in products:
    print(p)
    sheet.append(p)
workbook.save('export.xlsx')