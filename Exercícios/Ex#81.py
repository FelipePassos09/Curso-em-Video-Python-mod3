'''
Crie um programa que leia vários números e coloque-os em uma lista.
Depois disso mostre:

A) Quantos números foram digitados.
B) A lista de valores, ordenada de forma decrescente.
C) Se o valor 5 foi ou não digitado e se está ou não na lista.

'''

lista = []
c = 0

while True:
    val = int(input('Informe um número: \n'))
    c += 1
    if val in lista:
        print('Valor já existe.')
    else:
        print('Item unico.')
        lista.append(val)
    cont = str(input('Quer continuar? [ S/N ]')).strip().upper()
    if cont == 'N':
        break

print(f'Resposta A: Foram inseridos {c} valores, mas apenas {len(lista)} números entraram na lista.')

print(f'Resposta B:')
lista.sort(reverse=True)
for item in lista:
    print(item)

if 5 in lista:
    print(f'Resposta C: O valor 5 foi inserido {lista.count(5)} vezes na lista.')
else:
    print(f'Resposta C: O valor 5 não foi inserido.')