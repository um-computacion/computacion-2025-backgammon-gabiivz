import random

#defino dado 1 y 2

class Dice:
    def __init__(self):
        self.__dado1__ = 0
        self.__dado2__ = 0
        self.__movimientos__ = [] 

    def tirar(self):
        self.__dado1__ = random.randint(1, 6) 
        self.__dado2__ = random.randint(1, 6) 

        if self.__dado1__ == self.__dado2__:
            self.__movimientos__ = [self.__dado1__] * 4
        else:
            self.__movimientos__ = [self.__dado1__, self.__dado2__]

        return self.__dado1__, self.__dado2__

    def get_movimientos(self):
        return self.__movimientos__

    def tiene_movimientos(self):
        return len(self.__movimientos__) > 0

    def reiniciar_dados(self):
        self.__dado1__ = 0
        self.__dado2__ = 0
        self.__movimientos__ = []
        return self.__dado1__, self.__dado2__

    
    
    



    