'''
Crie uma tupla preenchida com os 20 primeiros colocados na tabela do camepeonato brasileiro de futebol, na ordem de colocação. Depois mostre:

A) Apenas os 5 primeiros colocados.
B) Os ultimos 4 colocados.
C) Uma lista com os times em ordem alfabética.
D) Em que posição da tabela está o Chapecoense.
'''

tabela = ("Corinthians","Palmeiras","Santos","Grêmio","Cruzeiro","Flamengo","Vasco","Chapecoense","Atlético-MG","Botafogo","Atlético-PR","Bahia","São Paulo","Fluminense","Sport","Vitória","Coritiba","Avaí","Ponte Preta","Atlético-GO")
tab = ('='*25)

print(f'\033[34m{tab}\nTABELA BRASILEIRÃO\n{tab}\n','\033[m')
print(f'Os cinco primeiros são:\n')
for pos,c in enumerate(tabela[0:5]):
    print(f'{pos+1}º colocado: {c}')
print(f'\n{tab}')
print('\nOs últimos colocados são:\n')
for pos, c in enumerate(tabela[len(tabela)-4:]):
  print(f'{pos+1+(len(tabela)-4)}º colocado: {c}')
print(f'\n{tab}')
print('\nTimes em ordem alfabética:\n')
for c in sorted(tabela):
  print(c)
print(f'\n{tab}')
print(f'\nA Chapecoense ficou em {tabela.index("Chapecoense")+1}º colocado.')