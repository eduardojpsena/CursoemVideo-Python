'''Escreva um programa que leia um numero inteiro qualquer e peça para ele escolher a
base de conversão: 1 para binário, 2 para octal e 3 para hexadecimal.'''

print("\033[0;34m-=-=-Conversor de base numérica-=-=-\033[m")

n = int(input("Escreve o número que deseja a conversão: "))
print('''Código de conversão: 
[1] BINÁRIO 
[2] OCTAL 
[3] HEXADECIMAL''')
cod = int(input("Digite o código de conversão: "))


if cod == 1:
    print("{} convertido para BINÁRIO é igual a {}".format(n, bin(n)[2:]))  #O [2:] é usado como opção de fatiamento
elif cod == 2:
    print("{} convertido para OCTAL é igual a {}".format(n, oct(n)[2:]))
elif cod == 3:
    print("{} convertido para HEXADECIMAL é igual a {}".format(n, hex(n)[2:]))
else:
    print("Código informado incorreto, tente novamente! ")
