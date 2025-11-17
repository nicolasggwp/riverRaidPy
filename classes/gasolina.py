import random, pygame
from caem import Caem

class Gasolina(Caem): 
    def __init__(self, dims, pos, velY):
        sprite_gasolina = "sprites/combustivel.png" 
        super().__init__(sprite_gasolina, dims, pos, velY)        

        self.combustivel = 100

        self.coletada = False

    def gera_gasolina(mapa):

        lista_gasolina = []  
        quantidade_gasolina = 0
        
        while quantidade_gasolina < 3:  
            x = random.randint(0, 800)  
            y = random.randint(-32, -800)
            
            teste_gasolina = Gasolina((31, 64), (x, y), 3)
            
            if not teste_gasolina.colisaoMask(mapa):
                lista_gasolina.append(teste_gasolina)
                quantidade_gasolina += 1
        return lista_gasolina