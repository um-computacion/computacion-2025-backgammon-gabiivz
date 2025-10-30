import unittest
from core.dice import Dice
from unittest.mock import patch

class TestDice(unittest.TestCase):

    def test_tirar_numero_valido(self):
        """Testea que el rango de la tirada del dado es válido."""
        dado = Dice()
        self.assertTrue(all( 1<= x <=6 for x in dado.tirar()))
    
    def test_tirar_numero_no_valido(self):
        """Testea que no hay valores de dado inválidos."""
        dado = Dice()
        self.assertFalse(any( x <1 or x >6 for x in dado.tirar()))
    
    def test_inicializacion(self):
        """Testea la inicialización de los dados."""
        dado = Dice()
        self.assertEqual(dado.__movimientos__, [])

    @patch('random.randint', side_effect=[5, 2])
    def test_tirar_dados_simples(self, randint_patched):
        """Testea una tirada de dados simple."""
        dado = Dice()
        resultado = dado.tirar()
        
        self.assertEqual(resultado, (5, 2))
        self.assertEqual(dado.__movimientos__, [5, 2])
        self.assertEqual(randint_patched.call_count, 2)

    @patch('random.randint', return_value=4)
    def test_tirar_dados_dobles(self, randint_patched):
        """Testea una tirada de dados dobles."""
        dado = Dice()
        resultado = dado.tirar()
        
        self.assertEqual(resultado, (4, 4))
        self.assertEqual(dado.__movimientos__, [4, 4, 4, 4])
        self.assertEqual(randint_patched.call_count, 2)


    def test_reiniciar_dados(self):
        """Testea el reinicio de los dados."""
        with patch('random.randint', side_effect=[5, 3]):
            dado = Dice()
            dado.tirar()
            
            resultado = dado.reiniciar_dados()
            
            self.assertEqual(resultado, (0, 0))
            self.assertEqual(dado.__movimientos__, [])

    @patch('random.randint', side_effect=Exception("Error de dados!"))
    def test_error_al_tirar(self, randint_patched):
        """Testea el manejo de errores al tirar los dados."""
        dado = Dice()
        with self.assertRaises(Exception):
            dado.tirar()

    def test_get_movimientos(self):
        """Testea obtener los movimientos actuales de los dados."""
        dado = Dice()
        dado.__movimientos__ = [2, 5]
        movimientos = dado.get_movimientos()
        
        self.assertEqual(movimientos, [2, 5])
    
    def test_get_movimientos_vacio(self):
        """Testea obtener los movimientos de los dados cuando está vacío."""
        dado = Dice()
        movimientos = dado.get_movimientos()
        self.assertEqual(movimientos, [])

    def test_tiene_movimientos_true(self):
        """Testea si hay movimientos de dados disponibles."""
        dado = Dice()
        dado.__movimientos__ = [1, 3]
        self.assertTrue(dado.tiene_movimientos())

    def test_tiene_movimientos_false(self):
        """Testea si no hay movimientos de dados disponibles."""
        dado = Dice()
        dado.__movimientos__ = []
        self.assertFalse(dado.tiene_movimientos())

if __name__ == '__main__':
    unittest.main()






