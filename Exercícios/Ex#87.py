'''
#Ex#87

Aprimore o desafio anterior  mostrando no final:

* A) A soma de todos os valores pares digitados.
* B) A soma dos valores da terceira coluna.
* C) O maior valor da segunda linha.
'''

'''
num = []
matriz = []
somapar = 0

for i in range(0, 9):
    num.append(int(input('Diga um número: ')))
    matriz.append(num[:])
    if num[0] % 2 == 0:
        somapar += num[0]
    num.clear()

segl = 0
l2 = []
for p,item in enumerate(matriz):
    if 2 < p < 6:
        segl += item[0]
        l2.append(item[0])
        

print('\nA matriz criada foi:\n')

for i in matriz[0:3]:
    print(i,end='')
print()

for i in matriz[3:6]:
    print(i,end='')
print()

for i in matriz[6:]:
    print(i,end='')
print('\n')
        
print(f'A) A soma de todos os pares é igual a {somapar}.')
print(f'B) A soma dos items na segunda linha é {segl}.')
print(f'C) O maior valor na linha 2 é {max(l2)}.')
'''

matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
spar = mai = c2 = 0

for l in range(0, 3):
    for c in range(0, 3):
        matriz[l][c] = int(input(f'Digite um número para a posição ({l},{c}): \n'))
        
for l in range(0, 3):
    for n in range(0, 3):
        print(f'[{matriz[l][n]:^5}]', end='')
        if matriz[l][c] % 2 == 0:
            spar += matriz[l][c]
    print()

for l in range(0, 3):
    c2 += matriz[l][2]
    
for c in range(0, 3):
    if c == 0:
        mai = matriz[1][c]
    elif matriz[1][c] > mai:
        mai = matriz[1][c]

print(f'A) A soma de todos os pares é igual a {spar}.')
print(f'B) A soma dos items na teceira coluna é {c2}.')
print(f'C) O maior valor na linha 2 é {mai}.')