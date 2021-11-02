import random
l1 = ['ótimo', 'excelente', 'acima da média', 'bom']
l2 = ['provas', 'andar de bicicleta', 'nadar', 'jogos', 'esportes']
while True:
    adjetivo = random.choice(l1)
    atividade = random.choice(l2)
    print('Gerador de cumprimentos.')
    n = input('''Qual o seu nome?
  ''')
    print('''aqui está o seu cumprimento {n}:
  {n} você é {adjetivo} em {atividade}.
  De nada!'''.format(n=n, adjetivo=adjetivo, atividade=atividade))
    p = input('''quer tentar de novo?(s/n)
  ''')
    if p == 'n':
        break
