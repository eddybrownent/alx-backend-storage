#!/usr/bin/env python3
"""
This function changes all topic of
school document based on name
"""


def update_topics(mongo_collection, name, topics):
    """
    Changes all topics of school document based on school name

    Argss:
        mongo_collection: MongoDB collection object
        name: school name to update
        topics: list of topics approached in school

    Returns:
        int number of documents updated
    """
    mongo_collection.update_many({"name": name},
                                 {"$set": {"topics": topics}})
