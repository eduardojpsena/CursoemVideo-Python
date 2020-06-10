'''Crie um programa que leia vários números e coloque em uma lista. Depois disso, crie
outras duas listas contento apenas os números pares e números ímpares e mostre todas as
listas.'''

print("•••DIVIDINDO VALORES EM VÁRIAS LISTAS•••")

lista = []
listapar = []
listaimpar = []
while True:
    n = int(input("Digite um valor: "))
    lista.append(n)
    if n % 2 == 0:
        listapar.append(n)
    else:
        listaimpar.append(n)
    condição = ' '
    while condição not in "SN":
        condição = str(input("Deseja continuar? [S/N] ")).strip().upper()[0]
    if condição == 'N':
        break
print("=-"*30)
print(f"A lista completa é: {lista}")
print(f"A lista de pares é: {listapar}")
print(f"A lista de ímpares é: {listaimpar}")
