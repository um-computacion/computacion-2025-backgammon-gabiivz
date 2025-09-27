import unittest
from core.player import Player

class TestPlayer(unittest.TestCase):
    
    def test_jugador_valido(self):
        jugador = Player("Mario", "Blanco")
        self.assertEqual(str(jugador), "Jugador: Mario, Color: Blanco")

    def test_jugador_no_valido(self):
        jugador = Player("Ana", "Rojo")
        self.assertNotEqual(str(jugador), "Jugador: Ana, Color: Azul")
    
    def test_jugador_vacio(self):
        jugador = Player("", "")
        self.assertEqual(str(jugador), "Jugador: , Color: ")

    def test_jugador1(self):
        jugador1 = Player("Luci","Blanco")
        self.assertEqual(jugador1.__nombre__, "Luci")
        self.assertNotEqual(jugador1.__color__, "Negro")

    def test_jugador2(self):
        jugador2 = Player("Gabi","Negro")
        self.assertEqual(jugador2.__nombre__, "Gabi")
        self.assertEqual(jugador2.__color__, "Negro")

    def test_get_nombre(self):
        jugador = Player("Joaco","Blanco")
        self.assertEqual(jugador.get_nombre(), "Joaco")
        self.assertNotEqual(jugador.get_nombre(), "Pablo")
        
if __name__ == '__main__':
    unittest.main()
