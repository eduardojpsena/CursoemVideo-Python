'''Digitar um valor em metros e converter para km, hm, dam, dm, cm, mm.'''

print(">>>> CONVERSOR DE MEDIDAS <<<<")

n = float(input("Digite a distância em metros: "))
print("A medida de {} m corresponde a:".format(n))
print("{} km;\n{} hm;\n{} dam;\n{} dm;\n{} cm;\n{} mm.".format(n/1000, n/100, n/10, n*10, n*100, n*1000))
