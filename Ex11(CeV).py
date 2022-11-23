'''Faça um programa que leia a largura e altura de uma parede em metros.
Calcule a sua área e a quantidade de tinta neessária para pinta-la.
Considere 1 litro de tinta para cada 2m^2 de parede.'''

l = float(input('Largura da parede: '))
a = float(input('Altura da parede: '))
p = l * a
t = p / 2
print('Sua parede tem a dimensão de {} x {} e sua área é de {} m^2\nPara pintar essa parede, você precisará de {:.2f} l de tinta'.format(l, a , p, t))