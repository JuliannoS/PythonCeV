'''Faça um programa que leia o nome completo de uma pessoa. Mostrando
em seguida o primeiro e o último nome separadamente'''

nome = str(input("Ponha seu nome completo:")).strip().title()
#n = nome.split()
print("Nome completo: {}"
      "\nPrimeiro nome: {}"
      "\nUltimo nome: {}".format(nome, nome[:nome.find(' ')], nome[nome.rfind(' '):]))
#print('ultimo nome: {}". format(nome[len(n) - 1] )
