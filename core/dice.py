import random

class Dice:
    def __init__(self):
        """Inicializa los dados y la lista de movimientos."""
        self.__dado1__ = 0
        self.__dado2__ = 0
        self.__movimientos__ = [] 

    def tirar(self):
        """
        Simula la tirada de dos dados, actualiza la lista de movimientos
        (manejando dobles) y devuelve los valores como una tupla.
        """
        self.__dado1__ = random.randint(1, 6) 
        self.__dado2__ = random.randint(1, 6) 

        if self.__dado1__ == self.__dado2__:
            self.__movimientos__ = [self.__dado1__] * 4
        else:
            self.__movimientos__ = [self.__dado1__, self.__dado2__]

        return self.__dado1__, self.__dado2__

    def get_movimientos(self):
        """Devuelve la lista de movimientos de dados disponibles."""
        return self.__movimientos__

    def tiene_movimientos(self):
        """Verifica si quedan movimientos de dados disponibles."""
        return len(self.__movimientos__) > 0

    def reiniciar_dados(self):
        """Reinicia los valores de los dados y la lista de movimientos."""
        self.__dado1__ = 0
        self.__dado2__ = 0
        self.__movimientos__ = []
        return self.__dado1__, self.__dado2__
    
    
    



    