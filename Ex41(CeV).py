'''A confederação nacional de natação precisa de um programa que
leia o ano de nascimento de um atleta e mostre sua categoria.
de acordo com a idade:
- Até 9 anos: mirin
- Até 14 anos: infantil
- Até 19 anos: junior
- Até 20 anos: senior
- Acima: master'''
from datetime import date

nasc = int(input('Seu ano de nascimento: '))
ano = date.today().year
a = ano - nasc

print('O atleta tem {} então a sua categoria é:'.format(a), end=' ')
if a <= 9:
    print('Mirin')
elif a <= 14:
    print('Infantil')
elif a <= 19:
    print('Junior')
elif a <= 25:
    print('Senior')
else:
    print('Master')