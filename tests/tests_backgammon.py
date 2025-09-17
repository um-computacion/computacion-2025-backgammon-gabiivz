import unittest
from core.backgammongame import BackgammonGame

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


    def test_movimientos_tipo_lista(self):
        game = BackgammonGame("Gabi", "Gabo")
        movimientos = game.movimientos_al_tirar_dado()
        self.assertIsInstance(movimientos, list)

    def test_movimientos_cantidad_valores(self):
        game = BackgammonGame("Gabi", "Gabo")
        movimientos = game.movimientos_al_tirar_dado()
        self.assertIn(len(movimientos), [2, 4])

    def test_movimientos_doble(self):
        game = BackgammonGame("Gabi", "Gabo")
        game.__dado1__.tirar = lambda: 6
        game.__dado2__.tirar = lambda: 6
        movimientos = game.movimientos_al_tirar_dado()
        self.assertEqual(movimientos, [6, 6, 6, 6])

    def test_movimientos_no_doble(self):
        game = BackgammonGame("Gabi", "Gabo")
        game.__dado1__.tirar = lambda: 3
        game.__dado2__.tirar = lambda: 5
        movimientos = game.movimientos_al_tirar_dado()
        self.assertEqual(movimientos, [3, 5])

    def test_turno_jugador_actual(self):
        game = BackgammonGame("Gabi", "Gabo")
        jugador = game.get_jugador_actual()
        self.assertEqual(str(jugador), "Jugador: Gabi, Color: Blancas")
        game.cambio_turnos()
        jugador = game.get_jugador_actual()
        self.assertEqual(str(jugador), "Jugador: Gabo, Color: Negras")

    


if __name__ == '__main__':
    unittest.main()
    
