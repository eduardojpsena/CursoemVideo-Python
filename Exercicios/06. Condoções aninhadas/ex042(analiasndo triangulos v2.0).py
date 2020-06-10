'''Faça um programa que leia 3 segmentos de reta e diga se o triângulo é equilátero,
isóscles, escaleno ou se não pode formar um triângulo.'''

print(">>>ANALISANDO TRIÂNGULOS<<<")

s1 = float(input("Primeiro segmento de reta: "))
s2 = float(input("Segundo segmento de reta: "))
s3 = float(input("Terceiro segmento de reta: "))

if s1 + s2 > s3 and s1 + s3 > s2 and s2 + s3 > s1:
    print("É possivel formar um triângulo", end=' ')
    if s1 != s2 != s3 != s1:
        print("ESCALENO!")
    elif s1 == s2 == s3:
        print("EQUILÁTERO!")
    else:
        print("ISÓCELES!")
else:
    print("Não é possivel formar um triângulo!")
