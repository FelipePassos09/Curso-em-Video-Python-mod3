'''
Crie um programa que gere 5 números aleatórios e colocar em uma tupla. Depois disso, mostre a listagem de números gerados e também indique o menor e o maior valor dessa tupla.
'''

num1 = int(input('Diga o primeiro número:'))
num2 = int(input('Diga o segundo número:'))
num3 = int(input('Diga o terceiro número:'))
num4 = int(input('Diga o quarto número:'))
nums = (num1, num2, num3, num4)

print(f'\nO maior número foi {max(nums)}.')
print(f'\nO menor número foi {min(nums)}.')