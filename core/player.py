class Player:
    def __init__(self, nombre, color):
        self.__nombre__= nombre
        self.__color__= color
    
    def __str__(self):
        return f"Jugador: {self.__nombre__}, Color: {self.__color__}"
    # definiendo nombre y ficha(color) de jugador
    def get_nombre(self):
        return self.__nombre__
    
    def get_color(self):
        return self.__color__


        
    


        
    