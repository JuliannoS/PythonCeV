'''Faça um programa que leia o ano de nascimento de um jovem e informe
de acordo com sua idade:
-Se ele ainda vai se alistar ao serviço militar.
-Se é a hora de se alistar
-Se já passou do tempo de alistamento

Considere: Seu programa também deverá mostrar o tempo que falta
ou passou do prazo'''
from datetime import date
ano = date.today().year
#a = 2022 - idade

s = str(input('Qual seu sexo: ').strip().title())
if s == "Feminino" or s == "F":
    print('Você não precisa fazer o alistamento obrigatorio!')
elif s == "Masculino" or s == 'M':
    nasc = int(input('Digite seu ano de nascimento: '))
    a = ano - nasc
    print('Quem nasceu no ano de {} tem {} anos em {}'.format(nasc, a, ano))

    if a == 18:
        print('Este ano você irar ter que se alistar')
    elif a <= 18:
        print('Você ainda vai precisar se alistar, mas não esse ano.')
        print('Faltam {} ano(s) para vc se alistar'.format(18 - a), end='. ')
        print('Sera no ano de {}'.format(ano + (18-a)))
    else:
        print('Você ja deveria ter se alistado há {} anos.'.format(a - 18))
        print('Seu alistamento foi em {}'.format(ano - (a - 18)))
else:
    print('Opção invalida, repita.')
'''-----------------------------------
from datetime import date 
atual = date.today().year
nasc = int(input('Ano de nascimento: ))
idade = atual - nasc
---------------------------------------'''