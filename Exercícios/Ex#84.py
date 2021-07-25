'''
x#84

Faça um programa que leia nome e peso de várias pessoas, guardando tudo como uma lista. No final mostre:

    A) Quantas pessoas foram cadastradas.
    B) Uma listagem com as pessoas mais pesadas.
    C) Uma listagem com as pessoas mais leves.

'''

pessoas = list()
pessoa = []
leves = pesadas = 0

while True:
  pessoa.append(str(input('Informe o nome da pessoa: \n')))
  pessoa.append(float(input('Informe o peso da pessoa: \n')))
  if len(pessoas) == 0:
    leves = pesadas = pessoa[1]
  else:
    if pessoa[1] > pesadas:
        pesadas = pessoa[1]
    if pessoa[1] < leves:
        leves = pessoa[1]
        

  pessoas.append(pessoa[:])
  cont = str(input('Quer continuar? [ S/N ]\n')).strip().upper()
  pessoa.clear()
  if cont == 'N':
    break

print(f'A) Foram cadastradas {len(pessoas)} pessoas.')
print(f'B) As pessoas mais pesadas foram: ')
for p in pessoas:
    if p[1] == pesadas:
        print(f'{p[0].capitalize()} com {p[1]}Kg.')
print(f'C) As pessoas mais leves foram: ')
for p in pessoas:
    if p[1] == leves:
        print(f'{p[0].capitalize()} com {p[1]}Kg.')