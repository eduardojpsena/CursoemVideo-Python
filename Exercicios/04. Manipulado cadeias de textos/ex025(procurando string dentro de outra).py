'''Crie um programa que leia o nome de uma pessoa e diga se ela tem "Silva" no nome.'''

print(">>>PROCURANDO NOME<<<")

nome = str(input("Digite seu nome completo: ")).title().strip()
print("Seu nome tem Silva?", "Silva" in nome)
