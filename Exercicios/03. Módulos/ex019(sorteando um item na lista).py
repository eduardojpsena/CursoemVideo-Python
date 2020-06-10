'''Faça um script que realize um sorteio entre 4 alunos.'''

print(">>>SORTEIO<<<")

import random

a1 = input("Primeiro aluno: ")
a2 = input("Segundo aluno: ")
a3 = input("Terceiro aluno: ")
a4 = input("Quarto aluno: ")
lista = [a1, a2, a3, a4]
print("O aluno escolhido é {}".format(random.choice(lista)))
