'''
Crie um programa que tenha uma função chamada voto() que vai receber como parametro o ano de nascimento de uma pessoa, retornando um valor literal indicando se uma pessoa tem voto negado, opcional ou obrigatório nas eleições.
'''

from datetime import date

def voto(ano=int):
    atual = date.today().year
    if (atual - ano) < 16:
        return 'NEGADO'
    elif (atual - ano) >=16 and (atual - ano) < 18:
        return 'OPCIONAL'
    elif (atual - ano) > 60:
        return 'OPCIONAL'
    else:
        return 'OBRIGATÓRIO'

nascimento = int(input('Qual sua data de nascimento?\n'))
print(f'Para a sua idade o voto é {voto(nascimento)}.')
    