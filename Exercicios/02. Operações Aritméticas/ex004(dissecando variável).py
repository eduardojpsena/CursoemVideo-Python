'''Ler algo pelo teclado e mostrar seu tipo primitivo e todas as informações sobre ele.'''

print(">>>DISSECANDO UMA VARIÁVEL<<<")

a = input("Digite algo: ")

print("O tipo primitivo dessa variável é: ", type(a))
print("É apenas espaços? ", a.isspace())
print("É um número? ", a.isnumeric())
print("É alfabético? ", a.isalpha())
print("É alfanumérico? ", a.isalnum())
print("Está em maisculas? ", a.isupper())
print("Está em minusculas? ", a.islower())
print("Está capitalizada? ", a.istitle())
