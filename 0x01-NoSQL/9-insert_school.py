#!/usr/bin/env python3
"""
This fumction inserts a new document in a collection
"""


def insert_school(mongo_collection, **kwargs):
    """
    Inserts document into a collection based on keyword args

    Parameters:
        mongo_collection: MongoDB collection object
        **kwargs: fields and values for the new document.

    Returns:
        ObjectId _id of newly inserted document
    """
    new_document = mongo_collection.insert_one(kwargs)
    return new_document.inserted_id
