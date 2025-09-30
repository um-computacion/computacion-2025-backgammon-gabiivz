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
        jugador = self.get_jugador_actual()
        color = jugador.get_color()
        # Si hay fichas en el bar, deben moverse primero
        if len(self.__board__.get_bar()) > 0:
            if origen != 0:  # 0 = bar
                raise FichaEnBarError("Debes mover primero las fichas del bar.")
            if not self.__board__.mover_ficha_comida(destino, color):
                raise PuntoOcupadoError("No puedes ingresar la ficha del bar en ese punto.")
        # Calcular la distancia y gastar el dado
            movida = self._calcular_distancia(origen, destino, color)
            if movida not in self.__dado__.movimientos:
                raise DadoNoDisponibleError(f"Necesitas un dado de valor {movida}.")
            self.__dado__.movimientos.remove(movida)
            return True
        # Validar movimiento según dirección
        self.__board__.movimiento_valido(origen, destino, color)
        # Calcular distancia
        movida = self._calcular_distancia(origen, destino, color)
        # Verificar que el movimiento esté en los dados
        if movida not in self.__dado__.movimientos:
            raise DadoNoDisponibleError(f"Necesitas un dado de valor {movida}.")
        # Intentar comer ficha si hay una sola contraria
        if self.__board__.comer_ficha(destino, origen, color, None):
            self.__dado__.movimientos.remove(movida)
            return True
        # Sino mover normalmente
        if self.__board__.mover_ficha(origen, destino, color):
            self.__dado__.movimientos.remove(movida)
            return True
        raise MovimientoInvalidoError("No se pudo completar el movimiento.")

    # Método auxiliar para eliminar duplicación
    def _calcular_distancia(self, origen, destino, color):
        """Calcula la distancia según el color del jugador."""
        if color == "Blancas":
            return self.__board__.distancia_blancas(origen, destino)
        else:
            return self.__board__.distancia_negras(origen, destino)


    def get_ganador(self):
        """Devuelve el nombre del jugador ganador si ya sacó todas sus fichas, sino None."""
        blancas_sacadas = len(self.__fichas_blancas__.get_fichas_sacadas_blancas())
        negras_sacadas = len(self.__fichas_negras__.get_fichas_sacadas_negras())
        if blancas_sacadas == 15:
            return self.__jugador_blancas__.get_nombre()
        if negras_sacadas == 15:
            return self.__jugador_negras__.get_nombre()
        return None

    



    
    

    

        


    