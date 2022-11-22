'''Escreva um programa que pergunte a quantidade de Km percorridos
por um carro alugado e a quantidade de dias pelos quais ele foi alugado.
Calcule o preço a pagar, considerando que o carro custa R$60/dia e R$0,15/km'''

d = int(input('Quantos Dias alugados? '))
k = float(input('Quantos Km rodados? '))
pd = 60 * d
pk = 0.15 * k
c = pd + pk
#c = (60 * d) + (0,15 * k) resolução em uma linha.
print('O total a pagar é de R$ {:.2f}'.format(c))
