'''
#Ex#85

Crie um programa onde o usuário possa digitar sete valores numéricos e cadastre-os em uma lista única que mantenha separados os valores pares e impares. No final mostre os valores pares e ímpares em ordem crescente.

'''
coleção = [[],[]]

for i in range(0,7):
    i = (int(input('Informe um número: \n')))
    if i % 2 == 0:
        coleção[0].append(i)
    else:
        coleção[1].append(i)

coleção[0].sort()
coleção[1].sort()

print(f'Os números pares são:', end=' ')
for i in coleção[0]:
    print(i, end=' ')
print()
print(f'Os números impares são:', end=' ')
for i in coleção[1]:
    print(i, end=' ')
print()
