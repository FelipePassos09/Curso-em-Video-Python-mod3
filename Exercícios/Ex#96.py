'''
Faça um programa que tenha uma função chamada area() que receba as dimensões de um terreno retangular e mostre a área do terreno.

'''

def area(largura, altura):
  return largura * altura


larg = int(input('Informe a largura do terreno:\n'))
alt = int(input('Informe o comprimento do terreno:\n'))

print(f'A área do terreno é {area(larg, alt)}m².')
