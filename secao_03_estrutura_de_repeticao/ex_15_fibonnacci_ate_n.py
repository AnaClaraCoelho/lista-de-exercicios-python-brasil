"""
Exercício 15 da seção de estrutura sequencial da Python Brasil:
https://wiki.python.org.br/EstruturaDeRepeticao

A série de Fibonacci é formada pela seqüência 1,1,2,3,5,8,13,21,34,55,... Faça um programa capaz de gerar a série até o
n−ésimo termo.

    >>> calcular_serie_de_fibonacci(1)
    '1'
    >>> calcular_serie_de_fibonacci(2)
    '1, 1'
    >>> calcular_serie_de_fibonacci(3)
    '1, 1, 2'
    >>> calcular_serie_de_fibonacci(4)
    '1, 1, 2, 3'
    >>> calcular_serie_de_fibonacci(5)
    '1, 1, 2, 3, 5'
    >>> calcular_serie_de_fibonacci(6)
    '1, 1, 2, 3, 5, 8'
    >>> calcular_serie_de_fibonacci(7)
    '1, 1, 2, 3, 5, 8, 13'

"""


def calcular_serie_de_fibonacci(n: int) -> str:
    """Escreva aqui em baixo a sua solução"""
    lista_fibonacci = [1]
    if n > 1:
        lista_fibonacci = [1, 1]
        for i in range(1, n-1):
            valor = (lista_fibonacci[-1] + lista_fibonacci[-2])
            lista_fibonacci.append(valor)
        return ', '.join(str(fn) for fn in lista_fibonacci).strip()
        # for i in lista_fibonacci[:-1]:
        #     print(f"{i},", end=' ')
        # print(f"{lista_fibonacci[-1]}'", end='')
    else:
        return f'{n}'


