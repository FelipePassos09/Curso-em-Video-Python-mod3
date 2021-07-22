'''
Crie um programa onde o usuário possa digitar cinco valores numéricos e cadastre-os em uma lista já na posição correta de inserção sem usar o sort().

No final mostre a lista ordenada na tela.
'''

lista = []
c = 0

for item in range(0,5):
    val = int(input('Digite um número:\n'))
    if val in lista:
        print('Número já existe...')
    else:
        if len(lista) == 0 or val > lista[-1]:
            lista.append(val)
            print(f'O número foi inserido na posição{lista.index(val)}.')
        else:
            pos = 0
            while pos < len(lista):
                if val <= lista[pos]:
                    lista.insert(pos,val)
                    print(f'O número foi inserido na posição{lista.index(val)}.')
                    break
                pos += 1
                
            
    
print(lista)