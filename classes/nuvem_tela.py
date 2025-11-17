import pygame, random

class Nuvens_tela():
    def gera_nuvem_tela():
        caminhos = [
            "sprites/animação/nuvens/nuvem_0.png",
            "sprites/animação/nuvens/nuvem_1.png",
            "sprites/animação/nuvens/nuvem_2.png",
            "sprites/animação/nuvens/nuvem_3.png"
        ]
        nuvens = []
        for n in caminhos:
            imagem = pygame.image.load(n)
            imagem = pygame.transform.scale(imagem, (400, 200))

            rect = imagem.get_rect()
            rect.x = random.randint(0, 1000)*(-1)
            rect.y = random.randint(0, 500)

            nuvens.append((imagem, rect))
        return nuvens