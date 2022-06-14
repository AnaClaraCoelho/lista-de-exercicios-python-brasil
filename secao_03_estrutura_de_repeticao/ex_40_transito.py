"""
Exercício 40 da seção de estrutura sequencial da Python Brasil:
https://wiki.python.org.br/EstruturaDeRepeticao

Foi feita uma estatística em cinco cidades brasileiras para coletar dados sobre acidentes de trânsito. Foram obtidos os
1) seguintes dados:
2) Código da cidade;
3) Número de veículos de passeio (em 1999);
4) Número de acidentes de trânsito com vítimas (em 1999).

Deseja-se saber:

1) Qual o maior e menor índice de acidentes de transito e a que cidade pertence;
2) Qual a média de veículos nas cinco cidades juntas;
3) Qual a média de acidentes de trânsito nas cidades com menos de 2.000 veículos de passeio.

Mostre os valores com uma casa decimail

    >>> calcular_estatisticas(('SJC', 190_000, 300), ('SP', 1_000_000, 2_000 ),
    ... ('BH', 800_000, 1000), ('FZ', 600_000, 700), ('FL', 150_000, 900)
    ... )
    O maior índice de acidentes é de FL, com 6.0 acidentes por mil carros.
    O menor índice de acidentes é de FZ, com 1.2 acidentes por mil carros.
    O média de veículos por cidade é de 548000.
    A média de acidentes total nas cidades com menos de 150 mil carros é de 900.0 acidentes.
"""

def calcular_estatisticas(*cidades):
    """Escreva aqui em baixo a sua solução"""
    maior_acidentes = cidades[0][2]/ (cidades[0][1]/1000)
    menor_acidentes = cidades[0][2]/(cidades[0][1]/1000)
    nome_cidade_maior = ''
    nome_cidade_menor = ''
    numero_veiculos = 0
    numero_acidentes = 0
    cidades_menos_150mil = 0
    for cidade in cidades: #Percorre a lista de tuplas
        qtd_por_1000_veiculos = cidade[2]/ (cidade[1]/1000)
        if qtd_por_1000_veiculos >= maior_acidentes:
            maior_acidentes = qtd_por_1000_veiculos
            nome_cidade_maior = cidade[0]
        if qtd_por_1000_veiculos <= menor_acidentes:
            menor_acidentes = qtd_por_1000_veiculos
            nome_cidade_menor = cidade[0]
        numero_veiculos += cidade[1]
        if cidade[1] <= 150000:
            numero_acidentes += cidade[2]
            cidades_menos_150mil += 1
    print(f'O maior índice de acidentes é de {nome_cidade_maior}, com {maior_acidentes:.1f} acidentes por mil carros.')
    print(f'O menor índice de acidentes é de {nome_cidade_menor}, com {menor_acidentes:.1f} acidentes por mil carros.')
    print(f'O média de veículos por cidade é de {numero_veiculos/len(cidades):.0f}.')
    print(f'A média de acidentes total nas cidades com menos de 150 mil carros é de {numero_acidentes/cidades_menos_150mil:.1f} acidentes.')


