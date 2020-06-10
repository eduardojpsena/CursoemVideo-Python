'''Faça um programa que leia 5 falores númericos e guarde em uma lista. No final
mostre qual foi o maior valor e o menor valor digitados e as suas respectivas posições
na lista.'''

print("•••MAIOR E MENOR VALORES EM LISTA•••")

lista = []
maior = menor = 0
for c in range(0, 5):
    lista.append(int(input(f"Digite o {c+1}º Valor: ")))
    if c == 0:
        maior = menor = lista[c]
    else:
        if lista[c] > maior:
            maior = lista[c]
        if lista[c] < menor:
            menor = lista[c]
# maior = max(lista)
# menor = min(lista)
print(f"Você digitou os valores: {lista}")
print("O maior valor digitado foi {}, nas posições ".format(maior),end='')
for i, v in enumerate(lista):
    if v == maior:
        print("{}... ".format(i+1),end='')
print("\nO menor valor digitado foi {}, nas posições ".format(menor),end='')
for i, v in enumerate(lista):
    if v == menor:
        print("{}... ".format(i + 1), end='')