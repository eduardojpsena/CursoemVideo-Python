'''Faça um programa para aprovar um emrprestimo bancário para a compra de uma casa.
O programa vai perguntar o valor da casa, o salário do comprador e em quantos anos
vai pagar Calculo do valor da prestação mensal sabendo que não pode exceder 30% do
salário ou o emprestimo é negado.'''

print("=-=-=Compra da casa nova=-=-=")

casa = float(input("Valor da casa: R$"))
salario = float(input("Salário do comprador: R$"))
anos = int(input("Quantos anos de financiamento: "))
parcelas = anos * 12
prestacao = casa / parcelas

if prestacao > (salario * 30/100):
    print("Emprestimo NEGADO!")
else:
    print("O valor da prestação mensal será R${:.2f}\nEmprestimo pode ser CONCEDIDO!".format(prestacao))
