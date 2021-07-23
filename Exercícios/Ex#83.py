'''
Crie um programa em que o usuário digite uma expressão qualquer que use parênteses. Seu aplicativo deverá analisar se a expressão passada está com os parênteses abertos e fechados an ordem correta.

'''

#Variáveis:
expr = str(input('Digite a expressão: \n'))
pilha = []

# Algoritmo:
for item in expr:
    if item == '(':
        pilha.append("(")
    elif item == ')':
        if len(pilha) > 0:
            pilha.pop()
        else:
            pilha.append(')')
            break        
        
# Resultado:        
if len(pilha) == 0:
    print('Sua expressão está correta.')
else:
    print('Sia expressão não é válida.')