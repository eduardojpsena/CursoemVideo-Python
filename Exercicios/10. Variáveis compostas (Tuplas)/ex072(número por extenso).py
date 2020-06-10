'''Crie um programa que tenha uma tupla totalmente preenchida com contagem por
extenso, de zero até 20. seu programa deverá ler um número pelo teclado (entre 0 e 20)
e mostrá-lo por extenso.'''

print(">>>NÚMERO POR EXTENSO<<<")

number1 = ('zero', 'um', 'dois', 'três', 'quatro', 'cinco')
number2 = ('seis', 'sete',' oito', 'nove', 'dez')
number3 = ('onze', 'doze', 'treze', 'quatorze', 'quinte')
number4 = ('dezesseis', 'dezessete', 'dezoito', 'dezenove', 'vinte')
totalnumber = number1 + number2 + number3 + number4

while True:
    n = int(input("Digite um número entre 0 e 20: "))
    if 0 <= n <= 20:
        break
    print("Tente novamente. ", end='')
print("Você digitou o número {}.".format(totalnumber[n]))
