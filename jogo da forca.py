import random
animal = ['zebra', 'leao', 'girafa', 'boi']
fruta = ['banana', 'morango', 'jaboticaba', 'melancia']
pessoa = ['pedro', 'maria', 'juliana', 'rafael']
temas = [animal, fruta, pessoa]
r = 'n'
while r != 's':
    print(''''
  >>>>>>> Jogo da Forca <<<<<<<<<<<<
  Olá seja bem vindo
  Escolha um tema para o jogo
  0 - animal
  1 - fruta 
  2 - pessoa
  3 - adicionar novo nome
  ''')
    t = int(input('> '))
    if t < 3:
        palavra_secreta = random.choice(temas[t])
        # print(palavra_secreta)
        quantidade_de_letras = len(palavra_secreta)
        tela = []
        for letra in range(quantidade_de_letras):
            tela.append('_')
        acertos = 0
        erros = 0
        tentativa = 3
        linha1 = '__________'
        linha2 = '|.   O'
        linha3 = '|.  /|\ '
        linha4 = '|.  / \ '
        forca = [linha1, linha2, linha3, linha4]

        while acertos < quantidade_de_letras and erros < tentativa:
            print(tela)
            entrada = input('> ').lower()
            if entrada not in tela:
                cont = 0
                acerto = False
                for letra in palavra_secreta:
                    if entrada == letra:
                        tela[cont] = letra
                        acertos = acertos + 1
                        acerto = True
                    cont = cont + 1
                if acerto == False:
                    erros = erros + 1
                    print('Errou')
                    for i in range(erros+1):
                        print(forca[i])
                    for i in range(tentativa - erros):
                        print('|')
            else:
                print('Essa letra vc já acertou')

        if acertos >= quantidade_de_letras:
            print('Parabéns você acertou')
            print(tela)
        else:
            print('Se FU')
    elif t == 3:
        u = input('Digite a palavra: ')
        print('''Escolha qual tema recebe a palavra
    0 - animal
    1 - fruta
    2 - pessoa''')
        l = int(input())
        temas[l].append(u)
    r = input('Se sair todos os nomes adicionados sumirão, quer sair?(s/n) ')
