'''
#Ex#88

Faça um programa que ajude um jogador da MEGASENA a criar palpites. O programa vai perguntar quantos jogos serão gerados e vai sortear 6 números entre 1 e 60 para cada jogo, cadastrando tudo em uma lista composta.
'''

from random import randint
from time import sleep

qjogos = int(input('Quantos jogos deseja fazer? '))
palpite =[]
tot = 0
jogos = []

print('\nOK\n\nSeu palpite fica:\n')

while tot < qjogos:
    c = 0
    while True:
        num = randint(1,60)
        if num not in palpite:
            palpite.append(num)
            c += 1
        if c >= 6:
            break
    palpite.sort()
    jogos.append(palpite[:])
    palpite.clear()
    tot+=1
    
for i, j in enumerate(jogos):
    print(f'Jogo {i+1}: {j}')
    sleep(1)
    





