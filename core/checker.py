class Checker:
    def __init__(self, ficha, color, jugador):
        self.__ficha__ = ficha
        self.__color__ = color
        self.__jugador__ = jugador
        self.__fichas_sacadas__ = []  # Lista para fichas retiradas
    
    def get_ficha(self):
        return self.__ficha__

    def get_color_y_jugador(self):
        return (self.__color__, self.__jugador__)
    
    def get_fichas_sacadas_blancas(self):
        fichas_blancas = []
        for ficha in self.__fichas_sacadas__:
            if ficha == "Blancas":
                fichas_blancas.append(ficha)
        return fichas_blancas
    
    def get_fichas_sacadas_negras(self):
        fichas_negras = []
        for ficha in self.__fichas_sacadas__:
            if ficha == "Negras":
                fichas_negras.append(ficha)
        return fichas_negras


    def agregar_ficha_sacada_blancas(self, ficha):
        if ficha == "Blancas":
            self.__fichas_sacadas__.append(ficha)
        else:
            raise ValueError("Solo se pueden agregar fichas blancas.")
    def agregar_ficha_sacada_negras(self, ficha):
        if ficha == "Negras":
            self.__fichas_sacadas__.append(ficha)
        else:
            raise ValueError("Solo se pueden agregar fichas negras.")
    

        
#ficha