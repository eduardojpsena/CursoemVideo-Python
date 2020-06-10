'''Crie um programa que leia dois valores e mostre um menu na tela:
somar, multiplicar, maior, novos números, sair do programa'''

print(">>MENU DE OPÇÕES<<")

n1 = float(input("Digite o primeiro número: "))
n2 = float(input("Digite o segundo número: "))
menu = 0
while menu != 5:
    menu = int(input("-=-=-=-=-=-=-=-=--=-=-=-=-=-=-=-=-"
                     "\n[1] Soma \n[2] Multiplicação \n[3] Maior valor \n[4] novos números \n[5] Sair do programa"
                     "\n Selecione uma opção: "))
    if menu == 1:
        soma = n1 + n2
        print("-=-=-=-=-=-=-=-=--=-=-=-=-=-=-=-=-")
        print("\033[0;033m A soma entre {} + {} = {:.2f} \033[m".format(n1, n2, soma))
    elif menu == 2:
        mult = n1 * n2
        print("-=-=-=-=-=-=-=-=--=-=-=-=-=-=-=-=-")
        print("\033[0;033m A multiplicação entre {} x {} = {:.2f} \033[m".format(n1, n2, mult))
    elif menu == 3:
        if n1 > n2:
            print("-=-=-=-=-=-=-=-=--=-=-=-=-=-=-=-=-")
            print("\033[0;033m Entre {} e {} o maior é {} \033[m".format(n1, n2, n1))
        else:
            print("-=-=-=-=-=-=-=-=--=-=-=-=-=-=-=-=-")
            print("\033[0;033m Entre {} e {} o maior é {} \033[m".format(n1, n2, n2))
    elif menu == 4:
        print("-=-=-=-=-=-=-=-=--=-=-=-=-=-=-=-=-")
        n1 = float(input("Digite o primeiro número: "))
        n2 = float(input("Digite o segundo número: "))
    else:
        print("-=-=-=-=-=-=-=-=--=-=-=-=-=-=-=-=-")
print("\033[0;033m Programa encerrado.\033[m")