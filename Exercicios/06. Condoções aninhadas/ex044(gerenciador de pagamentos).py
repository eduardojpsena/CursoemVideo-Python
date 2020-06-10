'''Faça um programa que calcule o valor a ser pago de um produto de acordo com a
condição de pagamento: 10% a vista, 5% debito, sem juros 2x, 20% de juros 3x ou mais.'''

print("-=-=-GERENCIADOR DE PAGAMENTOS-=-=-")

preço = float(input("Valor do produto: R$"))
condpag = int(input('''[1] A vista
[2] Débito
[3] A prazo
Método de pagamento: '''))

if condpag == 1:
    preço = preço - (preço * 10/100)
    print("Desconto de 10% no valor do produto: R$ {:.2f}".format(preço))
elif condpag == 2:
    preço = preço - (preço * 5/100)
    print("Desconto de 5% no valor do produto: R$ {:.2f}".format(preço))
elif condpag == 3:
    divisão = int(input("Informe em quantas parcelas deseja dividir: "))
    preço = preço + (preço * 20/100)
    parcelas = preço / divisão
    print("Juros de 20% em cima do valor do produto: R$ {:.2f}".format(preço))
    print("{}x de {:.2f} por mês!".format(divisão, parcelas))
else:
    print("Opção invalida, tente novamente!")
