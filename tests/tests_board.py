import unittest
from core.board import Board

class TestBoard(unittest.TestCase):

    def test_posiciones_iniciales(self):
        board = Board()
        self.assertEqual(board.__board__[5], ['Blancas'] * 5)
        self.assertEqual(board.__board__[7], ['Blancas'] * 3)  
        self.assertEqual(board.__board__[12], ['Blancas'] * 5)
        self.assertEqual(board.__board__[23], ['Blancas'] * 2)
        self.assertEqual(board.__board__[1], ['Negras'] * 2)
        self.assertEqual(board.__board__[11], ['Negras'] * 5)
        self.assertEqual(board.__board__[16], ['Negras'] * 3)
        self.assertEqual(board.__board__[18], ['Negras'] * 5)
        self.assertEqual(board.__board__[0], [])   
        self.assertEqual(board.__board__[25], [])

    def test_bar_salida(self):
        board = Board()
        self.assertEqual(board.get_bar(), [])
        self.assertEqual(board.get_salida(), [])

    def test_distancia_blanca_valida(self):
        board = Board()
        origen = 12
        destino = 7
        self.assertEqual(board.distancia_blancas(origen, destino), 5)
    
    def test_distancia_blanca_no_valida(self):
        board = Board()
        origen = 7
        destino = 12
        self.assertNotEqual(board.distancia_blancas(origen, destino), 5)
    
    def test_distancia_negra_valida(self):
        board = Board()
        origen = 7
        destino = 12
        self.assertEqual(board.distancia_negras(origen, destino), 5)

    def test_distancia_negra_no_valida(self):
        board = Board()
        origen = 12
        destino = 7
        self.assertNotEqual(board.distancia_negras(origen, destino), 5)

    def test_movimiento_valido_blancas(self):
        board = Board()
        color = 'Blancas'
        origen = 12     
        destino = 7
        self.assertTrue(board.movimiento_valido(origen, destino, color ))
    

    def test_movimiento_valido_negras(self):
        board = Board()
        color = 'Negras'
        origen = 7     
        destino = 12
        self.assertTrue(board.movimiento_valido(origen, destino, color ))

    def tests_movimiento_fuera_de_tablero(self):
        board = Board()
        self.assertFalse(board.movimiento_valido(-2,-3,'Blancas'))
    
    def tests_movimiento_fuera_de_tablero2(self):
        board = Board()
        self.assertFalse(board.movimiento_valido(26,30,'Negras'))

    def test_movimiento_blancas_incorrecto(self):
        board = Board()
        color = 'Blancas'
        origen = 7     
        destino = 12
        self.assertFalse(board.movimiento_valido(origen, destino, color ))

    def test_movimiento_negras_incorrecto(self):
        board = Board()
        color = 'Negras'
        origen = 12     
        destino = 7
        self.assertFalse(board.movimiento_valido(origen, destino, color ))
     
    def test_get_posicion_valida(self):
        board = Board()
        self.assertEqual(board.get_posicion(5), ['Blancas'] * 5)
    
    def test_get_posicion_no_valida(self):
        board = Board()
        self.assertIsNone(board.get_posicion(30))

    def test_fichas_negras_bar(self):
        board = Board()
        board.__board__[0] = ['Negras'] * 2
        self.assertTrue(board.ficha_negras_bar('Negras'))

    def test_bar_vacio_negras(self):
        board = Board()
        self.assertFalse(board.ficha_negras_bar('Negras'))

    def test_fichas_blancas_bar(self):
        board = Board()
        board.__board__[0] = ['Blancas'] * 2
        self.assertTrue(board.ficha_blancas_bar('Blancas'))
    
    def test_bar_vacio_blancas(self):
        board = Board()
        self.assertFalse(board.ficha_blancas_bar('Blancas'))
    



    

if __name__ == '__main__':
    unittest.main()
       