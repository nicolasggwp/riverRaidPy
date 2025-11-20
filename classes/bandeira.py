import pygame

class Bandeira_animação(pygame.sprite.Sprite):
    def __init__(self, pos_anim_x, pos_anim_y):
        super().__init__()
        self.bandeiras = [
            pygame.image.load("sprites/animação/bandeira/bandeira_0.png"),
            pygame.image.load("sprites/animação/bandeira/bandeira_1.png"),
            pygame.image.load("sprites/animação/bandeira/bandeira_2.png"),
            pygame.image.load("sprites/animação/bandeira/bandeira_3.png"),
            pygame.image.load("sprites/animação/bandeira/bandeira_4.png"),
            pygame.image.load("sprites/animação/bandeira/bandeira_3.png"),
            pygame.image.load("sprites/animação/bandeira/bandeira_2.png"),
            pygame.image.load("sprites/animação/bandeira/bandeira_1.png")
        ]
        self.imagem_inicial = 0
        self.animado = self.bandeiras[self.imagem_inicial]

        self.rect = self.animado.get_rect()
        self.rect.topleft = [pos_anim_x, pos_anim_y]

    def printa_bandeira(self, velocidade):
        
        self.imagem_inicial += velocidade
        
        if self.imagem_inicial >= len(self.bandeiras):
            self.imagem_inicial = 0
        self.animado = self.bandeiras[int(self.imagem_inicial)]
        self.image = self.animado