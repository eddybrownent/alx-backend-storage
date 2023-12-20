#!/usr/bin/env python3
"""
This script provides some stats about Nginx logs
stored in Mongodb
"""
from pymongo import MongoClient


def nginx_stats():
    """
    Displays Nginx logs stored in MongoDB collection

    Database: logs
    Collection: nginx
    """

    # connect to MongoDB
    client = MongoClient('mongodb://127.0.0.1:27017')
    logs_collection = client.logs.nginx

    # the HTTP methods
    http_methods = ["GET", "POST", "PUT", "PATCH", "DELETE"]

    # all the logs
    total_logs = logs_collection.count_documents({})
    print(f"{total_logs} logs")

    # display the method each
    print("Methods:")
    for method in http_methods:
        count = logs_collection.count_documents({"method": method})
        print(f"\tmethod {method}: {count}")

    # show status
    status_check = logs_collection.count_documents(
            {"method": "GET", "path": "/status"})
    print(f"{status_check} status check")

    # the top 10 ips
    arr_ips = logs_collection.aggregate(
            [{"$group": {"_id": "$ip", "count": {"$sum": 1}}},
             {"$sort": {"count": -1}},
             {"$limit": 10}
             ])
    for ip in arr_ips:
        print(f"\t{ip['_id']}: {ip['count']}")


if __name__ == "__main__":
    nginx_stats()
