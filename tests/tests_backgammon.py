import unittest
from core.backgammongame import BackgammonGame
from core.board import Board
from core.player import Player
from core.checker import Checker

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
        game = BackgammonGame("Gabi", "Gabo")
        game.tirar_dados()()  # Tirar los dados primero
        movimientos = game.get_dados()()
        self.assertIsInstance(movimientos, list)
        self.assertIn(len(movimientos), [2, 4])


    
    #def test_ganador_valido(self):
     #   game = BackgammonGame("Gabi", "Gabo")

    

    def test_ganador_no_valido(self):
        game = BackgammonGame("Gabi", "Gabo")
        self.assertIsNone(game.get_ganador())



    def test_mover_ficha_con_fichas_en_bar(self):
        game = BackgammonGame("Gabi", "Gabo")
        board = game.get_board()

        # Agregamos ficha al bar
        board.__board__[0] = ["Blancas"]

        # Intentar mover desde 1 a 5
        board.__board__[1] = ["Blancas"]
        board.__board__[5] = []

        game.__dado__.movimientos = [4]

        with self.assertRaises(ValueError):
            game.mover_ficha(1, 5)

    def test_mover_ficha_movimiento_no_en_dados(self):
        game = BackgammonGame("Gabi", "Gabo")
        board = game.get_board()

        # No hay fichas en el bar
        board.__board__[0] = []

        # Movimiento es de 1 a 5 (4), pero dado no lo permite
        board.__board__[1] = ["Blancas"]
        board.__board__[5] = []

        game.__dado__.movimientos = [3]  # 4 no está en los dados

        with self.assertRaises(ValueError):
            game.mover_ficha(1, 5)

    def test_mover_ficha_sin_ficha_en_origen(self):
        game = BackgammonGame("Gabi", "Gabo")
        board = game.get_board()

        # No hay fichas en la posición 1
        board.__board__[1] = []
        board.__board__[5] = []

        game.__dado__.movimientos = [4]

        with self.assertRaises(ValueError):
            game.mover_ficha(1, 5)

    def test_mover_ficha_no_permitido_por_board(self):
        game = BackgammonGame("Gabi", "Gabo")
        board = game.get_board()

        board.__board__[1] = ["Blancas"]
        board.__board__[5] = []

        # Los dados permiten el movimiento
        game.__dado__.movimientos = [4]

        # Simular que board.mover_ficha devuelve False
        original_mover = board.mover_ficha
        board.mover_ficha = lambda o, d, f: False

        with self.assertRaises(ValueError):
            game.mover_ficha(1, 5)

        # Restaurar el método original
        board.mover_ficha = original_mover
        



if __name__ == '__main__':
    unittest.main()
    
