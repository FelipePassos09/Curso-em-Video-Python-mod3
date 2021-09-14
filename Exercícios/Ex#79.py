'''
Crie um programa em que o usuário possa digitar vários valores numéricos e cadastre-os em uma lista. Caso o número já exista la dentro ele não será adicionado. No final serão exibidos todos os valores únicos digitados em ordem crescente.

'''

lista = []

while True:
  val = int(input('Informe um número: \n'))
  if val in lista:
    print('Número já existe...')
  else:
    lista.append(val)
    print('Número já existe...')
  cont = str(input('Quer continuar? [ S/N ]\n')).strip().upper()
  if cont not in ['S','N']:
    print('Opção errada..')
    cont = str(input('Quer continuar? [ S/N ]\n')).strip().upper()
  if cont == 'N':
    break


lista.sort()

print('Os números digitados foram: ', end=' ')
for item in lista:
  print(item, end=' ')
print()
