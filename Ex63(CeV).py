'''Escreva um programa que leia um numero N inteiro qualquer e mostre na tela os N primeiros elementos de uma sequencia de fibonacci'''
cont = 0
fib = int(input('Digite quantos elementos você quer ver: '))
n = 0
s = 1
print("0 --> ", end="")
while cont != fib -1:
    s = s + n
    n = s - n
    cont += 1
    print(n, end=" --> ")
print("Acabou")