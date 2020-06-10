'''Crie um programa que leia a idade e sexo de várias pessoas. A cada pessoa cadastrada,
o programa deve perguntar se o usuário quer ou não continuar. No final mostre:
[A] quantas pessoas tem mais de 18 anos, [B] quantos homens foram cadastrados e
[C] quantas mulheres tem menos de 20 anos.'''

print("*-*-ANÁLISE DE DADOS DO GRUPO-*-*")

c18 = 0
cmulher20 = 0
chomem = 0
while True:
    print("-------------------------")
    print("   CADASTRE UMA PESSOA")
    print("-------------------------")
    id = int(input("Idade: "))
    sx = ' '
    while sx not in 'MF':
        sx = str(input("Sexo [M/F]: ")).strip().upper()[0]
    if id >= 18:
        c18 += 1
    if id < 20 and sx in 'F':
        cmulher20 += 1
    if sx in 'M':
        chomem += 1
    print("-------------------------")
    selection = ' '
    while selection not in 'SN':
        selection = str(input("\033[0;33mDeseja continuar? [S/N]: \033[m")).strip().upper()[0]
    if selection in 'N':
        break
print("-------------------------")
print("\033[0;33mAnalisandos os dados cadastrados...\033[m"
      "\n• Pessoas com mais de 18 anos:      {}"
      "\n• Mulheres com menos de 20 anos:    {}"
      "\n• Quantidade de homens cadastrados: {}".format(c18, cmulher20, chomem))
