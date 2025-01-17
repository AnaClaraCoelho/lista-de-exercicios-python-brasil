"""
Exercício 18 da seção de estrutura de decisão da Python Brasil:
https://wiki.python.org.br/EstruturaDeDecisao

Faça um Programa que peça uma data no formato dd/mm/aaaa e determine se a mesma é uma data válida.

    >>> validar_data('')
    'Data inválida'
    >>> validar_data('1')
    'Data inválida'
    >>> validar_data('1/2/2004')
    'Data válida'
    >>> validar_data('1/02/2004')
    'Data válida'
    >>> validar_data('01/02/2004')
    'Data válida'
    >>> validar_data('30/02/2004')
    'Data inválida'
    >>> validar_data('01/13/2004')
    'Data inválida'

"""


def validar_data(data: str):
    """Escreva aqui em baixo a sua solução"""
    if data == '' or len(data) < 3:
        return 'Data inválida'
    else:
        data = data.split('/')
        dia = int(data[0])
        mes = int(data[1])
        ano = int(data[2])
        if dia > 28 and mes in (0o2, 2):
            return 'Data inválida'
        elif mes > 2 or dia > 31:
            return 'Data inválida'
        else:
            return 'Data válida'
