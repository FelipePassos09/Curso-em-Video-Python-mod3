'''Faça um programa que tenha uma função chamada ficha(), que receberá dois parametros: o nome de um jogador e quantos gols ele marcou.

O programa deverá ser capaz de mostrar a ficha do jogador mesmo que algum dado não tenha sido fornecido corretamente.'''

def ficha(name=str, gols=tuple()):
    """Function define a ticket with name and goals of a player
    and print the total in screen in dict format.

    Args:
        name ([type], optional): in this arg a name need inputed. Defaults to str.
        gols ([type], optional): in this place a tuple with total goals need inputed. Defaults to tuple().
    """
    ficha = {'name':name,
             'gols':gols
             }
    print(ficha)
    

ficha('Jão')