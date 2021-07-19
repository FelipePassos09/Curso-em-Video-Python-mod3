'''
Crie um programa que tenha uma tupla com várias palavras (não utilize acentos). Depois disso você deve mostrar, para cada palavra, quais são suas vogais.
'''

words = 'banana', 'morango', 'melância', 'colher', 'tangerina'
vogais = 'aáãàâeéiíoôóõuú'


for item in words:
  print(f'A palavra {item.upper()} contém',end=' ')
  for letra in vogais:
    if letra in item:
      print(letra.lower(), end=' ')
  print('')