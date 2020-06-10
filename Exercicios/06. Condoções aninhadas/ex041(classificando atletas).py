'''Faça um programa que classifique a categoria de atletas em: mirim ate 9 anos,
infantil até 14 anos, junior até 19 anos, senio até 20 anos e master acima de 20 anos.'''

print(">>>CLASSIFICAÇÃO DE ATLETAS<<<")

id = int(input("Informe a idade do atleta: "))

if id <= 9:
    print("Categoria Mirim!")
elif 9 < id <= 14:
    print("Categoria Infantil!")
elif 14 < id <= 19:
    print("Categoria Junior!")
elif id == 20:
    print("Categoria Sênior!")
else:
    print("Categoria Master!")
