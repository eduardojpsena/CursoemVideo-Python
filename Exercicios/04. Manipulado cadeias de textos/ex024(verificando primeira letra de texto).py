'''Crie um programa que leia o nome de uma cidade e diga se ela começa ou não com o
nome "Santo".'''

print(">>>VERIFICANDO PRIMEIRO NOME<<<")

txt = str(input("Digite o nome de uma cidade: ")).title().strip()
prinome = (txt.split()[0])
print("O nome da cidade começa com Santo? ", "Santo" in prinome)
