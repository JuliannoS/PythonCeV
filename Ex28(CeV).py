'''Escreva um programa que faça o computador "pensar'" em número
inteiro entre 0 e 5 e peça para o usuário tentar descobrir qual foi o número
escolhido pelo computador. O programa deverá escrever na tela se o usuário
venceu ou perdeu'''

from  random import randint
from time import sleep

n = randint(0,10)
num = int(input('Chute um numero de 0 a 10 : '))
print('Pensando....')
sleep(2)# pra dar uma pausa dramatica

if n == num:
    print('Acertou!!!')
else:
    print('Errou!!!')
    print('O número que o pc pensou foi: {}'.format(n))