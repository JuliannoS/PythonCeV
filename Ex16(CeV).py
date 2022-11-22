'''Crie um programa que leia um numero Real qualquer pelo teclado
e mostre na tela a sua parte inteira.'''
from math import trunc
num = float(input('Digite um numero: '))
print('O valor digitado foi {} e a sua parte inteira é {}'.format(num, trunc(num)))

'''outro metodo de arrendondar sem importar'''
ero = float(input('Digite outro numero: '))
print('O valor digitado foi {} e a sua parte inteira é {}'.format(ero, int(ero)))
