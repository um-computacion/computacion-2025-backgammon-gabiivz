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

    

if __name__ == '__main__':
    unittest.main()
       