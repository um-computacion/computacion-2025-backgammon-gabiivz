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

    def test_usar_dado_no_disponible(self):
        game = BackgammonGame("Gabi", "Gabo")
        game.__dado__.movimientos = [3, 5]
        self.assertRaises(DadoNoDisponibleError,game.usar_dados,4)

    def test_estado_actual(self):
        game = BackgammonGame("Gabi", "Gabo")
        estado = game.estado_actual()
        self.assertIsInstance(estado, dict)  # devuelve un diccionario
        self.assertEqual(estado["turno"], "Blancas")  # turno inicial es Blancas
        self.assertIn("Gabi", estado["jugador_blancas"])  # jugador blancas es Gabi
        self.assertIn("Gabo", estado["jugador_negras"])  # jugador negras es Gabo
        self.assertIsInstance(estado["dados"], list)  # los dados son una lista




if __name__ == '__main__':
    unittest.main()