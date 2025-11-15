import pygame, random, sys, time
from classes.aviao import Aviao
from classes.helic import *
from classes.helicopter_tela import Helicoptero_tela
from classes.bandeira import Bandeira_animação
from classes.nuvem_tela import Nuvens_tela

pygame.init() 
largurat = 800
alturat = 600

gameDisplay = pygame.display.set_mode((largurat, alturat))
pygame.display.set_caption('aviãozinho explode tudo') 
tempo = pygame.time.Clock() 

player = Aviao()

helic_list = []

balas = []
reload_time = 0.25
lastShot = 0

helicopteros = pygame.sprite.Group()
posicoes = []

def gera_heli_tela(qnt):
    for i in range(qnt):
        posicoes.append([-1*random.randint(0, 1000), random.randint(0, 500)])
    for x, y in posicoes:
        helicopteros.add(Helicoptero_tela(x, y))

def gera_nuvem(qnt):
    imagens_nuvem = Nuvens_tela.gera_nuvem_tela()
    nuvens = []
    for i in range(qnt):
        imagem, rect = random.choice(imagens_nuvem)
        nuvens.append((imagem, rect))
    return nuvens

def telainicial():
    bandeira_x = 500
    bandeira_y = 100

    gera_heli_tela(5)
    nuvem = gera_nuvem(7)

    bandeira = Bandeira_animação(bandeira_x, bandeira_y)
    movimento_bandeira = pygame.sprite.Group(bandeira)

    while True:
        tempo.tick(30)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_u:
                    return
        gameDisplay.fill("royalblue4")
   
        #=======Nuvens====== 
        for imagem, rect in nuvem:
            rect.x += 2
            if rect.x >= 800:
                nuvem.remove((imagem, rect))
                novas = gera_nuvem(1)
                nuvem.append(novas[0])

            gameDisplay.blit(imagem, (rect.x, rect.y))
       
        
        #=======Helicopteros======
        for heli in helicopteros:
            
            heli.printa_helicoptero(0.2)
            size = heli.image.get_width()
            if size <= 42:
                heli.rect.x += 2
            elif size <= 52:
                heli.rect.x += 4
            else:
                heli.rect.x += 6
        helicopteros.draw(gameDisplay)
        if heli.rect.x >= 800:
                helicopteros.remove(heli)
                gera_heli_tela(1)
        #=======Bandeira======
        if bandeira_x <= 50:
            bandeira_x = 50
        else:
            bandeira_x -= 4
        bandeira.rect.x = bandeira_x
        bandeira.printa_bandeira(0.1)
        movimento_bandeira.draw(gameDisplay)

        pygame.display.update()

telainicial()

while True:

    for evento in pygame.event.get():
       if evento.type == pygame.QUIT:
           sys.exit()

    gameDisplay.fill("royalblue4")
    tempo.tick(30)

    tecla = pygame.key.get_pressed()

    player.imprimir()
    player.movPlayer(tecla)

    #gerar bala
    if tecla[pygame.K_SPACE] and (time.time() - lastShot) >= reload_time:
        balas.append(player.atirar())
        lastShot = time.time()

    if random.randint(0,100) > 1:
        helic_list.append(gerarhelic())
    
    #imprime as entidades em vetores
    for bala in balas:
        bala.imprimir()
        bala.movTiro()
        if bala.y < -32:
            balas.remove(bala)
    
    for helic in helic_list:
        helic.imprimir()
        helic.movHoriz()
        helic.queda(tecla)
        if helic.y < -32:
            helic_list.remove(helic)

    pygame.display.update()