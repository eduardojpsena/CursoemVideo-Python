'''Crie uma tupla preenchida com os 20 primeiros colocados da Tabela do brasileirão,
na ordem de colocação. Depois mostre: [A] Os 5 primeiros colocados, [B] Os ultimos
4 colocados, [C] Uma lista com os times em ordem alfabetica, [D] Em que posição na
tabela está o time do Chapecoense.'''

print(">>>TABELA BRASILEIRÃO<<<")

times = ('Flamengo', 'Santos', 'Palmeiras', 'Gremio', 'Atlético-PR', 'São Paulo',
         'Internacional', 'Corintians', 'Fortaleza', 'Goiás', 'Bahia', 'Vasco',
         'Atlético-MG', 'Fluminense', 'Botafogo', 'Ceará', 'Cruzeiro', 'CSA',
         'Chapecoense', 'Avaí')
print('=-'*25)
print("A lista de times do Brasileirão 2019: {}".format(times))
print('=-'*25)
print("Os cinco primeiros colocados são: {}".format(times[:5]))
print('=-'*25)
print("Os ultimos 4 colocados são: {}".format(times[-4:]))
print('=-'*25)
print("Times em ordem alfabética: {}".format(sorted(times)))
print('=-'*25)
print("A Chapecoense está na {}ª Colocação.".format(times.index("Chapecoense")+1))
print('=-'*25)

