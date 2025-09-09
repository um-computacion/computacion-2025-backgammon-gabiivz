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
    
    def test_movimientos_no_dobles(self):
        dado = Dice()
        dado.dado1 = 3
        dado.dado2 = 5
        self.assertEqual(dado.movimientos(), [3,5])
    
    def test_movimientos_dobles(self):
        dado = Dice()
        dado.dado1 = 4
        dado.dado2 = 4  
        self.assertEqual(dado.movimientos(), [4,4,4,4])

    @patch('random.randint', side_effect=[5, 2])
    def test_simple(self, randint_patched):
        dado = Dice()
        dado.tirar()
        dice = dado.movimientos()
        self.assertEqual(len(dice), 2)
        self.assertEqual(dice[0], 5)
        self.assertEqual(dice[1], 2)
        self.assertTrue(randint_patched.called)
        self.assertEqual(randint_patched.call_count, 2)

    # Test dobles: testea que si salen dobles, se devuelven 4 movimientos iguales
    @patch('random.randint', return_value=3)
    def test_dobles(self, randint_patched):
        dado = Dice()
        dado.tirar()
        dice = dado.movimientos()
        self.assertEqual(len(dice), 4)
        self.assertEqual(dice[0], 3)
        self.assertEqual(dice[1], 3)
        self.assertEqual(dice[2], 3)
        self.assertEqual(dice[3], 3)
        self.assertTrue(randint_patched.called)
        self.assertEqual(randint_patched.call_count, 2)

    #test error: verifica que si hay un error en random.randint, se maneja correctamente
    @patch('random.randint', side_effect=Exception("Error de dados!"))
    def test_error(self, randint_patched):
        dado = Dice()
        with self.assertRaises(Exception):
            dado.tirar()
        self.assertTrue(randint_patched.called)
        self.assertEqual(randint_patched.call_count, 1)
    
    
    def test_multiples_casos(self):
        with patch('random.randint', side_effect=[4, 1]) as randint_patched:
            dado = Dice()
            dado.tirar()
            dice = dado.movimientos()
            self.assertEqual(len(dice), 2)
            self.assertEqual(dice, [4, 1])
            self.assertTrue(randint_patched.called)
            self.assertEqual(randint_patched.call_count, 2)


if __name__ == '__main__':
    unittest.main()
    
    

    
        
        
