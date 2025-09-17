from core.board import Board
from core.dice import Dice
from core.player import Player
from core.checker import Checker

class BackgammonGame:
    def __init__(self, nombre_blancas, nombre_negras):
        self.__board__ = Board()
        self.__turno__ = "Blancas"
        self.__dado1__ = Dice()
        self.__dado2__ =  Dice()
        self.__jugador_blancas__ = Player(nombre_blancas, "Blancas")
        self.__jugador_negras__ = Player(nombre_negras, "Negras")

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

    def movimientos_al_tirar_dado(self):
        valor1 = self.__dado1__.tirar()
        valor2 = self.__dado2__.tirar()
        print(f"Turno de: {self.get_jugador_actual().__str__()}")
        print(f"Dados: {valor1}, {valor2}")
        if valor1 == valor2:
            movimientos = [valor1] * 4
        else:
            movimientos = [valor1, valor2]
        return movimientos




    
    

    

        


    