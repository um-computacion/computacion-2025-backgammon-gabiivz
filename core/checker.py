class Checker:
    def __init__(self, ficha, color, jugador):
        self.__ficha__ = ficha
        self.__color__ = color
        self.__jugador__ = jugador
    
    def get_ficha(self):
        return self.__ficha__

    def get_color_y_jugador(self):
        return (self.__color__, self.__jugador__)
    

        
#ficha