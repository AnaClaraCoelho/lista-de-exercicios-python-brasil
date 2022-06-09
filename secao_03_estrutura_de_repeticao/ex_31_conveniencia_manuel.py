"""
Exercício 31 da seção de estrutura sequencial da Python Brasil:
https://wiki.python.org.br/EstruturaDeRepeticao

FO Sr. Manoel Joaquim expandiu seus negócios para além dos negócios de 1,99 e agora possui uma loja de conveniências.
Faça um programa que implemente uma caixa registradora rudimentar. O programa deverá receber um número desconhecido de
valores referentes aos preços das mercadorias.
Um valor zero deve ser informado pelo operador para indicar o final da compra.
Um valor -1 deve ser informado pelo operador para finalizar o programas
O programa deve então mostrar o total da compra e perguntar o valor em dinheiro que o cliente forneceu, para então
calcular e mostrar o valor do troco. Após esta operação, o programa deverá voltar ao ponto inicial,
para registrar a próxima compra.

    >>> from secao_03_estrutura_de_repeticao import ex_31_conveniencia_manuel
    >>> entradas = ['-1']  # Encerrando o programa sem nenhuma compra
    >>> ex_31_conveniencia_manuel.input = lambda k: entradas.pop()
    >>> ex_31_conveniencia_manuel.rodar_programa_de_caixa()
    Lojas Tabajara
    -------------------
    Programa encerrado!
    >>> entradas = ['2.00', '-1', '1.99']  # Compra de apenas um produto
    >>> ex_31_conveniencia_manuel.input = lambda k: entradas.pop()
    >>> ex_31_conveniencia_manuel.rodar_programa_de_caixa()
    Lojas Tabajara
    Total     : R$   1.99
    Dinheiro  : R$   2.00
    Troco     : R$   0.01
    -------------------
    Programa encerrado!
    >>> entradas = ['5.00', '-1', '1.99', '1.99']  # Compra de dois produtos
    >>> ex_31_conveniencia_manuel.input = lambda k: entradas.pop()
    >>> ex_31_conveniencia_manuel.rodar_programa_de_caixa()
    Lojas Tabajara
    Total     : R$   3.98
    Dinheiro  : R$   5.00
    Troco     : R$   1.02
    -------------------
    Programa encerrado!
    >>> entradas = ['10.00', '-1', '5.35', '5.00', '0', '1.98', '1.99']  # Compra de dois produtos
    >>> ex_31_conveniencia_manuel.input = lambda k: entradas.pop()
    >>> ex_31_conveniencia_manuel.rodar_programa_de_caixa()
    Lojas Tabajara
    Total     : R$   3.97
    Dinheiro  : R$   5.00
    Troco     : R$   1.03
    -------------------
    Lojas Tabajara
    Total     : R$   5.35
    Dinheiro  : R$  10.00
    Troco     : R$   4.65
    -------------------
    Programa encerrado!

"""


def rodar_programa_de_caixa():
    """Escreva aqui em baixo a sua solução"""
    sum = 0
    preco = float(input('Preco do item: '))
    if preco == -1:
        print('Lojas Tabajara')
        print('-------------------')
        print('Programa encerrado!')
    else:
        sum += preco
        while True:
            preco = float(input('Preco do item: '))
            if preco in (0,-1):
                if preco == -1:
                    print('Lojas Tabajara')
                    dinheiro = float(input('Dinheiro: '))
                    print(f'Total     : R$   {sum :.2f}')
                    str_dinheiro = f'{dinheiro:.2f}'
                    print(f'Dinheiro  : R${str_dinheiro.rjust(7)}')
                    print(f'Troco     : R$   {dinheiro - sum :.2f}')
                    print('-------------------')
                    print('Programa encerrado!')
                    break
                else:
                    print('Lojas Tabajara')
                    dinheiro = float(input('Dinheiro: '))
                    print(f'Total     : R$   {sum :.2f}')
                    str_dinheiro = f'{dinheiro:.2f}'
                    print(f'Dinheiro  : R${str_dinheiro.rjust(7)}')
                    print(f'Troco     : R$   {dinheiro - sum :.2f}')
                    print('-------------------')
                    sum = 0
            else:
                sum += preco



