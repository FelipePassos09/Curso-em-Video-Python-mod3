'''
#Ex#86

Crie um programa que crie uma matriz 3 x 3 e preencha com valores lidos pelo teclado.

No final mostre a matriz na tela com a formatação correta.
'''
'''
num = []
matriz = []


for i in range(0, 9):
    num.append(int(input('Diga um número: ')))
    matriz.append(num[:])
    num.clear()

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
'''       

# Correção:
matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]

for c in range(0, 3):
    for l in range(0, 3):
        matriz[l][c] = int(input(f'Digite um número para a posição ({l},{c}): \n'))
        
for l in range(0, 3):
    for n in range(0, 3):
        print(f'[{matriz[l][n]:^5}]', end='')
    print()
