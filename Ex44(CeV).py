'''Elabore um programa que calcule o valor a ser pago por um produto.
Considerando o seu preço normal e condição de pagamento:
- Á vista dinheiro/cheque: 10% de desconto
- Á vista no cartão: 5% de desconto
- Em até 2x no cartão: Preço normal
- 3x ou mais no cartão: 20% de juros'''

print('{:=^40}'.format(' Lojas Macedo ')) #{:=^40} -> ^ = centraliza ; =40  = adciona 40 tracinhos
p = float(input('Preço do produto: R$ '))
print('''Opções de pagamento
[1] Á Vista no dinheiro ou cheque
[2] No Cartão''')
f = int(input('Forma de pagamento: '))

if f == 1:
    d = p - (p * 10/100)
    print('-' * 50)
    print('O Valor do produto fica em R$ {:.2f}'.format(d))

elif f == 2:
    print('-' * 50)
    print('''Opções de parcelamento:
[1] Á vista
[2] 2x no cartão
[3] 3x ou mais parcelas''')
    a = int(input("Escolha: "))
    if a == 1:
        d = p - (p * 5 / 100)
        print('-' * 50)
        print('O valor do produto fica em R$ {:.2f}'.format(d))
    elif a == 2:
        print('-' * 50)
        print('O valor do produto fica em 2 parcelas de R$ {:.2f}'.format(p/2))
    elif a == 3:
        n = int(input('Quantas prestações: '))
        d = p + (p * (20 / 100))
        print('-' * 50)
        print('O valor do produto fica em {} parcelas de R$ {:.2f} com 20% de juros'.format(n, d/n))
        print('O valor do produto de R${:.2f} vai custar R${:.2f}'.format(p,d))
    else:
        print('-' * 50)
        print('Opção Invalida, escolha denovo!')
else:
    print('-' * 50)
    print('Você selecionou uma forma de pagamento indisponível, escolha denovo!')

print('Obrigado pela compra!')
