'''Crie um programa que leia o nome de uma pessoa e diga se ela tem Silva nome'''
nome = input('Ponha seu nome:').strip().title()
print('Seu nome tem Silva? {}'.format('Silva' in nome))
print(nome)

#//// . format.("silva" in nome.lower())
