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

    def get_bar(self):
        return self.__board__[0] 

    def get_salida(self):
        return self.__board__[25] 

