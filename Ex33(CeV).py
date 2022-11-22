'''Faça um programa que leia três números e mostre qual é o MAIOR e qual é o menor'''

a = float (input('Escolha um numero: '))
b = float(input('Escolha outro numero: '))
c = float(input('Escolha mais um numero: '))

menor = a
if b < a and b < c:
    menor = b
if c < a and c < b:
    menor = c
print('O menor numero é {:.1f}'.format(menor))

maior = a
if b > a and b > c:
    maior = b
if c > a and c > b:
    maior = c
print('O maior numero é o {:.1f}'.format(maior))