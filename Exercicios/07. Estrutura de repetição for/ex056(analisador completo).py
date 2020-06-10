'''Desenvolva um programa que leia: nome, idade e sexo de quatro pessoas. E no final
mostre: A média de idade do grupo, Qual é o nome do homem mais velho, quantas mulheres
tem menos de 20 anos.'''

print("♠♠ANÁLISADOR COMPLETO♠♠")

somaidade = 0
idadehomem = 0
nomehomem = ''
mulher20 = 0
for c in range(1, 5):
    print("-=-=-{}ª PESSOA-=-=-".format(c))
    n = str(input("Nome: ")).title()
    id = int(input("Idade: "))
    sx = str(input("Sexo (M ou F): "))
    somaidade += id
    if c == 1 and sx in 'mM':
        idadehomem = id
        nomehomem = n
    if sx in 'mM' and id > idadehomem:
        idadehomem = id
        nomehomem = n
    if sx in 'fF' and id < 20:
        mulher20 += 1
mediaidade = (somaidade / c)
print("A média de idade do grupo é de {} anos;".format(mediaidade))
print("O homem mais velho tem {} anos e se chama {};".format(idadehomem, nomehomem))
print("{} mulheres tem menos de 20 anos.".format(mulher20))
