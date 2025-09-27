import unittest
from core.checker import Checker

class TestChecker(unittest.TestCase):

    def test_get_ficha(self):
        checker = Checker("Ficha1", "Blanco", "Juan")
        self.assertEqual(checker.get_ficha(), "Ficha1")
    
    
    def test_jugador_y_color(self):
        checker = Checker("Ficha1", "Blanco", "Juan")
        self.assertEqual(checker.get_color_y_jugador(), ("Blanco", "Juan"))

    def test_agregar_ficha_sacada_blancas(self):
        checker = Checker("Blancas", "Blancas", "Ana")
        checker.agregar_ficha_sacada_blancas("Blancas")
        self.assertEqual(checker.get_fichas_sacadas_blancas(), ["Blancas"])
        with self.assertRaises(ValueError):
            checker.agregar_ficha_sacada_blancas("Negras")

    def test_agregar_ficha_sacada_negras(self):
        checker = Checker("Negras", "Negras", "Luis")
        checker.agregar_ficha_sacada_negras("Negras")
        self.assertEqual(checker.get_fichas_sacadas_negras(), ["Negras"])
        with self.assertRaises(ValueError):
            checker.agregar_ficha_sacada_negras("Blancas")

    def test_get_fichas_sacadas_blancas_vacio(self):
        checker = Checker("Blancas", "Blancas", "Ana")
        self.assertEqual(checker.get_fichas_sacadas_blancas(), [])

    def test_get_fichas_sacadas_negras_vacio(self):
        checker = Checker("Negras", "Negras", "Luis")
        self.assertEqual(checker.get_fichas_sacadas_negras(), [])
    
    def test_get_fichas_sacadas_blancas_varias(self):
        checker = Checker("Blancas", "Blancas", "Ana")
        checker.agregar_ficha_sacada_blancas("Blancas")
        checker.agregar_ficha_sacada_blancas("Blancas")
        self.assertEqual(checker.get_fichas_sacadas_blancas(), ["Blancas", "Blancas"])

    def test_get_fichas_sacadas_negras_varias(self):
        checker = Checker("Negras", "Negras", "Luis")
        checker.agregar_ficha_sacada_negras("Negras")
        checker.agregar_ficha_sacada_negras("Negras")
        self.assertEqual(checker.get_fichas_sacadas_negras(), ["Negras", "Negras"])
    

    
if __name__ == '__main__':
    unittest.main()


