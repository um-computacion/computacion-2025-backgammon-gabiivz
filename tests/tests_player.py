import unittest
from core.player import Player

class TestPlayer(unittest.TestCase):
    
    def test_jugador_valido(self):
        """Testea la creación de un jugador válido."""
        jugador = Player("Mario", "Blanco")
        self.assertEqual(str(jugador), "Jugador: Mario, Color: Blanco")

    def test_jugador_no_valido(self):
        """Testea la desigualdad de un jugador."""
        jugador = Player("Ana", "Rojo")
        self.assertNotEqual(str(jugador), "Jugador: Ana, Color: Azul")
    
    def test_jugador_vacio(self):
        """Testea la creación de un jugador vacío."""
        jugador = Player("", "")
        self.assertEqual(str(jugador), "Jugador: , Color: ")

    def test_jugador1(self):
        """Testea los atributos de un jugador."""
        jugador1 = Player("Luci","Blanco")
        self.assertEqual(jugador1.__nombre__, "Luci")
        self.assertNotEqual(jugador1.__color__, "Negro")

    def test_jugador2(self):
        """Testea los atributos de un segundo jugador."""
        jugador2 = Player("Gabi","Negro")
        self.assertEqual(jugador2.__nombre__, "Gabi")
        self.assertEqual(jugador2.__color__, "Negro")

    def test_get_nombre(self):
        """Testea el getter del nombre."""
        jugador = Player("Joaco","Blanco")
        self.assertEqual(jugador.get_nombre(), "Joaco")
        self.assertNotEqual(jugador.get_nombre(), "Pablo")
    
    def test_get_color(self):
        """Testea el getter del color."""
        jugador = Player("Sofi","Negro")
        self.assertEqual(jugador.get_color(), "Negro")
        self.assertNotEqual(jugador.get_color(), "Blanco")
        
if __name__ == '__main__':
    unittest.main()
