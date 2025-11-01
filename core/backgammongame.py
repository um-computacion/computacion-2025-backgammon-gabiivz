from core.board import Board
from core.dice import Dice
from core.player import Player
from core.exceptions import MovimientoInvalidoError, FichaEnBarError, DadoNoDisponibleError, DadosNoTiradosError

class BackgammonGame:
    """Clase principal que maneja la lógica del juego de Backgammon."""
    def __init__(self, nombre_blancas, nombre_negras):
        """Inicializa la partida, creando el tablero, los dados y los jugadores."""
        self.__board__ = Board()
        self.__turno__ = "Blancas"
        self.__dado__ = Dice()
        self.__jugador_blancas__ = Player(nombre_blancas, "Blancas")
        self.__jugador_negras__ = Player(nombre_negras, "Negras")
        self.__fichas_sacadas_blancas__ = []
        self.__fichas_sacadas_negras__ = []


    def get_board(self):
        """Devuelve la instancia del tablero."""
        return self.__board__
    
    def get_jugador_blancas(self):
        """Devuelve el objeto del jugador de Blancas."""
        return self.__jugador_blancas__
    
    def get_jugador_negras(self):
        """Devuelve el objeto del jugador de Negras."""
        return self.__jugador_negras__
    
    def get_jugador_actual(self):
        """Devuelve el objeto del jugador cuyo turno es."""
        if self.__turno__ == "Blancas":
            return self.__jugador_blancas__
        else:
            return self.__jugador_negras__
    
    def get_turno(self):
        """Devuelve el string del turno actual ('Blancas' o 'Negras')."""
        return self.__turno__
    
    def cambio_turnos(self):
        """Cambia el turno de Blancas a Negras o viceversa."""
        if self.__turno__ == "Blancas":
            self.__turno__ = "Negras"
        else:
            self.__turno__ = "Blancas"

    def tirar_dados(self):
        """Tira los dados y devuelve el resultado (tupla)."""
        return self.__dado__.tirar()
    
    def get_dados(self):
        """Devuelve la lista de movimientos de dados disponibles."""
        return self.__dado__.get_movimientos() 
    
    def usar_dados(self, valid):
        """Consume (quita) un valor de dado de la lista de movimientos."""
        movimiento = self.get_dados()
        if valid in movimiento:
            movimiento.remove(valid)
        else:
            raise DadoNoDisponibleError("Ese valor del dado no está disponible.")
    
    def tiene_movimientos_posibles(self):
        """
        Comprueba si el jugador actual tiene al menos un movimiento legal
        con los dados actuales. (Versión fácil de leer)
        """
        ficha = self.get_turno()
        dados = self.get_dados() 
        if not dados:
            return True 
        en_bar_blancas = (ficha == "Blancas" and len(self.__board__.get_bar_blancas()) > 0)
        en_bar_negras = (ficha == "Negras" and len(self.__board__.get_bar_negras()) > 0)
        
        if en_bar_blancas or en_bar_negras:
            for d in dados:
                destino = (25 - d) if ficha == "Blancas" else d
                if self.__board__.es_destino_legal(destino, ficha):
                    return True 
            return False   
        
        for origen in range(1, 25): 
            fichas_en_origen = self.__board__.get_posicion(origen)
            if fichas_en_origen and fichas_en_origen[0] == ficha:
                for d in dados:
                    destino = (origen - d) if ficha == "Blancas" else (origen + d)
                    if destino <= 0 or destino > 25:
                        try:
                            self.__board__.sacar_ficha_valido(ficha)
                            return True 
                        except MovimientoInvalidoError:
                            continue 
                    elif self.__board__.es_destino_legal(destino, ficha):
                        return True 
        return False 

    def mover_ficha(self, origen, destino):
        """Función principal para mover una ficha. Maneja la barra, sacar fichas y movimientos normales."""
        ficha = self.get_turno()
        origen = int(origen)
        destino = int(destino)
        mov = 0 
        
        if not self.get_dados():
            raise DadosNoTiradosError("No has tirado los dados o no tienes movimientos disponibles.")
        
        dados_disponibles = self.get_dados()

        # BARRA
        if (ficha == "Blancas" and len(self.__board__.get_bar_blancas()) > 0 and origen == 25) or \
           (ficha == "Negras" and len(self.__board__.get_bar_negras()) > 0 and origen == 0):
            
            if ficha == "Blancas":
                mov = 25 - destino 
            else: 
                mov = destino 
            
            if mov not in dados_disponibles:
                raise DadoNoDisponibleError("El movimiento no coincide con los dados disponibles.")
            
            self.__board__.mover_ficha_comida(origen, destino, ficha)
            self.usar_dados(mov)
            return

        # ERRORES DE BARRA
        if ficha == "Negras" and len(self.__board__.get_bar_negras()) > 0 and origen != 0:
            raise FichaEnBarError("Tienes fichas en el bar, tenés que moverlas primero.")

        if ficha == "Blancas" and len(self.__board__.get_bar_blancas()) > 0 and origen != 25:
            raise FichaEnBarError("Tienes fichas en el bar, tenés que moverlas primero.")

        # SACAR FICHAS
        if destino == 26:
            if ficha == "Blancas":
                mov = origen
            else: # Negras
                mov = 25 - origen
            try:
                self.__board__.sacar_ficha_valido(ficha)
            except MovimientoInvalidoError:
                raise MovimientoInvalidoError("No puedes sacar fichas hasta que todas estén en tu casa.")
            
            # (dados_disponibles ya está definido arriba)
            if mov in dados_disponibles:
                self.__board__.sacar_ficha(origen, ficha) 
                self.usar_dados(mov)
                if ficha == "Blancas":
                    self.__fichas_sacadas_blancas__.append(ficha)
                else:
                    self.__fichas_sacadas_negras__.append(ficha)
                return
            else:
                mayores_disponibles = [dado for dado in dados_disponibles if dado > mov]
                if mayores_disponibles:
                    mayor_dado = min(mayores_disponibles)
                    self.__board__.sacar_ficha(origen, ficha)
                    self.usar_dados(mayor_dado)
                    if ficha == "Blancas":
                        self.__fichas_sacadas_blancas__.append(ficha)
                    else:
                        self.__fichas_sacadas_negras__.append(ficha)
                    return
            raise DadoNoDisponibleError("Movimiento para sacar ficha no válido con los dados actuales.")
        
        # MOVIMIENTO NORMAL
        if ficha == "Blancas":
            mov = abs(origen - destino)
        else: # Negras
            mov = abs(destino - origen)
            
        if mov not in dados_disponibles:
            raise DadoNoDisponibleError("El movimiento no coincide con los dados disponibles.")
        
        self.__board__.movimiento_valido(origen, destino, ficha)

        # COMER FICHA o APILAR
        if self.__board__.get_posicion(destino) != [] and self.__board__.get_posicion(destino)[0] != ficha:
            self.__board__.comer_ficha(destino, origen, ficha, self.__board__.get_posicion(destino)[0])
        else:
            self.__board__.mover_ficha(origen, destino, ficha)
            
        self.usar_dados(mov)
        
        
    def estado_actual(self):
        """Devuelve una representación del estado actual del juego."""
        estado = {
            "turno": self.__turno__,
            "jugador_blancas": str(self.__jugador_blancas__),
            "jugador_negras": str(self.__jugador_negras__),
            "fichas_blancas_en_bar": len(self.__board__.get_posicion(25)),
            "fichas_negras_en_bar": len(self.__board__.get_posicion(0)),
            "fichas_blancas_sacadas": len(self.__fichas_sacadas_blancas__),
            "fichas_negras_sacadas": len(self.__fichas_sacadas_negras__),
            "dados": self.get_dados(),
            "tablero": {i: self.__board__.get_posicion(i) for i in range(1, 25)}
        }
        return estado
    
    def turno_completo(self):
        """Verifica si el jugador ha usado todos sus dados."""
        if not self.get_dados() and self.get_ganador() is None:
            return True
        return False
    
    def get_ganador(self):
        """Devuelve el nombre del jugador ganador si ya sacó todas sus fichas, sino None."""
        blancas_sacadas = len(self.__fichas_sacadas_blancas__)
        negras_sacadas = len(self.__fichas_sacadas_negras__)
        
        if blancas_sacadas == 15:
            return self.__jugador_blancas__.get_nombre()
        if negras_sacadas == 15:
            return self.__jugador_negras__.get_nombre()
        return None