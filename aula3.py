#Laços de repetição + Listas
for palavra in range(1,4):
  print('carregando')
'''
for item in colecao:
expressao
'''
for item in range(1, 20 +1):
  print(item)
  for item in range(1, 20 +1, 2):
    print(item)

nomes = ['jhonatan', 'cristian', 'roberto', 'camila']
for nome in nomes:
  print(nome)
#imprime os valores de 1 a N
valor_maximo = int(input('Digite o valor máximo'))
valor_inicial = 1
for numero in range(valor_inicial, valor_maximo + 1):
  print(numero)