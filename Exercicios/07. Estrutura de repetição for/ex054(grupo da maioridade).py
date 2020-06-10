'''# Crie um programa que leia o ano de nascimento de sete pessoas. No final mostre
quantas pessoas ainda não atingiram a maioridade e quantas já são maiores.'''

print("♦♦♦GRUPO DA MAIORIDADE♦♦♦")

import datetime

maior = 0
menor = 0
for c in range(1, 8):
    anonasc = int(input("Ano de nascimento da {}° Pessoa: ".format(c)))
    id = datetime.date.today().year - anonasc
    if id >= 18:
        maior += 1
    else:
        menor += 1
print("• De acordo com as datas informadas: "
      "\n► {} são maiores de idade; "
      "\n► {} são menores de idade.".format(maior, menor))
