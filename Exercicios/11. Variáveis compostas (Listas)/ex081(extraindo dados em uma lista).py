'''Crie um programa que vai ler vários números e colocar em uma lista. Depois disso,
mostre: [A] Quantos números foram digitados, [B] A lista de valores, ordenada de forma
decrescente, [C] Se o valor cinco foi digitado e está ou não na lista.'''

print("♦♦EXTRAINDO DADOS EM UMA LISTA♦♦")

lista = []
while True:
    n = int(input("Digite um valor: "))
    lista.append(n)
    condição = ' '
    while condição not in 'SN':
        condição = str(input("Deseja continuar? [S/N] ")).strip().upper()[0]
    if condição == 'N':
        break
print("-="*30)
print(f"Você digitou {len(lista)} elementos à lista.")
lista.sort(reverse=True)
print(f"Os valores em ordem decrescente são: {lista}")
if 5 in lista:
    print(f"O valor 5 está presente na lista.")
else:
    print(f"O valor 5 não foi encontrado na lista.")