'''um professor quer sortear um dos seus quatro alunos para apagar o quadro.
faça um programa que ajude ele. Lendo o nome delas escrevendo o nome do escolhido'''

#import random
from random import choice
a1 = input('Primeiro aluno: ')
a2 = input('Segundo aluno: ')
a3 = input('Terceiro aluno: ')
a4 = input('Quarto aluno: ')
lista = [a1, a2, a3, a4]
escolhido = choice(lista)
print("O aluno escolhido foi {}".format(escolhido))