'''
Desenvolva um programa que leia valores pelo teclado e guarde-os em uma tupla, no final mostre:

A) Quantas vezes apareceu o valor 9.
B) Em que posição foi digitado o primeiro valor 3.
C) quais foram os números pares.
'''

num1 = int(input('Informe um número: '))
num2 = int(input('Informe um número: '))
num3 = int(input('Informe um número: '))
num4 = int(input('Informe um número: '))
nums = (num1, num2, num3, num4)

print(nums)
while True:
  if 9 in nums:
    print(f'O número 9 aparece {nums.count(9)} nove vezes na sequencia.')
  if 3 in nums:
    print(f'O número 3 aparece primeiro na {nums.index(3)} posição.')  
  for item in nums: 
    print(f'Entre os números escolhidos são pares', end=' ')
    while (item % 2) == 0:
      print(item)
      break
  break
