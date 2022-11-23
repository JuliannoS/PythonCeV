'''Faça um programa que jogue par ou impar com o computador.
O jogo só será interrompido quando o jogador PERDER, mostrando o total
de vitórias consecutivas que ele conquistou no final do jogo'''
from random import randint

pc = n = c = vitorias = 0
print('Vamos jogar!')
while True:
    jg = ' '
    while jg not in 'IP':
        jg = str(input('Impar ou Par? ')).upper().strip()[0]

    c = int(input('escolha um numero[1 a 10]: '))
    n = randint(1, 10)
    print(f'Você escolheu {c} e o Pc escolheu {n} isso da {n + c}...')

    if (n+c) % 2 == 0:
        pc = str('P')
        if pc == jg:
            print('deu PAR, ganhou!')
            vitorias += 1
        else:
            print('Perdeu! era Par')
            break

    elif (n+c) % 2 > 0:
        pc = str('I')
        if pc == jg:
            print('Deu IMPAR, ganhou!')
            vitorias +=1
        else:
            print('Perdeu, era Impar')
            break
    print('Vamos jogar mais uma...')
print(f'Seu numero de vitorias foi {vitorias}')
vitorias = 0



