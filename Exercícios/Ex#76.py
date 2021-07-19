'''
Crie um programa que tenha uma tupla única com nomes de produtos e seus respectivos preços, na sequência.

No final mostre uma listagem de preços que organizando os dados de forma tabular.
'''

compras = ('Celular', 1765.65,'Cartão de Memória', 65.00, 'Caderneta', 35.06, 'Monitor', 860.95, 'Notebook', 3560.78, 'Mouse', 296.65, 'Teclado', 353.98)
c = 0

print(f'{"="*35}\nLISTA DE COMPRAS\n{"="*35}')

while True:
  if c < len(compras):
    print(f'{compras[0+c]:.<24}R${compras[1+c]:>9}')
  else:
    break
  c+=2
  
print(f'{"="*35}\n{"---FIM---":-^35}')