'''Faça um programa que leia um numero qualquer e mostre o seu fatorial'''
c = 1
b = 1
fat = int(input('Digite um valor: '))
print('Calculando {}! = '.format(fat), end='')

while fat > 0:
    print(fat, end='')
    print(' x ' if fat > 1 else ' = ', end="")
    c *= fat
    fat -= 1
print(c)

print('\nUsando for')
fato = int(input('Digite outro valor: '))
for rial in range(fato, 0, -1):
    print(rial, end ="")
    print(' * ' if rial > 1 else ' = ',end='')
    b *= rial
print(b)
