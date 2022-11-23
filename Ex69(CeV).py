'''Crie um programa que leia a idade e o sexo de varias pessoas.
a cada pessoa cadastrada, o programa devera perguntar se o usuario
quer ou não continuar, no final mostre
a) quantas pessoas tem mais de 18 anos
b) quantos homens foram cadastrados
c)quantas mulheres tem menos de 20 anos'''

idade = sexo = ci = ch = cm = 0
f = 's'
while f in "sS":
    idade = int(input('Qual sua idade: '))
    sexo = str(input('Qual seu sexo[M ou F]: ')).upper().strip()[0]
    print(sexo)
    if idade >= 18:
        ci += 1
    elif sexo in 'Mm':
        ch += 1
        print('a')
    elif 'F' in sexo and idade >= 20:
        cm += 1
        print('b')

    f = str(input('Deseja continuar [S ou N]')).upper().strip()[0]

print(f'''Operação finalizada!
O numero de maiores de 18 foi de {ci}
O numero de Homens cadastrados é de {ch}
O numero de Mulheres com mais de 20anos foi de {cm}''')
