#!/usr/bin/env python3
"""
Script that lists all documents in a collection
"""


def list_all(mongo_collection):
    """
    Lists all documents in specified collection

    Arg:
        mongo_collection: The MongoDB collection obj

    Returns:
        list containing all documents in collection
        or
        Returns an empty list if no documents
    """
    return mongo_collection.find()
