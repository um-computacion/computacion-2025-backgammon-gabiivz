from core.board import Board
from core.dice import Dice
from core.player import Player
from core.checker import Checker
from core.exceptions import BackgammonError, MovimientoInvalidoError, FichaEnBarError, DadoNoDisponibleError, PuntoOcupadoError, DireccionInvalidaError, MovimientoFueraDeRangoError, SinMovimientosPosiblesError, TurnoInvalidoError, DadosNoTiradosError, PartidaFinalizadaError

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
    
    def get_ficha(self):
        return self.__ficha

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
    
    def usar_dados(self, valid):
        movimiento = self.__dado__.movimientos
        if valid in movimiento:
            movimiento.remove(valid)
        else:
            raise DadoNoDisponibleError("Ese valor del dado no está disponible.")
        
    def estado_actual(self):
        """Devuelve una representación del estado actual del juego."""
        estado = {
            "turno": self.__turno__,
            "jugador_blancas": str(self.__jugador_blancas__),
            "jugador_negras": str(self.__jugador_negras__),
            "fichas_blancas_en_bar": len(self.__board__.get_posicion(0)),  # posición 0 = bar blancas
            "fichas_negras_en_bar": len(self.__board__.get_posicion(25)), # posición 25 = bar negras
            "fichas_blancas_sacadas": len(self.__fichas_blancas__.get_fichas_sacadas_blancas()),
            "fichas_negras_sacadas": len(self.__fichas_negras__.get_fichas_sacadas_negras()),
            "dados": self.__dado__.movimientos,
            "tablero": {i: self.__board__.get_posicion(i) for i in range(26)}
        }
        return estado
    
    def turno_completo(self):
        if self.__dado__.movimientos == [] and self.get_ganador() is None:
            return True
        return False
     
    def get_ganador(self):
        """Devuelve el nombre del jugador ganador si ya sacó todas sus fichas, sino None."""
        blancas_sacadas = len(self.__fichas_blancas__.get_fichas_sacadas_blancas())
        negras_sacadas = len(self.__fichas_negras__.get_fichas_sacadas_negras())
        if blancas_sacadas == 15:
            return self.__jugador_blancas__.get_nombre()
        if negras_sacadas == 15:
            return self.__jugador_negras__.get_nombre()
        return None

    



    
    

    

        


    