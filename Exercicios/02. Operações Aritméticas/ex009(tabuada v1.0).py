'''Digitar um número e mostrar sua tabuada.'''

print(">>>> TABUADA <<<<")

n = int(input("Digite um número: "))
print("••Tabuada de {}••".format(n))
print("  → {} x 1 = {}\n  → {} x 2 = {}\n  → {} x 3 = {}".format(n, n*1, n, n*2, n, n*3))
print("  → {} x 4 = {}\n  → {} x 5 = {}\n  → {} x 6 = {}".format(n, n*4, n, n*5, n, n*6))
print("  → {} x 7 = {}\n  → {} x 8 = {}\n  → {} x 9 = {}".format(n, n*7, n, n*8, n, n*9))
print("  → {} x 10 = {}".format(n, n*10))
print("•" * 17)
