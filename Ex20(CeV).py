'''Sorterar a ordem de apresentação de trabalhos dos alunos. Faça um programa
que leia o nome das quatro equipes e mostre a ordem sorteada'''

#import random
from random import shuffle
a1 = input("Primeira equipe:  ")
a2 = input('Segunda equipe:  ')
a3 = input('Terceira equipe: ')
a4 = input('Quarta equipe:  ')
lista = [a1, a2, a3, a4]
shuffle(lista)
print('A ordem de apresentação sera: ')
print(lista)