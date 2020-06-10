'''Crie um programa onde o usuário digite uma expressão qualquer que use parênteses.
Seu aplicativo deverá analisar se a expressão passada está com os parenteses abertos
e fechados na ordem correta.'''

print("••VALIDANDO EXPRESSÕES MATEMÁTICAS••")

expressão = str(input("Digite uma expressão: ")).strip()
lista = []
for unid in expressão:
    if unid == '(':
        lista.append("(")
    elif unid == ')':
        if len(lista) > 0:
            lista.pop()
        else:
            lista.append(")")
            break
if len(lista) == 0:
    print("A expressão está correta.")
else:
    print("A expressão está incorreta.")
