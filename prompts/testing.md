# Prompt: Testing de clase Dice con @patch

### Herramienta utilizada:
Claude.ai

## Contexto
Tengo una clase `Dice` en Python que simula el lanzamiento de dos dados:

```python
import random

class Dice:
    def __init__(self):
        self.__dado1__ = 0
        self.__dado2__ = 0

    def tirar(self):
        self.dado1 = random.randint(1,6)
        self.dado2 = random.randint(1,6)
        return self.dado1, self.dado2

    def movimientos(self):
        if self.dado1 == self.dado2:
            return [self.dado1]*4
        else:
            return [self.dado1, self.dado2]
```

## Mi duda inicial
Tenía dos tests diferentes y quería saber si testean lo mismo:

```python
@patch('random.randint', side_effect=[5, 2])
def test_simple(self, randint_patched):
    dice = Dice.tirar(self)  # ¿Esto está bien?
    # ... verificaciones

@patch('random.randint', side_effect=[5, 2])
def test_tirada_simple(self, mock_randint):
    dado = Dice()
    dado.tirar()
    mov = dado.movimientos()
    # ... verificaciones
```

## Tests de referencia del profesor
Mi profesor nos pasó estos tests como ejemplo:

```python
class TestDice(TestCase):
    @patch('random.randint', side_effect=[5, 2])
    def test_simple(self, randint_patched):
        dice = get_dice()
        self.assertEqual(len(dice), 2)
        self.assertEqual(dice[0], 5)
        self.assertEqual(dice[1], 2)
        self.assertTrue(randint_patched.called)
        self.assertEqual(randint_patched.call_count, 2)

    @patch('random.randint', return_value=1)
    def test_complex(self, randint_patched):
        dice = get_dice()
        self.assertEqual(len(dice), 4)
        self.assertEqual(dice[0], 1)
        self.assertEqual(dice[1], 1)
        self.assertEqual(dice[2], 1)
        self.assertEqual(dice[3], 1)
        self.assertTrue(randint_patched.called)
        self.assertEqual(randint_patched.call_count, 2)

    @patch('random.randint', side_effect=Exception("error!!"))
    def test_error(self, randint_patched):
        dice = get_dice()
        self.assertEqual(len(dice), 0)
        self.assertTrue(randint_patched.called)
        self.assertEqual(randint_patched.call_count, 1)

    def test_double(self):
        with patch('random.randint', side_effect=[5, 2]) as randint_patched:
            dice = get_dice()
            self.assertEqual(len(dice), 2)
            self.assertEqual(dice[0], 5)
            self.assertEqual(dice[1], 2)
            self.assertTrue(randint_patched.called)
            self.assertEqual(randint_patched.call_count, 2)

        with patch('random.randint', return_value=1) as randint_patched:
            dice = get_dice()
            self.assertEqual(len(dice), 4)
            self.assertEqual(dice[0], 1)
            self.assertEqual(dice[1], 1)
            self.assertEqual(dice[2], 1)
            self.assertEqual(dice[3], 1)
            self.assertTrue(randint_patched.called)
            self.assertEqual(randint_patched.call_count, 2)
```

## Lo que necesito entender:
1. **¿Mis tests originales testean lo mismo?**
2. **¿Cómo adaptar el patrón del profesor a mi clase sin agregar código extra?**
3. **¿Cómo funciona exactamente `@patch`?**
4. **¿Cuál es la diferencia entre `side_effect` y `return_value`?**
5. **¿Por qué el profesor usa `get_dice()` y cómo adapto eso a mi implementación?**

## Tests existentes que ya tengo:
También tengo estos tests que escribí antes:

```python
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
```

## Duda adicional:
**¿Debo borrar estos tests anteriores ahora que tengo los nuevos con @patch, o mantener ambos?**

## Restricción importante:
No quiero modificar mi clase `Dice` existente, solo crear los tests apropiados y entender si debo mantener o eliminar mis tests previos.
