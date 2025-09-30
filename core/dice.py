import random

#defino dado 1 y 2

class Dice:
    def __init__(self):
        self.__dado1__ = 0
        self.__dado2__ = 0
        self.movimientos = []
#defino metodo tirar que devuelve dos numeros random entre 1 y 6

    def tirar(self):
        self.dado1 = random.randint(1,6)
        self.dado2 = random.randint(1,6)
        if self.dado1 == self.dado2:
            self.movimientos = [self.dado1] * 4
        else:
            self.movimientos = [self.dado1, self.dado2]
        return self.dado1, self.dado2

#defino movimientos como la suma de los dos dados
 
    def usar_dado(self, valor):
        """Remueve un dado usado de los movimientos disponibles."""
        if valor in self.movimientos:
            self.movimientos.remove(valor)
        else:
            raise ValueError(f"El dado {valor} no está disponible.")
    
    def tiene_movimientos(self):
        """Verifica si quedan dados disponibles."""
        return len(self.movimientos) > 0
    
    def reiniciar_dados(self):
        self.__dado1__ = 0
        self.__dado2__ = 0
        self.movimientos = []
        return self.__dado1__, self.__dado2__

    
    
    



    