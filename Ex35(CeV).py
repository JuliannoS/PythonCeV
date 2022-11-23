'''Desenvolva um programa que leia o comprimento de três retas e diga
ao usuario se elas podem ou formar um triangulo'''

r1 = int(input('Primeira reta mede ? '))
r2 = int(input('Segunda reta mede? '))
r3 = int(input('Terceira reta mede? '))

if (r2 - r3 < r1 < r2 + r3) and (r1 - r3 < r2 < r1 + r3) and (r1 - r2 < r3 < r1 + r2):
    print('Essas três retas podem formar um triângulo')
else:
    print('Essas três retas nao podem formar um triângulo')