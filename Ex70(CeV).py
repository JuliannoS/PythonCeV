'''Crie um programa que leia nome e o preço de varios produtos;
O programa devera perguntar se o usuario vai continuar.
no final mostre:
a) qual é o total de gastos na compra.
b) quantos produtos custam mais de R$1000
c) qual é o produto mais barato.'''

n = p = g = m = bp = bn = cont = 0
e = 's'
while e in 'Ss':
    n = str(input('Nome do produto: ')).strip().capitalize()
    p = float(input('Qual o preço: R$ '))

    cont += 1
    g += p
    if p >= 1000:
        m += 1

    if cont == 1:
        bp = p
        bn = n
    else:
        if p < bp:
            bp = p
            bn = n

    e = str(input('Quer Continuar? [S / N] ')).upper().strip()[0]
print(f'''Fim da operação!
O total de gastos foi de R${g:.2f}
Teve ao todo {m} Produtos acima de R$1000
O produto {bn} foi o mais barato custando R${bp:.2f}''')
