from pymongo import MongoClient, ASCENDING, DESCENDING
from decouple import config

DB_HOST = config("DB_HOST", default="localhost")
DB_PORT = config("DB_PORT", default="27017")

client = MongoClient(host=DB_HOST, port=int(DB_PORT))
db = client.tech_news


# Requisito 10
def top_5_news():
    ordered = list(
        db.news.find({}, {"_id": False})
        .sort([("comments_count", DESCENDING), ("title", ASCENDING)])
        .limit(5)
    )

    result = []
    if len(ordered) < 5:
        for o in ordered:
            result.append((o["title"], o["url"]))
    else:
        for o in ordered:
            result.append((o["title"], o["url"]))
    return result


# Requisito 11
def top_5_categories():
    lista = list(
        db.news.aggregate(
            [
                {"$group": {"_id": "$category", "res": {"$sum": 1}}},
                {"$sort": {"res": -1, "_id": 1}},
                {"$limit": 5},
            ]
        )
    )
    result = []
    for lis in lista:
        result.append(lis["_id"])

    return result
