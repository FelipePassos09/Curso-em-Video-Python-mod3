'''
#Ex#98

Faça um programa que tenha uma função chamada contador que receba tres parâmetros: inicio, fim, passo e realize a contagem.

Seu programa tem que realizar tres contagens através da função criada:

* A) De 1 até 10, de 1 em 1.
* B) De 10 até 0, de 2 em 2.
* C) Uma contagem personalizada.
'''

def contador(i, f, p):
  'Função recebe os parâmetros e gera a contagem.'
  for item in range(i, f, p):
    print(item, end=' ')
  print('')
  print(f'-='*20)


def tab(msg):
  'Função cria a tabulação.'
  print(f'-='*20)
  print(f'{msg:-^20}')
  print(f'-='*20)


tab('Contagem de 1-10, passo 1.')
contador(1, 10, 1)


tab('Contagem de 10-0, passo -2.')
contador(10, 0, -2)


tab('Contagem de 3-30, passo 3.')
contador(3, 30, 3)
