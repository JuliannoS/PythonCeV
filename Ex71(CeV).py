'''Crie um programa que simule o funcioanamento de um caixa eletronico.
No inicio, pergunte ao usuario qual sera o valor a ser sacado(numero inteiro)
e o programa vai informar quantas cédulas de cada valor serao entregues.
considerando cédulas de: R$ 50,20,10,1'''

v = 0
e = 's'
while e in "Ss":
    v = int(input('Qual valor deseja sacar: R$'))
