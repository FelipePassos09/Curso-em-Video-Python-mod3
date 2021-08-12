'''#Ex#95

Aprimore o exercício 93 para que ele funcione com vários jogadores. Incluindo um sistema de visualização de detalhes do aproveitamento de cada jogador.'''


jogadores = []

while True:
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
    
    jogadores.append(camp.copy())
    
    cont = str(input('Quer continuar? [ S/N ]')).strip().upper()
    
    if cont == 'N':
        break


def faixa():
    print('-='*30)


faixa()
print(jogadores)

faixa()
for k, v in camp.items():
    print(f'O campo {k} tem o valor {v}.')
    
faixa()
print(f'O jogador {camp["nome"]} jogou {quant} partidas.')
for n, item in enumerate(camp['partidas']):
    print(f'     => Na partida {n+1}, fez {item} gols.')
print(f'Foi um total de {camp["total"]} gols.')