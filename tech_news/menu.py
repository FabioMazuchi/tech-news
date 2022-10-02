import sys
from tech_news.analyzer.ratings import top_5_categories, top_5_news
from tech_news.analyzer.search_engine import (
    search_by_category,
    search_by_date,
    search_by_tag,
    search_by_title,
)
from tech_news.scraper import get_tech_news


def zero_ao_tres(n):
    if n == "0":
        get_tech_news(int(input("Digite quantas notícias serão buscadas:")))
    elif n == "1":
        search_by_title(input("Digite o título:"))
    elif n == "2":
        search_by_date(input("Digite a data no formato aaaa-mm-dd:"))
    else:
        search_by_tag(input("Digite a tag:"))


def quatro_ao_seis(n):
    if n == "4":
        search_by_category(input("Digite a categoria:"))
    elif n == "5":
        print(top_5_news())
    else:
        print(top_5_categories())


def menu():
    return input(
        "Selecione uma das opções a seguir:\n 0 - Popular o banco com notícias"
        ";\n 1 - Buscar notícias por título;\n 2 - Buscar notícias por data;\n"
        " 3 - Buscar notícias por tag;\n 4 - Buscar notícias por categoria;\n "
        "5 - Listar top 5 notícias;\n 6 - Listar top 5 categorias;\n 7 - Sair."
    )


# Requisito 12
def analyzer_menu():
    n = menu()
    if n <= "3":
        zero_ao_tres(n)
    elif n <= "6":
        quatro_ao_seis(n)
    elif n == "7":
        print("Encerrando script")
    else:
        print("Opção inválida", file=sys.stderr)
