# 1. Calcular Média de Valores em uma Lista
lista_valores = [1,2,3,10,9,5]

def media_valores_lista(lista_valor: list) -> float:
    soma_valores_lista = 0
    for valor in lista_valor:
        soma_valores_lista = valor + soma_valores_lista
    quantidade_valores_na_lista = len(lista_valores)
    media = soma_valores_lista / quantidade_valores_na_lista
    return media

print(media_valores_lista(lista_valores))


# 2. Filtrar Dados Acima de um Limite


# 3. Contar Valores Únicos em uma Lista


# 4. Converter Celsius para Fahrenheit em uma Lista

# 5. Calcular Desvio Padrão de uma Lista


# 6. Encontrar Valores Ausentes em uma Sequência

