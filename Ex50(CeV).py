'''Desenvolva um programa que leia seis numeros interios e mostre a soma apenas daqueles que forem pares.
Se o valor digitado for impar. Desconsidere-o'''
s = 0
cont = 0
for a in range(1,7):
    b = int(input('Digite o {}º numero: '.format(a)))
    if b % 2 == 0:
        s += b
        cont += 1
print('A soma dos {} valores pares é {}'.format(cont, s))
print('--'*20)