'''#Ex#94

Crie um programa que leia nome, sexo e idade de várias pessoas, guardando os dados de cada pessoa em um dicionário e todos os dicionários em uma lista. No final mostre:

* A) Quantas pessoas foram cadastradas.
* B) A média de idade do grupo
* C) Uma lista com todas as mulheres.
* D) Uma lista com todas as pessoas com idade acima da média.'''


people = []
md = 0

while True:
    person = {'nome': str(input('Nome pessoa:\n')).strip().upper(),
              'sexo': str(input('Sexo pessoa:\n')).strip().upper(),
              'idade': int(input('Idade pessoa:\n'))}
    people.append(person.copy())
    
    md += person['idade']
    média = md / len(people)
    
    cont = str(input('Quer continuar? [ S/N ]')).strip().upper()
    
    if cont == 'N':
        break

print(f'A) Foram cadastradas {len(people)} pessoas.')
print(f'B) A média de idade do grupo foi {média} anos.')
print(f'C) as mulheres do grupo foram: ')
for i in people:
    if i['sexo'] == 'F':
        for k,v in i.items():
            if k == 'nome':
                print(f'{k}: {v}')
print(f'D) Pessoas com idade maior que a média:')
for i in people:
    if i['idade'] > média:
        for k, v in i.items():
            if k == 'nome':
                print(f'{k}: {v}')