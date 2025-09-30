import unittest
from core.dice import Dice
from unittest.mock import patch

class TestDice(unittest.TestCase):

    def test_tirar_numero_valido(self):
        dado = Dice()
        self.assertTrue(all( 1<= x <=6 for x in dado.tirar()))
    
    def test_tirar_numero_no_valido(self):
        dado = Dice()
        self.assertFalse(any( x <1 or x >6 for x in dado.tirar()))
    
    def test_inicializacion(self):
        """Test que los dados se inicializan correctamente."""
        dado = Dice()
        self.assertEqual(dado.movimientos, [])

    @patch('random.randint', side_effect=[5, 2])
    def test_tirar_dados_simples(self, randint_patched):
        """Test tirar dados no dobles."""
        dado = Dice()
        resultado = dado.tirar()
        
        self.assertEqual(resultado, (5, 2))
        self.assertEqual(dado.movimientos, [5, 2])
        self.assertEqual(randint_patched.call_count, 2)

    @patch('random.randint', return_value=4)
    def test_tirar_dados_dobles(self, randint_patched):
        """Test tirar dados dobles (4 movimientos)."""
        dado = Dice()
        resultado = dado.tirar()
        
        self.assertEqual(resultado, (4, 4))
        self.assertEqual(dado.movimientos, [4, 4, 4, 4])
        self.assertEqual(randint_patched.call_count, 2)

    def test_usar_dado_exitoso(self):
        """Test que usar_dado() remueve correctamente un dado."""
        with patch('random.randint', side_effect=[3, 5]):
            dado = Dice()
            dado.tirar()
            
            dado.usar_dado(3)
            self.assertEqual(dado.movimientos, [5])
            
            dado.usar_dado(5)
            self.assertEqual(dado.movimientos, [])
    
    def test_usar_dado_no_disponible(self):
        """Test error al usar un dado que no está disponible."""
        with patch('random.randint', side_effect=[3, 5]):
            dado = Dice()
            dado.tirar()
            
            with self.assertRaises(ValueError):
                dado.usar_dado(6)

    def test_tiene_movimientos(self):
        """Test verificar si quedan dados disponibles."""
        dado = Dice()
        self.assertFalse(dado.tiene_movimientos())
        
        with patch('random.randint', side_effect=[2, 4]):
            dado.tirar()
            self.assertTrue(dado.tiene_movimientos())
            
            dado.usar_dado(2)
            dado.usar_dado(4)
            self.assertFalse(dado.tiene_movimientos())

    def test_reiniciar_dados(self):
        """Test que reiniciar_dados() resetea todo."""
        with patch('random.randint', side_effect=[5, 3]):
            dado = Dice()
            dado.tirar()
            
            resultado = dado.reiniciar_dados()
            
            self.assertEqual(resultado, (0, 0))
            self.assertEqual(dado.movimientos, [])

    @patch('random.randint', side_effect=Exception("Error de dados!"))
    def test_error_al_tirar(self, randint_patched):
        """Test que se maneja error en random.randint."""
        dado = Dice()
        with self.assertRaises(Exception):
            dado.tirar()

if __name__ == '__main__':
    unittest.main()
    
    

    
        
        
