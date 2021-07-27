'''
#Ex#90

Faça um programa que leia um nome e média de um aluno, guardando também a situação em um dicionário. No final mostre o conteúdo da estrutura na tela.
'''

aluno = {
    'nome':str(input('Informe o nome do aluno: \n')),
    'média':float(input('Média do aluno: \n'))
}

if aluno['média'] > 5:
  aluno['situção'] = 'Aprovado'
else:
  aluno['situção'] = 'Reprovado'

print(f'O aluno {aluno["nome"].capitalize()} finalizou o curso com média {aluno["média"]:.1f}, foi {aluno["situção"]}.')