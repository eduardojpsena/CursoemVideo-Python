'''Crie um programa que leia o nome completo de uma pessoa e mostre: Quantas letras
ao todo, O nome com todas as letras maiusculas, com todas minusculas, quantas letras
tem o primeiro nome'''

print(">>>MANIPULANDO TEXTOS<<<")

nome = str(input("Digite seu nome completo: ")).strip()
prinome = nome.split()
print("Analisando seu nome...")
print("Seu nome tem ao todo {} letras;".format(len(nome) - nome.count(' ')))
print("Seu nome em letras maiúsculas: {};".format(nome.upper()))
print("Seu nome em letras minúsculas: {};".format(nome.lower()))
print("Seu primeiro nome é {} e tem {} letras.".format(prinome[0], len(prinome[0])))

'''► O split separa o nome em várias listas começando a contagem em [0]
► print("Seu primeiro nome tem {} letras".format(nome.find(' ')))'''
