'''61 Remake pt 2
Perguntando para o usuario se ele quer mostrar mais alguns termos. O programa encerra quando ele disser que quer mostrar "0 Termo"'''
from time import sleep
a1 = int(input('Digite o 1º termo: '))
r = int(input('Digite a razão: '))
cont = 1
conta = 0
termo = a1
mais = 1
a = 0

while mais != 0:
    while cont <= 10:
        print('{}'.format(termo), end='')
        print(' -> ' if cont < 10 else '...', end='')
        termo += r
        cont += 1
    mais = int(input('\nQuantos termos você quer mostrar a mais ? '))
    while conta != mais:
        print('{}'.format(termo), end='')
        print(' -> ' if conta < (mais -1) else"...", end='')
        termo += r
        conta += 1
    a += mais
    if conta == mais:
        conta = 0
print('''\nFim da contagem!
O numero de termos contados foi de {}'''.format((cont + a - 1)))
