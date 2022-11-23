'''Escreva um programa que perguunta o salário de um funcionário e calcule
o valor do seu aumento.
Para salários superiores a R$ 1250, calcule um aumento de 10%
Para salários abaixo ou iguais, o aumento é de 15%'''

s = float(input('Qual o valor do salario? R$ '))
if s <= 1250:
    d= (s * 15 / 100) + s
    print('O salário de R${:.2f} recebeu o aumento de 15% e foi para R${:.2f}'.format(s, d))
else:
    d = (s * 10 / 100) + s
    print('O salário de R${:.2f} recebeu o aumento de 10% e foi para R${:.2f}'.format(s, d))