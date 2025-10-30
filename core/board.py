from core.exceptions import BackgammonError, MovimientoInvalidoError, FichaEnBarError, DadoNoDisponibleError, PuntoOcupadoError, DireccionInvalidaError, MovimientoFueraDeRangoError, SinMovimientosPosiblesError, TurnoInvalidoError, DadosNoTiradosError, PartidaFinalizadaError
class Board:
    
    def __init__(self):
        self.__board__ = [[] for _ in range(28)] 
        self.__board__[0] = [] #bar negras

        self.__board__[6] = ['Blancas'] * 5    
        self.__board__[8] = ['Blancas'] * 3    
        self.__board__[13] = ['Blancas'] * 5   
        self.__board__[24] = ['Blancas'] * 2   
        
        self.__board__[1] = ['Negras'] * 2 
        self.__board__[12] = ['Negras'] * 5    
        self.__board__[17] = ['Negras'] * 3    
        self.__board__[19] = ['Negras'] * 5    

        self.__board__[25] = [] #bar blancas
        self.__board__[26] = [] #salida negras 

    def get_bar_negras(self):               #devuelve las fichas comidas negras
        return self.__board__[0]
    
    def get_bar_blancas(self):             #devuelve las fichas comidas blancas
        return self.__board__[25]

    def get_salida(self):          #devuelve las fichas que han salido
        return self.__board__[26] 
    
    def distancia_blancas(self, origen, destino):    #blancas van de izq a derecha
        posicion_blanca = origen - destino 
        return posicion_blanca

    def distancia_negras(self, origen, destino):     #negras van de derecha a izq
        posicion_negra = destino - origen 
        return posicion_negra
    
    def movimiento_valido(self, origen, destino, ficha): #que el movimiento sea valido, no pase de las 24 posiciones
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

    
    def get_posicion(self, numero_pos):    #devuelve las posiciones del tablero de una ficha
        if 0 <= numero_pos <= 25:
            return self.__board__[numero_pos]
        return None
    
    def mover_ficha(self, origen, destino, ficha):   #mueve la ficha de una posicion a otra vacia o con fichas del mismo color 
        if self.__board__[origen] == [] and self.__board__[destino] == []:
            raise MovimientoInvalidoError("No hay ficha en la posicion de origen")
        if self.__board__[destino] == []:
            self.__board__[destino] = self.__board__[destino] + [ficha]
            self.__board__[origen] = self.__board__[origen][:-1]
            return True
        #ahora si origen y destino tienen fichas iguales entonces puedo mover la ficha de or a destino
        if self.__board__[origen] != [] and self.__board__[destino] != [] and self.__board__[origen][0] == self.__board__[destino][0]:
            self.__board__[destino] = self.__board__[destino] + [ficha]
            self.__board__[origen] = self.__board__[origen][:-1]
            return True
        else:
            raise PuntoOcupadoError("No se puede mover la ficha a esa posicion")

    def comer_ficha(self, destino, origen, ficha, ficha_comida):  #mueve la ficha a una posicion con una ficha del color contrario
        if self.__board__[destino] == []:
            raise MovimientoInvalidoError("No hay ficha para comer en esa posicion")
        if len(self.__board__[destino]) < 2 and len(self.__board__[destino]) > 0 and self.__board__[destino][0] != ficha:
            ficha_comida = self.__board__[destino][0]
            self.__board__[destino] = [ficha]
            self.__board__[origen] = self.__board__[origen][:-1]
            if ficha_comida == 'Blancas':
                self.__board__[25] = self.__board__[25] + [ficha_comida]
            else:
                self.__board__[0] = self.__board__[0] + [ficha_comida] #se va al bar de las negras
        if len(self.__board__[destino]) >= 2:
            raise PuntoOcupadoError("No se puede mover la ficha a esa posicion porque hay mas de una ficha del color contrario")
        
    def mover_ficha_comida(self, origen, destino, ficha):  
        #si la ficha es blanca sale a la posicion 19-24
        #si la ficha es negra sale a la posicion 1-6
        if ficha == 'Blancas':
            if 24 >= destino >= 19:
                self.__board__[destino] = self.__board__[destino] + [ficha]
                self.__board__[25] = self.__board__[25][:-1]
                return True
            if destino < 19:
                raise MovimientoInvalidoError("No se puede mover la ficha comida a esa posicion")
        if ficha == 'Negras':
            if 6 >= destino >= 1:
                self.__board__[destino] = self.__board__[destino] + [ficha]
                self.__board__[0] = self.__board__[0][:-1]
                return True
            if destino > 6:
                raise MovimientoInvalidoError("No se puede mover la ficha comida a esa posicion")
        
    def sacar_ficha_valido(self, ficha):   #sacar ficha del tablero
        if ficha == "Blancas":
            rango = range(1, 7)
        else:
            rango = range(19, 25) #negras
        for i in range(24):
            if i not in rango and self.__board__[i]:
                if self.__board__[i][0] == ficha:
                    raise MovimientoInvalidoError("No puedes sacar fichas hasta que todas estén en tu casa.")
        return True
        
    def sacar_ficha(self, origen, ficha):
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






