import requests
from parsel import Selector
from time import sleep


# Requisito 1
def fetch(url):
    try:
        sleep(1)
        response = requests.get(
            url, timeout=3, headers={"user-agent": "Fake user-agent"}
        )
        response.raise_for_status()
    except (requests.HTTPError, requests.ReadTimeout):
        return None
    else:
        return response.text


# Requisito 2
def scrape_novidades(html_content):
    selector = Selector(html_content)
    links = []
    for link in selector.css("article.entry-preview"):
        links.append(link.css("a.cs-overlay-link::attr(href)").get())
    return links


# Requisito 3
def scrape_next_page_link(html_content):
    return Selector(html_content).css("a.next::attr(href)").get()


# Requisito 4
def scrape_noticia(html_content):
    sel = Selector(html_content)
    p = sel.css("div.entry-content > p:nth-of-type(1) *::text").getall()
    sumary = "".join(p)
    return {
        "url": sel.css("head link[rel=canonical]::attr(href)").get(),
        "title": str(sel.css("h1.entry-title::text").get()).strip(),
        "timestamp": sel.css(".meta-date::text").get(),
        "writer": sel.css("span.author > a::text").get(),
        "comments_count": len(sel.css(".comment-list > li").getall()) or 0,
        "summary": sumary.strip(),
        "tags": sel.css("section.post-tags > ul > li > a::text").getall(),
        "category": sel.css("a.category-style span.label::text").get(),
    }


# Requisito 5
def get_tech_news(amount):
    """Seu código deve vir aqui"""
