'''28 Remake
O computador vai "pensar" em um numero entre 0 e 0. Só que agora o jogador vai tentar addivinhar ate acertar. mostrando no final
quantas tentativas foram necessarios para vencer'''

from random import randint
from time import sleep

print('''Vamos jogar um jogo!
Temte acertar o numero que a maquina pensou.''')
print("--"*20)
n = randint(1, 10)
tentativas = 0
jogador = 0

while n != jogador:
    jogador = int(input('--> Chute um numero: '))
    tentativas += 1
    print('----- Pensando -----')
    sleep(0.5)
    if n != jogador:
        print('Errou!!! Tente denovo!')
        if jogador > n:
            print('Um pouco menos...')
        else:
            print('Um pouco mais...')

if n == jogador:
    print("GANHOU!!!")
    print('Foram nescessarias {} Tentativas'.format(tentativas))
    if tentativas <= 2:
        print('Ta hack junin ?!')
    elif tentativas <= 5:
        print('Você foi bem!')
    elif tentativas <= 8:
        print('Ganhou, mas foi bem mal em')
    else:
        print('Chutou todos os numeros que dava ? KKKKK')
print('--'*20)