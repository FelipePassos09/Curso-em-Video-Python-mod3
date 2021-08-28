'''Faça um mini programa que utilize o Interactive Help do python. O usuário vai digitar o comando e o manual vai aparecer. Quando o usuário digitar 'FIM' o programa se encerrará.
OBS.: Use cores.'''

import os

colors={
    'black' : '\033[0;30m',
    'blue' : '\033[0;34m',
    'b_yellow' : '\033[1;43;31m',
    'b_white' : '\033[47;30;1m',
    'b_blue' : '\033[44;30;1m',
    'white_blue': '\033[47;32;1m',
    'limpa': '\033[m'
}

def tab(msg):
  print(colors['b_white'])
  print('-='*30)
  print(f'{msg:-^60}')
  print('-='*30)
  print(colors['limpa'])


def hlp(func:str):
  """
  In this function we
  """
  print(colors['white_blue'])
  print(func.__doc__)


tab('PROGRAMA DE CONSULTA PARA FUNÇÕES')
cont = ''
while True:
  print(colors['b_blue'])
  print('-='*30)
  print(f'{"Qual função quer consultar?":^60}')
  print('-='*30)
  print(colors['limpa'])
  func = str(input(''))
  print('\n')

  hlp(func)

  print(colors['b_yellow'])
  print('-='*30)
  print(f'{"DESEJA UM NOVA CONSULTA?":^60}')
  print('-='*30)
  cont = str(input('')).strip().upper()

  if cont not in 'SsNn' :
    print('-='*30)
    print(f'{"OPÇÃO ERRADA, TENTE NOVAMENTE":^60}')
    print('-='*30)

    print(colors['b_yellow'])
    print('-='*30)
    print(f'{"DESEJA UM NOVA CONSULTA?":^60}')
    print('-='*30)
    cont = str(input('')).strip().upper()

  if cont == 'N':
    break

tab('PROGRAMA ENCERRADO!!!')