#coleção (lista)
precos = [20, 50, 200]
print(precos[0])
print(precos.index(200))
#diversidades
diversidades = [15, 'jhonatan',True]
print(diversidades[0])
print(diversidades[1])
print(diversidades[2])
#laços em interáveis
for preco in precos:
  print(preco)

'''
some os valores dados uma coleção de dados "idades" [1....5] imprima na tela a oma destes valores
'''
idades = [15,46,75,34,23]
total = 0
for idade in idades:
  total = total + idade
  print(total)