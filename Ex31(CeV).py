'''Desenvolva um programa que pergunte a distancia de uma viagem em Km.
Calcule o preço da passagem. Cobrando R$ 0.50/Km para viagens ate 200 Km
e R$ 0.45 para viagens mais longas'''

viagem = float(input('Qual a distancia da viagem em Km? '))

if viagem <= 200:
    p = viagem * 0.5
else:
    p = viagem * 0.45

print('A viagem de {} Km vai custar R$ {:.2f}'.format(viagem, p))

#p = viagem * 0.5 if viagem <= 200 else viagem * 0.45
#print('A viagem de {} Km vai custar R$ {:.2f}'.format(viagem, p))
