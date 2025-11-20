import random
from classes.inimigos import Inimigos

class Helic(Inimigos):
    def __init__ (self, pos, velY, direcao):
        sprite = "sprites/helic/helic1.png"
        dims = (40,40) 
        velx = random.randint(3,10)
        super().__init__(sprite, dims, pos, velY, direcao, velx)

def gerarhelic(dific):
    return Helic((random.randint(0, 800-32), -1*random.randint(0,500)), random.randint(2,dific), random.randint(0,1))


