#Condicionais 
# if, elif e else

#bora sair hoje?
'''
E aí, bora dar uma saída hoje?
Se eu terminar meu trabalho aqui, eu consigo.
'''
trabalho_terminado = True
if trabalho_terminado == True:
  print('Opa!, bora dar uma saída.')
else: 
  print('Não posso sair agora.')

#pede ajuda a meu irmão
'''
Ei, você consegue me ajudar a mover essas caixas lá para fora está tarde?
Se eu estiver livre, sim. Mas, se não der pede ao meu irmão para te ajudar
'''
estou_livre = False
if estou_livre == True:
  print('Ok, estou livre e posso te ajudar.')
else: 
  print('Peça ao meu irmão para te ajudar.')

  #atrasado ou não
  '''
  Eu cheguei atrasado na aula, ainda posso entrar?
  Se essa não for sua terceira vez chegando atrasado,então pode sim, caso contrário irá tomar uma suspensão.
  '''
  numero_de_atrasos = 2
  if numero_de_atrasos >= 3:
    print('Você está suspenso.')
  elif numero_de_atrasos == 1:
    print('Pode entrar, porém caso tome mais duas faltas, irá ser suspenso.')
  elif numero_de_atrasos == 2:
    print('Pode entrar, porém caso tome mais uma falta, irá ser suspenso.')
  else: 
    print('Pode entrar!')

#encontre o maior número entre 2 números
primeiro_valor = input('Digite o primeiro valor: ')
segundo_valor = input('Digite o segundo valor: ')
if int(primeiro_valor) > int(segundo_valor): 
  print('O primeiro valor é maior que o segundo valor.')
else: 
  print('O segundo valor é maior que o primeiro valor.')
 