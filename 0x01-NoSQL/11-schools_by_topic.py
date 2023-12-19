#!/usr/bin/env python3
"""
Function that returns the list of school
having a specific topic
"""


def schools_by_topic(mongo_collection, topic):
    """
    List of school having a specific tpoic

    Args:
        mongo_collection: mongo collection object
        topic: the topict to check of

    Return:
        list: list of the schools with that topic
    """
    ls = mongo_collection.find({"topics": topic})
    return ls
