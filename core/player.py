class Player:
    """Clase que representa a un jugador en el juego de Backgammon."""
    def __init__(self, nombre, color):
        """Inicializa un jugador con su nombre y color."""
        self.__nombre__= nombre
        self.__color__= color
    
    def __str__(self):
        """Devuelve una representación en string del jugador."""
        return f"Jugador: {self.__nombre__}, Color: {self.__color__}"
    
    def get_nombre(self):
        """Devuelve el nombre del jugador."""
        return self.__nombre__
    
    def get_color(self):
        """Devuelve el color del jugador ('Blancas' o 'Negras')."""
        return self.__color__