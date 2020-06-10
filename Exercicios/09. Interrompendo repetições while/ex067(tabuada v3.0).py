'''Faça um programa que mostre a tabuada de vários números, um de cada vez, para cada
valor digitado pelo usuário. O programa será interrompido quando o usuário digitar um
valor negativo'''

print("♣♣♣TABUADA V3♣♣♣")

while True:
    tab = int(input("Quer ver a tabuada de qual valor? (0 para finalizar):  "))
    if tab <= 0:
        break
    print("•"*30)
    for c in range (1, 11):
        print("     ► {} x {} = {}".format(tab, c, tab * c))
    print("•" * 30)
print("Programa finalizado.")