'''Crie um programa que leia o nome e preço de vários produtos. O programa deve
perguntar se o usuário vai continuar. No final mostre: [A] O total gasto na compra
[B] Quantos produtos custam mais de 1000 reais e [C] Qual o nome do produto mais
barato.'''

print("-=-ESTATÍSTICA EM PRODUTOS-=-")

gastototal = prodmil = menorpreço = 0
prodmenor = ' '
c = 0
while True:
    print("-" * 31)
    produto = str(input("Nome do produto: ")).strip()
    preço = float(input("Preço: R$ "))
    gastototal += preço
    c += 1
    if preço > 1000:
        prodmil += 1
    if c == 1:
        menorpreço = preço
        prodmenor = produto
    else:
        if preço < menorpreço:
            menorpreço = preço
            prodmenor = produto
    situation = ' '
    while situation not in 'SN':
        situation = str(input("Deseja continuar? [S/N]: ")).strip().upper()[0]
    if situation in 'N':
        break
print("------- FIM DO PROGRAMA -------")
print("O total gasto na compra foi de R$ {:.2f};".format(gastototal))
print("Temos {} produtos custando mais que R$ 1000,00;".format(prodmil))
print("O produto mais barato foi {} custando R$ {:.2f}.".format(prodmenor, menorpreço))
