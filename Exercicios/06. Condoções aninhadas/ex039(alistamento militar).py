'''Faça um programa que leia o ano de nascimento de um jovem e informe se ele ainda
vai se alistar, se é a hora de se alistar ou se já passou o tempo de alistamento deve
mostrar o tempo que falta ou o tempo que já passou também.'''

print("\033[0;32m=-=-=-Alistamento Militar-=-=-=\033[m")
import datetime

nasc = int(input("Ano de nascimento: "))
idade = datetime.date.today().year - nasc
print("Quem nasceu em {} tem {} anos.".format(nasc, idade))
if idade > 18:
    print("Seu alistamento foi em {}.".format(nasc + 18))
elif idade < 18:
    print("Seu alistamento será em {}.".format(nasc + 18))
else:
    print("Você deve se alistar neste ano.")
