import unittest
from core.board import Board
from core.exceptions import BackgammonError, MovimientoInvalidoError, FichaEnBarError, DadoNoDisponibleError, PuntoOcupadoError, DireccionInvalidaError, MovimientoFueraDeRangoError, SinMovimientosPosiblesError, TurnoInvalidoError, DadosNoTiradosError, PartidaFinalizadaError


class TestBoard(unittest.TestCase):

    def test_posiciones_iniciales(self):
        """Testea la configuración inicial del tablero."""
        board = Board()
        self.assertEqual(board.__board__[6], ['Blancas'] * 5)
        self.assertEqual(board.__board__[8], ['Blancas'] * 3)  
        self.assertEqual(board.__board__[13], ['Blancas'] * 5)
        self.assertEqual(board.__board__[24], ['Blancas'] * 2)
        self.assertEqual(board.__board__[1], ['Negras'] * 2)
        self.assertEqual(board.__board__[12], ['Negras'] * 5)
        self.assertEqual(board.__board__[17], ['Negras'] * 3)
        self.assertEqual(board.__board__[19], ['Negras'] * 5)
        self.assertEqual(board.__board__[0], [])   
        self.assertEqual(board.__board__[25], [])
        self.assertEqual(board.__board__[26], [])

    def test_bar_negras(self):
        """Testea el bar de las fichas negras."""
        board = Board()
        board.__board__[0] = ['Negras'] * 3
        self.assertEqual(board.get_bar_negras(), ['Negras'] * 3)

    def test_bar_blancas(self):
        """Testea el bar de las fichas blancas."""
        board = Board()
        board.__board__[25] = ['Blancas'] * 4
        self.assertEqual(board.get_bar_blancas(), ['Blancas'] * 4)

    def test_distancia_blanca_valida(self):
        """Testea una distancia válida para las fichas blancas."""
        board = Board()
        origen = 12
        destino = 7
        self.assertEqual(board.distancia_blancas(origen, destino), 5)
    
    def test_distancia_blanca_no_valida(self):
        """Testea una distancia no válida para las fichas blancas."""
        board = Board()
        origen = 7
        destino = 12
        self.assertNotEqual(board.distancia_blancas(origen, destino), 5)
    
    def test_distancia_negra_valida(self):
        """Testea una distancia válida para las fichas negras."""
        board = Board()
        origen = 7
        destino = 12
        self.assertEqual(board.distancia_negras(origen, destino), 5)

    def test_distancia_negra_no_valida(self):
        """Testea una distancia no válida para las fichas negras."""
        board = Board()
        origen = 12
        destino = 7
        self.assertNotEqual(board.distancia_negras(origen, destino), 5)

    def test_movimiento_valido_blancas(self):
        """Testea un movimiento válido para las fichas blancas."""
        board = Board()
        color = 'Blancas'
        origen = 12     
        destino = 7
        self.assertTrue(board.movimiento_valido(origen, destino, color ))

    def test_movimiento_valido_negras(self):
        """Testea un movimiento válido para las fichas negras."""
        board = Board()
        color = 'Negras'
        origen = 7     
        destino = 12
        self.assertTrue(board.movimiento_valido(origen, destino, color ))

    def tests_movimiento_fuera_de_tablero(self):
        """Testea un movimiento fuera del tablero."""
        board = Board()
        self.assertRaises(MovimientoFueraDeRangoError, board.movimiento_valido,-2,-3,'Blancas')
    
    def tests_movimiento_fuera_de_tablero2(self):
        """Testea otro movimiento fuera del tablero."""
        board = Board()
        self.assertRaises(MovimientoFueraDeRangoError, board.movimiento_valido,28,30,'Negras')

    def test_movimiento_blancas_incorrecto(self):
        """Testea un movimiento incorrecto para las fichas blancas."""
        board = Board()
        color = 'Blancas'
        origen = 7     
        destino = 12
        self.assertRaises(DireccionInvalidaError, board.movimiento_valido,origen, destino, color )

    def test_movimiento_negras_incorrecto(self):
        """Testea un movimiento incorrecto para las fichas negras."""
        board = Board()
        color = 'Negras'
        origen = 17
        destino = 2
        self.assertRaises(DireccionInvalidaError, board.movimiento_valido,origen, destino, color )
     
    def test_get_posicion_valida(self):
        """Testea el getter de una posición válida."""
        board = Board()
        self.assertEqual(board.get_posicion(6), ['Blancas'] * 5)
    
    def test_get_posicion_no_valida(self):
        """Testea el getter de una posición no válida."""
        board = Board()
        self.assertIsNone(board.get_posicion(30))

    def test_destino_y_origen_invalidos(self):
        """Testea un origen y destino inválidos."""
        board = Board()
        self.assertRaises(MovimientoFueraDeRangoError, board.movimiento_valido,0, 27, 'Blancas')
        self.assertRaises(MovimientoFueraDeRangoError, board.movimiento_valido,27, 0, 'Negras')

    def test_mover_ficha_a_lugar_vacio(self):
        """Testea mover una ficha a un lugar vacío."""
        board = Board()
        board.__board__[6] = [] 
        board.__board__[5] = ['Blancas'] * 5
        self.assertTrue(board.mover_ficha(5, 6, 'Blancas'))
        self.assertEqual(board.get_posicion(6), ['Blancas'])
        self.assertEqual(board.get_posicion(5), ['Blancas'] * 4)
    
    def test_mover_ficha_a_lugar_con_ficha_igual(self):
        """Testea mover una ficha a un lugar con fichas del mismo color."""
        board = Board()
        board.__board__[5] = ["Blancas"]*5
        board.__board__[6] = ["Blancas"]*2
        self.assertTrue(board.mover_ficha(5, 6, 'Blancas' ))    
        self.assertEqual(board.get_posicion(6), ['Blancas'] * 3)
        self.assertEqual(board.get_posicion(5), ['Blancas'] * 4)

    def test_ficha_movida_no_existe(self):
        """Testea mover una ficha que no existe."""
        board = Board()
        board.__board__[6] = [] 
        board.__board__[5] = [] 
        self.assertRaises(MovimientoInvalidoError, board.mover_ficha, 5, 6, 'Blancas')
        self.assertEqual(board.get_posicion(6), [])
        self.assertEqual(board.get_posicion(5), [])
    
    def test_ficha_movida_sumada(self):
        """Testea mover y apilar una ficha."""
        board = Board()
        board.__board__[6] = ['Blancas'] * 2
        board.__board__[5] = ['Blancas'] * 3
        self.assertTrue(board.mover_ficha(5, 6, 'Blancas'))
        self.assertEqual(board.get_posicion(6), ['Blancas'] * 3)
        self.assertEqual(board.get_posicion(5), ['Blancas'] * 2)

    def test_mover_ficha_invalido(self):
        """Testea un movimiento de ficha inválido."""
        board = Board()
        board.__board__[6] = ['Negras'] * 2
        board.__board__[5] = ['Blancas'] * 5
        self.assertRaises(PuntoOcupadoError, board.mover_ficha,5, 6, 'Blancas')
        self.assertEqual(board.get_posicion(6), ['Negras'] * 2)
        self.assertEqual(board.get_posicion(5), ['Blancas'] * 5)

    def test_comer_ficha_invalida(self):
        """Testea una acción de comer ficha inválida."""
        board = Board()
        board.__board__[6] = ['Negras'] * 3
        board.__board__[5] = ['Blancas'] * 5
        ficha_comida = None
        self.assertRaises(PuntoOcupadoError, board.comer_ficha, 6, 5, 'Blancas', ficha_comida)
        self.assertEqual(board.get_posicion(6), ['Negras'] * 3)
        self.assertEqual(board.get_posicion(5), ['Blancas'] * 5)

    def test_comer_ficha_invalida2(self):
        """Testea otra acción de comer ficha inválida."""
        board = Board()
        board.__board__[6] = ['Negras'] * 2
        board.__board__[5] = ['Blancas'] * 5
        ficha_comida = None
        self.assertRaises(PuntoOcupadoError, board.comer_ficha, 6, 5, 'Blancas', ficha_comida)
        self.assertEqual(board.get_posicion(6), ['Negras'] * 2)
        self.assertEqual(board.get_posicion(5), ['Blancas'] * 5)

    def test_comer_ficha_destino_una(self):
        """Testea comer una ficha cuando el destino tiene una."""
        board = Board()
        board.__board__[8] = ['Negras']
        board.__board__[5] = ['Blancas']*2
        self.assertEqual(board.comer_ficha(8, 5, 'Blancas','Negras'), None)
        self.assertEqual(board.get_posicion(8), ['Blancas'])
        self.assertEqual(board.get_posicion(5), ['Blancas'])

    def test_comer_ficha_blanca(self):
        """Testea comer una ficha blanca."""
        board = Board()
        board.__board__[6] = ['Blancas']
        board.__board__[5] = ['Negras'] * 5
        self.assertEqual(board.comer_ficha(6, 5, 'Negras', 'Blancas'), None)
        self.assertEqual(board.get_posicion(6), ['Negras'])
        self.assertEqual(board.get_posicion(5), ['Negras'] * 4)
        self.assertEqual(board.get_bar_blancas(), ['Blancas'])

    def test_comer_ficha_vacia(self):
        """Testea una acción de comer en un lugar vacío."""
        board = Board()
        board.__board__[6] = []
        board.__board__[5] = ['Blancas'] * 5
        ficha = 'Blancas'
        ficha_comida = []
        self.assertRaises(MovimientoInvalidoError, board.comer_ficha, 6, 5, ficha, ficha_comida)
        self.assertEqual(board.get_posicion(6), [])
        self.assertEqual(board.get_posicion(5), ['Blancas'] * 5)
        self.assertEqual(board.get_bar_negras(), [])

    def test_mover_ficha_comida_blanca_valida(self):
        """Testea mover una ficha blanca comida de forma válida."""
        board = Board()
        board.__board__[25] = ['Blancas'] * 2
        board.__board__[23] = []
        self.assertTrue(board.mover_ficha_comida(25,23, 'Blancas'))
        self.assertEqual(board.get_posicion(23), ['Blancas'])
        self.assertEqual(board.__board__[25], ['Blancas'])
    
    def test_mover_ficha_comida_negra_valida(self):
        """Testea mover una ficha negra comida de forma válida."""
        board = Board()
        board.__board__[0] = ['Negras'] * 3
        board.__board__[5] = []
        self.assertTrue(board.mover_ficha_comida(0,5, 'Negras'))
        self.assertEqual(board.get_posicion(5), ['Negras'])
        self.assertEqual(board.__board__[0], ['Negras'] * 2)

    def test_mover_ficha_comida_blanca_invalida(self):
        """Testea mover una ficha blanca comida de forma inválida."""
        board = Board()
        board.__board__[25] = ['Blancas'] * 2
        board.__board__[18] = ['Negras']
        with self.assertRaises(MovimientoInvalidoError):
            board.mover_ficha_comida(25, 18, 'Blancas')
        self.assertEqual(board.get_posicion(18), ['Negras'])
        self.assertEqual(board.__board__[25], ['Blancas'] * 2)

    def test_mover_ficha_comida_negra_invalida(self):
        """Testea mover una ficha negra comida de forma inválida."""
        board = Board()
        board.__board__[0] = ['Negras'] * 3
        board.__board__[8] = ['Blancas']
        with self.assertRaises(MovimientoInvalidoError):
            board.mover_ficha_comida(0, 8, 'Negras')
        self.assertEqual(board.get_posicion(8), ['Blancas'])
        self.assertEqual(board.__board__[0], ['Negras'] * 3)


    def test_comer_ficha_destino_con_mas_1ficha_opuesta(self):
        """Testea comer ficha cuando el destino tiene más de una ficha opuesta."""
        board = Board()
        board.__board__[6] = ['Negras'] * 3
        board.__board__[5] = ['Blancas'] * 5
        ficha_comida = None
        self.assertRaises(PuntoOcupadoError, board.comer_ficha, 6, 5, 'Blancas', ficha_comida)
        self.assertEqual(board.get_posicion(6), ['Negras'] * 3)
        self.assertEqual(board.get_posicion(5), ['Blancas'] * 5)
        self.assertEqual(board.get_bar_negras(), [])

    def test_sacar_ficha_color_incorrecto(self):
        """Testea sacar ficha con color incorrecto."""
        board = Board()
        board.__board__ = [[] for _ in range(24)]
        board.__board__[11] = ["negro"]
        self.assertFalse(board.sacar_ficha(11, "blanco"))

    def test_sacar_ficha_permitido_negro_con_fichas_fuera(self):
        """Testea sacar ficha negra no permitido con fichas fuera de casa."""
        board = Board()
        board.__board__[10] = ["negro"]
        self.assertRaises(MovimientoInvalidoError, board.sacar_ficha, 10, "negro")

    def test_sacar_ficha_permitido_blanco_con_fichas_fuera(self):
        """Testea sacar ficha blanca no permitido con fichas fuera de casa."""
        board = Board()
        board.__board__[10] = ["blanco"]
        self.assertRaises(MovimientoInvalidoError, board.sacar_ficha, 10, "blanco")
        
    def test_get_salida(self):
        """Testea el getter de la zona de salida."""
        board = Board()
        self.assertEqual(board.get_salida(), board.__board__[26])
    
    def test_sacar_ficha_valido_blancas_exitoso(self):
        """Testea que es válido para las blancas sacar fichas."""
        board = Board()
        board.__board__ = [[] for _ in range(26)]
        board.__board__[3] = ['Blancas'] 
        self.assertTrue(board.sacar_ficha_valido('Blancas'))

    def test_sacar_ficha_valido_negras_falla(self):
        """Testea que no es válido para las negras sacar fichas si tienen fuera."""
        board = Board()
        board.__board__[10] = ['Negras'] 
        with self.assertRaises(MovimientoInvalidoError):
            board.sacar_ficha_valido('Negras')

    def test_sacar_ficha_exitoso(self):
        """Testea sacar una ficha exitosamente."""
        board = Board()
        board.__board__ = [[] for _ in range(27)]
        board.__board__[20] = ['Negras']
        self.assertTrue(board.sacar_ficha(20, 'Negras'))
        self.assertEqual(board.get_posicion(20), [])
        self.assertEqual(board.get_salida(), ['Negras'])

    def test_sacar_ficha_origen_vacio(self):
        """Testea sacar una ficha de un origen vacío."""
        board = Board()
        board.__board__ = [[] for _ in range(27)]
        self.assertFalse(board.sacar_ficha(20, 'Negras'))

    def test_sacar_ficha_color_incorrecto_en_origen(self):
        """Testea sacar una ficha con color incorrecto en el origen."""
        board = Board()
        board.__board__ = [[] for _ in range(27)]
        board.__board__[20] = ['Blancas']
        self.assertFalse(board.sacar_ficha(20, 'Negras'))

if __name__ == '__main__':
    unittest.main()
