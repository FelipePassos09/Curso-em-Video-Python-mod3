'''
#Ex#92

Crie um programa que leia  nome, ano de nascimento e carteira de trabalho, cadastre-os (com idade) em um dicionário e, se por acaso, a CTPS for diferente de 0, o dicionário receberá também o ano de contratação e o salário.

Calcule e acrescente, além da idade, com quantos anos a pessoa vai se aposentar.
'''

from datetime import date
atual = date.today().year
cad = {
    'nome': str(input('Informe o nome: \n')),
    'ctps': int(input('Informe o nmr da CTPS, se não tiver, informe 0.\n')),
    'idade': 0,
}

cad['idade'] = atual - int(input('Ano de nascimento: \n'))

if cad['ctps'] != 0:
  cad['ano.contrato'] = date.today().year
  cad['salario'] = float(input('Diga o salário: \n'))
  cad['aposentadoria'] = cad['idade'] + 35
  
  for k, v in cad.items():
      print(f'O {k} tem {v}.')

else:
    for k, v in cad.items():
        print(f'O {k} tem {v}.')
 

    
