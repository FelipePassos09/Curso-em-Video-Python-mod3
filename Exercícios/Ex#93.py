'''#Ex#93

Crie um programa que gerencie o aproveitamento de um jogador de futebol. O programa vai ler o nome do jogador e quantas partidas ele jogou. Depois vai ler a quantidade de gols feitos em cada partida. No final, tudo isso deverá ser guardado em um dicionário incluindo o total de gols feitos durante o campeonato.'''



camp = {
    'nome': str(input('Nome do Jogador: ')).capitalize(),
    'partidas': [],
    'total': 0
}

quant = int(input(f'Quantas partidas {camp["nome"]} jogou?'))

for n,i in enumerate(range(0,quant)):
    gols = int(input(f'Quantos gols {camp["nome"]} fez na partida {n+1}? '))
    camp['partidas'].append(gols)
    camp['total'] += gols


def faixa():
    print('-='*30)


faixa()
print(camp)

faixa()
for k, v in camp.items():
    print(f'O campo {k} tem o valor {v}.')
    
faixa()
print(f'O jogador {camp["nome"]} jogou {quant} partidas.')
for n, item in enumerate(camp['partidas']):
    print(f'     => Na partida {n+1}, fez {item} gols.')
print(f'Foi um total de {camp["total"]} gols.')
