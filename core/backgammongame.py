from core.board import Board
from core.dice import Dice
from core.player import Player
from core.checker import Checker

class BackgammonGame:
    def __init__(self, nombre_blancas, nombre_negras):
        self.__board__ = Board()
        self.__turno__ = "Blancas"
        self.__dado__ = Dice()
        self.__jugador_blancas__ = Player(nombre_blancas, "Blancas")
        self.__jugador_negras__ = Player(nombre_negras, "Negras")
        self.__fichas_blancas__ = Checker("Blancas", "Blancas", self.__jugador_blancas__)
        self.__fichas_negras__ = Checker("Negras", "Negras", self.__jugador_negras__)

    def get_board(self):
        return self.__board__

    def get_jugador_blancas(self):
        return self.__jugador_blancas__
    
    def get_jugador_negras(self):
        return self.__jugador_negras__
    
    def get_jugador_actual(self):
        if self.__turno__ == "Blancas":
            return self.__jugador_blancas__
        else:
            return self.__jugador_negras__
    
    def get_turno(self):
        return self.__turno__
    
    def cambio_turnos(self):   #creo que hay una regla agregar despues con excepcion y cuando ya haya sacado todas las fichas cambia
        if self.__turno__ == "Blancas":
            self.__turno__ = "Negras"
        else:
            self.__turno__ = "Blancas"
    def tirar_dados(self):   #faltaria lo de sumar los dados
        return self.__dado__.tirar
    
    def get_dados(self):
        return self.__dado__.movimientos
    
    def mover_ficha(self, origen, destino):
        origen = int(origen)
        destino = int(destino)
    # Validar si hay fichas en el bar
        if len(self.__board__.get_bar()) > 0:
            raise ValueError("No puedes mover fichas porque tenés fichas en el bar.")
        ficha = self.__board__.get_posicion(origen)
    # Validar que hay una ficha en la posición origen
        if not ficha:
            raise ValueError("No hay ficha en la posición de origen.")
    # Calcular el movimiento dependiendo del color
        if ficha == "Blancas":
            movida = destino - origen
        else:
            movida = origen - destino
    # Verificar si el movimiento está permitido por los dados
        if movida in self.__dado__.movimientos:
            if self.__board__.mover_ficha(origen, destino, ficha):
                return True
            else:
                raise ValueError("No se puede mover la ficha a esa posición.")
        else:
            raise ValueError("Movimiento no válido según los dados.")

    def get_ganador(self):
        """Devuelve el nombre del jugador ganador si ya sacó todas sus fichas, sino None."""
        blancas_sacadas = len(self.__fichas_blancas__.get_fichas_sacadas_blancas())
        negras_sacadas = len(self.__fichas_negras__.get_fichas_sacadas_negras())
        if blancas_sacadas == 15:
            return self.__jugador_blancas__.get_nombre()
        if negras_sacadas == 15:
            return self.__jugador_negras__.get_nombre()
        return None

    



    
    

    

        


    