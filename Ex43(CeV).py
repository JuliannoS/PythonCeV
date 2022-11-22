'''Desenvolva uma lógica que leia o peso e a altura de uma pessoa
calcule seu IMC e mostre seu status. De acordo com a tabela abaixo
- Abaixo de 18.5: Abaixo do peso
- Entre 18.5 e 25: Peso ideal
- 25 até 30: Sobrepeso
- 30 até 40: Obesidade
- Acima de 40: Obesidade Mórbida'''

peso = float(input('Qual seu peso? (Kg) '))
alt = float(input('Qual sua altura? (M) '))

imc = peso / (alt ** 2)
print('Seu imc é {:.1f}, então você está '.format(imc), end='')
if imc < 18.5:
    print('abaixo do peso!')
elif 18.5 <= imc < 25:
    print('com Peso ideal!')
elif 25 <= imc < 30:
    print('com Sobrepeso!')
elif 30 <= imc < 40:
    print('Com obesidade!')
else:
    print('Com Obesidade Mórbida!')
