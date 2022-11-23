'''Crie um programa que leia o nome de uma cidade e diga se ela começa com o nome
Santo'''

cidade = input('Ponha o nome de uma cidade: ').strip().title()
dividido = cidade.split()
print("Santo" in dividido[0])
print(cidade)