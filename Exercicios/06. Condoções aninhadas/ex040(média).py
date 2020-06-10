'''Crie um programa que calcule a média de duas notas e informe se o aluno está
aprovado, reprovado ou em recuperação.'''

print("\033[0;35m>>>CALCULO DA MÉDIA<<<\033[m")

n1 = float(input("Digite a primeira nota: "))
n2 = float(input("Digite a segunda nota: "))
md = (n1 + n2) / 2

if md >= 7:
    print("\033[0;34mALUNO APROVADO!\033[m")
elif md > 4 and md < 7:
    print("\033[0;33mALUNO EM RECUPERAÇÃO!\033[m")
else:
    print("\033[0;31mALUNO REPROVADO!\033[m")
