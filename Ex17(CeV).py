''' Faça um programa que leia o comprimento do cateto oposto e do cateto adjacente
Calcule e mostre o comprimento da hipotenusa'''

co = float(input('Comprimento do cateto oposto:  '))
ca = float(input('Comprimento do cateto adjacente:  '))
h = (co ** 2 + co ** 2) ** (1/2)

print('A hipotenusa vai medir {:.2f}'.format(h))

''' outro modo de resolver '''
from  math import hypot
hi = hypot(co, ca)
print('A hipotenusa vai medir {:.2f}'.format(hi))