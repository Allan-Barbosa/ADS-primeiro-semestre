import random

# retorna uma lista com as três portas em posições aleatórias.


def lista_portas(lista):
    lista.append(aleatorio(portas))
    while len(lista) < 3:
        auxiliar = aleatorio(portas)
        if auxiliar not in lista:
            lista.append(auxiliar)
    return lista

# retorna a mensagem da porta escolhida.


def porta(x):
    global psyduck
    global chave
    global retorno
    morte = aleatorio(porta_derrota)
    premio = aleatorio(porta_sorte)

    if porta_1 == 'porta_sorte':
        porta_certa = 'A porta da sorte era a 1.'
    elif porta_2 == 'porta_sorte':
        porta_certa = 'A porta da sorte era a 2.'
    elif porta_3 == 'porta_sorte':
        porta_certa = 'A porta da sorte era a 3.'

    if x == 'porta_derrota':
        if psyduck == 1:
            mensagem = ('''{porta_certa}
Você escolheu a porta da derrota, mas o psyduck entrou no seu lugar!
PSYDUCK
- Psy 
- Duck?'''.format(porta_certa=porta_certa))
        else:
            mensagem = ('''{porta_certa}
A porta que você entrou é a da derrota e nela você foi {morte}'''.format(morte=morte, porta_certa=porta_certa))
        return print(mensagem)

    elif x == 'porta_sorte':
        if premio == 'tesouro':
            return print('Você encontrou um tesouro!')
        elif premio == 'psyduck':
            if psyduck == 0:
                mensagem = ('''Você encontrou o psyduck e ele vai te salvar de uma porta da derrota!
PSYDUCK
- Psy 
- Duck?''')
            elif psyduck == 1:
                mensagem = ('''Você encontrou o psyduck de novo, parece que ele se perdeu.
PSYDUCK
- Psy 
- Duck?''')
            psyduck = 1
            return psyduck, mensagem

    elif x == 'porta_azar':
        pergunta = perguntas[chave]
        mensagem = ('''{porta_certa}
Você encontrou a esfinge e precisa resolver o enigma dela para não perder um ponto!
ESFINGE
{pergunta}'''.format(pergunta=pergunta, porta_certa=porta_certa))
        return print(mensagem)

# retorna a potuação.


def pontuacao(y):
    global psyduck
    global pontuação
    global chave

    if y == 'porta_derrota':
        if psyduck == 0:
            pontuação = 0
        if psyduck == 1:
            psyduck = 0
            pontuação = pontuação
        return pontuação

    elif y == 'porta_sorte':
        pontuação = pontuação + 1
        return pontuação

    elif y == 'porta_azar':
        if resposta == respostas[chave]:
            pontuação = pontuação + 1
            return pontuação
        else:
            pontuação = pontuação - 1
            return pontuação

# retorna um item aleatório.


def aleatorio(lista):
    porta = random.choice(lista)
    return porta


# listas que definem os conteúdos das portas.
portas = ['porta_azar', 'porta_sorte', 'porta_derrota']
perguntas = {'a': '- Eu tenho 1000 irmãos, cada um tem 1000.Quantos somos?', 'b': '- O que tem dentes, mas não come?', 'c': '- Quantas perguntas Naruto acertou na primeira fase do exame Chūnin?', 'd': '- Quantos portões Rock Lee conseguiu abrir em sua luta contra Gaara?', 'e': '- Em harry potter quem perde a orelha é jorge ou é fred?', 'f': '- Quem foi o primeiro a destruir uma horcrux de voldemort?', 'g': '- Qual personagem de iCarly tem mania de tirar a camisa?',
             'h': '- Qual elemento o avatar aang teve mais dificuldade em dominar?', 'i': '- Ante de quem, mesmo a pessoa mais influente do mundo, deve tirar o chapéu?', 'j': '- Megan é irmã biológica de drake ou de josh?', 'k': '- Qual parte do corpo de cassios foi arrancada por seiya', 'l': '- Qual animal decide cuidar do bebê em a era do gelo?', 'm': '- Qual foi o primeiro animal a fugir do zoológico em madagascar?', 'n': '- Qual foi o primeiro pokemon capturado por ash?', 'o': '- Quem foi o primeiro a se transformar em super sayajin 2?'}
respostas = {'a': '1001', 'b': 'pente', 'c': '0', 'd': '5', 'e': 'jorge', 'f': 'harry', 'g': 'gibby', 'h': 'terra',
             'i': 'cabeleireiro', 'j': 'drake', 'k': 'orelha', 'l': 'preguiça', 'm': 'zebra', 'n': 'caterpie', 'o': 'gohan'}
porta_derrota = ['devorado por leões!', 'picado por cobras!', 'esmagado pelas paredes!',
                 'queimado pela lava que estava na sala!', 'chifrado por um boi!', 'espancado por um gorila!']
porta_sorte = ['psyduck', 'tesouro', 'psyduck', 'psyduck', 'psyduck']

psyduck = 0
continuar = 's'

while continuar == 's':
    pontuação = 0
    # introdução.
    nome = input('''Não utilize a tecla espaço.
Digite seu nome: ''')
    print('''==========================================================
PORTA DA FORTUNA
Olá {nome}, este é o jogo porta da fortuna e nele teremos 3 possibilidades de portas para escolher: 
Porta da sorte: você ganha um prêmio.
Porta do azar: você pode perder ou ganhar 1 pontos.
porta da derrota: você perde todos os pontos.
Ao final da partida os seus pontos serão adicionados a um ranking.
'''.format(nome=nome))

    rodadas = int(input('Digite quantas rodadas você quer nesta partida: '))
    for rodada in range(rodadas):

        print('''Escolha uma das 3 portas.
             _______         _______          _______
            |       |       |       |        |       |
            |  [1]  |       |  [2]  |        |  [3]  |
            |       |       |       |        |       |
            |_______|       |_______|        |_______|
    ==========================================================''')

        # adicionando conteúdo aleatório as portas.
        portas_aleatorias = []
        lista_portas(portas_aleatorias)
        porta_1 = portas_aleatorias[0]
        porta_2 = portas_aleatorias[1]
        porta_3 = portas_aleatorias[2]
        # faz o jogador escolher uma porta válida.
        escolha = int(input('> '))
        if escolha != 1 and escolha != 2 and escolha != 3:
            while escolha != 1 and escolha != 2 and escolha != 3:
                print('porta inválida.')
                escolha = int(input('> '))
        chave = aleatorio(list(perguntas.keys()))
        # porta 1
        if escolha == 1:
            resultado = porta(porta_1)
            if type(resultado) == tuple:
                print(resultado[1])
            if porta_1 == 'porta_azar':
                resposta = input('>').lower()
                if resposta == respostas[chave]:
                    print('Acertou.')
                else:
                    print('Errou, a esfinge fica com 1 dos seus pontos.')
            pontuação = pontuacao(porta_1)
            print('A sua pontuação atual é', str(pontuação)+'.')
        # porta 2
        elif escolha == 2:
            resultado = porta(porta_2)
            if type(resultado) == tuple:
                print(resultado[1])
            if porta_2 == 'porta_azar':
                resposta = input('>').lower()
                if resposta == respostas[chave]:
                    print('Acertou.')
                else:
                    print('Errou, a esfinge fica com 1 dos seus pontos.')
            pontuação = pontuacao(porta_2)
            print('A sua pontuação atual é', str(pontuação)+'.')
        # porta 3
        elif escolha == 3:
            resultado = porta(porta_3)
            if type(resultado) == tuple:
                print(resultado[1])
            if porta_3 == 'porta_azar':
                resposta = input('>').lower()
                if resposta == respostas[chave]:
                    print('Acertou.')
                else:
                    print('Errou, a esfinge fica com 1 dos seus pontos.')
            pontuação = pontuacao(porta_3)
            print('A sua pontuação atual é', str(pontuação)+'.')
    # mensagens finais para o jogador.
    print('Sua pontuação nessa partida foi', pontuação)
    porcentagem = (pontuação * 100) / rodadas
    if porcentagem <= 0:
        m = 'azarado!'
    elif porcentagem == 100:
        m = 'sortudo!'
    elif porcentagem > 0 and porcentagem < 50:
        m = 'mais sorte na próxima.'
    elif porcentagem > 50 and porcentagem < 100:
        m = 'muito bem.'
    print('Você conseguiu pontuar', porcentagem, '%,', m)
    # apaga o ranking e faz novamente.
    controle = 0
    ranking = open('ranking.txt', 'r')
    ranking_novo = []
    for linhas in ranking:
        linha = linhas
        linha = linha.split(' ')
        if linha[0] == nome:
            pontos = int(linha[1])
            pontos += pontuação
            linha[1] = str(pontos)
            controle = 1
        linha[1] = linha[1].replace('\n', '')
        linha = list(reversed(linha))
        linha[0] = int(linha[0])
        ranking_novo.append(linha)
    ranking.close()
    ranking_novo.sort(reverse=True)
    ranking_pronto = []
    for linha in ranking_novo:
        linha[0] = str(linha[0])
        linha = list(reversed(linha))
        linha = linha[0] + ' ' + linha[1] + '\n'
        ranking_pronto.append(linha)
    if controle == 1:
        ranking = open('ranking.txt', 'w')
        for linha in ranking_pronto:
            ranking.write(linha)
    elif controle == 0:
        ranking = open('ranking.txt', 'w')
        for linha in ranking_pronto:
            ranking.write(linha)
        linha = nome + ' ' + str(pontuação) + '\n'
        ranking.write(linha)
        ranking.close()

    r = input('''quer o ranking atual?(s/n)
''')
    if r == 's':
        ranking = open('ranking.txt', 'r')
        print(ranking.read())
        ranking.close()
    continuar = input('''Deseja jogar novamente?(s/n)
''')
print('Obrigado por jogar.')
