'''Faça um script que realize um sorteio entre 4 alunos e ordene os escolhidos.'''

print(">>>SORTEIO ORDENADO<<<")

import random

a1 = input("Primeiro aluno: ")
a2 = input("Segundo aluno: ")
a3 = input("Terceiro aluno: ")
a4 = input("Quarto aluno: ")
lista = [a1, a2, a3, a4]
random.shuffle(lista)
print("A ordem dos alunos escolhidos é {}".format(lista))

#o método shuffle é utilizado para embaralhar as opções#