'''Faça uma tabuada de um número selecionado pelo usuário utilizando laço for.'''

print("-=-=-TABUADA-=-=-")

n = int(input("Digite um número para exibir sua tabuada: "))
for c in range(1, 11):
    print("• {} x {} = {}".format(n, c, n*c))
print("FIM!!")