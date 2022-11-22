'''Desafio 09 Remake
Mostrando a tabuada de um numero que o usuario escolher. Só que agora utilizando o laço for'''

num = int(input('Digite um numero: '))
for a in range(2,21):
    #total = num * a
    #print('{} x {:2} = {}'.format(num, a, total))
    print('{} x {:2} = {}'.format(num, a, num * a))
