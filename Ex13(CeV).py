'''Faça um algoritmo que leia o salário de um funcinário e mostre seu novo salário. Com 13% de aumento'''

f = float(input('Qual é o salário do Funcionário? R$ '))
s = (f * 13 / 100) + f
print('Um funcionário que ganhava R$ {:.2f}, com 13% de aumento, passa a receber R$ {:.2f}'.format(f, s))
#---------------------------------------------------------
#exercicio extra: faça um algoritmo que calcule o desconto de um produto a vista e o aumento a prazo.
#-18% a vista e +9% a prazo
c = float(input('\nQual o valor do produto? R$ '))
a = c - (c * 18 / 100)
p = c + (c * 9 / 100)

print('O Produto Custa R${:.2f},\nPorem pagando A vista ganha desconto de 18%, com isso o preço fica R${:.2f}\nParcelando aumenta 9% do valor, ficando R${:.2f}'.format(c, a, p))