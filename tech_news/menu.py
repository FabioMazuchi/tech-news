# Requisito 12
def analyzer_menu():
    n = input(
        "Selecione uma das opções a seguir:\n 0 - Popular o banco com notícias"
        ";\n 1 - Buscar notícias por título;\n 2 - Buscar notícias por data;\n"
        " 3 - Buscar notícias por tag;\n 4 - Buscar notícias por categoria;\n "
        "5 - Listar top 5 notícias;\n 6 - Listar top 5 categorias;\n 7 - Sair."
    )
    if n == 0:
        qtd_noticias = input("Digite quantas notícias serão buscadas:")
    elif n == 1:
        titulo = input("Digite o título:")
    elif n == 2:
        titulo = input("Digite a data no formato aaaa-mm-dd:")
    elif n == 3:
        titulo = input("Digite a tag:")
    elif n == 4:
        titulo = input("Digite a categoria:")
    else:
        print("Opção inválida")


# print(analyzer_menu())
