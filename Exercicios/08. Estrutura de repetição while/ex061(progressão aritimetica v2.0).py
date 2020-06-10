'''Desenvolva um programa que leia o primeiro termo e a razão de uma PA. No final
mostre os 10 primeiros termos dessa progressão usando while.'''

print(">>>PROGRESSÃO ARITIMETICA V2<<<")
print("♦"*20)
t1 = int(input("Primeiro termo da PA: "))
r = int(input("Razão da PA: "))
print("♦"*20)
c = 0
while c < 10:
    c += 1
    print("{} ".format(t1), end="► ")
    t1 += r
print("FIM!")