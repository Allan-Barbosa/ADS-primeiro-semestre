import random
print('''Nomes de cachorro
Eu te direi vários nomes de cachorro para te ajudar na escolha.
Qual é o sexo do seu animal?(m/f)''')
nomesM = ['Thor', 'Bob', 'Fred', 'Billy', 'Marley', 'Theo', 'Pingo', 'Bidu']
nomesF = ['Mel', 'Nina', 'Paçoca', 'Luna',
          'Amora', 'Flora', 'Belinha', 'Cacau']
n = input()
if n == 'm':
    for i in range(8):
        z = random.choice(nomesM)
        x = nomesM.index(z)
        nomesM.pop(x)
        print(z)
        e = input('gostou desse nome?(s/n)')
        if i == 7:
            print('Lamento os nomes acabaram.')
if n == 'f':
    for i in range(8):
        z = random.choice(nomesF)
        x = nomesF.index(z)
        nomesF.pop(x)
        print(z)
        e = input('gostou desse nome?(s/n)')
        if i == 7:
            print('Lamento os nomes acabaram.')
