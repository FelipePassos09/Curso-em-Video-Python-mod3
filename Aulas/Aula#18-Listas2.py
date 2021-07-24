
'''
teste = list()
teste.append('Gustavo')
teste.append(40)
print(teste)
galera = []
galera.append(teste[:])
teste[0]= 'Maria'
teste[1]= 22
galera.append(teste[:])
print(galera)
'''

'''
lista = [['João', 25], ['Pedro',32], ['Maria', 28], ['Felipe', 30]]
print(lista[0])
print(lista[0][0])
print(lista[2][1])

for p in lista:
    print(p)
    

for p in lista:
    print(p[1])
    

for p in lista:
    print(f'{p[0]} tem {p[1]} anos de idade.')
'''

turma = []
dado = []
totmai = totmen = 0

for i in range(0,3):
    dado.append(str(input('Diga o nome: \n')))
    dado.append(int(input('Informe a idade: \n')))
    turma.append(dado[:])
    dado.clear()

for p in turma:
    if p[1] >= 21:
        print(f'O {p[0].capitalize()} é maior de idade.')
        totmai += 1
    else:
        print(f'O {p[0].capitalize()} é menor de idade.')
        totmen += 1

print(f'Temos {totmai} pessoas maiores de idade e {totmen} menores de idade.')