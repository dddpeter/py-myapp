#!/usr/bin/env python
# -*- coding: utf-8 -*-

import pymongo
import json


def is_json(vjson):
    try:
        json.dumps(vjson)
    except ValueError:
        return False
    return True


def get_db(db_name, host="127.0.0.1", port=27017):
    # 建立连接
    client = pymongo.MongoClient(host, port)
    database = client[db_name]
    return database


def get_collection(db, collection_name):
    # 选择集合（mongo中collection和database都是延时创建的）
    collection = db[collection_name]
    print db.collection_names()
    return collection


def insert(db, collection_name, doc):
    # 插入一个document
    if is_json(doc):
        collection = db[collection_name]
        information_id = collection.insert(doc)
        print information_id
        return information_id
    else:
        return None


def get(db, collection_name, queryJson={}):
    # 有就返回一个，没有就返回None
    if is_json(queryJson):
        coll = db[collection_name]
        result_list = coll.find(queryJson)  # 返回第一条记录
        return result_list
    else:
        return None

def clear_all_datas(db, collection_name):
    #清空一个集合中的所有数据
    db[collection_name].remove()

if __name__ == '__main__':
    db = get_db('mydb')
    cl = get(db, 'informations')
    for item in cl:
        print item