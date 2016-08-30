# coding=utf-8
__author__ = 'lijinde-lhq'

import xlrd
from pymongo import MongoClient

# 连接数据库
client = MongoClient('localhost', 27017)
db = client.mydb
area = db.area

data = xlrd.open_workbook('d:\\area.xls')
table = data.sheets()[0]
# 读取excel第一行数据作为存入mongodb的字段名
rows_tag = table.row_values(0)
rows = table.nrows
print rows
returnData = {}
for i in range(1, rows):
    row = table.row_values(i)
    my_id = str(int(row[0]))
    level = str(int(row[1]))
    area_name = row[2]
    parent_id = str(int(row[3]))
    returnData["_id"] = my_id
    returnData["lever"] = level
    returnData["area_name"] = area_name
    returnData["parent_id"] = parent_id
    area.insert(returnData)