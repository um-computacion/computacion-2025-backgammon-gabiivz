import unittest
from core.backgammongame import BackgammonGame
from core.board import Board
from core.player import Player
from core.checker import Checker
from unittest.mock import Mock,patch 
from core.dice import Dice
from core.exceptions import BackgammonError, MovimientoInvalidoError, FichaEnBarError, DadoNoDisponibleError, PuntoOcupadoError, DireccionInvalidaError, MovimientoFueraDeRangoError, SinMovimientosPosiblesError, TurnoInvalidoError, DadosNoTiradosError, PartidaFinalizadaError

class TestBackgammonGame(unittest.TestCase):
    def test_empieza_jugador_blanco(self):
        game = BackgammonGame("Gabi", "Gabo")
        self.assertEqual(game.get_turno(), "Blancas")
    
    def test_get_jugador_actual_blancas(self):
        game = BackgammonGame("Gabi", "Gabo")
        self.assertEqual(str(game.get_jugador_actual()), "Jugador: Gabi, Color: Blancas")

    def test_get_jugador_actual_negras(self):
        game = BackgammonGame("Gabi", "Gabo")
        game.cambio_turnos()
        self.assertEqual(str(game.get_jugador_actual()), "Jugador: Gabo, Color: Negras")

    def test_get_turno(self):
        game = BackgammonGame("Gabi", "Gabo")
        self.assertEqual(game.get_turno(), "Blancas")
        game.cambio_turnos()
        self.assertEqual(game.get_turno(), "Negras")
    
    def test_turnos_cambiado(self):
        game = BackgammonGame("Gabi", "Gabo")
        self.assertEqual(game.get_turno(), "Blancas")
        self.assertNotEqual(game.get_turno(), "Negras")
        game.cambio_turnos()
        self.assertEqual(game.get_turno(), "Negras")
        game.cambio_turnos()
        self.assertEqual(game.get_turno(), "Blancas")

    def test_turno_jugador_actual(self):
        game = BackgammonGame("Gabi", "Gabo")
        jugador = game.get_jugador_actual()
        self.assertEqual(str(jugador), "Jugador: Gabi, Color: Blancas")
        game.cambio_turnos()
        jugador = game.get_jugador_actual()
        self.assertEqual(str(jugador), "Jugador: Gabo, Color: Negras")

    def test_get_board(self):
        game = BackgammonGame("Gabi", "Gabo")
        self.assertIsInstance(game.get_board(), Board)

    def test_get_jugador_blancas(self):
        game = BackgammonGame("Gabi", "Gabo")
        jugador = game.get_jugador_blancas()
        self.assertIsInstance(jugador, Player)
        self.assertEqual(jugador.__color__, "Blancas")
        self.assertEqual(jugador.__nombre__, "Gabi")

    def test_get_jugador_negras(self):
        game = BackgammonGame("Gabi", "Gabo")
        jugador = game.get_jugador_negras()
        self.assertIsInstance(jugador, Player)
        self.assertEqual(jugador.__color__, "Negras")
        self.assertEqual(jugador.__nombre__, "Gabo")

    def test_tirar_dados(self):
        game = BackgammonGame("Gabi", "Gabo")
        resultado = game.tirar_dados()()
        self.assertIsInstance(resultado, tuple)
        self.assertEqual(len(resultado), 2)
        self.assertTrue(1 <= resultado[0] <= 6)
        self.assertTrue(1 <= resultado[1] <= 6)

    def test_get_dados(self):
        """Test corregido: get_dados() retorna una lista, no una función"""
        game = BackgammonGame("Gabi", "Gabo")
        game.tirar_dados()()  # Tirar los dados primero
        movimientos = game.get_dados()  # Sin el segundo ()
        self.assertIsInstance(movimientos, list)
        self.assertIn(len(movimientos), [2, 4])

    def test_ganador_no_valido(self):
        game = BackgammonGame("Gabi", "Gabo")
        self.assertIsNone(game.get_ganador())

    def test_usar_dados(self):
        game = BackgammonGame("Gabi", "Gabo")
        game.__dado__.movimientos = [3, 5]
        self.assertEqual(game.usar_dados(3),None)

    def test_usar_dado_invalido(self):
        game = BackgammonGame("Gabi", "Gabo")
        game.__dado__.movimientos = [3, 5]
        self.assertNotEqual(game.usar_dados(3),[3,5])

    #def test_mover_ficha_en_bar(self):
     #   game = BackgammonGame("Gabi", "Gabo")
      #  len(game.__board__.get_bar())>0
       # game.get_board().__board__[3] = ["Blancas"]    
        #game.get_board().__board__[1] = []    #
        #game.__dado__.movimientos = [3, 5]
       # with self.assertRaises(FichaEnBarError):
        #    game.mover_ficha(3,1)

    def test_mover_ficha_comida_punto_ocupado(self):
        game = BackgammonGame("Gabi", "Gabo")
        game.get_board().__board__[0] = ["Blancas"]    # Simula que hay fichas blancas en el bar
        def no_ingresa(destino, ficha):    # Simula que no se puede ingresar la ficha en ese punto
            return False
        game.get_board().mover_ficha_comida = no_ingresa
        game.__dado__.movimientos = [5]
        self.assertRaises(PuntoOcupadoError,game.mover_ficha,0, 5)

    def test_turno_completo_false_por_dados(self):
        game = BackgammonGame("Gabi", "Gabo")
        game.__dado__.movimientos = [3]
        # No hay ganador, así que get_ganador debe devolver None por defecto
        self.assertFalse(game.turno_completo())

    #def test_turno_completo_false_por_ganador(self):
     #   game = BackgammonGame("Gabi", "Gabo")
      #  game.get_board().__board__[1] = ["Blancas"]
       # game.get_board().__board__[4] = []
        #game.__dado__.movimientos = [3, 5]
        #game.mover_ficha(1, 4)
        #self.assertEqual(game.get_board().__board__[1], [])
        #self.assertEqual(game.get_board().__board__[4], ["Blancas"])
        #self.assertEqual(game.__dado__.movimientos, [5])

    def _test_mover_fichas_negras(self):
        game = BackgammonGame("Gabi", "Gabo")
        game.cambio_turnos()   #ahora es el turno de las negras
        game.get_board().__board__[24] = ["Negras"]
        game.get_board().__board__[21] = []
        game.__dado__.movimientos = [3, 5]
        game.mover_ficha(24, 21)
        self.assertEqual(game.get_board().__board__[24], [])
        self.assertEqual(game.get_board().__board__[21], ["Negras"])
        self.assertEqual(game.__dado__.movimientos, [5])

if __name__ == '__main__':
    unittest.main()