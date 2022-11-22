'''Crie um programa que converta a quantia de dinheiro de Real para Dolar, Euro e yenis
considerando(22/07/22) US$ 1 = R$ 5,46 / EU$ 1 = R$ 5,56 /  JP$ 1 = R$ 0,040'''
r = float(input('Quanto dinheiro você tem? R$ '))
d = r / 5.46
e = r / 5.56
i = r / 0.040
print('''Com R$ {:.2f} você pode comprar:
US$ {:.2f}
EU$ {:.2f}
{:.2f} Ienes'''.format(r, d, e, i))

#FLOAT USA PONTO, NUNCA USE VIRGULA PRA NUMERO