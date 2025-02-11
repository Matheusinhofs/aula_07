valor_1 = 6
valor_2 = 7

valor_3 = valor_1 + valor_2

valor_4 = 8
valor_5 = 7

valor_6 = valor_4 + valor_5
valor_8 = 0

# DON´T REPEAT YOURSELF -> as operações estão se repetindo

def soma(valor_1_soma:float, valor_2_soma:float = 10) -> float:
    """
    
    uma função criada de exemplo de uma calculadora
    
    """

    valor_resultado = valor_1_soma + valor_2_soma
    return valor_resultado


valor_3 = soma(valor_1_soma=valor_1, valor_2_soma=valor_2)
valor_6 = soma(valor_4, valor_5)
valor_7 = soma(valor_8)

print(valor_3)
print(valor_6)
print(valor_7)