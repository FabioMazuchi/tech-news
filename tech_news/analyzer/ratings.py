from pymongo import MongoClient, ASCENDING, DESCENDING
from decouple import config

DB_HOST = config("DB_HOST", default="localhost")
DB_PORT = config("DB_PORT", default="27017")

client = MongoClient(host=DB_HOST, port=int(DB_PORT))
db = client.tech_news


# Requisito 10
def top_5_news():
    # https://stackoverflow.com/questions/8109122/how-to-sort-mongodb-with-pymongo
    # https://stackoverflow.com/questions/29604573/how-to-limit-mongo-query-in-python
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
    """Seu código deve vir aqui"""
