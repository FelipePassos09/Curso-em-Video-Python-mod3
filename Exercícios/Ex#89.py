'''
#Ex#89

Crie um programa que leia nome e duas notas de vários alunos e guarde tudo em uma lista composta. No final mostre um boletim contando a média de cada um e permita que o usuário possa mostrar as notas de cada aluno individualmente.
'''

def faixa():
    print('='*40)


faixa()
print(f'{"CURSO EM VÍDEO":-^40}')
print(f'{"CONTROLE DE NOTAS":-^40}')
faixa()


aluno = []
boletim= []

while True:
    aluno.insert(0,str(input('Aluno: ').strip().upper()))
    aluno.insert(1,[float(input('Nota 1: ')), float(input('Nota 2: '))])
    aluno.insert(2, (aluno[1][0]+aluno[1][1])/2)
    
    
    cont = str(input('Quer continuar? [ S/N] \n')).strip().upper()  
    boletim.append(aluno[:])
    aluno = []
    if cont == 'N':
        break

faixa()
print(f'{"BOLETIM":-^40}')
faixa()
print(f'{"ID":<3}{"Aluno":^32}{"Média":>}')
faixa()

for id_aluno,item in enumerate(boletim):
    print(f'{id_aluno+1:<3}{item[0]:-<32}{item[2]:>5.1f}')
faixa()
print('\n')

while True:
    faixa()
    check = int(input('Gostaria de ver as notas de algum aluno?\n\nDigite o ID ou 999 para sair:\n'))
    print('\n')
    if check != 999:
        faixa()
        print(f'{"NOME":<26}{"NOTA 1":^7}{"NOTA 2":^7}')
        print(f'{boletim[check-1][0]:-<26}{boletim[check-1][1][0]:^7}{boletim[check-1][1][1]:^7}')
    if check == 999:
        break

faixa()
print(f'{"OK, SISTEMA ENCERRANDO":-^40}')
faixa()