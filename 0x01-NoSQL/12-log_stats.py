#!/usr/bin/env python3
"""calculate nginx log stats"""
from pymongo import MongoClient


if __name__ == "__main__":
    client = MongoClient("mongodb://127.0.0.1:27017")
    collection = client.logs.nginx
    total_logs = len(list(collection.find()))
    post = len(list(collection.find({'method' : 'POST'})))
    get = len(list(collection.find({'method' : 'GET'})))
    put = len(list(collection.find({'method' : 'PUT'})))
    patch = len(list(collection.find({'method' : 'PATCH'})))
    delete = len(list(collection.find({'method' : 'DELETE'})))
    status = len(list(collection.find({'method' : 'GET', 'path': '/status'})))
    print(f"{total_logs} logs")
    print("Methods:")
    print(f"\tmethod GET: {get}")
    print(f"\tmethod POST: {post}")
    print(f"\tmethod PUT: {put}")
    print(f"\tmethod PATCH: {patch}")
    print(f"\tmethod DELETE: {delete}")
    print(f"{status} status check")
