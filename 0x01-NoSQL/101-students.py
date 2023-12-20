#!/usr/bin/env python3
"""
This functions returns students
sorted by average score
"""


def top_students(mongo_collection):
    """
    query students sorted by average score

    Args:
        mongo_collection: mongo collection object

    Returns:
        list: students sorted by average score
    """
    pipeline = [{"$project": {
        "name": "$name",
        "averageScore": {"$avg": "$topics.score"}
        }},
        {"$sort": {"averageScore": -1}}]
    return mongo_collection.aggregate(pipeline)
