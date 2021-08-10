'''
Faça um programa que tenha a função chamada escreva que receba um texto qualquer como parâmetro e mostre uma mensagem com tamanho adaptável.
'''

def escreva(txt):
  print('=-'*((len(txt)//2)+1))
  print(txt)
  print('=-'*((len(txt)//2)+1))
  

escreva(input('Informe o texto a ser impresso:\n'))
