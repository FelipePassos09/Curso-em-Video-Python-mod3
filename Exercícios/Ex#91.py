'''
#Ex#91

Crie um programa onde 4 jogadores joguem um dado e tenham resultados aleatórios. Guarde esses resultados em um dicionário. No final coloque esse dicionário em ordem sabendo que o vencedor tirou o maior número. 
'''

from random import randint
from time import sleep

jogadas = {
    'jogador1': randint(1, 6),
    'jogador2': randint(1, 6),
    'jogador3': randint(1, 6),
    'jogador4': randint(1, 6)
}

for k,v in jogadas.items():
  print(f'{k} tirou {v}.')
  sleep(1)

print('='*20)

for n,i in enumerate(sorted(jogadas, key=jogadas.get, reverse=True)):
  print(f'O {n+1}º colocado foi {i} com {jogadas[i]}.')
  sleep(1)

