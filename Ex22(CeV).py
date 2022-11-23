''''Crie um programa que leia o nome completo de uma pessoa e mostre
Nome com todas as letras maiusculas
Nome com todas as letras minusculas
Quantas letras ao todo(sem espaços)
Quantas letras tem o primeiro nome'''
nome = str(input('Ponha seu nome completo:')).strip()
print('Seu nome em maiuscula é {}'.format(nome.upper()))
print('Seu nome em minusculo é {}'.format(nome.lower()))
print('Seu nome tem {} letras'.format(len(nome) - nome.count(' ')))
dividido = nome.split()
print('Seu primeiro nome tem {} letras'.format(len(dividido[0])))
#/ / / . format(nome.find(' ')))