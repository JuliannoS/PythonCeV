'''Desenvolva um programa que leia o primeiro termo e a razão de uma PA.
No final. Mostre os 10 primeiros termos dessa progressão'''

a1 = int(input('Digite o primeiro Termo: '))
r = int(input('Digite a razão da PA: '))
f = 0

f = a1 + (10 - 1) * r #calculo da pa
for pa in range(a1 , f + r, r):
    print(pa, end=' --> ')
print('Acabou.')