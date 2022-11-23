'''Crie um programa que faça o cmputador jogar Jokenpô'''

from random import choice
from time import sleep
escolhas = ['Pedra', "Papel", "Tesoura"]
print('Vamos jogar Jokenpô!')
print('''Regras:
Pedra ganha de tesoura, mas perde pra papel;
Papel ganha de pedra, mas perde pra tesoura;
Tesoura ganha de papel, mas perde pra pedra\n''')
jogador = str(input('Escolha: ').strip().title())
boss = choice(escolhas)

if (("Pedra" in jogador) or ("Papel" in jogador) or ("Tesoura" in jogador)):
    print('Jo...')
    sleep(0.2)
    print('Ken...')
    sleep(0.2)
    print('Pô!')
    print('''===================================
Você escolheu {} 
pc escolheu {}'''.format(jogador.upper(), boss.upper()))

    if jogador == "Pedra" and boss == "Tesoura":
        print('GANHOU!!!')
    elif jogador == "Papel" and boss == "Pedra":
        print('GANHOU!!!')
    elif jogador == "Tesoura" and boss == "Papel":
        print('GANHOU!!!')
    elif jogador == boss:
        print('EMPATE!!!')
    else:
        print("PERDEU!!!")
else:
    print('Jogada invalida!')
print('='*35)




