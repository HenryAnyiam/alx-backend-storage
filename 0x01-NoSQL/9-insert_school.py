#!/usr/bin/env python3
"""insert into mongodb collection"""


def insert_school(mongo_collection, **kwargs):
    """insert into mongo_collection and return id"""
    return mongo_collection.insert_one(kwargs).inserted_id
