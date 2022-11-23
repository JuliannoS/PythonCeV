'''Faça um programa que mostre a tabuada de vários números, um de cada vez
para cada valor digitado pelo usuário. O programa será interrompido quando
o número solicitado for negativo'''

n = m = 0
cont = 1

while True:
    print("--"*20)
    n = int(input('Digite um valor {valor negativo para parar}: '))

    cont = 1
    if n >= 0:
        m = int(input('Quantos valores você quer na tabuada: '))
        while cont <= m:
            print(f'{n} x {cont} = {n * cont}')
            cont += 1
    else:
        print('Fim da operação!')
        break