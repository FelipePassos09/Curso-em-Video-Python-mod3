'''
#Ex#100

Faça um programa que teha uma lista chamada números e duas funções chamadas sorteio e somaPara. A primeira função irá sortear 5 números e colocá-los dentro da ista e a segunda função vai mostrar a soma entre todos os valores pares sorteados pela função anterior.

'''

from random import randint


def sorteio():
  'função para sortear 5 numeros.'
  num = []
  for i in range(0,5,1):
    num.append(randint(1,99))
  return num


def somapar(num: list):
  'função para somar os pares'
  par = imp = cpar = cimpar = 0
  for i in num:
    if i % 2 == 0:
      par += i
      cpar += 1
    else:
      imp += i
      cimpar += 1
  return par, imp, cpar, cimpar


numeros = sorteio()

print(f'Os números sorteados foram {numeros}.')
print(f'Destes, {somapar(numeros)[2]} são pares e a soma foi {somapar(numeros)[0]}.')
print(f'E dos impares houveram {somapar(numeros)[3]} ocorrencias, onde a soma é {somapar(numeros)[1]}.')
