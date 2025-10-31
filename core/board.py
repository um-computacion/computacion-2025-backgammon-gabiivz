from core.exceptions import BackgammonError, MovimientoInvalidoError, FichaEnBarError, DadoNoDisponibleError, PuntoOcupadoError, DireccionInvalidaError, MovimientoFueraDeRangoError, DadosNoTiradosError
class Board:
    
    def __init__(self):
        """Inicializa el tablero con la configuración estándar de Backgammon."""
        self.__board__ = [[] for _ in range(28)] 
        self.__board__[0] = [] # Bar Negras
        self.__board__[6] = ['Blancas'] * 5    
        self.__board__[8] = ['Blancas'] * 3    
        self.__board__[13] = ['Blancas'] * 5   
        self.__board__[24] = ['Blancas'] * 2   
        
        self.__board__[1] = ['Negras'] * 2 
        self.__board__[12] = ['Negras'] * 5    
        self.__board__[17] = ['Negras'] * 3    
        self.__board__[19] = ['Negras'] * 5    

        self.__board__[25] = [] # Bar Blancas
        self.__board__[26] = [] # Salida

    def get_bar_negras(self):
        """Devuelve la lista de fichas Negras en la barra."""
        return self.__board__[0]
    
    def get_bar_blancas(self):
        """Devuelve la lista de fichas Blancas en la barra."""
        return self.__board__[25]

    def get_salida(self):
        """Devuelve la lista de fichas (ambos colores) que han salido del tablero."""
        return self.__board__[26] 
    
    def distancia_blancas(self, origen, destino):
        """Calcula la distancia de movimiento para las Blancas."""
        posicion_blanca = origen - destino 
        return posicion_blanca

    def distancia_negras(self, origen, destino):
        """Calcula la distancia de movimiento para las Negras."""
        posicion_negra = destino - origen 
        return posicion_negra
    
    def movimiento_valido(self, origen, destino, ficha):
        """Valida si un movimiento está en la dirección correcta y dentro del tablero."""
        if destino < 1 or destino > 24 or origen < 1 or origen > 24:
            raise MovimientoFueraDeRangoError("El destino debe estar entre 1 y 24")
        if ficha == 'Blancas' and origen > destino:
            return True
        if ficha == 'Blancas' and destino > origen:
            raise DireccionInvalidaError("Las fichas blancas solo pueden moverse de izquierda a derecha")
        if ficha == 'Negras' and destino > origen:
            return True
        if ficha == 'Negras' and origen > destino:
            raise DireccionInvalidaError("Las fichas negras solo pueden moverse de derecha a izquierda")

    
    def get_posicion(self, numero_pos):
        """Devuelve la lista de fichas en un punto específico (1-24) o barra (0, 25)."""
        if 0 <= numero_pos <= 25:
            return self.__board__[numero_pos]
        return None
    
    def mover_ficha(self, origen, destino, ficha):
        """Mueve una ficha a un punto vacío o a un punto con fichas propias (apila)."""
        if self.__board__[origen] == [] and self.__board__[destino] == []:
            raise MovimientoInvalidoError("No hay ficha en la posicion de origen")
        if self.__board__[destino] == []:
            self.__board__[destino] = self.__board__[destino] + [ficha]
            self.__board__[origen] = self.__board__[origen][:-1]
            return True
        if self.__board__[origen] != [] and self.__board__[destino] != [] and self.__board__[origen][0] == self.__board__[destino][0]:
            self.__board__[destino] = self.__board__[destino] + [ficha]
            self.__board__[origen] = self.__board__[origen][:-1]
            return True
        else:
            raise PuntoOcupadoError("No se puede mover la ficha a esa posicion")

    def comer_ficha(self, destino, origen, ficha, ficha_comida):
        """Mueve una ficha a un punto ocupado por una sola ficha rival (la come)."""
        if self.__board__[destino] == []:
            raise MovimientoInvalidoError("No hay ficha para comer en esa posicion")
        if len(self.__board__[destino]) < 2 and len(self.__board__[destino]) > 0 and self.__board__[destino][0] != ficha:
            ficha_comida = self.__board__[destino][0]
            self.__board__[destino] = [ficha]
            self.__board__[origen] = self.__board__[origen][:-1]
            if ficha_comida == 'Blancas':
                self.__board__[25] = self.__board__[25] + [ficha_comida]
            else:
                self.__board__[0] = self.__board__[0] + [ficha_comida]
        if len(self.__board__[destino]) >= 2:
            raise PuntoOcupadoError("No se puede mover la ficha a esa posicion porque hay mas de una ficha del color contrario")
        
    def mover_ficha_comida(self, origen, destino, ficha): 
        """
        Mueve una ficha desde la barra (origen 0 o 25) a un destino,
        manejando lógicas de bloqueo, apilado y comida.
        """
        if ficha == 'Blancas' and not (19 <= destino <= 24):
             raise MovimientoFueraDeRangoError("Las blancas solo pueden salir de la barra a los puntos 19-24")
        if ficha == 'Negras' and not (1 <= destino <= 6):
             raise MovimientoFueraDeRangoError("Las negras solo pueden salir de la barra a los puntos 1-6")

        oponente = "Negras" if ficha == "Blancas" else "Blancas"
        fichas_en_destino = self.get_posicion(destino)
        
        if fichas_en_destino and fichas_en_destino[0] == oponente and len(fichas_en_destino) > 1:
            raise PuntoOcupadoError(f"El punto {destino} está bloqueado por el oponente.")
        
        elif fichas_en_destino and fichas_en_destino[0] == oponente and len(fichas_en_destino) == 1:
            ficha_comida = self.__board__[destino][0]
            self.__board__[destino] = [ficha]
            
            if ficha_comida == 'Blancas':
                self.__board__[25] = self.__board__[25] + [ficha_comida]
            else:
                self.__board__[0] = self.__board__[0] + [ficha_comida]
        else:
            self.__board__[destino] = self.__board__[destino] + [ficha]

        if ficha == 'Blancas':
            self.__board__[25] = self.__board__[25][:-1]
        else:
            self.__board__[0] = self.__board__[0][:-1]
            
        return True
        
    def es_destino_legal(self, destino, ficha):
        """
        Verifica si una ficha puede aterrizar legalmente en un destino.
        No comprueba los dados, solo si el punto está bloqueado.
        """
        if destino == 26:
            return True
        if not (1 <= destino <= 24):
            return False 
        oponente = "Negras" if ficha == "Blancas" else "Blancas"
        fichas_en_destino = self.get_posicion(destino)
        if not fichas_en_destino:
            return True
        if fichas_en_destino[0] == ficha:
            return True
        if fichas_en_destino[0] == oponente:
            if len(fichas_en_destino) == 1:
                return True
            else:
                return False
        return False
        
    def sacar_ficha_valido(self, ficha):
        """Verifica si el jugador está habilitado para sacar fichas (todas en casa)."""
        if ficha == "Blancas":
            rango = range(1, 7)
        else:
            rango = range(19, 25)
        for i in range(24):
            if i not in rango and self.__board__[i]:
                if self.__board__[i][0] == ficha:
                    raise MovimientoInvalidoError("No puedes sacar fichas hasta que todas estén en tu casa.")
        return True
        
    def sacar_ficha(self, origen, ficha):
        """Saca una ficha del tablero (bear off) si el movimiento es válido."""
        try:
            self.sacar_ficha_valido(ficha)
        except MovimientoInvalidoError:
            raise MovimientoInvalidoError("No puedes sacar fichas hasta que todas estén en tu casa.")
        if self.__board__[origen]:
            if self.__board__[origen][-1] == ficha:
                self.__board__[origen].pop()
                self.__board__[26] += [ficha]
                return True
        return False