#!/usr/bin/env python3
"""calculate average score of students"""


def top_students(mongo_collection):
    """gets student data and calculate average score"""
    students = list(mongo_collection.find())
    new_data = []
    for i in students:
        student = {}
        student['_id'] = i.get('_id')
        student['name'] = i.get('name')
        topics = i.get('topics')
        topic = 0
        total = 0
        for i in topics:
            topic += 1
            total += i.get('score')
        student['averageScore'] = total / topic
        new_data.append(student)
    new_data.sort(key=lambda x: x['averageScore'], reverse=True)
    return new_data
