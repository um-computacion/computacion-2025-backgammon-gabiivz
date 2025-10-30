import unittest
from core.backgammongame import BackgammonGame
from core.board import Board
from core.player import Player
from core.dice import Dice
from core.exceptions import BackgammonError, MovimientoInvalidoError, FichaEnBarError, DadoNoDisponibleError, PuntoOcupadoError, DireccionInvalidaError, MovimientoFueraDeRangoError, SinMovimientosPosiblesError, TurnoInvalidoError, DadosNoTiradosError, PartidaFinalizadaError

class TestBackgammonGame(unittest.TestCase):

    def test_empieza_jugador_blanco(self):
        """Testea que el jugador blanco empieza."""
        game = BackgammonGame("Gabi", "Gabo")
        self.assertEqual(game.get_turno(), "Blancas")
    
    def test_get_jugador_actual_blancas(self):
        """Testea que se obtiene el jugador blanco actual."""
        game = BackgammonGame("Gabi", "Gabo")
        self.assertEqual(str(game.get_jugador_actual()), "Jugador: Gabi, Color: Blancas")

    def test_get_jugador_actual_negras(self):
        """Testea que se obtiene el jugador negro actual."""
        game = BackgammonGame("Gabi", "Gabo")
        game.cambio_turnos()
        self.assertEqual(str(game.get_jugador_actual()), "Jugador: Gabo, Color: Negras")

    def test_get_turno(self):
        """Testea el getter del turno."""
        game = BackgammonGame("Gabi", "Gabo")
        self.assertEqual(game.get_turno(), "Blancas")
        game.cambio_turnos()
        self.assertEqual(game.get_turno(), "Negras")
    
    def test_turnos_cambiado(self):
        """Testea el cambio de turnos."""
        game = BackgammonGame("Gabi", "Gabo")
        self.assertEqual(game.get_turno(), "Blancas")
        self.assertNotEqual(game.get_turno(), "Negras")
        game.cambio_turnos()
        self.assertEqual(game.get_turno(), "Negras")
        game.cambio_turnos()
        self.assertEqual(game.get_turno(), "Blancas")

    def test_turno_jugador_actual(self):
        """Testea el jugador actual después del cambio de turno."""
        game = BackgammonGame("Gabi", "Gabo")
        jugador = game.get_jugador_actual()
        self.assertEqual(str(jugador), "Jugador: Gabi, Color: Blancas")
        game.cambio_turnos()
        jugador = game.get_jugador_actual()
        self.assertEqual(str(jugador), "Jugador: Gabo, Color: Negras")

    def test_get_board(self):
        """Testea el getter del tablero."""
        game = BackgammonGame("Gabi", "Gabo")
        self.assertIsInstance(game.get_board(), Board)

    def test_get_jugador_blancas(self):
        """Testea el getter del jugador blanco."""
        game = BackgammonGame("Gabi", "Gabo")
        jugador = game.get_jugador_blancas()
        self.assertIsInstance(jugador, Player)
        # Nota: Asumo que corregiste la nomenclatura en Player a __nombre__ y __color__
        # Si no lo hiciste, estos tests fallarán.
        self.assertEqual(jugador.get_color(), "Blancas") 
        self.assertEqual(jugador.get_nombre(), "Gabi")

    def test_get_jugador_negras(self):
        """Testea el getter del jugador negro."""
        game = BackgammonGame("Gabi", "Gabo")
        jugador = game.get_jugador_negras()
        self.assertIsInstance(jugador, Player)
        self.assertEqual(jugador.get_color(), "Negras")
        self.assertEqual(jugador.get_nombre(), "Gabo")

    def test_tirar_dados(self):
        """Testea el lanzamiento de dados."""
        game = BackgammonGame("Gabi", "Gabo")
        resultado = game.tirar_dados()
        self.assertIsInstance(resultado, tuple)
        self.assertEqual(len(resultado), 2)
        self.assertTrue(1 <= resultado[0] <= 6)
        self.assertTrue(1 <= resultado[1] <= 6)

    def test_get_dados(self):
        """Testea el getter de los dados."""
        game = BackgammonGame("Gabi", "Gabo")
        game.tirar_dados()
        movimientos = game.get_dados()
        self.assertIsInstance(movimientos, list)
        self.assertIn(len(movimientos), [2, 4])

    def test_estado_actual(self):
        """Testea el getter del estado del juego."""
        game = BackgammonGame("Gabi", "Gabo")
        estado = game.estado_actual()
        self.assertEqual(estado["turno"], "Blancas")
        self.assertIn("Gabi", estado["jugador_blancas"])
        self.assertIn("Gabo", estado["jugador_negras"])
        self.assertIsInstance(estado["fichas_blancas_en_bar"], int)
        self.assertIsInstance(estado["fichas_negras_en_bar"], int)
        self.assertIsInstance(estado["fichas_blancas_sacadas"], int)
        self.assertIsInstance(estado["fichas_negras_sacadas"], int)
        self.assertIsInstance(estado["dados"], list)
        self.assertIsInstance(estado["tablero"], dict)

    def test_turno_completo_true(self):
        """Testea que el turno está completo cuando no quedan dados."""
        game = BackgammonGame("Gabi", "Gabo")
        game.__dado__.__movimientos__ = []
        self.assertTrue(game.turno_completo())

    def test_turno_completo_false(self):
        """Testea que el turno está incompleto cuando quedan dados."""
        game = BackgammonGame("Gabi", "Gabo")
        game.__dado__.__movimientos__ = [1]
        self.assertFalse(game.turno_completo())

    def test_get_ganador_none(self):
        """Testea que no hay ganador inicialmente."""
        game = BackgammonGame("Gabi", "Gabo")
        self.assertIsNone(game.get_ganador())
    
    def test_get_ganador_blancas(self):
        """Testea que el jugador blanco gana."""
        game = BackgammonGame("Gabi", "Gabo")
        for _ in range(15):
            game.__fichas_sacadas_blancas__.append("Blancas")       
        self.assertEqual(game.get_ganador(), "Gabi")

    def test_get_ganador_negras(self):
        """Testea que el jugador negro gana."""
        game = BackgammonGame("Gabi", "Gabo")
        for _ in range(15):
            game.__fichas_sacadas_negras__.append("Negras")
        self.assertEqual(game.get_ganador(), "Gabo")

    def test_usar_dados_no_disponible(self):
        """Testea el uso de un dado no disponible."""
        game = BackgammonGame("Gabi", "Gabo")
        game.__dado__.__movimientos__ = [2]
        with self.assertRaises(DadoNoDisponibleError):
            game.usar_dados(1)

    def test_usar_dados_exitoso(self):
        """Testea el uso exitoso de un dado."""
        game = BackgammonGame("Gabi", "Gabo")
        game.__dado__.__movimientos__ = [2, 3]
        game.usar_dados(2)
        self.assertEqual(game.get_dados(), [3])
        game.usar_dados(3)
        self.assertEqual(game.get_dados(), [])

    def test_dados_vacios(self):
        """Testea la lista de dados vacía."""
        game = BackgammonGame("Gabi", "Gabo")
        game.__dado__.__movimientos__ = []
        with self.assertRaises(DadoNoDisponibleError):
            game.usar_dados(1)
        self.assertEqual(game.get_dados(), [])

    def test_cubre_movimiento_regular_negras_comer(self):
        """Testea movimiento regular de negras comiendo una ficha."""
        game = BackgammonGame("Gabi", "Gabo")
        game.cambio_turnos() 
        game.__dado__.__movimientos__ = [5, 2]
        board = game.get_board()
        board.__board__[7] = ['Blancas'] 
        game.mover_ficha(2, 7)
        self.assertEqual(game.get_dados(), [2])
        self.assertEqual(board.get_posicion(7), ['Negras']) 
        self.assertEqual(board.get_bar_blancas(), ['Blancas']) 

    def test_cubre_movimiento_regular_blancas_stack(self):
        """Testea movimiento regular de blancas apilando fichas."""
        game = BackgammonGame("Gabi", "Gabo") # Turno de Blancas
        game.__dado__.__movimientos__ = [4, 2]
        board = game.get_board()
        board.__board__[22] = ['Blancas'] 
        board.__board__[18] = ['Blancas'] 
        game.mover_ficha(22, 18) 
        self.assertEqual(game.get_dados(), [2])
        self.assertEqual(board.get_posicion(18), ['Blancas', 'Blancas'])
        self.assertEqual(board.get_posicion(22), [])

    def test_cubre_mover_blancas_bar_dado_incorrecto(self):
        """Testea mover ficha blanca desde bar con dado incorrecto."""
        game = BackgammonGame("Gabi", "Gabo") 
        game.__dado__.__movimientos__ = [3, 4]
        board = game.get_board()
        board.__board__[25] = ['Blancas'] 
        with self.assertRaises(DadoNoDisponibleError):
            game.mover_ficha(25, 20)

    def test_cubre_sacar_ficha_blancas_exitoso(self):
        """Testea sacar una ficha blanca exitosamente."""
        game = BackgammonGame("Gabi", "Gabo")
        game.__dado__.__movimientos__ = [4, 5]
        board = game.get_board()
        board.__board__ = [[] for _ in range(27)]
        board.__board__[4] = ['Blancas']
        game.mover_ficha(4, 26) 
        self.assertEqual(game.get_dados(), [5])
        self.assertEqual(game.estado_actual()["fichas_blancas_sacadas"], 1)

    def test_cubre_sacar_ficha_negras_dado_mayor(self):
        """Testea sacar ficha negra con un dado mayor al necesario."""
        game = BackgammonGame("Gabi", "Gabo")
        game.cambio_turnos() 
        game.__dado__.__movimientos__ = [6, 5]
        board = game.get_board()
        board.__board__ = [[] for _ in range(27)]
        board.__board__[22] = ['Negras'] 
        game.mover_ficha(22, 26) 
        self.assertEqual(game.get_dados(), [6]) 
        self.assertEqual(game.estado_actual()["fichas_negras_sacadas"], 1)

    def test_cubre_sacar_ficha_dado_invalido(self):
        """Testea sacar ficha con un dado inválido."""
        game = BackgammonGame("Gabi", "Gabo")
        game.__dado__.__movimientos__ = [1, 2] 
        board = game.get_board()
        board.__board__ = [[] for _ in range(27)]
        board.__board__[4] = ['Blancas'] 
        with self.assertRaises(DadoNoDisponibleError):
            game.mover_ficha(4, 26)

    def test_cubre_turno_completo_con_ganador(self):
        """Testea que el turno no se considera completo si hay un ganador."""
        game = BackgammonGame("Gabi", "Gabo")
        game.__dado__.__movimientos__ = []
        for _ in range(15):
            game.__fichas_sacadas_blancas__.append("Blancas")
        self.assertFalse(game.turno_completo())

    def test_cubre_mover_ficha_sin_dados_lanza_error(self):
        """Testea que mover ficha sin haber tirado los dados lanza error."""
        game = BackgammonGame("Gabi", "Gabo")
        game.__dado__.__movimientos__ = [] 
        with self.assertRaises(DadosNoTiradosError):
            game.mover_ficha(12, 10)

    def test_cubre_error_blancas_debe_mover_de_bar(self):
        """Testea error cuando una ficha blanca debe salir del bar."""
        game = BackgammonGame("Gabi", "Gabo") 
        game.__dado__.__movimientos__ = [3, 4]
        board = game.get_board()
        board.__board__[25] = ['Blancas']  
        with self.assertRaises(FichaEnBarError):
            game.mover_ficha(12, 8)

    def test_cubre_mover_ficha_negra_desde_bar_dado_invalido(self):
        """Testea mover ficha negra desde bar con dado inválido."""
        game = BackgammonGame("Gabi", "Gabo")
        game.cambio_turnos() 
        game.__dado__.__movimientos__ = [1, 2]  
        board = game.get_board()
        board.__board__[0] = ['Negras']
        with self.assertRaises(DadoNoDisponibleError):
            game.mover_ficha(0, 5)

    def test_cubre_movimiento_regular_dado_invalido(self):
        """Testea movimiento regular con un dado inválido."""
        game = BackgammonGame("Gabi", "Gabo") 
        game.__dado__.__movimientos__ = [1, 2]  
        board = game.get_board()
        board.__board__[12] = ['Blancas']
        with self.assertRaises(DadoNoDisponibleError):
            game.mover_ficha(12, 8)

    def test_cubre_mover_blancas_desde_bar_exitoso(self):
        """Testea mover ficha blanca desde el bar exitosamente."""
        game = BackgammonGame("Gabi", "Gabo")
        game.__dado__.__movimientos__ = [4, 5]
        board = game.get_board()
        board.__board__[25] = ['Blancas']
        game.mover_ficha(25, 21)
        self.assertEqual(game.get_dados(), [5])
        self.assertEqual(board.get_posicion(25), [])
        self.assertEqual(board.get_posicion(21), ['Blancas'])
    
    def test_cubre_mover_desde_bar_dado_invalido(self):
        """Testea mover desde el bar con un dado inválido."""
        game = BackgammonGame("Gabi", "Gabo")
        game.cambio_turnos() 
        game.__dado__.__movimientos__ = [1, 2] 
        board = game.get_board()
        board.__board__[0] = ['Negras'] 
        with self.assertRaises(DadoNoDisponibleError):
            game.mover_ficha(0, 5)

    def test_cubre_error_negras_debe_mover_de_bar(self):
        """Testea error cuando una ficha negra debe salir del bar."""
        game = BackgammonGame("Gabi", "Gabo")
        game.cambio_turnos() 
        game.__dado__.__movimientos__ = [3, 4]
        board = game.get_board()
        board.__board__[0] = ['Negras'] 
        with self.assertRaises(FichaEnBarError):
            game.mover_ficha(10, 7) 

    def test_cubre_sacar_ficha_con_fichas_fuera(self):
        """Testea error al sacar ficha cuando aún hay fichas fuera de la casa."""
        game = BackgammonGame("Gabi", "Gabo") # Turno Blancas
        game.__dado__.__movimientos__ = [3, 4]
        board = game.get_board()
        board.__board__[10] = ['Blancas']
        board.__board__[4] = ['Blancas']
        with self.assertRaises(MovimientoInvalidoError):
            game.mover_ficha(4, 26)

    def test_cubre_sacar_ficha_blancas_dado_mayor(self):
        """Testea sacar ficha blanca con un dado mayor al necesario."""
        game = BackgammonGame("Gabi", "Gabo") 
        game.__dado__.__movimientos__ = [6, 5]   
        board = game.get_board()
        board.__board__ = [[] for _ in range(27)]
        board.__board__[4] = ['Blancas'] 
        game.mover_ficha(4, 26) 
        self.assertEqual(game.get_dados(), [6]) 
        self.assertEqual(game.estado_actual()["fichas_blancas_sacadas"], 1)
        self.assertEqual(board.get_posicion(4), [])

if __name__ == '__main__':
    unittest.main()