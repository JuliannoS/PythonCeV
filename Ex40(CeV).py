'''Crie um programa que leia duas notas de um aluno e calcule
sua média. Mosrando uma mensagem no final. De acordo com a média
- média abaixo de 5: Reprovado
- média entre 5 e 6.9: Recuperação
- média 7 ou maior: Aprovado'''

n1 = float(input('Nota 1: '))
n2 = float(input('Nota 2: '))

m = (n1 + n2) / 2

if m >= 7:
    print('Parabens você esta aprovado, sua média foi {:.1f}'.format(m))
elif m >= 5:
    print('Sua média foi {:.1f}, Esta de recuperação.'.format(m))
else:
    print('Infelizmente você esta reprovado. Sua média foi {:.1f}'.format(m))