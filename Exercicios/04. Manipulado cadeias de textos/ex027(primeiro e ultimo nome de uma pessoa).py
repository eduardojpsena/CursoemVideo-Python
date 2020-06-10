'''Faça um programa que leia o nome completo de uma pessoa, e mostre separadamente
o primeiro e ultimo nome dessa pessoa.'''

print(">>>VERIFICANDO PRIMEIRO e ULTIMO NOME<<<")

nome = str(input("Digite seu nome completo: ")).title().strip()
sepnome = nome.split()
print("Muito prazer em te conhecer!")
print("O seu primeiro nome é {}".format(sepnome[0]))
print("O seu ultimo nome é {}.".format(sepnome[len(sepnome)-1]))
