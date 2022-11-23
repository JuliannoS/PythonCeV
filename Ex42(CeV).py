'''35 REMASTER
-Equilatero = todos os lados iguais
-Isósceles = dois lados iguais
-Escaleno = Todos os lados diferentes'''

s1 = int(input('Primeiro segmento: '))
s2 = int(input('Segundo segmento: '))
s3 = int(input('Terceiro segmento: '))

if (s2 - s3 < s1 < s2 + s3) and (s1 - s3 < s2 < s1 + s3) and (s1 - s2 < s3 < s1 + s2):
    print('Esses três segmentos podem formar um triangulo!')
    if s1 == s2 and s1 == s3:
    #if s1 == s2 == s3:
        print('O triangulo possui todos os lados iguais, então:')
        print('é Equilatero')
    elif s1 != s2 and s1 != s3 and s2 != s3:
    #if s1 != s2 != s3 != s1:
        print('O triangulo nao tem nenhum segmeto igual, então:')
        print('é Escaleno')
    elif (s1 != s2 and s2 == s3) or (s1 != s3 and s3 == s2) or (s2 != s3 and s1 == s3):
    #else:
        print('O triangulo tem dois segmentos iguais, então:')
        print('é Isósceles')
else:
    print('Os 3 segmentos não podem formar um triangulo!')