'''Desenvolva um programa que leia quatro valores pelo teclado e guarde em uma tupla.
No final mostre: [A] Quantas vezes apareceu o número 9, [B] Em que posição foi digitado
o primeiro valor 3, [C] Quais foram os números pares.'''

print("•••ANÁLISE DE DADOS COM TUPLAS•••")

num = (int(input("Digite o 1º número: ")), int(input("Digite o 2º número: ")),
       int(input("Digite o 3º número: ")), int(input("Digite o 4º número: ")))
print("=-"*20)
print("Você digitou os valores: {}".format(num))
print("=-"*20)
print("O valor 9 apareceu {} vezes;".format(num.count(9)))
if 3 in num:
    print("O valor 3 apareceu na {}ª posição;".format(num.index(3)+1))
else:
    print("O valor 3 não foi encontrado em nenhuma posição;")
print("Os valores pares foram: ", end='')
for n in num:
    if n % 2 == 0:
        print(n, end=' ')
