import random

#defino dado 1 y 2

class Dice:
    def __init__(self):
        self.__dado1__ = 0
        self.__dado2__ = 0

#defino metodo tirar que devuelve dos numeros random entre 1 y 6

    def tirar(self):
        self.dado1 = random.randint(1,6)
        self.dado2 = random.randint(1,6)
        return self.dado1, self.dado2


#defino movimientos como la suma de los dos dados
 
    def movimientos(self):
        if self.dado1 == self.dado2:
            return [self.dado1]*4
        else:
            return [self.dado1, self.dado2]

    
    
    



    