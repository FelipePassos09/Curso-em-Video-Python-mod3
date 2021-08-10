'''
#Ex#99

Faça um programa que tenha uma função chamada maior que receba vários parâmetros com valores inteiros.

Seu programa tem que analisar todos os valores e dizer qual deles é o maior.
'''


def maior(val: list):
  'Função recebe a lista e cria o resultado da análise.'
  print('=='*15)
  cont = mai = men = 0
  
  for i in val:
    print(i, end=' ')
    cont += 1
    if cont == 1:
      mai = men = i
    else:
      if i >= mai:
        mai = i
      elif i <=men:
        men = i
  print(f'\nForam inseridos {cont} valores.\nDesses o maior foi {mai} e o menor {men}.')

maior([3,5,4,9,12])
maior([5,2,4])
maior([])
maior(range(2,36,2))
lista = []
while True:
  lista.append(int(input('Diga um número:\n')))
  cont = str(input('Quer Parar?\n')).upper()
  maior(lista)
  if cont == 'S':
    break
