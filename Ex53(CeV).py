'''Crie um programa que leia uma frase qualquer e diga se ela é um palindromo.desconsiderando os espaços'''

f = str(input('Digite um frase: ').strip().upper())
seperado = f.split()
junto = ''.join(seperado)
inverso = ""
#solução com for
for a in range(len(junto)-1, -1, -1):
    inverso += junto[a]
print('O inverso de {} é {}'.format(junto, inverso))
if inverso == junto:
    print('É um palindromo!')
else:
    print('Não é um palindromo!')
