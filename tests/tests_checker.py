import unittest
from core.checker import Checker

class TestChecker(unittest.TestCase):

    def test_get_ficha(self):
        checker = Checker("Ficha1", "Blanco", 5, "Juan")
        self.assertEqual(checker.get_ficha(), "Ficha1")
    
    def test_get_posicion(self):
        checker = Checker("Ficha1", "Blanco", 10, "Juan")
        self.assertEqual(checker.get_posicion(), 10)
    
    def test_jugador_y_color(self):
        checker = Checker("Ficha1", "Blanco", 5, "Juan")
        self.assertEqual(checker.get_color_y_jugador(), ("Blanco", "Juan"))
    
if __name__ == '__main__':
    unittest.main()


