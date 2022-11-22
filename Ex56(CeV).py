'''Desenvolva um programa que leia o nome, dade e sexo de 4 pessoas. no final do programa mostre
-A média da idade do grupo
-qual é o nome do homen mais velho
-quantas mulheres tem menos de 20 anos'''
velho = ""
id = 0
media = 0
cont = 0
for a in range(1, 5):
    print('----- {}ª PESSOA -----'.format(a))
    nome = str(input('Nome: ')).strip().title()

    idade = int(input('Idade: '))
    media += idade

    sexo = str(input('Sexo [M/F]: ')).upper().strip()
    if ("F" in sexo) and idade <= 20:
        cont += 1

    if "M" in sexo:
        if a == 1:
            velho = nome
            id = idade
        else:
            if idade > id:
                velho = nome
                id = idade



print('A média de idade do grupo é de {} anos'.format(media / a))
print('Ao todo são {} mulheres com menos de 20 anos'.format(cont))
print('O Homem mais velho tem {} anos e se chama {}'.format(id, velho))