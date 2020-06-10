'''Crie um programa que leia uma frase qualquer e diga se ela é um palíndromo,
desconsiderando os espaços.'''

print("•••DETECTOR DE PALÍNDROMO•••")

frase = str(input("Digite uma frase: ")).upper().strip()
fraseseparada = frase.split()
frasejunta = "".join(fraseseparada)
inverso = ''
for letra in range (len(frasejunta) - 1, 0 - 1, -1):
    inverso += frasejunta[letra]
print("Frase: {}".format(frasejunta))
print("Inverso: {}".format(inverso))
if frasejunta == inverso:
    print("A frase é um Palíndromo.")
else:
    print("Não é um Palíndromo.")
