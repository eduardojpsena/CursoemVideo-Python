'''Crie um programa que tenha uma Tupla com várias palavras (não usar acentos). Depois
disso, você deve mostrar, para cada palavra, quais são suas vogais.'''

print("♠♠♠CONTANDO VOGAIS EM TUPLAS♥♥♥")

palavras = ('aprender', 'programar', 'linguagem', 'python',
           'curso', 'gratis', 'estudar', 'praticar', 'trabalhar',
           'mercado', 'programador', 'futuro')
for p in palavras:
    print("\nNa palavra {} temos as vogais: ".format(p.upper()), end='')
    for letra in p:
        if letra.lower() in 'aeiou':
            print(letra, end=' ')
