class Board:
    
    def __init__(self):
        self.__board__ = [None] * 26  #de 0 a 25, 2 demas, (0) que se va a referir al bar, donde van las fichas "comidas" 
                                      # y luego 25 que se va a referir a donde salen las fichas 

        self.__board__[0] = [] #bar

        self.__board__[5] = ['Blancas'] * 5    
        self.__board__[7] = ['Blancas'] * 3    
        self.__board__[12] = ['Blancas'] * 5   
        self.__board__[23] = ['Blancas'] * 2   
        
        self.__board__[1] = ['Negras'] * 2 
        self.__board__[11] = ['Negras'] * 5    
        self.__board__[16] = ['Negras'] * 3    
        self.__board__[18] = ['Negras'] * 5    

        self.__board__[25] = [] #salida

    def get_bar(self):               #devuelve las fichas comidas
        return self.__board__[0] 

    def get_salida(self):          #devuelve las fichas que han salido
        return self.__board__[25] 

    
    def distancia_blancas(self, origen, destino):    #blancas van de izq a derecha
        posicion_blanca = origen - destino 
        return posicion_blanca

    def distancia_negras(self, origen, destino):     #negras van de derecha a izq
        posicion_negra = destino - origen 
        return posicion_negra
    
    def movimiento_valido(self, origen, destino, color): #que el movimiento sea valido, no pase de las 24 posiciones

        if destino < 1 or destino > 24 or origen < 1 or origen > 24:
            raise ValueError("El destino debe estar entre 1 y 24")
        if color == 'Blancas' and origen > destino:
            return True
        if color == 'Blancas' and destino > origen:
            raise ValueError("Las fichas blancas solo pueden moverse de izquierda a derecha")
        if color == 'Negras' and destino > origen:
            return True
        if color == 'Negras' and origen > destino:
            raise ValueError("Las fichas negras solo pueden moverse de derecha a izquierda")

    
    def get_posicion(self, numero_pos):    #devuelve las posiciones del tablero de una ficha
        if 0 <= numero_pos <= 25:
            return self.__board__[numero_pos]
        return None
    
    def ficha_negras_bar(self, color):     #devuelve fichas comidas de jugador con fichas negras
        if color == 'Negras' and len(self.__board__[0]) > 0:
            return self.__board__[0]
        return False
    
    def ficha_blancas_bar(self, color):             #devuelve fichas comidas de jugador con fichas blancas
        if color == 'Blancas' and len(self.__board__[0]) > 0:
            return self.__board__[0]
        return False
    
    def mover_ficha(self, origen, destino, ficha):   #mueve la ficha de una posicion a otra vacia o con fichas del mismo color 
        if self.__board__[origen] == [] and self.__board__[destino] == []:
            return False
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
            raise ValueError("No se puede mover la ficha a esa posicion")

    def comer_ficha(self, destino, origen, ficha, ficha_comida):  #mueve la ficha a una posicion con una ficha del color contrario
        if self.__board__[destino] == []:
            return False
        if len(self.__board__[destino]) < 2 and len(self.__board__[destino]) > 0 and self.__board__[destino][0] != ficha:
            ficha_comida = self.__board__[destino][0]
            self.__board__[destino] = [ficha]
            self.__board__[origen] = self.__board__[origen][:-1]
            self.__board__[0] = self.__board__[0] + [ficha_comida]
            return True
        if len(self.__board__[destino]) >= 2:
            raise ValueError("No se puede mover la ficha a esa posicion porque hay mas de una ficha del color contrario")


        
    def mover_ficha_comida(self, destino, ficha):   #mueve la ficha comida a una posicion vacia o con fichas del mismo color
        if self.__board__[destino] == [] or self.__board__[destino] == [ficha]:
            self.__board__[destino].append(ficha)
            self.__board__[0] = self.__board__[0][:-1]
            return True
        else:
            return False
        
    def sacar_ficha(self, origen, ficha):   #saca la ficha del tablero una vez que todas las fichas estan en la zona de salida
        if ficha == 'Blancas' and origen >= 19 and origen <= 24 and self.__board__[origen] != [] and self.__board__[origen][0] == ficha:
            self.__board__[origen] = self.__board__[origen][:-1]
            self.__board__[25] = self.__board__[25] + [ficha]
            return True
        if ficha == 'Negras' and origen >= 1 and origen <= 6 and self.__board__[origen] != [] and self.__board__[origen][0] == ficha:
            self.__board__[origen] = self.__board__[origen][:-1]
            self.__board__[25] = self.__board__[25] + [ficha]
            return True
        else:
            raise ValueError("No se puede sacar la ficha de esa posicion")











        
        
        

