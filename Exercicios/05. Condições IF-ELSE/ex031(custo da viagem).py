'''Faça um programa que calcule o preço da passagem de acordo com os kms percorridos:
50 centavos por km para viajem ate 200km e 45 centavos para viagens mais longas.'''

print(">>>CUSTO DA VIAGEM<<<")

dist = float(input("Qual a distância da sua viajem? "))
if dist <= 200:
    preco = dist * 0.50
else:
    preco = dist * 0.45
print("Sua viajem de {} km vai custar R$ {:.2f}".format(dist, preco))
