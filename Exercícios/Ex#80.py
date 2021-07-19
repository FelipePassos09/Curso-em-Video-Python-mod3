'''
Crie um programa onde o usuário possa digitar cinco valores numéricos e cadastre-os em uma lista já na posição correta de inserção sem usar o sort().

No final mostre a lista ordenada na tela.
'''

lista = []

for item in range(0,5):
    val = int(input('Digite um número:\n'))
    if len(lista) == 0:
        lista.append(val)
    else:
        if val in lista:
            print('Erro: Valor duplicado.')
            val = int(input('Digite um número:\n'))
        else:
            lista.append(val)

            
    
print(lista)