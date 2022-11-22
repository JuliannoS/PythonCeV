'''Crie um programa que leia varios numeros interiros pelo teclado. No final da execução mostre a media entre todos os
valores e qual foi o maior e o menor valores lidos. O programa deve perguntar ao usuario se ele quer ou nao continuar a digitar valores
 '''
e = 'S'
cont = n = soma = maior = menor = 0


while e in "Ss":
    n = int(input('Digite um numero: '))
    e = str(input('''Deseja continuar?[S/N]
    Escolha: ''')).upper().strip()[0]
    soma += n
    cont += 1

    if cont == 1:
        menor = maior = n
    else:
        if n > maior:
            maior = n
        if n < menor:
            menor = n

print('O total de numeros digitados foi {}'.format(cont))
print('A Média dos valores foi de {}'.format(soma / cont))
print('A soma dos valores foi {}'.format(soma))
print('O maior valor foi {} e o menor {}'.format(maior, menor))