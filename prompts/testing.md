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

Prompt Desarrollo
Herramienta utilizada:

Claude

Texto exacto del Prompt:

"Estoy testando mi código con coverage y me dice que algunas líneas faltan que para mí están testadas, ¿es porque mi código está mal?"

Respuesta de la IA (Claude):

Claude explicó que no necesariamente significa que el código esté mal. Coverage puede reportar líneas faltantes por varias razones:

Condiciones no evaluadas completamente → en if/elif/else hay que cubrir todos los caminos.

Excepciones no probadas → si no se provoca el error, el bloque except queda sin cubrir.

Código defensivo → ramas que no se ejecutan si siempre se pasan datos válidos.

Métodos auxiliares → getters, setters, __str__, etc. que nunca se llaman.

Luego analizamos mi caso particular:

Coverage marcaba como no cubiertas las líneas 88 y 89 de board.py.

Mis tests usaban assertRaises(ValueError, ...), pero Claude recomendó cambiar a with self.assertRaises(ValueError): ... para que coverage detecte mejor la ejecución.

Explicó la diferencia entre ambos enfoques y mostró ejemplos de tests nuevos con 2 y 3 fichas en destino.

Finalmente, al revisar el reporte HTML de coverage, vimos:

Línea 88 → marcada como parcial (amarilla), porque la condición siempre fue True en mis tests, nunca probé el caso donde sea False.

Línea 89 → estaba verde (cubierta).

También faltaban cubrir las líneas 101–106 (sacar_ficha) y la línea 45 (otra condición siempre True).

Conclusión de Claude:

Mis tests funcionan, pero coverage es estricto: para llegar al 100% debo agregar un test donde la condición de la línea 88 sea False (ej. destino con solo una ficha).

También cubrir el método sacar_ficha.
