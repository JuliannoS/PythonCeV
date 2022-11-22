'''Escreva um programa para aprovar o empréstimo bancário para
a compra de uma casa. O programa vai perguntar o VALOR DA CASA,
o SALÁRIO do comprador e em QUANTOS ANOS ele vai pagar.
Calcule O valor da prestação mensal, sabendo que ela não pode
exceder 30% do salário ou então o empréstimo sera negado.'''

casa = float(input('Qual o valor da Casa? R$ '))
sal = float(input('Qual seu salário? R$ '))
ano = int(input('Durante quantos anos irar pagar ? '))

m = 12 * ano
p = casa / m
d = sal * 30/100

print('Seu pagamento ficara em {} vezes de R${:,.2f}'.format(m, p))
if p <= d:
    print('Parabens você pode receber o Emprestimo')
else:
    print('Infelizmente você não pode receber')
