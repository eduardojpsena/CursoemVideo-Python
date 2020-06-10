'''Digitar um valor em metros e converter para km, hm, dam, dm, cm, mm.'''

print(">>>> CONVERSOR DE MOEDAS <<<<")

real = float(input("Digite o valor em real: R$"))
cotação = 4.86
dolar = real / cotação

print("→ R${:.2f} reais equivale a US${:.2f} dolars".format(real,dolar))
