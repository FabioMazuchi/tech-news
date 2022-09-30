# Requisito 10
from tech_news.database import find_news


def top_5_news():
    noticias = find_news()
    # https://pt.stackoverflow.com/questions/371321/itemgetter-ordenar-lista-de-dicion%C3%A1rios-python
    ordered = sorted(
        noticias,
        key=lambda row: (row["comments_count"], row["title"]),
        reverse=1,
    )

    result = []
    if len(ordered) < 5:
        for o in ordered:
            result.append((o["title"], o["url"]))
    else:
        for c in range(5):
            result.append((ordered[c]["title"], ordered[c]["url"]))
            c += 1
    return result


# Requisito 11
def top_5_categories():
    """Seu código deve vir aqui"""
