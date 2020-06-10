'''Crie um programa onde o usuário possa cadastrar vários valores númericos, e
cadastre-os em uma lista. Caso o número já exista la dentro, ele não será adicionado.
No final, serão exibidos todos os valores únicos digitados em ordem crescente.'''

print("◘◘◘VALORES ÚNICOS EM UMA LISTA◘◘◘")

lista = []
while True:
    n = int(input("Digite um número: "))
    if n not in lista:
        lista.append(n)
        print("Valor adicionado com sucesso.")
    else:
        print("Valor duplicado, não pode ser adicionado.")
    condição = str(input("Deseja continuar? [S/N] ")).strip().upper()[0]
    while condição not in "SN":
        condição = str(input("Deseja continuar? [S/N] ")).strip().upper()[0]
    if condição in 'N':
        break
print("=-"*20)
print("Você adicionou os valores {}".format(sorted(lista)))
