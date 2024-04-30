import pygame
import threading
import time
import emoji
import os
def music_inicio():
    pygame.init()
    pygame.mixer.music.load('C:/Users/Luciano_cleberton/Documents/Python-game-/musica/inicio.mp3')
    pygame.mixer.music.play()

threading.Thread(target=music_inicio).start()

def limpar_tela():
    os.system('cls' if os.name == 'nt' else 'clear')

branco='\033[38;2;247;237;237m'
cinza='\033[38;2;146;147;148m'
roxo='\033[38;2;106;31;161m'
pastel='\033[38;2;255;181;209m'
nuvem='\033[38;2;227;184;200m'
rosa='\033[38;2;247;74;139m'
pet=0
vermelho='\033[38;2;245;125;137m'
azul_claro='\033[38;2;179;227;255m'
limpar_tela()
print(f'''
                                    █▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀█
                                    █ ░░ ░░ ░░ ░░ ░░ ░░ ░░ ░░ ░░ ░░ ░░ ░░ ░░ ░░ ░░ ░░ ░░ ░░ ░░ ░░ ░░ ░░ ░░ ░░ ░░ ░░ ░░ ░░ ░░ ░░ ░░░░ ░░ ░░ ░░  ░░ █ 
                                    █ ░░      _                                                   _       _     _                              ░░ █
                                    █ ░░     | |                                                 (_)     | |   | |                             ░░ █
                                    █ ░░   __| |_ __ ___  __ _ _ __ ___  ___    ___  _ __   _ __  _  __ _| |__ | |_ _ __ ___   __ _ _ __ ___   ░░ █
                                    █ ░░  / _` | '__/ _ \/ _` | '_ ` _ \/ __|  / _ \| '__| | '_ \| |/ _` | '_ \| __| '_ ` _ \ / _` | '__/ _ \  ░░ █
                                    █ ░░ | (_| | | |  __/ (_| | | | | | \__ \ | (_) | |    | | | | | (_| | | | | |_| | | | | | (_| | | |  __/  ░░ █
                                    █ ░░  \__,_|_|  \___|\__,_|_| |_| |_|___/  \___/|_|    |_| |_|_|\__, |_| |_|\__|_| |_| |_|\__,_|_|  \___|  ░░ █
                                    █ ░░                                                            __/ |                                      ░░ █
                                    █ ░░                                                           |___/                                       ░░ █
                                    █ ░░ ░░ ░░ ░░ ░░ ░░ ░░ ░░ ░░ ░░ ░░ ░░ ░░ ░░ ░░ ░░ ░░ ░░ ░░ ░░ ░░ ░░ ░░ ░░ ░░ ░░ ░░ ░░ ░░ ░░ ░░ ░░ ░░ ░░ ░░ ░░ █
                                    █▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄█''')
time.sleep(5)
limpar_tela()
print(f''' 
================================== █▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀█ ==================================  
                                   █ ░░ ░░ ░░ ░░ ░░ ░░ ░░ ░░ ░░ ░░ ░░ ░░ ░░ ░░ ░░ ░░ ░░ ░░ ░░ ░░ ░░ ░░ ░░ ░░ ░░ ░░ ░░ ░░ ░░ ░░ ░░ ░░ ░░ ░░ ░░ ░░ █ 
                                   █ ░░                  _____      _             _                                _           _              ░░ █
                                   █ ░░                 / ____|    (_)           | |                              (_)         | |             ░░ █
                                   █ ░░                | (___   ___ _  __ _      | |__   ___ _ __ ___       __   ___ _ __   __| | ___         ░░ █
                                   █ ░░                 \___ \ / _ \ |/ _` |     | '_ \ / _ \ '_ ` _ \      \ \ / / | '_ \ / _` |/ _ \        ░░ █
                                   █ ░░                 ____) |  __/ | (_| |     | |_) |  __/ | | | | |      \ V /| | | | | (_| | (_) |       ░░ █
                                   █ ░░                |_____/ \___| |\__,_|     |_.__/ \___|_| |_| |_|       \_/ |_|_| |_|\__,_|\___/        ░░ █
                                   █ ░░                           _/ |                                                                        ░░ █
                                   █ ░░                          |__/                                                                         ░░ █
                                   █ ░░ ░░ ░░ ░░ ░░ ░░ ░░ ░░ ░░ ░░ ░░ ░░ ░░ ░░ ░░ ░░ ░░ ░░ ░░ ░░ ░░ ░░ ░░ ░░ ░░ ░░ ░░ ░░ ░░ ░░ ░░ ░░ ░░ ░░ ░░ ░░ █
                                   █▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄█''')
time.sleep(5)
limpar_tela()
print(pastel+'|=|'*67)
print(pastel+'-=-'*30,'\033[0;31mDREAMS OR NIGHTMARES\033[m',pastel+'-=-'*29,end='=-')
print('|=|'*67)
print(branco+'.'*201)
print(branco+'.'*201)
print(branco+'.'*201)
print(branco+'.'*61,vermelho+'_'*80,branco+'.'*58)
print(branco+'.'*60,vermelho+'|\033[4mVIVEMOS E MORREMOS PELOS NOSSOS SONHOS, E SEM SONHAR, QUEM SOMOS? E QUEM SEREMOS?\033[m\033[38;2;255;181;209m|\033[m',branco+'.'*56)
time.sleep(0.6)
print(branco+'.'*60,vermelho+'|\033[4m __________ATÉ ONDE VAMOS?ATÉ O QUE FAZEMOS? E O QUE CONQUISTAMOS?_______________\033[m\033[38;2;255;181;209m|\033[m',branco+'.'*56)
time.sleep(0.6)
print(branco+'.'*60,vermelho+'|\033[4m___________SOMOS APENAS CRIANÇAS BRINCANDO EM UM GRANDE ESPETÁCULO.______________\033[m\033[38;2;255;181;209m|\033[m',branco+'.'*56)
time.sleep(0.6)
print(branco+'.'*60,vermelho+'|\033[4m_______SERÁ QUE VIVEMOS EM SONHOS OU PESADELOS? CUIDADO COM SUAS DECISÕES._______\033[m\033[38;2;255;181;209m|\033[m',branco+'.'*56)
time.sleep(0.6)
print(branco+'.'*60,vermelho+'|\033[4m________SÓ VOCÊ PODE DECIDIR SEU FUTURO, TUDO DEPENDE DAS SUAS  ESCOLHAS.________\033[m\033[38;2;255;181;209m|\033[m',branco+'.'*56)
time.sleep(0.6)
print(branco+'.'*60,vermelho+'|\033[4m____BOA SORTE, PEQUENA CRIANÇA, EM SUA JORNADA, E CUIDADO COM SUAS ESCOLHAS.______\033[m\033[38;2;255;181;209m|\033[m',branco+'.'*55)
print(branco+'.'*201)
print(branco+'.'*201)
print(branco+'.'*201)
time.sleep(4)

start=str(input(vermelho+ 'Deseja iniciar o jogo [Sim/Não]:\033[38;2;179;227;255m ')).strip()
while start not in "SIMsimSsSim":
    start=str(input(vermelho+'Deseja iniciar o jogo [SIM/Não]:\033[38;2;179;227;255m ')).strip()
    
pygame.mixer.music.load('C:/Users/Luciano_cleberton/Documents/Python-game-/musica/meio.mp3')
pygame.mixer.music.play(loops=-1)
limpar_tela()
time.sleep(1)
print('\033[0;38;2;247;237;237m|','-'*38,'>', '|\033[m\033[38;2;179;227;255mAPLAUSOS 👏👏👏👏👏👏👏  APLAUSOS 👏👏👏👏👏👏👏 APLAUSOS 👏👏👏👏👏👏👏 APLAUSOS 👏👏👏👏👏👏👏 APLAUSOS 👏👏👏👏👏👏👏\033[m\033[038;2;247;237;237m|','<','-'*31,'|')
time.sleep(0.7)
print('\033[0;38;2;247;237;237m|','-'*34,'>', '|\033[m\033[38;2;179;227;255mPARA A MELHOR DANÇARINA E CANTORA  DO MUNDO 👏👏👏👏👏👏 APENAS COM SEUS 14 ANOS,ELA REVIROU O MUNDO COM SEU TALENTO 👏👏👏👏👏👏 \033[m\033[038;2;247;237;237m|','<','-'*25,'|')
time.sleep(0.7)
print('\033[0;38;2;247;237;237m|','-'*24,'>', '|\033[m\033[38;2;179;227;255mSUA HISTÓRIA EMOCIONANTE CONQUISTOU SEUS FÃS. A GAROTA COMEÇOU A CANTAR E DANÇAR PARA FAZER SUCESSO E ENCONTRAR SEU PAI, QUE NUNCA A CONHECEU\033[m\033[038;2;247;237;237m|','<','-'*24,'|')
time.sleep(0.7)
print('\033[0;38;2;247;237;237m|','-'*32,'>', '|\033[m\033[38;2;179;227;255mESSA CRIANÇA QUE SUPEROU DIFICULDADES CRESCENDO NO INTERIOR DO NORDESTE EM UMA PEQUENA CIDADE, FEZ NOME NO MUNDO INTEIRO\033[m\033[038;2;247;237;237m|','<','-'*37,'|')
time.sleep(0.7)
print('\033[0;38;2;247;237;237m|','-'*38,'>', '|\033[m\033[38;2;179;227;255mE CALOU SUA MÃE, QUE NUNCA ACREDITOU EM SEU PONTENCIAL, QUE ESCONDEU INFORMAÇÕES DO SEU PAI E A PROIBIA DE CANTAR E DANÇAR\033[m\033[038;2;247;237;237m|','<','-'*29,'|')
time.sleep(0.7)
print('\033[0;38;2;247;237;237m|','-'*23,'>', '|\033[m\033[38;2;179;227;255mHOJE AQUELA CRIANÇA, QUE SUA PRÓPRIA MÃE PROIBIA DE DANÇAR E CANTAR, VIROU ESSA ESTRELA ADMIRADA POR TODOS, E TODOS DESEJAM ESTAR EM SUA PRESENÇA\033[m\033[038;2;247;237;237m|','<','-'*21,'|')
time.sleep(0.7)
jogador=str(input('\033[0;33m|------------------------>|CRIANÇA, DIGA AO MUNDO COMO VOCÊ SE CHAMA:\033[m\033[38;2;179;227;255m ').strip().title())
time.sleep(0.7)     
print('\033[0;38;2;247;237;237m|------------>|BEEP BEEP BEEP ')
time.sleep(2)
print('|------------>|O DESPERTADOR COMEÇOU A TOCAR COM UM ZUMBIDO ESTRIDENTE QUE ENCHIA O QUARTO...')
time.sleep(2)
print('|------------[{}]>|JÁ CONSEGUIA ESCUTAR OS GRITOS DA MINHA MÃE PEDINDO PARA EU LEVANTAR DA CAMA, MAS A PREGUIÇA ESTAVA MAIS FORTE.'.format(jogador))
time.sleep(2)
print('|------------[MÃE]>|{} LEVANTA E VEM TOMAR CAFÉ DA MANHÂ!'.format(jogador))
time.sleep(2)
café_da_manha=str(input(vermelho+'|------------>|{} ESCOLHA A LETRA QUE DECIDIR SUA ESCOLHA:(A)-[CONTINUAR DORMINDO], (B)-[LEVANTAR E DESCER PARA TOMAR CAFÉ]:\033[m \033[38;2;179;227;255m'.format(jogador)).strip().lower())[0]
while café_da_manha not in 'ab':
    print('Alternativa inexistente!!')
    café_da_manha=str(input(vermelho+'|------------>|{} ESCOLHA A LETRA QUE DECIDIR SUA ESCOLHA:(A)-[CONTINUAR DORMINDO], (B)-[LEVANTAR E DESCER PARA TOMAR CAFÉ]:\033[m \033[38;2;179;227;255m'.format(jogador)).strip().lower())[0]

limpar_tela()
time.sleep(1)
if café_da_manha=='a':
    print('\033[m------------>|ELA VAI ATÉ MEU QUARTO E ME PUXA DA CAMA')
    time.sleep(1)
    print('|------------[MÃE]>|LEVANTA!!! GAROTA PREGUIÇOSA')
    time.sleep(1)
    print('|------------[{}]>|LEVANTO COM PREGUIÇA E CAMINHO ATÉ A COZINHA'.format(jogador))
    time.sleep(1)
if café_da_manha=='b':
    print('\033[m|------------[{}]>|LEVANTO E VOU EM DIREÇÃO Á COZINHA, JÁ CONSIGO SENTIR O CHEIRO DE PÃO COM OVO E O CHEIRO DO CAFÉ.'.format(jogador))
    time.sleep(2)
    print('|------------[MÃE]>|PARABÉNS,HOJÉ EU NÃO PRECISEI IR TE PUXAR DA CAMA...','  "ela falou sorrindo."')
    time.sleep(1)
print('|------------[{}]>|TOMO O CAFÉ AINDA COM OS PENSAMENTOS PERDIDOS NO SONHO QUE TIVE ANTES, SÓ DE LEMBRAR FAZ SORRISOS ESCAPAREM'.format(jogador))
time.sleep(1)
print('|------------[{}]>|"UM DIA IREI FAZER ESSE SONHO SER TORNAR REALIDADE E IREI ENCONTRAR MEU PAI PARA MOSTRAR TUDO QUE EU CONQUISTEI." '.format(jogador))
time.sleep(1)
print('|------------[MÃE]>|"FILHA, QUANDO TERMINAR DE TOMAR O CAFÉ, VÁ LAVAR A LOUÇA.CUIDADO COM A HORA, LOGO, LOGO SERÁ MEIO-DIA E VOCÊ  DEVE IR PARA A ESCOLA."','diz ela terminando de tomar café...')
time.sleep(1)
print('|------------[{}]>|RESPIREI FUNDO E TENTEI REUNIR CORAGEM PARA ABORDAR O ASSUNTO SOBRE O MEU PAI E O MOTIVO DE NUNCA TÊ-LO CONHECIDO.'.format(jogador))
time.sleep(1)
print('|------------[{}]>|"NO ENTANTO, APÓS O SONHO, SENTI UM CRESCENTE DESEJO DE DESCOBRIR MAIS SOBRE ELE."'.format(jogador))
time.sleep(1)
print('|------------[{}]>|"MAS SEI QUE É UM ASSUNTO QUE DEIXA MINHA MÃE IRRITADA. SERÁ UMA BOA IDEIA PERGUNTAR SOBRE ELE?"'.format(jogador))
time.sleep(1)
manha_pergunta=str(input(vermelho+'|------------>|{} ESCOLHA A LETRA QUE DECIDIR SUA ESCOLHA:(A)-[PERGUNTAR SOBRE SEU PAI], (B)-[PERGUNTA SOBRE O PASSADO DA SUA MÃE], (C)-[CONTINUAR COMENDO]:\033[m \033[38;2;179;227;255m'.format(jogador)).strip().lower())[0]
while manha_pergunta not in 'abc':
    print('Alternativa inexistente!!')
    manha_pergunta=str(input(vermelho+'|------------>|{} ESCOLHA A LETRA QUE DECIDIR SUA ESCOLHA:(A)-[PERGUNTAR SOBRE SEU PAI], (B)-[PERGUNTA SOBRE O PASSADO DA SUA MÃE], (C)-[CONTINUAR COMENDO]:\033[m \033[38;2;179;227;255m'.format(jogador)).strip().lower())[0]
limpar_tela()
time.sleep(1)
if manha_pergunta=='a':
    print('\033[m|------------[{}]>|MÃE, ONDE ESTÁ MEU PAI? QUEM É ELE? E POR QUE VOCÊ NUNCA ME FALOU SOBRE ELE?'.format(jogador))
    time.sleep(1)
    print('|------------[MÃE]>|GAROTA, NUNCA ME PERGUNTE ISSO! VOCÊ JÁ TEM A MIM, POR QUE QUER AQUELE TRASTE?')
    time.sleep(1)
    print('|------------[MÃE]>|AQUELE HOMEM NUNCA TE QUIS, ELE NUNCA TE AMOU!','  "ela sair irritada da cozinha"')
    time.sleep(1)
    print('|------------[{}]>|Lágrimas descem do meu rosto, formando caminho como rios...'.format(jogador))
    time.sleep(4)
if manha_pergunta=='b':
    print('\033[mPOR UM MOMENTO, A COZINHA É TOMADA PELO SILENCIO...')
    time.sleep(1)
    print('|------------[MÃE]>|FILHA, QUANDO EU ERA PEQUENA, AMAVA DANÇAR E CANTAR COMO VOCÊ. QUANDO CANTAVA NAS FESTAS DE FAMÍLIA AO LADO DO SEU AVÔ, QUE TOCAVA VIOLÃO...')
    time.sleep(1)
    print('|------------[MÃE]>|MAS FUI CRESCENDO E CONHECIMENTO O MUNDO. HOJE EM DIA, ODEIO DANÇAR E NÃO GOSTO DE CANTAR.')
    time.sleep(1)
    print('|------------[MÃE]>|ME ARREPENDO DE NÃO TER ESTUDADO E DE NÃO TER IDO PARA AQUELAS ESCOLAS GRANDES NA CAPITAL, ONDE AS PESSOAS ESTUDAM PARA TRABALHAR EM PROFISSÕES QUE GANHAM UM BOM DINHEIRO.')
    time.sleep(4)
if manha_pergunta=='c':
    print('\033[m|------------[{}]>|"É MELHOR EU APENAS TOMAR O CAFÉ DA MANHÃ. SER EU PERGUNTAR, ELA PASSA O DIA TODO IRRITADA '.format(jogador))
    time.sleep(3)
print('|--------[{}]>|Começo a lavar os pratos enquanto ela prepara o almoço.'.format(jogador))
time.sleep(1)
print('Toc, toc, toc.')
time.sleep(1)
print('De repente, um chamado ecoou pela casa, interrompendo o silêncio da manhã. Com um sobressalto, Maria levantou-se da mesa do café e correu em direção à porta.')
time.sleep(1)
print('Ao abri-la, deparou-se com o carteiro, segurando duas cartas em suas mãos.')
time.sleep(1)
print('Seu coração começou a bater mais rápido, ansiosa para descobrir o conteúdo dessas cartas que poderiam trazer notícias de longe ou segredos guardados há tempos."')
time.sleep(1)
print('|------------[MÃE]>|MENINA, CUIDE LOGO DE SER APRONTAR PARA IR À ESCOLA! JÁ SÃO 11 HORAS E VOCÊ AINDA PRECISA PEGAR O ÔNIBUS!','disse ela irritada e com uma voz apreensiva')
time.sleep(1.5)
print('|------------[MÃE]>|Ela leu as duas cartas e, ao terminar a primeira, lágrimas começaram a descer pelo seu rosto.') 
time.sleep(1.5)
print('|------------[MÃE]>|Com um gesto brusco, ela jogou a carta no lixo, incapaz de suportar a dor que as palavras escritas lhe trouxeram.')
time.sleep(1.5)
print('|------------[MÃE]>|Ela voltou a se arrumar para ir trabalhar na feira, vendendo as roupas feitas de crochê que ela mesma fez.')
time.sleep(1.5)
print('|--------[{}]>|Vejo a carta jogada no lixo'.format(jogador))
time.sleep(1.5)
escolha_carta=str(input(vermelho+'|------------>|{} ESCOLHA A LETRA QUE DECIDIR SUA ESCOLHA:(A)-[PEGAR A CARTA QUE ESTÁ NO LIXO], (B)[PERGUNTA QUEM ENVIARAM AS CARTAS], (C)-[IR PARA ESCOLA]:\033[m \033[38;2;179;227;255m'.format(jogador))).strip().lower()[0]
while escolha_carta not in 'abc':
    print('Alternativa inexistente!!!')
    escolha_carta=str(input(vermelho+'|------------>|{} ESCOLHA A LETRA QUE DECIDIR SUA ESCOLHA:(A)-[PEGAR A CARTA QUE ESTÁ NO LIXO], (B)[PERGUNTA QUEM ENVIARAM AS CARTAS], (C)-[IR PARA ESCOLA]:\033[m \033[38;2;179;227;255m'.format(jogador))).strip().lower()[0]
limpar_tela()
time.sleep(1.5)
if escolha_carta=='a':
    print('\033[mEla pegou a carta do lixo, desdobrou-a e começou a ler.')
    time.sleep(1.5)
    print(f'''
              ===============================================================================
              =---|OLÁ DANÇARINA DAS CHAMAS, QUANDO VOCÊ VAI TRAZER MINHA PEQUENA FILHA?|=---
              =---|FINALMENTE CONSEGUIR ENCONTRA SEU ENDEREÇO.UM CONHECIDO ESTAVA  NA   |=---
              =---|FEIRA E AVISTOU VOCÊ VENDENDO BLUSAS ARTESANAIS. ELE TE RECONHECEU.  |=---
              =---|DISSE QUE CONTINUAVA COM OLHOS DE FERA,IGUALZINHO QUANDO ERA MAIS    |=---
              =---|NOVA, MARIA, SINTO SAUDADES SUAS.TRAGA MINHA CRIANÇA,QUE VOCÊ NÃO VAI|=---
              =---|PRECISAR TRABALHAR.EU PAGO E CUIDO DE VOCÊS, E DAREI TUDO DE MELHOR  |=---
              =---|PARA MINHA QUERIDA FILHA, QUE SEMPRE QUIS CONHECER.                  |=---
              =---|                                                                     |=---
              =---|                                   Assinado:                         |=---
              =---|                                            Sebastião de Moura       |=---
              =---|                                                                     |=---
              =---|PS: MEU ENDEREÇO É :AVENIDA DAS FLORES 145,Caruaru (Pernambuco)      |=---
              ===============================================================================''')
    time.sleep(6)
    print('|--------[{}]>|EU SABIA QUE MEU PAI QUERIA ME CONHECER. EU SABIA QUE ELE ME AMAVA'.format(jogador))
    time.sleep(1.5)
    print('|--------[{}]>|POR QUE MINHA MÃE SEMPRE MENTIU PARA MIM? EU A ODEIO. EU VOU FUGIR E ENCONTRA ELE'.format(jogador))
    time.sleep(1.5)
if escolha_carta=='b':
    print('\033[m|-------[{}]>|MÂE, QUEM ENVIOU AS CARTAS? POR QUE A SENHORA ESTÁ TÃO NERVOSA? FOI MEU PAI?'.format(jogador))
    time.sleep(1.5)
    print('|-------[MÃE]>|MENINA, PARA DE FALAR BESTEIRA. TEU PAI NUNCA PROCUROU A GENTE, QUEM ENVIOU AS CARTAS FORAM AMIGAS DE INFÂNCIA MINHA.')
    time.sleep(1.5)
    print('|-------[MÃE]>|AGORA CUIDE PRA IR PRA ESCOLA, SENÃO VAI LEVAR UMAS PALMADAS.') 
    time.sleep(1.5)
    print('|-------[{}]>|CERTO MÃE...','falo triste e ao mesmo tempo curiosa para ler as cartas'.format(jogador))
    time.sleep(1.5)
    tentar_pegar=str(input(vermelho+'|------------>|{} ESCOLHA A LETRA QUE DECIDIR SUA ESCOLHA:(A)-[PEGAR A CARTA QUE ESTÁ NO LIXO],(B)-[IR PARA A ESCOLA]:\033[m \033[38;2;179;227;255m'.format(jogador)).strip().lower())[0]
    while tentar_pegar not in 'ab':
        print('Alternativa inexistente!!!')
        tentar_pegar=str(input(vermelho+'|------------>|{} ESCOLHA A LETRA QUE DECIDIR SUA ESCOLHA:(A)-[PEGAR A CARTA QUE ESTÁ NO LIXO],(B)-[IR PARA A ESCOLA]:\033[m \033[38;2;179;227;255m'.format(jogador)).strip().lower())[0]
    limpar_tela()
    if tentar_pegar=='a':
        print('\033[mEla pegou a carta do lixo, desdobrou-a e começou a ler.')
        time.sleep(1.5)
        print(f'''
              ===============================================================================
              =---|OLÁ DANÇARINA DAS CHAMAS, QUANDO VOCÊ VAI TRAZER MINHA PEQUENA FILHA?|=---
              =---|FINALMENTE CONSEGUIR ENCONTRA SEU ENDEREÇO.UM CONHECIDO ESTAVA  NA   |=---
              =---|FEIRA E AVISTOU VOCÊ VENDENDO BLUSAS ARTESANAIS. ELE TE RECONHECEU.  |=---
              =---|DISSE QUE CONTINUAVA COM OLHOS DE FERA,IGUALZINHO QUANDO ERA MAIS    |=---
              =---|NOVA, MARIA, SINTO SAUDADES SUAS.TRAGA MINHA CRIANÇA,QUE VOCÊ NÃO VAI|=---
              =---|PRECISAR TRABALHAR.EU PAGO E CUIDO DE VOCÊS, E DAREI TUDO DE MELHOR  |=---
              =---|PARA MINHA QUERIDA FILHA, QUE SEMPRE QUIS CONHECER.                  |=---
              =---|                                                                     |=---
              =---|                                   Assinado:                         |=---
              =---|                                            Sebastião de Moura       |=---
              =---|                                                                     |=---
              =---|PS: MEU ENDEREÇO É :AVENIDA DAS FLORES 145,Caruaru (Pernambuco)      |=---
              ===============================================================================''')
        time.sleep(6)
        print('|--------[{}]>|EU SABIA QUE MEU PAI QUERIA ME CONHECER. EU SABIA QUE ELE ME AMAVA'.format(jogador))
        time.sleep(1.5)
        print('|--------[{}]>|POR QUE MINHA MÃE SEMPRE MENTIU PARA MIM? EU A ODEIO. EU VOU FUGIR E ENCONTRA ELE'.format(jogador))
        time.sleep(1.5)
    if tentar_pegar=='b':
        print('\033[mME ARRUMEI E FUI PARA ESCOLA, TENTANDO ESQUECER A FORMA QUE MINHA MÃE REAGIU ÁS CARTAS.')
        time.sleep(1.5)
        print('As coisas continuavam como sempre, e nada mudava.')
        time.sleep(2)
        print(f'''------------------------------------------------------------------------------------------------------------------------------------
=-=-=-=-=-=-=-|==============================================================================|-=-=-=-=-=--=-=-=-=-=-=-=-=-=-=-=-=
=-=-=-=-=-=-=-|"{jogador} resolveu não abrir a carta, sendo assim, nunca descobriu a verdade.|-=-=-=-=-=--=-=-=-=-=-=-=-=-=-=-=-=
=-=-=-=-=-=-=-| {jogador} teve uma vida plena e feliz.                                       |-=-=-=-=-=--=-=-=-=-=-=-=-=-=-=-=-=
=-=-=-=-=-=-=-| Se casou, teve dois filhos, e morreu de velhice enquanto dormia"          |-=-=-=-=-=--=-=-=-=-=-=-=-=-=-=-=-=
=-=-=-=-=-=-=-|==============================================================================|-=-=-=-=-=--=-=-=-=-=-=-=-=-=-=-=-=''')
        print('\033[0;33m"Parabéns {} ! Você conquistou o final pacífico e feliz."\033[m'.format(jogador))
        time.sleep(10)
        exit()
if escolha_carta=='c':
    print('\033[mME ARRUMEI E FUI PARA ESCOLA, TENTANDO ESQUECER A FORMA QUE MINHA MÃE REAGIU ÁS CARTAS.')
    time.sleep(1.5)
    print('As coisas continuavam como sempre, e nada mudava.')
    time.sleep(1.5)
    print(f'''------------------------------------------------------------------------------------------------------------------------------------
=-=-=-=-=-=-=-|==============================================================================|-=-=-=-=-=--=-=-=-=-=-=-=-=-=-=-=-=
=-=-=-=-=-=-=-|"{jogador} resolveu não abrir a carta, sendo assim, nunca descobriu a verdade.|-=-=-=-=-=--=-=-=-=-=-=-=-=-=-=-=-=
=-=-=-=-=-=-=-| {jogador} teve uma vida plena e feliz.                                       |-=-=-=-=-=--=-=-=-=-=-=-=-=-=-=-=-=
=-=-=-=-=-=-=-| Se casou, teve dois filhos, e morreu de velhice enquanto dormia"          |-=-=-=-=-=--=-=-=-=-=-=-=-=-=-=-=-=
=-=-=-=-=-=-=-|==============================================================================|-=-=-=-=-=--=-=-=-=-=-=-=-=-=-=-=-=''')
    print('\033[0;33m"Parabéns {} ! Você conquistou o final pacífico e feliz."\033[m'.format(jogador))
    time.sleep(10)
    exit()
print('Espero do lado de fora da casa, permanecendo ali até que minha mãe finalmente vá trabalhar.')
time.sleep(1)
print('Observo enquanto ela parte para o trabalho, com uma expressão ainda carregada de preocupação.')
time.sleep(1)
print('Entro e reúno algumas roupas e um pouco do dinheiro que tinha guardado. Coloco tudo na bolsa e, com a caneta tremendo entre os dedos, escrevo uma carta de despedida. ')
time.sleep(1)
print('Vou embora perdida em pensamentos. O que será que vou conseguir realizar: meuS sonhoS, ou meu objetivo de conhecer meu pai? Ou será que irei fazer tudo isso se tornar realidade?"')
pensamentos=str(input(vermelho+'|------------>|{} ESCOLHA A LETRA QUE DECIDIR SUA ESCOLHA:(A)-[ACHO QUE REALIZAR MEUS SONHOS],(B)-[CONHECER MEU PAI],(C)-[CONSEGUIR REALIZAR TUDO]:\033[m  \033[38;2;179;227;255m'.format(jogador))).strip().lower()[0]
while pensamentos not in 'abc':
    print('Alternativa inexistente!!')
    pensamentos=str(input(vermelho+'|------------>|{} ESCOLHA A LETRA QUE DECIDIR SUA ESCOLHA:(A)-[ACHO QUE REALIZAR MEUS SONHOS],(B)-[CONHECER MEU PAI],(C)-[CONSEGUIR REALIZAR TUDO]:\033[m \033[38;2;179;227;255m'.format(jogador))).strip().lower()[0]

limpar_tela()
pygame.mixer.music.load('C:/Users/Luciano_cleberton/Documents/Python-game-/musica/fuga.mp3')
pygame.mixer.music.play(loops=-1)
dinheiro=60
time.sleep(3)
print('\033[mEstou toda animada para essa jornada. Nem tô cabendo em mim de tanta empolgação!')
time.sleep(1)
print('Caminhei até a rodoviária, com o sol quente do meio-dia batendo forte sobre minha pele.','  "A rodoviaria de Lagoa dos gatos é bem parada..."')
time.sleep(1)
print('Chegando lá, respirei fundo e, uma mistura de alegria e medo dançava dentro de mim, me aproximei do guichê.')
time.sleep(1) 
print('|-------[{}]>|Oh moço, me diga, qual desses ônibus vai pra Caruaru? E quanto tá a passagem?'.format(jogador))
time.sleep(1)
print('|---[Funcionario]>|Ah, minha jovem, infelizmente não tem nenhum ônibus direto pra Caruaru não. Você vai ter que pegar um ônibus que vai até Agrestina e de lá seguir pra Caruaru.')
time.sleep(1)
print('|---[Funcionario]>|O preço da passagem é R$:24.00, mas calma minha jovem que de lá para Caruaru fica apenas 10 reais o preço da passagem')
time.sleep(1)
print('Paro e vejo quanto dinheiro eu tenho na mochila')
time.sleep(2)
print('Eu tenho R${},00'.format(dinheiro))
time.sleep(1)
print('|-------[{}]>|Certo, vou comprar uma passagem para Agrestina. Toma aqui o dinheiro, moço.'.format(jogador))
time.sleep(1)
dinheiro=36
print('|---[Funcionario]>|O õnibus só vai sair daqui a 30 minutos.')
time.sleep(1)
print('|-------[{}]>|Sentei na cadeira e comecei a pensar no que fazer durante os próximos 30 minutos. Olhei na bolsa para ver quanto fiquei, só sobrou R$:{},00'.format(jogador,dinheiro))
time.sleep(1)
print('Vejo um gatinho no canto e uma loja de vendas perto de mim')
time.sleep(1)
estação=str(input(vermelho+'|------------>|{} ESCOLHA A LETRA QUE DECIDIR SUA ESCOLHA:(A)-[COMPRAR LANCHES],(B)-[ME APROXIMAR DO GATINHO],(C)-[FICAR SENTADA ESPERANDO O TEMPO PASSAR]:\033[m \033[38;2;179;227;255m'.format(jogador))).strip().lower()[0]
while estação not in 'abc':
    print('Alternativa inexistente!!')
    estação=str(input(vermelho+'|------------>|{} ESCOLHA A LETRA QUE DECIDIR SUA ESCOLHA:(A)-[COMPRAR LANCHES],(B)-[ME APROXIMAR DO GATINHO],(C)-[FICAR SENTADA ESPERANDO O TEMPO PASSAR]:\033[m \033[38;2;179;227;255m'.format(jogador))).strip().lower()[0]
limpar_tela()
if estação=='a':
    lanches='Treloso..R$2:00','Refrigerante..R$3.00','Barra de chocolate..R$7.00'
    print('\033[mCaminho até a loja e vejo quais lanches têm')
    print('Na pratileira tem {}'.format(lanches))
    escolha_lanche=str(input((vermelho+'|------------>|{} ESCOLHA A LETRA QUE DECIDIR SUA ESCOLHA:(A)-[TRELOSO],(B)-[REFRIGERANTE],(C)-[BARRA DE CHOCOLATE]:\033[m \033[38;2;179;227;255m'.format(jogador))).strip().lower()[0])
    while escolha_lanche not in 'abc':
        print('Alternativa inexistente!!')
        escolha_lanche=str(input((vermelho+'|------------>|{} ESCOLHA A LETRA QUE DECIDIR SUA ESCOLHA:(A)-[TRELOSO],(B)-[REFRIGERANTE],(C)-[BARRA DE CHOCOLATE]:\033[m \033[38;2;179;227;255m'.format(jogador))).strip().lower()[0])
    continuar_lanche='lanche'
    if escolha_lanche=='a':
        dinheiro-=2
    if escolha_lanche=='b':
        dinheiro-=3
    if escolha_lanche=='c':
        dinheiro-=7
    while continuar_lanche not in 'n':   
        time.sleep(2)
        print('\033mHum será que compro mais lanches?')
        continuar_lanche=str(input(vermelho+'|------------>|{} ESCOLHA A LETRA QUE DECIDIR SUA ESCOLHA:[S/N]:\033[m \033[38;2;179;227;255m'.format(jogador)).lower().strip()[0])
        if continuar_lanche=='n':
            break
        escolha_lanche=str(input((vermelho+'|------------>|{} ESCOLHA A LETRA QUE DECIDIR SUA ESCOLHA:(A)-[TRELOSO],(B)-[REFRIGERANTE],(C)-[BARRA DE CHOCOLATE]:\033[m \033[38;2;179;227;255m'.format(jogador))).strip().lower()[0])
        if escolha_lanche=='a':
            dinheiro-=2
        if escolha_lanche=='b':
            dinheiro-=3
        if escolha_lanche=='c':
            dinheiro-=7
        print('tenho agora R$:{},00'.format(dinheiro))
        if dinheiro<=0:
            break
    print('O ônibus chegou e logo em seguida eu subi nele')
    time.sleep(1)
    print('Fiquei dormindo o caminho inteiro')
    time.sleep(1)
    print('Fiquei com apenas R$:{},00'.format(dinheiro))
if estação=='b':
    limpar_tela()
    print('\033[mMe aproximo do gatinho, ele é um filhote laranjinha.')
    time.sleep(1)
    print('O gatinho me olha com seus grandes olhos curiosos, demonstrando uma mistura de curiosidade e ternura.')
    time.sleep(1)
    print('Sem hesitar, ele se aproxima de mim e começa a brincar com os cadarços do meu sapato, batendo neles com as patinhas e dando pequenas mordidinhas')
    time.sleep(1)
    print('|---[Funcionario]>|EI, MENINA, POR QUE VOCÊ NÃO LEVA ESSE GATINHO?')
    time.sleep(1)
    print('|---[Funcionario]>|EU O ENCONTREI JOGADO NO LIXO DENTRO DE UMA SACOLA. Às VEZES, FICO ESPANTADO COM A MALDADE HUMANA')
    time.sleep(1)
    gato_escolha=str(input(vermelho+f'|------------>|{jogador} ESCOLHA A LETRA QUE DECIDIR SUA ESCOLHA:(A)-[FICAR COM O GATO],(B)-[NÃO FICAR COM O GATO]:\033[m \033[38;2;179;227;255m')).strip().lower()[0]
    while gato_escolha not in 'ab':
        print('Alternativa inexistente!!')
        gato_escolha=str(input(vermelho+f'|------------>|{jogador} ESCOLHA A LETRA QUE DECIDIR SUA ESCOLHA:(A)-[FICAR COM O GATO],(B)-[NÃO FICAR COM O GATO]:\033[m \033[38;2;179;227;255m')).strip().lower()[0]
    if gato_escolha=='a':
        pet+=1
        gato='gato'
        gato=str(input(vermelho+'DE UM NOME AO SEU GATO: ').strip())
        print('\033[m|-------[{}]>|EU VOU CUIDAR MUITO BEM DE VOCê {} VOCÊ É MEU TESOURO'.format(gato))
        time.sleep(1)
        print('O ônibus chegou e logo em seguida eu subi nele')
        time.sleep(1)
        print('Fiquei brincando o caminho todo com o {}, depois dormir e deixei ele brincando debaixo da minha cadeira'.format(gato))
        time.sleep(1)
        print('O ônibus finalmente chegou em Agrestina.','  "Já está de noite..."')
        time.sleep(2)
    if gato_escolha=='b':
        print('\033[mDeixo o gatinho lá e deixo a sorte decidir seu destino.','Enquanto caminho para longe, vejo-o chamando-me ao longe')
        time.sleep(1)
        print('O ônibus chegou e logo em seguida eu subi nele')
        time.sleep(1)
        print('Fiquei dormindo o caminho inteiro')
        time.sleep(1)
        print('O ônibus finalmente chegou em Agrestina.','  "Já está de noite..."')
        time.sleep(2)
if estação=='c':
    print('\033[mPermaneço sentada até o ônibus chegar')
    time.sleep(1)
    print('O ônibus chegou e logo em seguida eu subi nele')
    time.sleep(1)
    print('Fiquei dormindo o caminho inteiro')
    time.sleep(1)
    print('O ônibus finalmente chegou em Agrestina.','  "Já está de noite..."')
    time.sleep(2)
#Quase final
limpar_tela()
pygame.mixer.music.load('C:/Users/Luciano_cleberton/Documents/Python-game-/musica/noite.mp3')
pygame.mixer.music.play(loops=-1)
print('\033[mSinto muito sono, mas vou perguntar quando sai o ônibus que vai para Caruaru.')
time.sleep(1)
print('Mas antes de ir, vou dar uma olhada na minha bolsa para ver quanto tenho, eu tenho R$:{},00'.format(dinheiro))
time.sleep(1)
print('Caminhei até o guichê')
time.sleep(1)
print('Vejo o moço jogando uma sacola no lixo que aparenta ter algo pequeno se mexendo.')
time.sleep(1)
print('|-------[{}]>|Moço, que horas sai o ônibus? E quanto custa a passagem para Caruaru?'.format(jogador))
time.sleep(2)
print('|---[Funcionário]>|Garota, o ônibus só vai sair ás 7h da manhâ e a passagem custará R$:15,00. A passagem aumentou. Você vai querer uma?')
time.sleep(1)
if dinheiro>=15:
    print('Vou querer sim')
    dinheiro-=15
    print('Fiquei só com R$:{}.00'.format(dinheiro))
    time.sleep(1)
    print('Ser eu tivesse mais dinheiro, poderia dormir em algum lugarzinho')
    time.sleep(1)
    print('Vou ter que dormir no banco da rodoviária, estou com medo e com frio....')
    time.sleep(1)
    if pet>=1:
        print('Pelo menos eu tenho o {} para me fazer companhia'.format(gato))
        time.sleep(1)
        print('Logo pego no sono. Quando acordo, não vejo mais o {} '.format(gato))
        time.sleep(1)
        print('Procurei, procurei e não achei. O õnibus estava vindo e eu precisava subir')
        time.sleep(1)
        print('Subo chorando e me odiando por não ter conseguido encontrá-lo e ter que deixá-lo. Torço para que ele esteja bem.')
        time.sleep(1)
    if pet<=1:
        print('Vou dormir aqui sozinha. Tomara que nada aconteça')
        time.sleep(1)
        print("Acordo com um homem estranho me olhando, e ele aparenta estar fazendo algo, mas não consigo ver o que é",'  "O mais estranho é que ele parece o funcionário que me atendeu')
        time.sleep(1)
        print('Corro chorando, com coração disparado, e caminho até encontra um canto para dormir perto do lixo. Pelo menos aqui sei que nenhum estranho viria.')
        time.sleep(1)
        print('O dia amanhece e subo no ônibus para Caruaru.')
if dinheiro<15:
    print('Fico desesperada não tenho dinheiro para ir e nem para voltar')
    time.sleep(1)
    print('Me pego chorando e pensando em como vou fazer para conseguir dinheiro')
    time.sleep(1)
    print('Penso em um jeito de ganhar dinheiro. Vou cantar e dançar para as pessoas que passarem e me darem dinheiro.')
    time.sleep(1)
    print('Começo a dançar e cantar, logo as pessoas jogam algumas moedas e param para admirar.')
    time.sleep(1)
    print('Uma senhorita caminha até mim')
    time.sleep(1)
    print('|---[Senhorita]>|GAROTA, VOCÊ TEM TALENTO! SUA VOZ É LINDA E VOCÊ TEM JEITO PARA DANÇA')
    time.sleep(1)
    print('|---[Senhorita]>|MENINA, CADÊ SEUS PAIS? QUERO FALAR COM ELES. QUERO TER DAR UMA GRANDE OPORTUNIDADE.')
    time.sleep(1)
    print('Conto toda minha história e ela me olha com um olhar triste e preocupado.')
    time.sleep(1)
    print('|---[Senhorita]>|ME CHAMO ALICE RAMOS DRUMNOND, SOU UMA AGENTE ARTÍSTICA.')
    time.sleep(1) 
    print('|---[ALICE]>|MENINA, VENHA COMIGO.É PERIGOSO FICAR POR AQUI À NOITE. VOU CUIDAR DE VOCÊ E TE LEVAR ATÉ SEU PAI AMANHÃ. VOU TE DAR UMA OPORTUNIDADE DE MELHORAR DE VIDA')
    time.sleep(1)
    destino=str(input(vermelho+'|------------>|{} ESCOLHA A LETRA QUE DECIDIR SUA ESCOLHA:(A)-[IR COM A MOÇA], (B)-[NÃO IR COM A MOÇA]:\033[ \033[38;2;179;227;255m')).strip().lower()[0]
    while destino not in 'ab':
        print('Alternativa inexistente!!')
        destino=str(input(vermelho+'|------------>|{} ESCOLHA A LETRA QUE DECIDIR SUA ESCOLHA:(A)-[IR COM A MOÇA], (B)-[NÃO IR COM A MOÇA]:\033[ \033[38;2;179;227;255m')).strip().lower()[0]
    limpar_tela()
    time.sleep(1)
    if destino=='a':
        print(f'''---------------------------------------------------------------------------------------------------------------------------------------------------
=-=-=-=-=-=-=-|===============================================================================================================|-=-=-=-=-=--=-=-=-=-=-=-=-=-=-=-=-=
=-=-=-=-=-=-=-|"{jogador} Foi com a Alice que a ajudou a encontra seu pai. Ela descobriu a verdade.                           |-=-=-=-=-=--=-=-=-=-=-=-=-=-=-=-=-=
=-=-=-=-=-=-=-|Seu pai nunca foi seu pai, ele era chefe de um grupo de tranficantes de mulheres e crianças                    |-=-=-=-=-=-=-=-=-=-=-=-=---=-=--=-=
=-=-=-=-=-=-=-|O endereço escrito na carta era uma armadilha onde planejavam prender e força {jogador}                        |-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=--=-=
=-=-=-=-=-=-=-|A prostituição infartil. Eles prometiam um futuro incrível para as meninas jovens, e após elas irem com eles   |-=-=-=-=-=-=-=--=-==-=-=-=-=-=-=-==
=-=-=-=-=-=-=-|Para fugir da pobreza, acabavam presas em lugares como esse, onde eram forçadas a dançar e ser prostituirem    |-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-==                                                                                                      |-=-=-=-=-=--=-=-=-=-=-=-=-=-=-=-=-=
=-=-=-=-=-=-=-|Alice e {jogador} denunciaram e salvaram mais de 15 mulheres e 5 meninas das mãos de Sebastião                 |-=-=-=-=-=-=-=-=-=-=-=-=--=-=-=-=-=
=-=-=-=-=-=-=-|A {jogador}, com ajuda de Alice, se tornou uma cantora famosa e com o dinheiro que ganhou                      |-=-=-=-=-=-=-=-=-=-=-=--=-=-=-=-=-=
=-=-=-=-=-=-=-|deu uma vida melhor para sua mãe e auxilio o combate contra a prostituição infatil, salvando muitas crinças de |-=-=-=-=-==-=-=-=-=-=-=-=-=-=-=--==
=-=-=-=-=-=-=-|um destino cruel.                                                                                              |-=-=-=-=-=--=-=-=-=-=-=-=-=-=-=-=-=
=-=-=-=-=-=-=-|===============================================================================================================|-=-=-=-=-=--=-=-=-=-=-=-=-=-=-=-=-=''')
        print('\033[0;33m"Parabéns {} ! Você conquistou o final Heroico."\033[m'.format(jogador))
        time.sleep(12)
        exit()
    if destino=='b':
        print(f'''---------------------------------------------------------------------------------------------------------------------------------------------------
=-=-=-=-=-=-=-|===============================================================================================================|-=-=-=-=-=--=-=-=-=-=-=-=-=-=-=-=-=
=-=-=-=-=-=-=-|"{jogador} não foi com Alice, pois achou suspeito ir com uma estranha. Continuou a cantar e dançar, mas não    |-=-=-=-=-=--=-=-=-=-=-=-=-=-=-=-=-=
=-=-=-=-=-=-=-|conseguiu reunir o dinheiro necessário e caminhou pelas ruas de Agrestina em busca de dinheiro.                |-=-=-=-=-=-=-=-=-=-=-=-=---=-=--=-=
=-=-=-=-=-=-=-|{jogador} desapareceu e nunca tiveram notíciais da menina. Alguns dizem que virou moradora de rua, outros dizem|-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=--=-=
=-=-=-=-=-=-=-|que a menina encontrou o pai e sumiu do mundo com ele.                                                         |-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-==
=-=-=-=-=-=-=-|===============================================================================================================|-=-=-=-=-=--=-=-=-=-=-=-=-=-=-=-=-=''')
        print('\033[0;33m! Você conquistou o final Triste pesadelo."\033[m')
        time.sleep(10)
        exit()
limpar_tela()
#final
pygame.mixer.music.load('C:/Users/Luciano_cleberton/Documents/Python-game-/musica/final.mp3')
pygame.mixer.music.play(loops=-1)
print('Cheguei de tarde em Caruaru')
time.sleep(1)
print('Sentei no banco da rodoviária e pensei em tudo o que me aconteceu e como foi difícil chegar ali.')
time.sleep(1)
print('Senti saudades de casa, saudades da minha mãe mesmo ela sendo brava.')
time.sleep(1)
print('Saudades da minha cama quentinha e dos gritos da minha mãe me pedindo para levantar.')
time.sleep(1)
print('Mas já estou aqui, irei encontrar meu pai, e as coisas vão melhorar. Finalmente vou conhecer ele, e ele vai me amar e me ajudar.')
time.sleep(1)
print('Vai ser aqui que vou realizar meus sonhos.')
time.sleep(1)
print('Vou perguntando às pessoas onde fica a Avenida das Flores.')
time.sleep(1)
print('Chegando lá me deparo com varias casas')
time.sleep(1)
print('|---[{}]>|LEMBRO QUE ERA UMA CASA QUE COMEÇAVA COM O NÚMERO 14. O ULTIMO NÚMERO, NÃO ESTOU LEMBRADO.'.format(jogador))
time.sleep(1)
casa=str(input(vermelho+'Digite o número de 3 dígitos da casa para onde gostaria de ir:\033[m \033[38;2;179;227;255m')).strip()
time.sleep(1)
while casa !=145:
    print('\033[mCasa errada!')
    time.sleep(1)
    casa=str(input(vermelho+'Digite o número de 3 dígitos da casa para onde gostaria de ir:\033[m \033[38;2;179;227;255m')).strip()
limpar_tela()
print('\033[mVejo uma menina que aparenta ter uns 10 anos na frente da casa.')
time.sleep(1)
print('|----[{}]>|EI MENINA ESSA É A CASA 145?'.format(jogador))
time.sleep(1)
print('|----[menina]HUM, MEU CHEFE FALOU QUE NÃO ERA BOM EU FALAR COM ESTRANHOS SEM A PERMISSÃO DELE')
time.sleep(1)
print('|----[{}]>|O PIRRALHA ME DIGA SE ESSA É A CASA 145 E EU TE COMPRO UM DOCE DEPOIS.'.format(jogador))
time.sleep(1)
print('|----[menina]>|Hummmm, ELE FALOU QUE EU NÃO PODIA FALAR COM ESTRANHOS, MAS VOU CONVERSAR COM O VENTO. EI, VENTO, ESSA É A CASA 145')
time.sleep(1)
print('|----[{}]>|QUAL É O SEU NOME, MENINA?'.format(jogador))
time.sleep(1)
print('|----[menina]>|MEU NOME É MENINA, MAS MEU CHEFE DISSE QUE DAQUI A UMAS SEMANAS VOU RECEBER UM NOME, COMO MINHA MÃE TINHA QUANDO SUMIU COM O MOÇO ESTRELA.')
time.sleep(1)
print(f'|----[{jogador}]>|COMO ASSIM MOÇO ESTRELA?', '  "acho estranho tudo que essa menina está falando')
time.sleep(1)
print('|----[menina]>|É O MOÇO COM CABELOS LOIROS E FALA ESTRANHO. MEU CHEFE DISSE QUE ELE FALA UM TAL DE  INGLÊS') 
time.sleep(1)
print('|----[menina]>|E QUE LEVAVA AS MELHORES DANÇARINAS PARA VIAJAREM PARA FORA E SE TORNAREM FAMOSAS.')
time.sleep(8)
limpar_tela()
print('Quando vou fazer mais perguntas, aparece um senhor com barba grande, dentes amarelados, roupas desgatadas e com cheiro de bebida e cigarro.')
time.sleep(1)
print('|----[desconhecido]>|Opa, quem é você, linda moça? Você se perdeu da sua família? Vem com o tio que vou te ajudar.')
time.sleep(1)
print('|----[{}]>|SOU FILHA DE MARIA. VIM AQUI PORQUE ACHEI A CARTA QUE MEU PAI ME MANDOU. O NOME DELE É...'.format(jogador))
time.sleep(1)
print('|----[SEBASTIÃO]>|O NOME DELE É SEBASTIÃO. OPA, MENINA, VOCÊ É MEU TESOURO PRECIOSO QUE INFELIZMENTE TINHA ESCAPADO DO MEU GRANDE AMOR.')
time.sleep(1)
print('Meu coração quebra por dentro ao perceber que tudo que eu imaginei, um pai bondoso, cheiroso, e rico, se quebrou ao ver esse homem.')
time.sleep(5)
limpar_tela()
print('|----[SEBASTIÃO]>|ENTRE, FILHA, VOU TE MOSTRA A CASA.')
time.sleep(1)
print('A casa era muito grande e tinhas vários quartos. Cada quarto tinha 2 a 3 meninas e mulheres, e homens velhos que acho que eram os pais delas, pois viviam abraçado com todas')
time.sleep(1)
print('|----[SEBASTIÃO]>|MENINA, SUA MÃE TINHA UM GRANDE TALENTO PARA DANÇA. MESMO QUE DANÇASSE ATÉ LÁGRIMAS CAÍREM DE TANTA FELICIDADE, TODAS AS PESSOAS FICAVAM IMPRESSIONADAS.')
time.sleep(1)
print('"Ele diz isso enquanto mostra um sorriso amalerado."')
time.sleep(1)
print('|----[SEBASTIÃO]>|VOCÊ TAMBÉM DANÇA, MINHA PRECIOSA?')
time.sleep(1)
print('|----[{}]>|SIM, EU DANÇO E CANTO. PAI, SEMPRE QUIS TE CONHECER E QUERIA TE MOSTRAR QUE SEI DANÇAR E CANTAR, E QUE UM DIA SEREI UMA ESTRELA.'.format(jogador))
time.sleep(1)
print('|----[SEBASTIÃO]>|QUE MARAVILHOSO, DOCINHO! EU TENHO UM PALCO GIGANTE ONDE VÁRIAS PESSOAS VÊM TODAS AS NOITES.')
time.sleep(1)
print('|----[SEBASTIÃO]>|TENHO VÁRIAS ESTRELAS, E ELES VÃO À LOUCURA QUANDO CHEGA UMA ESTRELA NOVA. E SEI QUE VOCÊ TERÁ MUITO FANS COMO SUA MÃE TEVE.')
time.sleep(1)
print('Algo dentro de mim me diz que não devo ficar aqui, e que meus sonhos aqui virariam pesadelos')
time.sleep(1)
print('|----[SEBASTIÃO]>|FILHA, TEREI QUE ARRUMAR O PALCO PARA O SHOW DESTA NOITE. VOCÊ PODE FICAR NESTE QUARTO. EU LOGO VOLTO. PROMETO QUE HOJE SEUS SONHOS IRÃO SE REALIZAR DE SER UMA ESTRELA!')
limpar_tela()
time.sleep(7)
print('ele vai embora e eu fico sozinha com uma menina de cabelos loiros e olhos claros ela parece ter 15 anos')
time.sleep(1)
print('|----[GAROTA]>|EI, MENINA, FUJA DAQUI. AQUI NÃO É LUGAR DE REALIZAR SONHOS.')
time.sleep(1)
print('|----[GAROTA]>|EU ME CHAMO KRIS E HOJE EM DIA ELES ME CHAMAM  DE DANÇARINA DE FOGO, DO MESMO JEITO QUE ELE CHAMA AS OUTRAS VÍTIMAS.')
time.sleep(1)
print('|----[KRIS]>|FUJA E ENCONTRE AJUDA PARA A GENTE, POR FAVOR. EU JÁ PEDI AJUDA PARA FUGIR, MAS AS OUTRAS MENINAS TÊM OLHOS MORTOS, COMO SE NÃO ESTIVESSEM MAIS AQUI.')
time.sleep(1)
print('|----[KRIS]>|AGORA É O MELHOR MOMENTO PARA FUGIR. O PATRÃO VAI REUNIR VELHOS NOJENTOS PARA O ESPERTÁCULOS , E OS HOMENS QUE GUARDAM O PRÉDIO VÃO ESTAR OCUPADOS.')
time.sleep(1)
print('|----[KRIS]>|EU FAÇO UMA GRITARIA AQUI DENTRO E VOCÊ FOGE BUSCANDO AJUDA. POR FAVOR, TIRE A GENTE DESSE INFERNO.')
time.sleep(1)
print('Eu fico assustada com tudo que a menina está falando. Ela parece estar um pouco louca. Não sei em quem acreditar, não sei o que está acontecendo. Eu só quero minha mãe.')
time.sleep(1)
fim=str(input(vermelho+'|------------>|{} ESCOLHA A LETRA QUE DECIDIR SUA ESCOLHA:(A)-[FUGIR], (B)-[FICAR]:\033[m \033[38;2;179;227;255m')).strip().lower()[0] 
while fim not in 'ab':
    print('Alternativa inexistente!!')
    fim=str(input(vermelho+'|------------>|{} ESCOLHA A LETRA QUE DECIDIR SUA ESCOLHA:(A)-[FUGIR], (B)-[FICAR]:\033[m \033[38;2;179;227;255m')).strip().lower()[0] 
if fim=='a':
    print('\033[m|----[{}]>|Certo Kris iremos fugir')
    time.sleep(1)
    print('Kris começa a gritaria no meio da confusão. Saio correndo pela porta quando estou já algumas casas de distancia um barulho ecoaa.')
    time.sleep(1)
    print('Pewwwww.... um barulho de um tiro.')
    time.sleep(1)
    print('Continuo correndo, com lágrimas descendo pelos meus olhos.')
    time.sleep(1)
    print(f'''---------------------------------------------------------------------------------------------------------------------------------------------------
=-=-=-=-=-=-=-|====================================================================================================================|-=-=-=-=-=--=-=-=-=-=-=-=-=-=-=-=-=
=-=-=-=-=-=-=-|"{jogador} conseguiu fugir e buscar ajuda. Chegando lá, viaturas cercaram o local e 5 homens foram presos.          |-=-=-=-=-=--=-=-=-=-=-=-=-=-=-=-=-=
=-=-=-=-=-=-=-|Entre eles, um era o Sebastião, que alegou que {jogador} não era filha dele, mas sim apenas de um dos seus clientes |-=-=-=-=-=-=-=-=-=-=-=-=---=-=--=-=
=-=-=-=-=-=-=-|O caso chocou o Nordeste inteiro. {jogador} foi chamada para dar entrevistas e descobriram seu talento para dança.  |-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=--=-=
=-=-=-=-=-=-=-|E canto. A pequena garota, junto com sua mãe, fez sucesso na música e apoiaram projetos que combatia                |-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-==
=-=-=-=-=-=--=|a prostituição infantil. Nas entrevista, o que mais entristece {jogador} é que não pôde salvar sua heroína.         |-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-==
=-=-=-=-=-=-=-|O corpo de Kris FOI ENCONTRADO PELA POLÍCIA AO CHEGAR NO LOCAL.                                                     |-=-=-=-=-=-=-=-=-=-=-=-=--=-=-=-=-=
=-=-=-=-=-=-=-|====================================================================================================================|-=-=-=-=-=--=-=-=-=-=-=-=-=-=-=-=-=''')
    time.sleep(1)
    print('\033[0;33m! Você conquistou o final [verdade-heroica]."\033[m')
    time.sleep(8)
if fim=='b':
    print('Fico com medo e decido ficar. Kris começa a chorar e eu não consigo entender.')
    print(f'''---------------------------------------------------------------------------------------------------------------------------------------------------
=-=-=-=-=-=-=-|======================================================================================================================|-=-=-=-=-=--=-=-=-=-=-=-=-=-=-=-=-=
=-=-=-=-=-=-=-|"{jogador} não fugiu e acabou descobrindo a cruel realidade daquele lugar. À noite, todos os seus sonhos ser quebrarao|-=-=-=-=-=--=-=-=-=-=-=-=-=-=-=-=-=
=-=-=-=-=-=-=-|Ela ser tornou mais uma de inúmeras vítimas e nunca mais houve notícias da menina.                                    |-=-=-=-=-=-=-=-=-=-=-=-=---=-=-=-=
=-=-=-=-=-=-=-|======================================================================================================================|-=-=-=-=-=--=-=-=-=-=-=-=-=-=-=-=-=''')
    time.sleep(1)
    print('\033[0;33m! Você conquistou o final [DESTINO CRUEL]."\033[m')
    time.sleep(10)

print('=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-[Fim]=-=-=-=-=-=-=-=-=-=-==-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=--=-===-')
print('''
      É verdade, a violência sexual contra menores de idade é uma questão séria e preocupante no Brasil, 
      e os casos têm aumentado ao longo dos anos. A história narrada reflete a triste realidade de algumas crianças que são vítimas desse tipo de crime. 
      É importante conscientizar a sociedade sobre esse problema e promover medidas eficazes de prevenção e combate à violência sexual infantil. 
      O apoio às vítimas e o fortalecimento das políticas públicas são fundamentais para enfrentar essa situação e garantir a proteção dos direitos das crianças.
''')
exit()