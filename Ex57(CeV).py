'''faça um programa que leia o sexo de uma pessoa. mas so aceite os valores "M" ou "F". Caso esteja errado faça a digitação novamente até ter um valor
 correto'''

s = ""
cont = 0
#while s not in 'MmFf'
#   s = str(input('Opção invalida, tente novamente:  )).strip().upper()[0]
while cont != 1:
    s = str(input('M OU F : ')).upper().strip()[0]
    if ("M" in s) or ('F' in s):
        cont += 1
    else:
        print('Opção Invalida, tente novamente!')
print('--'*20)
print('Opção foi registrada!')

