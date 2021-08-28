'''Faça um programa que tenha uma função notas() que pode receber vários valores de notas de alunos e vai retornar um dicionário com as seguintes informações:
* Quantidade de notas.
* A maior nota.
* A menor nota.
* A média da turma.
* A situação(opcional)
'''

def notas(notes: list, showsit: False, show_dict=False):
  """This function return a dict with upper note, minor note, group media and (opcionally) situation of the turm.

  notes (tuple, optional): in this arg all notes need inputed to calculate all results.
  """
  c = mai = men = med = tot = 0
  sit = ''
  for i in notes:
    if c == 0:
      mai = men = i
    else:
      if i > mai:
        mai = i
      elif i < men:
        men = i
        
    tot += i
    c += 1
  med = tot / c
  if show_dict == False:
    if showsit == True:
      if med > 8:
        sit = 'BOA'
      elif 4 < med <= 8:
        sit = 'REGULAR'
      elif med <= 4:
        sit = 'RUIM'
      print(f'Foram informadas {c} notas.\nA média da turma foi {med:.2f}\nA menor nota foi {men}\nA maior nota foi {mai}\nA situação da turma está {sit}')

    else:
      print(f'Foram informadas {c} notas.\nA média da turma foi {med:.2f}\nA menor nota foi {men}\nA maior nota foi {mai}')
  

  boletim= {
      'notas':notes,
      'sitiation':sit
  }
  if show_dict == True:
    return boletim 



notes = []
cont = ''
while True:
  notes.append(float(input('Informe a nota:')))

  cont = str(input('Quer inserir mais alguma nota?\n[ S ] SIM\n[ N ] NÃO\n')).strip().upper()

  if cont == 'N':
    break
  if cont == 'S':
    True
  else:
    print(f'Wrong option.\n{"-="*20}\nNew attempt.')
    cont = str(input('Quer inserir mais alguma nota?\n[ S ] SIM\n[ N ] NÃO\n')).strip().upper()

notas(notes, True)

boletim = notas(notes, True, True)
print('As notas informadas foram:',end=' ')
for k,v in boletim.items():
  if k == 'notas':
    for i in v:
      print(i, end=', ')
  