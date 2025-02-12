# Desafio: Análise de Vendas de Produtos 
# Objetivo: Dado um arquivo CSV contendo dados de vendas de produtos, o desafio consiste em:
#     ler os dados, 
#     processá-los em um dicionário para análise 
#     e filtrar os produtos entregues

import csv

path_arquivo = r"C:\Users\Uso Geral\workspace\jornada\bootcamp_python\aula_07\vendas.csv"

def ler_csv(nome_arquivo_csv: str) -> list[dict]:
    """
    Função que le um CSV e em seguida vai retornar uma lista de dicionarios

    """
    lista = []
    
    with open(nome_arquivo_csv, mode="r", encoding='utf-8') as arquivo:
        leitor = csv.DictReader(arquivo)
        for linha in leitor:
            lista.append(linha)
    return lista

# EXEMPLO FEITO NA AULA
# def filtrar_produtos_nao_entregues(lista: list[dict]) -> list[dict]:
#     """
#     Função para filtrar entregas = True

#     """

#     lista_com_produtos_filtrados = []

#     for produto in lista:
#         if produto.get("entregue") == "True":
#             lista_com_produtos_filtrados.append(produto)
#     return lista_com_produtos_filtrados
    

def somar_valores(lista: list[dict]) -> int:
    """
    Função para somar o total das vendas

    """

    valor_total = 0

    for produto in lista:
        valor_total += int(produto.get("Venda"))
    return valor_total

