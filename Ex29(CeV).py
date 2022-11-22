'''Escreva um programa que leia a velocidade de um carro.
Se ele ultrapassar 80km/h, mostre uma mensagem dizendo que ele foi multado.
A multa vai custar R$7.0/km acima do limite'''

v = float(input('Qual a velocidade do carro: '))
if v >= 80:
    m = (v - 80) * 7
    print('''''Você foi multado!
O carro estava a {:.2f} e ultrapassou o limite de 80km/h
Tera que pagar multa de valor R$ {:.2f}'''.format(v, m))

print('Tenha um bom dia'.format(v))