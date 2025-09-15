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
        self.assertRaises(ValueError, board.movimiento_valido,-2,-3,'Blancas')
    
    def tests_movimiento_fuera_de_tablero2(self):
        board = Board()
        self.assertRaises(ValueError, board.movimiento_valido,26,30,'Negras')

    def test_movimiento_blancas_incorrecto(self):
        board = Board()
        color = 'Blancas'
        origen = 7     
        destino = 12
        self.assertRaises(ValueError, board.movimiento_valido,origen, destino, color )

    def test_movimiento_negras_incorrecto(self):
        board = Board()
        color = 'Negras'
        origen = 17
        destino = 2
        self.assertRaises(ValueError, board.movimiento_valido,origen, destino, color )
     
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

    def test_destino_y_origen_invalidos(self):
        board = Board()
        self.assertRaises(ValueError, board.movimiento_valido,0, 26, 'Blancas')
        self.assertRaises(ValueError, board.movimiento_valido,26, 0, 'Negras')

    def test_mover_ficha_a_lugar_vacio(self):
        board = Board()
        board.__board__[6] = [] 
        board.__board__[5] = ['Blancas'] * 5
        self.assertTrue(board.mover_ficha(5, 6, 'Blancas'))
        self.assertEqual(board.get_posicion(6), ['Blancas'])
        self.assertEqual(board.get_posicion(5), ['Blancas'] * 4)
    
    def test_mover_ficha_a_lugar_con_ficha_igual(self):
        board = Board()
        board.__board__[5] = ["Blancas"]*5
        board.__board__[6] = ["Blancas"]*2
        self.assertTrue(board.mover_ficha(5, 6, 'Blancas' ))    
        self.assertEqual(board.get_posicion(6), ['Blancas'] * 3)
        self.assertEqual(board.get_posicion(5), ['Blancas'] * 4)

    def test_ficha_movida_no_existe(self):
        board = Board()
        board.__board__[6] = [] 
        board.__board__[5] = [] 
        self.assertFalse(board.mover_ficha(5, 6, 'Blancas'))
        self.assertEqual(board.get_posicion(6), [])
        self.assertEqual(board.get_posicion(5), [])
    
    def test_ficha_movida_sumada(self):
        board = Board()
        board.__board__[6] = ['Blancas'] * 2
        board.__board__[5] = ['Blancas'] * 3
        self.assertTrue(board.mover_ficha(5, 6, 'Blancas'))
        self.assertEqual(board.get_posicion(6), ['Blancas'] * 3)
        self.assertEqual(board.get_posicion(5), ['Blancas'] * 2)

    def test_mover_ficha_invalido(self):
        board = Board()
        board.__board__[6] = ['Negras'] * 2
        board.__board__[5] = ['Blancas'] * 5
        self.assertRaises(ValueError, board.mover_ficha,5, 6, 'Blancas')
        self.assertEqual(board.get_posicion(6), ['Negras'] * 2)
        self.assertEqual(board.get_posicion(5), ['Blancas'] * 5)


    def test_comer_ficha_invalida(self):
        board = Board()
        board.__board__[6] = ['Negras'] * 3
        board.__board__[5] = ['Blancas'] * 5
        ficha_comida = None
        self.assertRaises(ValueError, board.comer_ficha, 5,6, 'Blancas', ficha_comida)
        self.assertEqual(board.get_posicion(6), ['Negras'] * 3)
        self.assertEqual(board.get_posicion(5), ['Blancas'] * 5)

    def test_comer_ficha_invalida2(self):
        board = Board()
        board.__board__[6] = ['Negras'] * 2
        board.__board__[5] = ['Blancas'] * 5
        ficha_comida = None
        self.assertRaises(ValueError, board.comer_ficha, 5,6, 'Blancas', ficha_comida)
        self.assertEqual(board.get_posicion(6), ['Negras'] * 2)
        self.assertEqual(board.get_posicion(5), ['Blancas'] * 5)



    def test_comer_ficha_destino_una(self):
        board = Board()
        board.__board__[8] = ['Negras']
        board.__board__[5] = ['Blancas']
        self.assertTrue(board.comer_ficha(8, 5, 'Blancas', None))


    def test_comer_ficha_vacia(self):
        board = Board()
        board.__board__[6] = []
        board.__board__[5] = ['Blancas'] * 5
        ficha = 'Blancas'
        ficha_comida = None
        self.assertFalse(board.comer_ficha(6, 5, ficha, ficha_comida))
        self.assertEqual(board.get_posicion(6), [])
        self.assertEqual(board.get_posicion(5), ['Blancas'] * 5)
        self.assertEqual(board.get_bar(), [])

    def test_mover_ficha_comida_valida(self):
        board = Board()
        board.__board__[0] = ['Blancas'] * 2
        board.__board__[6] = [] 
        self.assertTrue(board.mover_ficha_comida(6, 'Blancas'))
        self.assertEqual(board.get_posicion(6), ['Blancas'])
        self.assertEqual(board.__board__[0], ['Blancas'])
    
    def test_mover_ficha_comida_invalida(self):
        board = Board()
        board.__board__[0] = ['Blancas'] * 2
        board.__board__[6] = ['Negras']
        self.assertFalse(board.mover_ficha_comida(6, 'Blancas'))
        self.assertEqual(board.get_posicion(6), ['Negras'])
        self.assertEqual(board.__board__[0], ['Blancas'] * 2)

    def test_comer_ficha_destino_con_mas_1ficha_opuesta(self):
        board = Board()
        board.__board__[6] = ['Negras'] * 3
        board.__board__[5] = ['Blancas'] * 5
        ficha_comida = None
        self.assertRaises(ValueError, board.comer_ficha, 6, 5, 'Blancas', ficha_comida)
        self.assertEqual(board.get_posicion(6), ['Negras'] * 3)
        self.assertEqual(board.get_posicion(5), ['Blancas'] * 5)
        self.assertEqual(board.get_bar(), [])

    def test_sacar_ficha_blanca(self):
        board = Board()
        board.__board__[24] = ['Blancas'] * 3
        self.assertTrue(board.sacar_ficha(24, 'Blancas'))
        self.assertEqual(board.get_posicion(24), ['Blancas'] * 2)
        self.assertEqual(board.get_salida(), ['Blancas'])
    
    def test_sacar_ficha_negra(self):
        board = Board()
        board.__board__[1] = ['Negras'] * 4
        self.assertTrue(board.sacar_ficha(1, 'Negras'))
        self.assertEqual(board.get_posicion(1), ['Negras'] * 3)
        self.assertEqual(board.get_salida(), ['Negras'])
    
    def test_sacar_ficha_blanca_invalida(self):
        board = Board()
        board.__board__[18] = ['Blancas'] * 3
        self.assertRaises(ValueError, board.sacar_ficha,18, 'Blancas')
        self.assertEqual(board.get_posicion(18), ['Blancas'] * 3)
        self.assertEqual(board.get_salida(), [])

    def test_sacar_ficha_negra_invalida(self):
        board = Board()
        board.__board__[7] = ['Negras'] * 3
        self.assertRaises(ValueError,board.sacar_ficha,7, 'Negras')
        self.assertEqual(board.get_posicion(7), ['Negras'] * 3)
        self.assertEqual(board.get_salida(), [])

    

if __name__ == '__main__':
    unittest.main()
       