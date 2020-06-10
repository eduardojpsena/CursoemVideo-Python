'''Realizar calculo de reajuste salarial.'''

print(">>>> CALCULANDO REAJUSTE SALARIAL <<<< ")

salario = float(input("Qual seu salário? R$"))
reajuste = float(input("Valor do reajuste (%): "))
novo = salario + (salario*reajuste/100)
print("Um funcionário que ganhava R${:.2f}".format(salario), end=", ")
print("com reajuste de {}%, passa a receber R${:.2f}".format(reajuste, novo))
