#!/usr/bin/env python3
"""use the pymongos find with a filter"""


def schools_by_topic(mongo_collection, topic):
    """return lists of school that match a topic"""
    return list(mongo_collection.find({'topics': {'$in': [topic]}}))
