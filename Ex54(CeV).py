'''Crie um programa que leia o ano de nascimento de sete pessoas. No final mostre quantas pessoas ainda não atigiram a maioridade
 e quantas ja são maiores'''
from datetime import date
ano = date.today().year
maior = 0
menor = 0

for a in range(1,8):
    nasc = int(input('Qual o ano do nascimento da {}° pessoa: '.format(a)))
    if ano - nasc >= 18:
        maior += 1
    else:
        menor += 1
print('Ao todo tivemos {} pessoas de maior'.format(maior))
print('E {} pessoas de menor'.format(menor))