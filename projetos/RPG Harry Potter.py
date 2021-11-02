import random
import os
import time
mapa = {
    'escadas': {
        'terreo': 'terreo',
        'segundo_andar': 'segundo_andar',
        'setimo_andar': 'setimo_andar'
    },
    'terreo': {
        'escadas': 'escadas',
        'masmorras': 'masmorras',
        'terrenos': 'terrenos'
    },
    'terrenos': {
        'terreo': 'terreo',
        'floresta_proibida': 'floresta_proibida'
    },
    'floresta_proibida': {
        'terrenos': 'terrenos',
        'item': 'chapéu_seletor',
        'inimigo': 'dementador'
    },
    'masmorras': {
        'sala_poções': 'sala_poções',
        'cozinha': 'cozinha',
        'terreo': 'terreo',
        'item': 'chave_snape'
    },
    'segundo_andar': {
        'banheiro': 'banheiro',
        'escadas': 'escadas'
    },
    'setimo_andar': {
        'sala_comunal_grifinória': 'sala_comunal_grifinória',
        'sala_diretor': 'sala_diretor',
        'escadas': 'escadas',
        'sala_precisa': 'sala_precisa'
    },
    'sala_poções': {
        'masmorras': 'masmorras',
        'item': 'felix_felicis'
    },
    'cozinha': {
        'masmorras': 'masmorras',
        'item': 'dobby'
    },
    'banheiro': {
        'segundo_andar': 'segundo_andar',
        'câmara_secreta': 'câmara_secreta'
    },
    'sala_comunal_grifinória': {
        'setimo_andar': 'setimo_andar',
        'item': 'capa_invisibilidade',
    },
    'sala_diretor': {
        'setimo_andar': 'setimo_andar',
        'item': 'fawkes'
    },
    'sala_dursley': {
        'cozinha': 'cozinha',
        'quarto_harry': 'quarto_harry'
    },
    'cozinha_dursley': {
        'sala_dursley': 'sala_dursley'
    },
    'quarto_harry': {
        'sala_dursley': 'sala_dursley',
        'item': 'vassoura',
        'inimigo': 'bicho-papão'
    },
    'câmara_secreta': {
        'item': 'gina_weasley',
        'inimigo': 'basilisco'
    },
    'sala_precisa': {
        'setimo_andar': 'setimo_andar',
        'item': 'vira-tempo'
    }
}
luta = [0]*25 + [1]*75
luta2 = [0] * 25 + [1] * 75
luta3 = [1] * 99 + [0]
chavep = [1]*25 + [0]*75
invisibilidade = 0
veneno = 0
dementador = True
bicho_papão = True
basilisco = True
senha1 = random.randint(1, 1000)
senha2 = random.randint(1, 1000)
inventário = ['mapa_maroto', 'varinha']
# inventário=['mapa_maroto','varinha','dobby','capa_invisibilidade','fawkes','vassoura','chapéu_seletor','vira-tempo','felix_felicis']
vidas = ['❤️ ', '❤️ ', '❤️ ']
local_atual = 'escadas'

minerva = 0
rony = 0
dumbledore = 0
snape = 0
elfo = 0
valter = 0
hagrid = 0
hagrid2 = 0
filch = 0
voldemort = 0


def mensagem(local):
    global minerva
    global rony
    global dumbledore
    global snape
    global elfo
    global valter
    global hagrid
    global hagrid2
    global filch
    global voldemort
    if local_atual == 'escadas' and minerva == 0:
        print('''\033[1;93mMINERVA
- O que faz andando pelas escadas harry? volte para a sala comunal e espere o trem que levará os alunos.''')
        minerva = 1
    elif local_atual == 'sala_comunal_grifinória' and rony == 0:
        print('''\033[1;93mRONY
- Harry se for entrar na câmara secreta, vai precisar ver o dumbledore primeiro.''')
        rony = 1
    elif local_atual == 'sala_diretor' and dumbledore == 0:
        print('''\033[1;93mALVO DUMBLEDORE
- A comida feita pelos elfos é incrível, não concorda harry?''')
        dumbledore = 1
    elif local_atual == 'masmorras' and snape == 0:
        print('''\033[1;93mSNAPE
- Demorou meses, mas finalmente consegui preparar a felix felicis. Agora eu te pego potter...''')
        snape = 1
    elif local_atual == 'cozinha' and elfo == 0:
        print('''\033[1;93mDOBBY
- Harry potter deve retornar para casa, hogwarts não é segura para harry potter...''')
        elfo = 1
    elif local_atual == 'sala_dursley' and valter == 0:
        print('''\033[1;93mVALTER DURSLEY
- O que faz na minha casa moleque? pegue logo o que veio buscar no seu quarto e volte para sua escola de aberrações.''')
        valter = 1
    elif local_atual == 'terrenos' and hagrid == 0 and 'chapéu_seletor' not in inventário:
        print('''\033[1;93mHAGRID
- Canino está com medo hoje, deve ter alguma coisa na floresta...''')
    elif local_atual == 'terrenos' and hagrid2 == 0 and 'chapéu_seletor' in inventário:
        print('''\033[1;93mHAGRID
- Não ande perto do banheiro harry, foi lá que o monstro atacou da ultima vez...''')
        hagrid2 = 1
    elif local_atual == 'segundo_andar' and filch == 0:
        print('''\033[1;93mFILCH
- Essas pestes vão me pagar pelo que fizeram a minha gata...''')
        filch = 1
    elif local_atual == 'câmara_secreta' and voldemort == 0:
        print('''\033[1;93mVOLDEMORT(lembrança)
- Não entendo como lorde voldemort, o maior bruxo de todos, pode perder para um garoto burro e sem talento algum...''')
        voldemort = 1


def mostrar_status(local, inventario, mapa):
    print('\033[1;97m---------------')
    print(vidas)
    print('\033[1;31mSeu local atual:'+local)
    print('\033[1;34minventário', inventario)
    if local == 'setimo_andar' and vidas == ['❤️ ', '❤️ '] or local == 'setimo_andar' and vidas == ['❤️ ', '❤️ ', '❤️ ']:
        print(
            "\033[1;33mO que estou vendo:['sala_comunal_grifinória','sala_diretor','escadas']")
    elif local == 'banheiro':
        print("\033[1;33mO que estou vendo:['segundo_andar']")
    else:
        print('\033[1;33mO que estou vendo:', list(mapa[local_atual].values()))
    print('\033[1;97m---------------')


nome = input('\033[;1mDigite seu nome:')
print('''==========================================
\033[;1mOlá {nome}, este é um jogo rpg de harry potter.
Objetivo do jogo: Gina Weasley está na camara secreta e você precisa derrotar o basilisco para resgata-la.
Como matar o basilisco: você vai precisar de uma espada e uma fênix ou uma espada e um pouco de sorte.
personagem: Harry Potter
==========================================
comandos:
varinha [nome do feitiço]
usar [item]
pegar [item]
ir [local]
aparatar [local] (para aparatar em hogwarts vai precisar achar um elfo domestico)
{senha2}
=========================================='''.format(nome=nome, senha2=senha2))
r = input('''\033[;1mTerminou de ler?(s/n)
> ''')
while r != 's':
    r = input('''\033[;1mTerminou de ler?(s/n)
> ''')
if r == 's':
    os.system('clear')

while True:
    if 'inimigo' in mapa[local_atual]:
        if mapa[local_atual]['inimigo'] == 'bicho-papão':
            medo = input('''\033[1;35mQual seu medo jogador?
> ''')
            while bicho_papão == True:
                print('\033[1;35mSeu inimigo é o(a)', medo)
                feitiço = input('\033[1;35m> ')
                if feitiço == 'varinha riddikulus' and 'varinha' in inventário:
                    chance = random.choice(luta)
                    print(
                        '\033[1;35mO {medo} ganhou as roupas da avó do neville.'.format(medo=medo))
                    if chance == 1:
                        print('\033[1;35mVocê derrotou o bicho-papão.')
                        bicho_papão = False
                        del mapa[local_atual]['inimigo']
                    else:
                        print(
                            '\033[1;35mO bixo papão venceu, você não riu o suficiente.')
                        vidas.pop()
                elif 'varinha' not in inventário:
                    print(
                        '\033[1;35mVocê foi morto pelo bicho-papão, pois não tem uma varinha')
                    vidas = []
                    c = 0
                    break
                else:
                    print('\033[1;35mFeitiço errado!')
                print(vidas)
                time.sleep(3)
                os.system('clear')

        elif mapa[local_atual]['inimigo'] == 'dementador':
            while dementador == True:
                print(
                    '\033[1;36mVocê encontrou criaturas cobertas por capuzes negros e que se alimentam de felicidade.')
                print(
                    '\033[1;36mTudo está frio e escuro, tenha pensamentos felizes.')
                feitiço = input('> ')
                if feitiço == 'varinha expecto patronum' and 'varinha' in inventário:
                    chance = random.choice(luta)
                    print('\033[1;36mVocê produziu um patrono!')
                    if chance == 1:
                        print('\033[1;36mVocê afugentou os dementadores.')
                        dementador = False
                        del mapa[local_atual]['inimigo']
                    else:
                        print(
                            '\033[1;36mOs dementador passaram pelo seu patrono, sua lembrança não foi feliz o suficiente.')
                        vidas.pop()
                elif 'varinha' not in inventário:
                    print(
                        '\033[1;36mVocê foi morto pelo dementador, pois não tem uma varinha')
                    vidas = []
                    c = 0
                    break
                else:
                    print('\033[1;36mFeitiço errado!')
                print(vidas)
                time.sleep(3)
                os.system('clear')

        elif mapa[local_atual]['inimigo'] == 'basilisco':
            while basilisco == True:
                os.system('clear')
                if vidas == []:
                    break
                feitiço = input('''\033[1;32mNão consigo ver nada.
> ''')
                if feitiço == 'varinha lumos' and 'varinha' in inventário:
                    print('''\033[1;32m=====================================
Parabéns, você conseguiu passar por todos os desafios que levam á câmara secreta.
Agora você deve enfrentar seu inimigo final para vencer, uma cobra de seis metros de comprimento, que mata todos que olham em seus olhos e é venenosa.
VOLDEMORT(lembrança)
- Hoje você vai me pagar pelo que causou a mim e vai se arrepender do dia em que nasceu.''')

                    ação0 = input('''\033[1;32mQual sua ação?
> ''')
                    while ação0 != 'usar chapéu_seletor':
                        print('Você não vai conseguir derrotar o basilisco com isso.')
                        ação0 = input('''\033[1;32mQual sua ação?
> ''')
                    inventário.append('espada_gryffindor')
                    print('\033[1;31mVocê pegou a espada de gryffindor.')
                    inventário.pop(inventário.index('chapéu_seletor'))
                    while basilisco == True:
                        ação1 = input('''\033[1;32mQual sua ação?
> ''')
                        if ação1 == 'usar felix_felicis' and 'felix_felicis' in inventário:
                            inventário.pop(inventário.index('felix_felicis'))
                            while basilisco == True:
                                print(
                                    '\033[1;32mAgora você está com sorte, qual sua ação?')
                                ação2 = input('> ')
                                if ação2 == 'usar espada_gryffindor' and 'espada_gryffindor' in inventário:
                                    chance = random.choice(luta3)
                                    if chance == 1:
                                        print(
                                            '\033[1;32mVocê atravessou a espada de gryffindor no basilisco, ele está morto!')
                                        del mapa[local_atual]['inimigo']
                                        basilisco = False
                                    if chance == 0:
                                        print(
                                            '\033[1;32mVocê não foi veloz o suficiente para perfurar o basilisco, ele se desvia e te bate de volta.')
                                        vidas.pop()
                                    if vidas == []:
                                        break
                        elif ação1 == 'usar espada_gryffindor' and 'espada_gryffindor' in inventário:
                            chance = random.choice(luta2)
                            if chance == 1:
                                print('''\033[1;32mVocê atravessou a espada de gryffindor no basilisco, ele está morto!
Parece que você foi envenenado, agora você vai precisar de algo que cure veneno de basilisco!''')
                                del mapa[local_atual]['inimigo']
                                basilisco = False
                                veneno = 1
                            if chance == 0:
                                print(
                                    '\033[1;32mVocê não foi veloz o suficiente para perfurar o basilisco, ele se desvia e te bate de volta.')
                                vidas.pop()
                            if vidas == []:
                                break
                        else:
                            print('\033[1;32mVocê não possui este item.')
                else:
                    print('\033[1;32mainda não consigo ver nada')
                time.sleep(5)
                os.system('clear')

    mostrar_status(local_atual, inventário, mapa)
    mensagem(local_atual)
    comando = input('\033[1;97m> ').lower().split(' ')

    if comando[0] == 'aparatar' and 'dobby' in inventário:
        if comando[1] == 'segundo_andar':
            if invisibilidade > 0:
                print(
                    '\033[;1mFilch está neste corredor, mas você está invisível e vai poder passar.')
                local_atual = 'segundo_andar'
            else:
                print('''\033[1;32mFILCH
- O que faz andando pelos corredores pirralho, não ouviu que tem um monstro aqui? volte para a sala comunal!''')
                vidas.pop()
                local_atual = 'sala_comunal_grifinória'

        elif comando[1] == 'masmorras':
            if invisibilidade > 0:
                print(
                    '\033[;1mSnape está neste corredor, mas você está invisível e vai poder passar.')
                local_atual = 'masmorras'
            else:
                print('''\033[1;32mSNAPE
- O que faz andando pelos corredores potter? vamos para a detenção agora!''')
                print('''\033[1;32mGAME OVER, você perdeu.
agora você é um trouxa!''')
                c = 0
                break
        elif comando[1] in mapa and comando[1] != 'sala_diretor' and comando[1] != 'banheiro' and comando[1] != 'câmara_secreta' and comando[1] != 'quarto_harry' and comando[1] != 'sala_poções' and comando[1] != 'floresta_proibida' and local_atual != 'câmara_secreta':
            local_atual = comando[1]
            print('\033[;1maparatando...')
        elif local_atual == 'câmara_secreta' or comando[1] == 'sala_diretor' or comando[1] == 'banheiro' or comando[1] == 'câmara_secreta' or comando[1] == 'quarto_harry' or comando[1] == 'sala_poções' or comando[1] == 'floresta_proibida':
            print('\033[;1mProibido aparatar nesse local.')
        else:
            print('\033[;1mNão existe esse local no mapa.')
            print('\033[;1mO preço pelo seu erro é uma vida')
            vidas.pop()

    elif comando[0] == 'usar':
        if comando[1] == 'felix_felicis':
            print('\033[;1magora você tem sorte.')
            inventário.pop(inventário.index('felix_felicis'))
        elif comando[1] == 'vira-tempo' and 'vira-tempo' in inventário:
            vidas = ['❤️ ', '❤️ ', '❤️ ']
            local_atual = 'escadas'
            inventário.pop(inventário.index('vira-tempo'))
        elif comando[1] == 'mapa_maroto':
            senha = input('> ')
            if senha == 'varinha juro solenemente que não pretendo fazer nada de bom':
                print('''
\033[;1mOs Srs. Aluado, Rabicho, Almofadinha e Pontas, fornecedores de recursos para feiticeiros malfeitores, têm a honra de apresentar:

O MAPA DO MAROTO
             sala_diretor({senha1})
                |
        --- setimo_andar --- sala_comunal_grifinória({senha2})
        |       
        |              sala_poções
        |                 |
escadas --- terreo --- masmorras --- cozinha
        |     |
        |   terrenos --- floresta_proibida
        | 
        --- segundo_andar --- banheiro
'''.format(senha1=senha1, senha2=senha2))
                while senha != 'varinha malfeito feito':
                    senha = input('> ')
                inventário.pop(inventário.index('mapa_maroto'))
            else:
                print('\033[;1mvocê não está usando o mapa corretamente')
        elif comando[1] == 'vassoura' and 'vassoura' in inventário and local_atual == 'câmara_secreta' and 'gina_weasley' in inventário:
            print('''\033[1;33mVocê conseguiu resgatar a gina da câmara secreta, parabéns!
Por ter conseguido resolver todos os desafios, você agora é um bruxo!''')
            time.sleep(3)
            c = 1
            inventário.pop(inventário.index('vassoura'))
            break
        elif comando[1] == 'vassoura' and 'vassoura' in inventário:
            inventário.pop(inventário.index('vassoura'))
        elif comando[1] == 'vassoura' and 'vassoura' in inventário and local_atual == 'câmara_secreta' and 'gina_weasley' not in inventário:
            local_atual = 'banheiro'
            inventário.pop(inventário.index('vassoura'))
        elif comando[1] == 'fawkes' and 'fawkes' in inventário and veneno == 1:
            print('''\033[1;33mVocê usou a fênix, as lágrimas dela têm poderes curativos, você está curado do veneno do basilisco!
Agora você só prencisa sair da câmara secreta!''')
            inventário.pop(inventário.index('fawkes'))
            time.sleep(3)
            veneno = 0
        elif comando[1] == 'fawkes' and 'fawkes' in inventário:
            vidas = vidas.append('/❤️ ')
            inventário.pop(inventário.index('fawkes'))

        elif comando[1] == 'capa_invisibilidade' and 'capa_invisibilidade' in inventário:
            invisibilidade = 3
    elif comando[0] == 'ir' and comando[1] == 'sala_precisa' and local_atual == 'setimo_andar' and vidas == ['❤️ ']:
        local_atual = 'sala_precisa'
    elif comando[0] == 'ir' and comando[1] != 'sala_precisa':
        if comando[1] == 'sala_poções':
            if 'chave_snape' in inventário and comando[1] in mapa[local_atual]:
                novo_local = comando[1]
                local_atual = mapa[local_atual][novo_local]
                inventário.pop(inventário.index('chave_snape'))
            else:
                print('\033[;1mVocê precisa da chave do snape para entrar.')

        elif comando[1] == 'banheiro':
            os.system('clear')
            print('\033[;1mPorta trancada')
            porta = input('> ')
            if porta == 'varinha alohomora' and 'varinha' in inventário and comando[1] in mapa[local_atual]:
                novo_local = comando[1]
                local_atual = mapa[local_atual][novo_local]

        elif comando[1] == 'sala_diretor':
            senha = int(input('> '))
            if senha == senha1 and comando[1] in mapa[local_atual]:
                novo_local = comando[1]
                local_atual = mapa[local_atual][novo_local]
            else:
                vidas.pop()
                print('\033[;1mSenha incorreta.')
                print('\033[;1mO preço pelo seu erro é uma vida')

        elif comando[1] == 'sala_comunal_grifinória':
            senha = int(input('> '))
            if senha == senha2 and comando[1] in mapa[local_atual]:
                novo_local = comando[1]
                local_atual = mapa[local_atual][novo_local]
            else:
                vidas.pop()
                print('\033[;1mSenha incorreta.')
                print('\033[;1mO preço pelo seu erro é uma vida')

        elif comando[1] == 'segundo_andar':
            if invisibilidade > 0:
                print(
                    '\033[;1mFilch está neste corredor, mas você está invisível e vai poder passar.')
                if comando[1] in mapa[local_atual]:
                    novo_local = comando[1]
                    local_atual = mapa[local_atual][novo_local]
            else:
                print('''\033[1;32mFilch
- O que faz andando pelos corredores pirralho, não ouviu que tem um monstro aqui? volte para a sala comunal!''')
                vidas.pop()
                local_atual = 'sala_comunal_grifinória'

        elif comando[1] == 'masmorras':
            if invisibilidade > 0:
                print(
                    '\033[;1mSnape está neste corredor, mas você está invisível e vai poder passar.')
                if comando[1] in mapa[local_atual]:
                    novo_local = comando[1]
                    local_atual = mapa[local_atual][novo_local]
            else:
                print('''\033[1;32mSNAPE
- O que faz andando pelos corredores potter? vamos para a detenção agora!''')
                print('''\033[1;32mGAME OVER, você perdeu.
agora você é um trouxa!''')
                c = 0
                break

        elif comando[1] in mapa[local_atual]:
            novo_local = comando[1]
            local_atual = mapa[local_atual][novo_local]

    elif comando[0] == 'pegar' and 'item' in list(mapa[local_atual].keys()):
        if local_atual == 'masmorras':
            item2 = comando[1]
            if item2 in mapa[local_atual]['item']:
                chance = random.choice(chavep)
                if chance == 0:
                    print('''\033[1;32mSNAPE
- O que faz andando pelos corredores potter? vamos para a detenção agora!''')
                    print('''\033[1;32mGAME OVER, você perdeu.
agora você é um trouxa!''')
                    c = 0
                    break
                if chance == 1:
                    print(
                        '\033[1;32mparabéns! você conseguiu a chave da sala de poções.')
                    inventário.append(item2)
                    del mapa[local_atual]['item']

        else:
            item2 = comando[1]
            if item2 in mapa[local_atual]['item']:
                inventário.append(item2)
                del mapa[local_atual]['item']
                print('\033[1;94mvocê conseguiu', item2)

    else:
        print('\033[;1mComando inválido')

    if veneno == 1:
        print('''\033[1;32mVocê não conseguiu curar o veneno do basilisco e morreu envenenado.
GAME OVER, você perdeu.
Agora você é um trouxa!''')
        c = 0
        break

    if vidas == []:
        print('''\033[1;32mGAME OVER, você perdeu.
Agora você é um trouxa!''')
        c = 0
        break
    if len(comando) == 2 and comando[1] == 'dobby':
        print(
            '\033[;1mAgora você pode aparatar com o elfo para a sala_dursley (e quase todos os lugares de hogwarts)')

    if invisibilidade > 0:
        invisibilidade -= 1
        if invisibilidade == 2:
            print('\033[;1mVocê estará invisível no próximo local que você for.')

    print('\033[;1m...')
    time.sleep(3)
    os.system('clear')
lbruxos = []
q = 0
bruxos = open('bruxos.txt', 'r')
for i in bruxos:
    if c == 1 and q == 0:
        linha = nome + '\n'
        lbruxos.append(linha)
        q = 1
    linha = i
    linha = linha.strip()
    if linha != nome:
        linha = linha + '\n'
        lbruxos.append(linha)
bruxos.close()

bruxos = open('bruxos.txt', 'w')
for i in lbruxos:
    bruxos.write(i)
bruxos.close()

ltrouxas = []
trouxas = open('trouxas.txt', 'r')
for i in trouxas:
    if c == 0 and q == 0:
        linha = nome + '\n'
        ltrouxas.append(linha)
        q = 1
    linha = i
    linha = linha.strip()
    if linha != nome:
        linha = linha + '\n'
        ltrouxas.append(linha)
trouxas.close()

trouxas = open('trouxas.txt', 'w')
for i in ltrouxas:
    trouxas.write(i)
trouxas.close()

bruxos = open('bruxos.txt', 'r')
print('\033[1;31mBRUXOS')
print(bruxos.read())
bruxos.close()

trouxas = open('trouxas.txt', 'r')
print('\033[1;32mTROUXAS')
print(trouxas.read())
trouxas.close()
