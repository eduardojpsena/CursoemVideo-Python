'''Calcular a média de dois valores digitados pelo usuário.'''

print(">>>> CALCULO DA MÉDIA <<<<")

n1 = float(input("Digite o primeiro número: "))
n2 = float(input("Digite o segundo número: "))
md = (n1+n2)/2
print("A média entre {:.1f} e {:.1f} é {:.1f}!". format(n1, n2, md))
