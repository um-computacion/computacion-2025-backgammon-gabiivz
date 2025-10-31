import unittest
from core.board import Board
from core.exceptions import BackgammonError, MovimientoInvalidoError, FichaEnBarError, DadoNoDisponibleError, PuntoOcupadoError, DireccionInvalidaError, MovimientoFueraDeRangoError, DadosNoTiradosError


class TestBoard(unittest.TestCase):

    def setUp(self):
        """Se ejecuta antes de cada test."""
        self.board = Board()

    def test_posiciones_iniciales(self):
        """Testea la configuración inicial del tablero."""
        self.assertEqual(self.board.__board__[6], ['Blancas'] * 5)
        self.assertEqual(self.board.__board__[8], ['Blancas'] * 3) 
        self.assertEqual(self.board.__board__[13], ['Blancas'] * 5)
        self.assertEqual(self.board.__board__[24], ['Blancas'] * 2)
        self.assertEqual(self.board.__board__[1], ['Negras'] * 2)
        self.assertEqual(self.board.__board__[12], ['Negras'] * 5)
        self.assertEqual(self.board.__board__[17], ['Negras'] * 3)
        self.assertEqual(self.board.__board__[19], ['Negras'] * 5)
        self.assertEqual(self.board.__board__[0], [])   
        self.assertEqual(self.board.__board__[25], [])
        self.assertEqual(self.board.__board__[26], [])

    def test_bar_negras(self):
        """Testea el bar de las fichas negras."""
        self.board.__board__[0] = ['Negras'] * 3
        self.assertEqual(self.board.get_bar_negras(), ['Negras'] * 3)

    def test_bar_blancas(self):
        """Testea el bar de las fichas blancas."""
        self.board.__board__[25] = ['Blancas'] * 4
        self.assertEqual(self.board.get_bar_blancas(), ['Blancas'] * 4)

    def test_distancia_blanca_valida(self):
        """Testea una distancia válida para las fichas blancas."""
        origen = 12
        destino = 7
        self.assertEqual(self.board.distancia_blancas(origen, destino), 5)
    
    def test_distancia_blanca_no_valida(self):
        """Testea una distancia no válida para las fichas blancas."""
        origen = 7
        destino = 12
        self.assertNotEqual(self.board.distancia_blancas(origen, destino), 5)
    
    def test_distancia_negra_valida(self):
        """Testea una distancia válida para las fichas negras."""
        origen = 7
        destino = 12
        self.assertEqual(self.board.distancia_negras(origen, destino), 5)

    def test_distancia_negra_no_valida(self):
        """Testea una distancia no válida para las fichas negras."""
        origen = 12
        destino = 7
        self.assertNotEqual(self.board.distancia_negras(origen, destino), 5)

    def test_movimiento_valido_blancas(self):
        """Testea un movimiento válido para las fichas blancas."""
        color = 'Blancas'
        origen = 12     
        destino = 7
        self.assertTrue(self.board.movimiento_valido(origen, destino, color ))

    def test_movimiento_valido_negras(self):
        """Testea un movimiento válido para las fichas negras."""
        color = 'Negras'
        origen = 7      
        destino = 12
        self.assertTrue(self.board.movimiento_valido(origen, destino, color ))

    def tests_movimiento_fuera_de_tablero(self):
        """Testea un movimiento fuera del tablero."""
        self.assertRaises(MovimientoFueraDeRangoError, self.board.movimiento_valido,-2,-3,'Blancas')
    
    def tests_movimiento_fuera_de_tablero2(self):
        """Testea otro movimiento fuera del tablero."""
        self.assertRaises(MovimientoFueraDeRangoError, self.board.movimiento_valido,28,30,'Negras')

    def test_movimiento_blancas_incorrecto(self):
        """Testea un movimiento incorrecto para las fichas blancas."""
        color = 'Blancas'
        origen = 7      
        destino = 12
        self.assertRaises(DireccionInvalidaError, self.board.movimiento_valido,origen, destino, color )

    def test_movimiento_negras_incorrecto(self):
        """Testea un movimiento incorrecto para las fichas negras."""
        color = 'Negras'
        origen = 17
        destino = 2
        self.assertRaises(DireccionInvalidaError, self.board.movimiento_valido,origen, destino, color )
    
    def test_get_posicion_valida(self):
        """Testea el getter de una posición válida."""
        self.assertEqual(self.board.get_posicion(6), ['Blancas'] * 5)
    
    def test_get_posicion_no_valida(self):
        """Testea el getter de una posición no válida."""
        self.assertIsNone(self.board.get_posicion(30))

    def test_destino_y_origen_invalidos(self):
        """Testea un origen y destino inválidos."""
        self.assertRaises(MovimientoFueraDeRangoError, self.board.movimiento_valido,0, 27, 'Blancas')
        self.assertRaises(MovimientoFueraDeRangoError, self.board.movimiento_valido,27, 0, 'Negras')

    def test_mover_ficha_a_lugar_vacio(self):
        """Testea mover una ficha a un lugar vacío."""
        self.board.__board__[6] = [] 
        self.board.__board__[5] = ['Blancas'] * 5
        self.assertTrue(self.board.mover_ficha(5, 6, 'Blancas'))
        self.assertEqual(self.board.get_posicion(6), ['Blancas'])
        self.assertEqual(self.board.get_posicion(5), ['Blancas'] * 4)
    
    def test_mover_ficha_a_lugar_con_ficha_igual(self):
        """Testea mover una ficha a un lugar con fichas del mismo color."""
        self.board.__board__[5] = ["Blancas"]*5
        self.board.__board__[6] = ["Blancas"]*2
        self.assertTrue(self.board.mover_ficha(5, 6, 'Blancas' ))      
        self.assertEqual(self.board.get_posicion(6), ['Blancas'] * 3)
        self.assertEqual(self.board.get_posicion(5), ['Blancas'] * 4)

    def test_ficha_movida_no_existe(self):
        """Testea mover una ficha que no existe."""
        self.board.__board__[6] = [] 
        self.board.__board__[5] = [] 
        self.assertRaises(MovimientoInvalidoError, self.board.mover_ficha, 5, 6, 'Blancas')
        self.assertEqual(self.board.get_posicion(6), [])
        self.assertEqual(self.board.get_posicion(5), [])
    
    def test_ficha_movida_sumada(self):
        """Testea mover y apilar una ficha."""
        self.board.__board__[6] = ['Blancas'] * 2
        self.board.__board__[5] = ['Blancas'] * 3
        self.assertTrue(self.board.mover_ficha(5, 6, 'Blancas'))
        self.assertEqual(self.board.get_posicion(6), ['Blancas'] * 3)
        self.assertEqual(self.board.get_posicion(5), ['Blancas'] * 2)

    def test_mover_ficha_invalido(self):
        """Testea un movimiento de ficha inválido."""
        self.board.__board__[6] = ['Negras'] * 2
        self.board.__board__[5] = ['Blancas'] * 5
        self.assertRaises(PuntoOcupadoError, self.board.mover_ficha,5, 6, 'Blancas')
        self.assertEqual(self.board.get_posicion(6), ['Negras'] * 2)
        self.assertEqual(self.board.get_posicion(5), ['Blancas'] * 5)

    def test_comer_ficha_invalida(self):
        """Testea una acción de comer ficha inválida."""
        self.board.__board__[6] = ['Negras'] * 3
        self.board.__board__[5] = ['Blancas'] * 5
        ficha_comida = None
        self.assertRaises(PuntoOcupadoError, self.board.comer_ficha, 6, 5, 'Blancas', ficha_comida)
        self.assertEqual(self.board.get_posicion(6), ['Negras'] * 3)
        self.assertEqual(self.board.get_posicion(5), ['Blancas'] * 5)

    def test_comer_ficha_invalida2(self):
        """Testea otra acción de comer ficha inválida."""
        self.board.__board__[6] = ['Negras'] * 2
        self.board.__board__[5] = ['Blancas'] * 5
        ficha_comida = None
        self.assertRaises(PuntoOcupadoError, self.board.comer_ficha, 6, 5, 'Blancas', ficha_comida)
        self.assertEqual(self.board.get_posicion(6), ['Negras'] * 2)
        self.assertEqual(self.board.get_posicion(5), ['Blancas'] * 5)

    def test_comer_ficha_destino_una(self):
        """Testea comer una ficha cuando el destino tiene una."""
        self.board.__board__[8] = ['Negras']
        self.board.__board__[5] = ['Blancas']*2
        self.assertEqual(self.board.comer_ficha(8, 5, 'Blancas','Negras'), None)
        self.assertEqual(self.board.get_posicion(8), ['Blancas'])
        self.assertEqual(self.board.get_posicion(5), ['Blancas'])

    def test_comer_ficha_blanca(self):
        """Testea comer una ficha blanca."""
        self.board.__board__[6] = ['Blancas']
        self.board.__board__[5] = ['Negras'] * 5
        self.assertEqual(self.board.comer_ficha(6, 5, 'Negras', 'Blancas'), None)
        self.assertEqual(self.board.get_posicion(6), ['Negras'])
        self.assertEqual(self.board.get_posicion(5), ['Negras'] * 4)
        self.assertEqual(self.board.get_bar_blancas(), ['Blancas'])

    def test_comer_ficha_vacia(self):
        """Testea una acción de comer en un lugar vacío."""
        self.board.__board__[6] = []
        self.board.__board__[5] = ['Blancas'] * 5
        ficha = 'Blancas'
        ficha_comida = []
        self.assertRaises(MovimientoInvalidoError, self.board.comer_ficha, 6, 5, ficha, ficha_comida)
        self.assertEqual(self.board.get_posicion(6), [])
        self.assertEqual(self.board.get_posicion(5), ['Blancas'] * 5)
        self.assertEqual(self.board.get_bar_negras(), [])

    def test_mover_ficha_comida_blanca_valida(self):
        """Testea mover una ficha blanca comida de forma válida a un punto vacío."""
        self.board.__board__[25] = ['Blancas'] * 2
        self.board.__board__[23] = []
        self.assertTrue(self.board.mover_ficha_comida(25, 23, 'Blancas'))
        self.assertEqual(self.board.get_posicion(23), ['Blancas'])
        self.assertEqual(self.board.__board__[25], ['Blancas'])
    
    def test_mover_ficha_comida_negra_valida(self):
        """Testea mover una ficha negra comida de forma válida a un punto vacío."""
        self.board.__board__[0] = ['Negras'] * 3
        self.board.__board__[5] = []
        self.assertTrue(self.board.mover_ficha_comida(0, 5, 'Negras'))
        self.assertEqual(self.board.get_posicion(5), ['Negras'])
        self.assertEqual(self.board.__board__[0], ['Negras'] * 2)

    def test_mover_ficha_comida_blanca_invalida_rango(self):
        """Testea mover una ficha blanca comida fuera de rango."""
        self.board.__board__[25] = ['Blancas'] * 2
        self.board.__board__[18] = ['Negras']
        with self.assertRaises(MovimientoFueraDeRangoError):
            self.board.mover_ficha_comida(25, 18, 'Blancas')
        self.assertEqual(self.board.get_posicion(18), ['Negras'])
        self.assertEqual(self.board.__board__[25], ['Blancas'] * 2)

    def test_mover_ficha_comida_negra_invalida_rango(self):
        """Testea mover una ficha negra comida fuera de rango."""
        self.board.__board__[0] = ['Negras'] * 3
        self.board.__board__[8] = ['Blancas']
        with self.assertRaises(MovimientoFueraDeRangoError):
            self.board.mover_ficha_comida(0, 8, 'Negras')
        self.assertEqual(self.board.get_posicion(8), ['Blancas'])
        self.assertEqual(self.board.__board__[0], ['Negras'] * 3)

    def test_mover_ficha_comida_blanca_bloqueada(self):
        """Testea mover una ficha blanca comida a un punto bloqueado."""
        self.board.__board__[25] = ['Blancas'] * 1
        self.board.__board__[20] = ['Negras', 'Negras']
        with self.assertRaises(PuntoOcupadoError):
            self.board.mover_ficha_comida(25, 20, 'Blancas')
        self.assertEqual(self.board.get_posicion(20), ['Negras', 'Negras'])
        self.assertEqual(self.board.get_bar_blancas(), ['Blancas'])

    def test_mover_ficha_comida_negra_comiendo(self):
        """Testea mover una ficha negra comida comiendo una ficha rival."""
        self.board.__board__[0] = ['Negras'] * 1
        self.board.__board__[3] = ['Blancas']
        self.assertTrue(self.board.mover_ficha_comida(0, 3, 'Negras'))
        self.assertEqual(self.board.get_posicion(3), ['Negras'])
        self.assertEqual(self.board.get_bar_negras(), [])
        self.assertEqual(self.board.get_bar_blancas(), ['Blancas'])
    
    def test_comer_ficha_destino_con_mas_1ficha_opuesta(self):
        """Testea comer ficha cuando el destino tiene más de una ficha opuesta."""
        self.board.__board__[6] = ['Negras'] * 3
        self.board.__board__[5] = ['Blancas'] * 5
        ficha_comida = None
        self.assertRaises(PuntoOcupadoError, self.board.comer_ficha, 6, 5, 'Blancas', ficha_comida)
        self.assertEqual(self.board.get_posicion(6), ['Negras'] * 3)
        self.assertEqual(self.board.get_posicion(5), ['Blancas'] * 5)
        self.assertEqual(self.board.get_bar_negras(), [])

    def test_sacar_ficha_color_incorrecto(self):
        """Testea sacar ficha con color incorrecto."""
        self.board.__board__ = [[] for _ in range(27)]
        self.board.__board__[11] = ["Negras"]
        self.assertFalse(self.board.sacar_ficha(11, "Blancas"))

    def test_sacar_ficha_permitido_negro_con_fichas_fuera(self):
        """Testea sacar ficha negra no permitido con fichas fuera de casa."""
        self.board.__board__[10] = ["Negras"]
        self.assertRaises(MovimientoInvalidoError, self.board.sacar_ficha, 10, "Negras")

    def test_sacar_ficha_permitido_blanco_con_fichas_fuera(self):
        """Testea sacar ficha blanca no permitido con fichas fuera de casa."""
        self.board.__board__[10] = ["Blancas"]
        self.assertRaises(MovimientoInvalidoError, self.board.sacar_ficha, 10, "Blancas")
        
    def test_get_salida(self):
        """Testea el getter de la zona de salida."""
        self.assertEqual(self.board.get_salida(), self.board.__board__[26])
    
    def test_sacar_ficha_valido_blancas_exitoso(self):
        """Testea que es válido para las blancas sacar fichas."""
        self.board.__board__ = [[] for _ in range(26)]
        self.board.__board__[3] = ['Blancas'] 
        self.assertTrue(self.board.sacar_ficha_valido('Blancas'))

    def test_sacar_ficha_valido_negras_falla(self):
        """Testea que no es válido para las negras sacar fichas si tienen fuera."""
        self.board.__board__[10] = ['Negras'] 
        with self.assertRaises(MovimientoInvalidoError):
            self.board.sacar_ficha_valido('Negras')

    def test_sacar_ficha_exitoso(self):
        """Testea sacar una ficha exitosamente."""
        self.board.__board__ = [[] for _ in range(27)]
        self.board.__board__[20] = ['Negras']
        self.assertTrue(self.board.sacar_ficha(20, 'Negras'))
        self.assertEqual(self.board.get_posicion(20), [])
        self.assertEqual(self.board.get_salida(), ['Negras'])

    def test_sacar_ficha_origen_vacio(self):
        """Testea sacar una ficha de un origen vacío."""
        self.board.__board__ = [[] for _ in range(27)]
        self.assertFalse(self.board.sacar_ficha(20, 'Negras'))

    def test_sacar_ficha_color_incorrecto_en_origen(self):
        """Testea sacar una ficha con color incorrecto en el origen."""
        self.board.__board__ = [[] for _ in range(27)]
        self.board.__board__[20] = ['Blancas']
        self.assertFalse(self.board.sacar_ficha(20, 'Negras'))

    def test_es_destino_legal_vacio(self):
        """Testea que un destino vacío es legal."""
        self.assertTrue(self.board.es_destino_legal(2, "Blancas"))
        self.assertTrue(self.board.es_destino_legal(2, "Negras"))

    def test_es_destino_legal_propio(self):
        """Testea que un destino con fichas propias es legal."""
        self.assertTrue(self.board.es_destino_legal(6, "Blancas"))
        self.assertTrue(self.board.es_destino_legal(1, "Negras"))

    def test_es_destino_legal_comer_ficha_rival(self):
        """Testea que un destino con una ficha rival es legal."""
        self.board.__board__[10] = ["Negras"]
        self.assertTrue(self.board.es_destino_legal(10, "Blancas"))

    def test_es_destino_legal_punto_bloqueado(self):
        """Testea que un destino con dos o más fichas rivales no es legal."""
        self.assertFalse(self.board.es_destino_legal(1, "Blancas"))
        self.assertFalse(self.board.es_destino_legal(6, "Negras"))

    def test_es_destino_legal_para_sacar(self):
        """Testea que el destino 26 (sacar) es legal."""
        self.assertTrue(self.board.es_destino_legal(26, "Blancas"))

    def test_es_destino_legal_fuera_de_rango(self):
        """Testea que las barras (0 y 25) no son destinos legales."""
        self.assertFalse(self.board.es_destino_legal(0, "Blancas"))
        self.assertFalse(self.board.es_destino_legal(25, "Negras"))
        self.assertFalse(self.board.es_destino_legal(-1, "Blancas"))
        
    def test_mover_ficha_comida_negra(self):
        """Testea mover una ficha negra comida de forma válida a un punto vacío."""
        self.board.__board__[0] = ['Negras', 'Negras'] 
        self.board.__board__[3] = []
        self.board.mover_ficha_comida(0, 3, 'Negras')
        self.assertEqual(self.board.get_posicion(3), ['Negras'])
        self.assertEqual(self.board.get_bar_negras(), ['Negras'])

    def test_es_destino_legal_punto_bloqueado(self):
        """Testea es_destino_legal para un punto bloqueado"""
        es_legal = self.board.es_destino_legal(6, 'Negras')
        self.assertFalse(es_legal)
        
if __name__ == '__main__':
    unittest.main()
