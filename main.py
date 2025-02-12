from desafio import ler_csv, somar_valores

path_arquivo = r"C:\Users\Uso Geral\workspace\jornada\bootcamp_python\aula_07\vendas.csv"

lista_de_produtos = ler_csv(path_arquivo)
soma_total = somar_valores(lista_de_produtos)
print(soma_total)