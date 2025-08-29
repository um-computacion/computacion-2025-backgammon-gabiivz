import unittest
from core.dice import Dice

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
    
    

    
        
        
