import turtle
import random
# fracasso
while True:
    print('''CORRIDA DE TARTARUGAS
---------------------
Olá jogador, neste jogo tartarugas irão apostar uma corrida.''')
    def retangulo(l,h,x):
        x.begin_fill()
        for i in range(2):
            x.fd(l)
            x.rt(90)
            x.fd(h)
            x.rt(90)
        x.end_fill()
        x.up()
    def retangulo2(l,h,x):
        x.begin_fill()
        for i in range(2):
            x.fd(l)
            x.lt(90)
            x.fd(h)
            x.lt(90)
        x.end_fill()
        x.up()
    def posicao():
        pintor.up()
        pintor.goto(random.randint(-759,759),random.randint(5,391))
    def estrela(lado):
        pintor.color('white')
        pintor.down()
        pintor.begin_fill()
        for i in range(5):
            pintor.fd(lado)
            pintor.lt(144)
        pintor.end_fill()
    def pista(x):
        pintor.down()
        pintor.fd(1000)
        for i in range(0,18):
            pintor.forward(10+x)
            pintor.right(10)
        pintor.fd(1000)
        for i in range(0,18):
            pintor.forward(10+x)
            pintor.right(10)
    def correr(x,y):
        y.fd(1000)
        for i in range(0,18):
            y.fd(12+x)
            y.rt(10)
        y.fd(1000)
        for i in range(0,18):
            y.fd(12+x)
            y.rt(10)
    def posicionar_pista():
        pintor.lt(90)
        pintor.up()
        pintor.fd(20)
        pintor.down()
        pintor.right(90)
    def criar(x,y):
        global competidor1
        global competidor2
        global competidor3
        global competidor4
        x.shape('turtle')
        x.speed(0)
        x.up()
        x.goto(-500,-120+y)
    x= turtle.Screen()
    x.screensize(1520,785)
    pintor = turtle.Turtle()
    pintor.speed(0)
    pintor.shape('turtle')
    pintor.up()
    pintor.goto(-759,0)
    pintor.down()
    pintor.color('green')
    retangulo(1518,391,pintor)
    pintor.goto(-759,1)
    pintor.down()
    pintor.color('midnight blue')
    retangulo2(1518,391,pintor)
    pintor.lt(90)
    pintor.lt(90)
    for i in range(100):
        posicao()
        estrela(1)
    pintor.rt(90)
    pintor.rt(90)
    pintor.up()
    pintor.color('gainsboro')
    pintor.goto(0,195)
    pintor.down()
    pintor.begin_fill()
    pintor.circle(50)
    pintor.end_fill()
    pintor.up()
    pintor.color('black')
    pintor.goto(-500,-130)
    pista(0)
    posicionar_pista()
    pintor.fillcolor('light slate gray')
    pintor.begin_fill()
    pista(4)
    posicionar_pista()
    pista(8)
    posicionar_pista()
    pista(12)
    posicionar_pista()
    pista(16)
    pintor.end_fill()
    pintor.color('white')
    pintor.rt(90)
    pintor.fd(115)
    pintor.up()
    pintor.lt(90)
    pintor.goto(-500,-130)
    pintor.down()
    pintor.fillcolor('green')
    pintor.begin_fill()
    pintor.ht()
    pintor.color('green')
    pista(0)
    pintor.end_fill()
    competidor1= turtle.Turtle()
    competidor2= turtle.Turtle()
    competidor3= turtle.Turtle()
    competidor4= turtle.Turtle()
    criar(competidor1,0)
    criar(competidor2,+20)
    criar(competidor3,+40)
    criar(competidor4,+60)
    distancia1=0
    distancia2=0
    distancia3=0
    distancia4=0
    juiz = turtle.Turtle()
    juiz.shape('turtle')
    juiz.color('black')
    juiz.up()
    juiz.goto(-500,-35)
    juiz.rt(90)
    competidor1.color('blue')
    competidor2.color('purple')
    competidor3.color('red')
    competidor4.color('orange')
    def ir(x):
        x.rt(90)
        x.fd(8)
        x.lt(90)
        x.fd(5)
        if x== competidor1:
            x.write('Leonardo')
        if x== competidor2:
            x.write('Donatello')
        if x== competidor3:
            x.write('Raphael')
        if x == competidor4:
            x.write('Michelangelo')
    def volta(x):
        x.back(5)
        x.lt(90)
        x.fd(8)
        x.rt(90)
    ir(competidor1)
    ir(competidor2)
    ir(competidor3)
    ir(competidor4)
    volta(competidor1)
    volta(competidor2)
    volta(competidor3)
    volta(competidor4)
    nome=input('Digite seu nome:')
    aposta = int(input('''Digite qual tartaruga você acha que vai vencer:
(1)Leonardo(azul)🐢
(2)Donatello(magenta)🐢
(3)Raphael(vermelho)🐢
(4)Michelangelo(laranja)🐢
> '''))
    while aposta<1 or aposta>4:
        aposta = int(input('''Valor inválido
> '''))
    if aposta>0 and aposta<5:
        rodadas = int(input('Digite quantas rodadas as tartarugas correrão:'))
        for i in range(rodadas):
            if i>0:
                distancia1 = distancia1 - 2000
                distancia2 = distancia2 - 2000
                distancia3 = distancia3 - 2000
                distancia4 = distancia4 - 2000
            while distancia1 <2010 or distancia2<2010 or distancia3<2010 or distancia4<2010:
                if distancia1 == 1000 or distancia1 == 2000:
                    for i in range(0,18):
                        competidor1.fd(12)
                        competidor1.rt(10)
                if distancia2 == 1000 or distancia2 == 2000:
                    for i in range(0,18):
                        competidor2.fd(16)
                        competidor2.rt(10)
                if distancia3 == 1000 or distancia3 == 2000:
                    for i in range(0,18):
                        competidor3.fd(20)
                        competidor3.rt(10)
                if distancia4 == 1000 or distancia4 == 2000:
                    for i in range(0,18):
                        competidor4.fd(24)
                        competidor4.rt(10)
                vai1 = random.randint(5,9)
                vai2 = random.randint(5,9)
                vai3 = random.randint(5,9)
                vai4 = random.randint(5,9)
                distancia1 += vai1
                distancia2 += vai2
                distancia3 += vai3
                distancia4 += vai4
                competidor1.fd(vai1)
                competidor2.fd(vai2)
                competidor3.fd(vai3)
                competidor4.fd(vai4)
                if distancia1 >990 and distancia1<1000:
                    go = 1000 - distancia1
                    distancia1+=go
                    competidor1.fd(go)
                    distancia1 = 1000
                if distancia2 >990 and distancia2<1000:
                    go = 1000 - distancia2
                    distancia2+=go
                    competidor2.fd(go)
                    distancia2 = 1000
                if distancia3 >990 and distancia3<1000:
                    go = 1000 - distancia3
                    distancia3+=go
                    competidor3.fd(go)
                    distancia3 = 1000
                if distancia4 >990 and distancia4<1000:
                    go = 1000 - distancia4
                    distancia4+=go
                    competidor4.fd(go)
                    distancia4 = 1000
                if distancia1 >1990 and distancia1<2000:
                    go = 2000 - distancia1
                    distancia1+=go
                    competidor1.fd(go)
                if distancia2 >1990 and distancia2<2000:
                    go = 2000 - distancia2
                    distancia2+=go
                    competidor2.fd(go)
                if distancia3 >1990 and distancia3<2000:
                    go = 2000 - distancia3
                    distancia3+=go
                    competidor3.fd(go)
                if distancia4 >1990 and distancia4<2000:
                    go = 2000 - distancia4
                    distancia4+=go
                    competidor4.fd(go)
                if distancia1 >= 2001 and distancia2 <2001 and distancia3<2001 and distancia4 <2001:
                    azul = 1
                    laranja=0
                    vermelha=0
                    roxa=0
                if distancia1 < 2001 and distancia2 >=2001 and distancia3<2001 and distancia4 <2001:
                    roxa = 1
                    azul = 0
                    laranja=0
                    vermelha=0
                if distancia1 < 2001 and distancia2 <2001 and distancia3>=2001 and distancia4 <2001:
                    vermelha = 1
                    azul = 0
                    laranja=0
                    roxa=0
                if distancia1 < 2001 and distancia2 <2001 and distancia3<2001 and distancia4 >=2001:
                    laranja = 1
                    azul = 0
                    roxa=0
                    vermelha=0
        if azul == 1:
            juiz.write('Leonardo venceu!')
        elif vermelha == 1:
            juiz.write('Raphael venceu!')
        elif roxa == 1:
            juiz.write('Donatello venceu!')
        elif laranja == 1:
            juiz.write('Michelangelo venceu!')
        if aposta == 2 and roxa ==1 or aposta == 1 and azul ==1 or aposta ==3 and vermelha ==1 or aposta == 4 and laranja==1:
            print('Parabéns jogador, você acertou!')
            pontuação=1
        else:
            print('Não foi dessa vez, mais sorte na próxima')
            pontuação=0
        controle = 0
        ranking = open('ranking.txt','r')
        ranking_novo = []
        for linhas in ranking:
            linha = linhas
            linha = linha.split(' ')
            if linha[0] == nome:
                pontos = int(linha[1])
                pontos += pontuação
                linha[1] = str(pontos)
                controle = 1
            linha[1] = linha[1].replace('\n','')
            linha = list(reversed(linha))
            linha[0] = int(linha[0])
            ranking_novo.append(linha)
        if controle == 0:
            linha = [(pontuação),nome]
            ranking_novo.append(linha)
        ranking.close()
        ranking_novo.sort(reverse=True)
        ranking_pronto = []
        ranking = open('ranking.txt','w')
        for linha in ranking_novo:
            linha[0] = str(linha[0])
            linha = list(reversed(linha))
            linha = linha[0] + ' ' + linha [1] + '\n'
            ranking_pronto.append(linha)
        for linha in ranking_pronto:
            ranking.write(linha)  
        ranking.close()
        r = input('''quer o ranking atual?(s/n)
> ''')
        if r == 's':
            ranking = open('ranking.txt','r')
            print('Quantas vezes os jogadores acertaram a tartaruga vencedora:')
            print(ranking.read())
            ranking.close()
        print('Obrigado por jogar.')
        j = input('''Quer jogar novamente?(s/n)
> ''')
        while j!= 'n' and j!='s':
            print('comando inválido')
            j = input('''Quer jogar novamente?(s/n)
> ''')
        if j == 'n':
            break
