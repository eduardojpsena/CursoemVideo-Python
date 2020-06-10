'''Desenvolva um programa que leia o primeiro termo e a razão de uma PA. No final
mostre os 10 primeiros termos dessa progressão. Quando acabar pergunta ao usuário
se quer mostrar mais termos. encerra quando disser que quer mostrer 0 termos.'''

print(">>PROGRESSÃO ARITIMETICA V3<<")

print("♦"*40)
t1 = int(input("Primeiro termo da PA: "))
r = int(input("Razão da PA: "))
print("♦"*40)
print("Os 10 primeiros termos da PA são:")

qtermos = 10
ctotal = 0
while qtermos != 0:
    c = 0
    while c < qtermos:
        c += 1
        print("{} ".format(t1), end="► ")
        t1 += r
        ctotal += 1
    print("PAUSA!")
    qtermos = int(input("Quantos termos quer mostrar a mais? "))

print("Progressão finalizada com {} termos exibidos.".format(ctotal))

