'''Faça um programa que leia um número de 0 a 9999
e mostre na tela cada um dos digitos separados
exemplo: numero = 1234
unidade:4 // dezena: 3 // centena: 2 // milhar: 1'''
'''Modo String'''

numero = input('Ponha um numero entre 0 e 9999: ')
print('''O numero {} é dividido em
unidade: {}
dezena: {}
centenas: {}
milhar: {} '''.format(numero, numero[3], numero[2], numero[1], numero[0]))

'''Esse modo tem um problema que se o numero nao tiver os 4 digitos ele trava
existe modos pra resolver isso, mas o usado agr é o Metodo numerico'''

'''Metodo numerico'''
num = int(input('Digite um numero: '))
"''Fatiando um numero, divide por tanto de o % pega o resto"
u = num // 1 % 10
d = num // 10 % 10
c = num // 100 % 10
m = num // 1000 % 10
print('''Analisando o número {}
Unidade: {}
Dezenas: {}
Centenas: {}
Milhar: {}'''.format(num,u,d,c,m))