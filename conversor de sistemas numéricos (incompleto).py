escolha=input('''esse é um conversor de bases.
digite 1 para converter de decimal para outra base
digite 2 para converter de outra base para decimal
digite 3 para converter de binário para outra base
digite 4 para converter de outra base para binário
''')
while True:
    if escolha =='1':
        l=[]
        n=int(input('numero:'))
        b=int(input('base:'))
        while True:  
                q=n//b
                r=n%b
                n=q
                l.append(r)
                if n<b:
                    l.append(q)
                    c=len(l)-1
                    while c>=0:
                        print('{} '.format(l[c]),end='')
                        c-=1
                    break
        print('')
        c=input('quer ir de novo?(s/n)')
        if c=='n':
            break
    if escolha =='2':
        while True:
            n=input('numero:')
            b=int(input('base:'))
            numero=int(n,b)
            print(numero)
            c=input('quer ir de novo?(s/n)')
            if c=='n':
                break
    if escolha =='3':
        while True:
            x=input('octal ou hexadecimal?(o/h)')
            if x=='o':
                print('Digite espaço a cada 3 numeros e o ultimo esquerdo complete com 0.')
                n=input('numero:').split(' ')
                print(n)
            if x=='h':
                print('Digite espaço a cada 3 numeros e o ultimo esquerdo complete com 0.')
                n=input('numero:').split(' ')
                print(n)
            c=input('quer ir de novo?(s/n)')
            if c=='n':
                break
    if escolha =='4':
        print('Digite o numero com espaçamento a cada algarismo')
        n=input().split(' ')
    escolha=input('''esse é um conversor de bases.
digite 1 para converter de decimal para outra base
digite 2 para converter de outra base para decimal
digite 3 para converter de binário para outra base
digite 4 para converter de outra base para binário
''')
