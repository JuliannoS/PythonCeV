'''Faça um programa que leia uma frase pelo teclado e mostre:
Quantas vezes aparece a letra "a"
Em que posição ela aparece a primeira vez
Em que posição ela aparece a ultima vez'''

frase = str(input('Ponha uma frase: ')).strip().lower()
print('A letra "a" apareceu um total de {} vezes'.format(frase.count("a")))
print('A letra "a" apereceu a primeira vez em {}'.format(frase.find("a")+1))
print('A letra "a" apareceu pela ultima vez em {}'.format(frase.rfind("a")+1))