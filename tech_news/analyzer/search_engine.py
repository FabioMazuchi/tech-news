# Requisito 6
from tech_news.database import search_news


def search_by_title(title):
    response = search_news({"title": {"$regex": title, "$options": "i"}})
    result = []
    for r in response:
        result.append((r["title"], r["url"]))
    return result


# Requisito 7
def search_by_date(date):
    pass


# Requisito 8
def search_by_tag(tag):
    response = search_news({"tags": {"$regex": tag, "$options": "i"}})
    result = []
    for r in response:
        result.append((r["title"], r["url"]))
    return result


# Requisito 9
def search_by_category(category):
    """Seu código deve vir aqui"""
