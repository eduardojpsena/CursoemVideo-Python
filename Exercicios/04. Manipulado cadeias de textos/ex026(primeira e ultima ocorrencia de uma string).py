'''Faça um programa que leia uma frase pelo teclado e mostre: Quantas vezes aparece a
letra "a", em que posição ela aparece a primeira vez, em que posição ela aparece a
ultima vez.'''

print(">>>VERIFICANDO OCORRÊNCIA DE STRING<<<")

txt = str(input("Digite uma frase: ")).upper().strip()
print("A letra A aparece {} vezes".format(txt.count("A")))
print("A primeira letra A aparece na posição {}".format(txt.find("A")+1))
print("A ultima letra A aparece a posição {}".format(txt.rfind("A")+1))
