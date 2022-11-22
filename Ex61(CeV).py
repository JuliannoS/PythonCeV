'''51 Remake
Lendo o primeiro termo e a razão de uma Pa. Mostrando os 10 primeiros termos da prograssão usando a estrura while'''

a1 = int(input('Digite o 1º termo: '))
r = int(input('Digite a razão: '))
cont = 1
termo = a1

while cont <= 10:
    print('{}'.format(termo), end='')
    print(' -> ' if cont < 10 else '   ', end='')
    termo += r
    cont +=1
