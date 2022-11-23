'''Faça um programa que leia um numero inteiro e diga se ele é ou não um numero primo'''

n = int(input('Digite um numero: '))
primo = 0
for a in range(1, n + 1):
    if n % a == 0:
        primo += 1
print('O {} pode ser dividido {} vezes'.format(n,primo))
if primo == 2:
    print('O {} é primo!'.format(n))
else:
    print('O {} não é primo'.format(n))