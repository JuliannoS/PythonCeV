'''Faça um programa que leia um ano qualquer e mostre se ele é bissexto'''
from  datetime import date
ano = int(input("Qual ano? "))
b = ano % 4
b1 = ano % 100
b2 = ano % 400
if b == 0 and b1 != 0 or b2 == 0 : #and e or pra por mais variaveis

    print('Este ano é bissexto')
else:
    print('Este ano não é bissexto')