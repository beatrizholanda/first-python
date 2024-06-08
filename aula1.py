#variáveis
#números
velocidade_internet = 10
print(velocidade_internet)
nota_filme = 8.5  #float
#valores boleanos
esta_aberto = True
#strings
nome_do_curso = 'Lógica de Programação'
#como variáveis seriakm usadas em um programa real?
#problema 1 - valor pro hora
#escreva um programa que retorna o valor hora de um funncionário com base no seu salário mensal e horas trabalhadas por mês.
''''
input salario_mensal
input horas_trabalhadas_por_mes
valor_hora = salario_mensal
print valor_hora
'''
salario_mensal = input('Qual é o seu salário mensal?')
horas_trabalhadas_por_mes = input('Quantas horas trabalha por mes?')
valor_hora = int(salario_mensal) / int(horas_trabalhadas_por_mes)
print(valor_hora)
