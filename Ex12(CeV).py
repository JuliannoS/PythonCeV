'''Faça um algoritmo que leia o preço de um produto e mostre seu novo preço com desconto'''

p = float(input('Preço do produto: R$'))
d = p * 10 / 100
v = p - d
#v = p - (p * 10 / 100)

print('O produto que custa R${:.2f} com desconto de 10% fica com o valor de R${:.2f}'.format(p, v))