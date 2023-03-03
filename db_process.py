# -*- coding: utf-8 -*-


import time
import os
import urllib.request
import requests
import datetime
import sys

import sqlite3
import xlrd


# # Open the Excel file
# workbook = xlrd.open_workbook('mylibrary.xls')

# # Select the first sheet
# worksheet = workbook.sheet_by_index(0)

# # Get the value of the cell in the first row and first column
# value = worksheet.cell(0, 0).value

# # Print the value
# print(value)

# num_rows = worksheet.nrows
# num_cols = worksheet.ncols

# for i in range(num_rows):
#     for j in range(num_cols):
#         cell_value = worksheet.cell_value(i, j)
#         print(cell_value)


import pandas as pd

# Load the XLSX file into a Pandas DataFrame
df = pd.read_excel('mylibrary.xls', sheet_name='图书')

# Convert the DataFrame to a list of dicts
data = df.to_dict('records')

# Print the list of dicts
# print(data)

# data[lens]
print(data[0]['標題'])
print(data[0]['ISBN'])
print(data[0]['封面路徑'])


book_num = len(data)
print(book_num)

update_ISBN = "UPDATE BOOK SET ISBN = " + str(data[0]['ISBN']) +  " WHERE COVER_PATH = '" +  data[0]['封面路徑'] + "'"
print (update_ISBN)

# replace 's to ''s to avoid sqlite3.OperationalError: near "s": syntax error


for i in range(book_num):
    data[i]['標題'] = data[i]['標題'].replace("'", "''")

conn = sqlite3.connect('mylibrary.db')
c = conn.cursor()

# c.execute("SELECT * FROM BOOK")

# # Fetch all rows and print data
# rows = c.fetchall()
# for row in rows:
#     print(row)


for i in range(book_num):
    update_ISBN     = "UPDATE BOOK SET ISBN = " + str(data[i]['ISBN']) +  " WHERE COVER_PATH = '" +  data[i]['封面路徑'] + "'"
    update_title    = "UPDATE BOOK SET TITLE = " + "'" + data[i]['標題'] + "'"+  " WHERE COVER_PATH = '" +  data[i]['封面路徑'] + "'"
    print (update_title)
    c.execute(update_ISBN)
    c.execute(update_title)


conn.commit()

# Close connection
conn.close()



time.sleep(5)
