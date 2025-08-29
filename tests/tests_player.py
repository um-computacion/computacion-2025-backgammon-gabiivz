import unittest
from core.player import Player

class TestPlayer(unittest.TestCase):
    
    def test_jugador_valido(self):
        jugador = Player("Mario", "Blanco")
        self.assertEqual(str(jugador), "Jugador: Mario, Color: Blanco")

    def test_jugador1(self):
        jugador1 = Player("Luci","Blanco")
        self.assertEqual(jugador1.__nombre__, "Luci")
        self.assertNotEqual(jugador1.__color__, "Negro")

    def test_jugador2(self):
        jugador2 = Player("Gabi","Negro")
        self.assertEqual(jugador2.__nombre__, "Gabi")
        self.assertEqual(jugador2.__color__, "Negro")

if __name__ == '__main__':
    unittest.main()
