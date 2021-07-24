'''
x#84

Faça um programa que leia nome e peso de várias pessoas, guardando tudo como uma lista. No final mostre:

    A) Quantas pessoas foram cadastradas.
    B) Uma listagem com as pessoas mais pesadas.
    C) Uma listagem com as pessoas mais leves.

'''

pessoas = list()
pessoa = []

while True:
  pessoa.append(str(input('Informe o nome da pessoa: \n')))
  pessoa.append(float(input('Informe 0 peso da pessoa: \n')))
  pessoas.append(pessoa[:])
  cont = str(input('Quer continuar? [ S/N ]\n')).strip().upper()
  pessoa.clear()
  if cont == 'N':
    break

leves = []
pesadas = []
for p in pessoas:
    if p[1] >= 90:
        pesadas.append(p)
    if p[1] <= 70:
        leves.append(p)

print(pessoas)

print(f'A) Foram cadastradas {len(pessoas)} pessoas.')
print(f'B) As pessoas mais pesadas foram: ')
for p in pesadas:
    print(p)
print(f'C) As pessoas mais leves foram: ')
for p in leves:
    print(p)