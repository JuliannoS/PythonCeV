'''Crie um programa que leia vários números inteiros pelo teclado.
O programa so vai parar quando o usuário digitar o valor 999.
No final mostre quantos números foram digitados e qual foi a soma entre eles'''

n = cont = soma = 0

while True:
    n = int(input('Digite um valor {999 para fechar}: '))
    if n != 999:
        cont += 1
        soma += n
    else:
        break
print(f'''\nFim do processo!
A Quantidade de valores digitados foram {cont}
E a soma entre esses valores é de {soma}''')
