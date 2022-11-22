'''Faça um programa que mostre na tela uma contagem regressiva para o estouro de fogos de artificio. Indo de 10 até 0.
com uma pausa de 1 seg entre elas'''
from time import sleep

print('Contagem regressiva para os fogos:')

for a in range(10,-1,-1):
    print(a)
    sleep(1)
print('POW POW KABUUMMM!!!')
