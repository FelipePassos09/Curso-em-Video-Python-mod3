pessoas = {
    'nome': 'Gustavo',
    'sexo': 'M',
    'idade': '22'
}

def faixa():
    print('='*45)


print(f'O {pessoas["nome"]} tem {pessoas["idade"]} anos.')
faixa()
print(pessoas.items())
faixa()
print(pessoas.values())
faixa()
print(pessoas.keys())
faixa()
for k in pessoas.keys():
    print(k)
faixa()    
for k in pessoas.values():
    print(k)
faixa()    
for k, v in pessoas.items():
    print(f'{k} = {v}')
    
pessoas['nome'] = 'Felipe'
pessoas['peso'] = 62

del pessoas["sexo"]

faixa()
for k, v in pessoas.items():
    print(f'{k} = {v}')
    
