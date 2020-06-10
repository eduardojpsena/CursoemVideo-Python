'''Faça um programa que leia um ano e mostre se ele é um ano bissexto.'''

print(">>>ANO BISSEXTO<<<")

import datetime

ano = int(input("Qual ano quer análisar? Coloque 0 para analisar o ano atual: "))
if ano == 0:
    ano = datetime.date.today().year
if (ano % 4 == 0) and (ano % 100 != 0) or (ano % 400 == 0):
    print("O ano {} é bissexto".format(ano))
else:
    print("O ano {} não é bissexto".format(ano))
