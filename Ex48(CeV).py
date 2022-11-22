'''Faça um programa que calcule a soma entre todos os numeros impares que são multiplos de 3 e que se encontram no intervalo de 1 até
 500'''

s = 0
cont = 0
for a in range(1,501,2): #era 500, 50 é so pra acelerar o teste
    if a % 3 == 0:
        s += a
        cont += 1
print('\n A soma dos {} numeros é {}'.format(cont, s))
