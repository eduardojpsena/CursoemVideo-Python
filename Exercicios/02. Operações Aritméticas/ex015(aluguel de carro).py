'''Calcular o valor do aluguel de um carros pelos dias alugados.'''

print(">>>> ALUGUEL DE CARRO <<<<")

dias = int(input("Quantos dias alugados? "))
km = float(input("Quantos Km rodados? "))
pago = (60 * dias) + (0.15 * km)
print("O total a pagar é R${:.2f}".format(pago))
