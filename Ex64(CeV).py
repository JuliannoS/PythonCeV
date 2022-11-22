'''Crie um programa que leia varios numeros inteiros pelo teclado. O programa so vai parar quando o usuario digitar o valor 999
que é a condição de parada. No final mostre quantos numeros foram digitados e qual foi a soma entre eles.Desconsiderando o flag'''

numero = cont = soma = 0
while numero != 999:
    numero = int(input('Digite um numero[999 para parar]: '))
    cont += 1
    soma += numero
print('A soma dos {} numeros que você digitou é {}'.format(cont - 1, soma-999))