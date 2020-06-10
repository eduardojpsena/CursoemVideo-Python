'''Faça um programa que calcule o aumento de salário de um funcionário para salario
acima de 1250 reais aumento de 10%, para salarios abaixo aumento de 15%.'''

print(">>>AUMENTO DE SALÁRIO<<<")

salario = float(input("Qual é o salário do funcionário? R$ "))
if salario > 1250:
    newsalario = salario + (salario * 10/100)
else:
    newsalario = salario + (salario * 15/100)
print("Quem ganhava R$ {:.2f} passa a receber R$ {:.2f}".format(salario, newsalario))
