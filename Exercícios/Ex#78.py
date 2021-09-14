'''
Faça um programa que leia 5 valores numéricos e guarde-os em uma lista.

No final mostre qual foi o menor e maior valores digitados e suas respectivas posições.
'''

lista = []

for item in range(0,5):
  val = int(input('Informe um número: \n'))
  lista.append(val)

print(f'O maior número informado foi {max(lista)}, ele foi o {lista.index(max(lista))+1}º digitado.')
print(f'Já o menor número informado foi {min(lista)}, ele foi o {lista.index(min(lista))+1}º digitado.')
