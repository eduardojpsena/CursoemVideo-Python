'''Faça um programa que leia o sexo de uma pessoa, mas só aceite 'M' ou 'F'.
Caso esteja errado, peça a digitação novamente até ter um valor correto.'''

print("-=VALIDAÇÃO DE DADOS-=")

sexo = str(input("Informe seu sexo [M/F]: ")).strip().upper()[0]
while sexo not in 'MF':
    sexo = str(input("Dados inválidos. Por favor informe seu sexo [M/F]: ")).strip().upper()[0]
print("Sexo {} registrado com sucesso.".format(sexo))

#Esse [0] é pra pegar apenas a primeira letra do nome digitado