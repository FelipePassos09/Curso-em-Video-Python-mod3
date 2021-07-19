'''
Crie um programa que vai ler vários numeros e colocá-los em uma lista.

Depois disso crie duas listas, uma com os números pares e outra com os números ímpares digitados, respectivamente.

Ao final mostre o conteúdo das trẽs listas geradas.

'''

lista = []
lis_par = []
lis_impar = []

while True:
    val = int(input('Digite um número:\n'))
    if val in lista:
        val = int(input('Digite um número:\n'))
    else:
        lista.append(val)
    if val % 2 == 0:
        lis_par.append(val)
    if val % 2 != 0:
        lis_impar.append(val)
    cont = str(input('Quer continuar? [ S/N ]\n')).strip().upper()
    while cont not in ('N', 'S'):
        cont = str(input('Quer continuar? [ S/N ]\n')).strip().upper()
    if cont == 'N':
        break

lista.sort()
lis_impar.sort()
lis_par.sort()

print(f'\n\nLista completa:')
for item in lista:
    print(item, end=' ')

print('\n\nLista Pares:')
for item in lis_par:
    print(item, end=' ')

print('\n\nLista Impares:')
for item in lis_impar:
    print(item, end=' ')
print('\n')
