'''Crie um programa que tenha uma função fatorial que receba dois parametros: o primeiro que indique o número a calcular e o outro chamado show, que será um valor boolean(opcional) indicando se será mostrado ou não na tela o processo de calculo do fatorial.'''

def fatorial(num, show=True):
    """This function apply to print or return a value of one fatorial.

    Args:
        num (int, float): number to calculate a fatorial
        show (bool, optional): if False print on terminal a result, 
        if True, return the value. Defaults to True.
    """
    cont = fat = 0
    for i in range(num,2,-1):
        if cont == 0:
            fat = (num - 1) * num
            num = num-2
        else:
            fat = fat * num
            num = num-1
        cont += 1
    if show == True:
        print(fat)
    if show == False:
        return fat
        

print(f'O Fatorial de 5 é {fatorial(5,False)}')
print(help(fatorial))