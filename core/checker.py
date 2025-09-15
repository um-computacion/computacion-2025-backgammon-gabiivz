class Checker:
    def __init__(self, ficha, color, posicion, jugador):
        self.__checker__ = ficha
        self.__color__ = color
        self.__jugador__ = jugador
        self.__posicion__ = posicion
    
    def get_ficha(self):
        return self.__checker__

    def get_color_y_jugador(self):
        return (self.__color__, self.__jugador__)
    
    def get_posicion(self):
        return self.__posicion__


        
#ficha