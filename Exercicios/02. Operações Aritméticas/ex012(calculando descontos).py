'''Realizar calculo de desconto de um produto.'''

print(">>>> CALCULANDO DESCONTO <<<< ")

vl = float(input("Digite o valor do produto: R$ "))
ds = float(input("Informe o desconto (%): "))
tt = vl * (ds/100)
total = vl - tt
print("•" * 29)
print("Preço da mercadoria: R${:.2f}\nDesconto: {:.2f}%".format(vl, ds))
print("Valor a pagar: R${:.2f}".format(total))
print("•" * 29)
