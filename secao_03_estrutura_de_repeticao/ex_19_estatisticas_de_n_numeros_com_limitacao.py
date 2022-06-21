"""
Exercício 19 da seção de estrutura sequencial da Python Brasil:
https://wiki.python.org.br/EstruturaDeRepeticao

Altere o programa anterior para que ele aceite apenas números entre 0 e 1000.

    >>> calcular_estatisticas()
    'Maior valor: não existe. Menor valor: não existe. Soma: 0'
    >>> calcular_estatisticas(1)
    'Maior valor: 1. Menor valor: 1. Soma: 1'
    >>> calcular_estatisticas(1, 2)
    'Maior valor: 2. Menor valor: 1. Soma: 3'
    >>> calcular_estatisticas(1, 2, -1)
    'Somente números de 0 a 1000 são permitidos'
    >>> calcular_estatisticas(1, 2, -10)
    'Somente números de 0 a 1000 são permitidos'
    >>> calcular_estatisticas(1, 2, 1001)
    'Somente números de 0 a 1000 são permitidos'
    >>> calcular_estatisticas(1, 2, 1198)
    'Somente números de 0 a 1000 são permitidos'

"""


def calcular_estatisticas(*numeros) -> str:
    """Escreva aqui em baixo a sua solução"""
    lista = [*numeros]
    count = 0
    if lista == []:
        print("'Maior valor: não existe. Menor valor: não existe. Soma: 0'")
    else:
        for i in range(0,len(lista)):
            if 0 < lista[i] < 1000:
                    count += 1
        if count == len(lista):
            print(f"'Maior valor: {max(lista)}. Menor valor: {min(lista)}. Soma: {sum(lista)}'")
        else:
            print(f"'Somente números de 0 a 1000 são permitidos'")


