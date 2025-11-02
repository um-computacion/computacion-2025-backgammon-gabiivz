# Justificación del Proyecto Backgammon

**Alumno:** Gabriela Ivazov  
**Repositorio:** `computacion-2025-backgammon-gabiivz`  
**Fecha:** Noviembre 2025

---

## 1. Resumen del Diseño General

Este proyecto implementa un juego completo de Backgammon en Python siguiendo principios de Programación Orientada a Objetos (POO). La arquitectura está diseñada para ser modular, extensible y fácil de mantener.

### Estructura del Proyecto

```
core/
├── board.py           # Tablero y lógica de movimientos
├── dice.py            # Sistema de dados
├── player.py          # Representación de jugadores
├── backgammongame.py  # Orquestador principal del juego
└── exceptions.py      # Excepciones personalizadas

cli/
└── cli.py            # Interfaz de línea de comandos

pygame_ui/
├── ui.py             # Interfaz gráfica principal con Pygame
└── board_game.py     # Renderizador del tablero visual

tests/
├── tests_board.py
├── tests_dice.py
├── tests_player.py
├── tests_backgammon.py
└── tests_cli.py
```

### Flujo del Juego

1. **Inicialización**: `BackgammonGame` crea el tablero, jugadores y dados
2. **Turno**: El jugador tira dados → mueve fichas → cambia turno
3. **Validación**: Cada movimiento se valida contra reglas de Backgammon
4. **Victoria**: El juego detecta cuando un jugador saca todas sus 15 fichas

---

## 2. Justificación de las Clases Elegidas

### 2.1. Clase `Player`

**Responsabilidad:** Representar un jugador del juego.

**Por qué existe:**
- Encapsula la información de cada participante (nombre y color)
- Facilita la identificación del jugador actual en cada turno
- Permite extender funcionalidad (ej: estadísticas, puntos acumulados)

**Decisión de diseño:**
Se optó por una clase simple ya que el jugador no tiene comportamientos complejos, solo datos identificatorios. Esto cumple con el **Principio de Responsabilidad Única (SRP)**.

---

### 2.2. Clase `Dice`

**Responsabilidad:** Gestionar el lanzamiento de dados y movimientos disponibles.

**Por qué existe:**
- Centraliza la lógica de generación aleatoria de dados
- Maneja la regla especial de dados dobles (4 movimientos)
- Controla qué movimientos ya fueron usados durante un turno

**Decisión de diseño:**
Inicialmente se consideró delegar esto a `BackgammonGame`, pero separarla:
- Facilita el testing con mocks/patches de `random.randint`
- Permite reutilizar la lógica de dados en otros contextos
- Cumple con **SRP**: solo se encarga de dados, no de lógica de juego

**Atributos clave:**
- `__movimientos__`: Lista dinámica que representa dados disponibles
- `__dado1__`, `__dado2__`: Valores individuales de cada dado

---

### 2.3. Clase `Board`

**Responsabilidad:** Representar el tablero y ejecutar movimientos de fichas.

**Por qué existe:**
- Encapsula la estructura de datos del tablero (26 posiciones)
- Implementa todas las reglas de movimiento de Backgammon:
  - Movimientos normales (apilar)
  - Capturas (comer fichas)
  - Re-entrada desde la barra
  - Bearing off (sacar fichas)
- Valida direcciones de movimiento según el color

**Decisión de diseño:**

**¿Por qué 26 posiciones y no 24?**
```python
self.__board__ = [[] for _ in range(28)]
# [0] = Bar Negras
# [1-24] = Tablero principal
# [25] = Bar Blancas
# [26] = Salida (bearing off)
```

Usar posiciones especiales (0, 25, 26) simplifica la lógica:
- No se necesitan estructuras adicionales para barra/salida
- Los movimientos desde/hacia barra se manejan uniformemente
- Facilita el cálculo de distancias

**Métodos clave:**
- `movimiento_valido()`: Valida dirección y rango
- `mover_ficha()`: Movimientos normales y apilado
- `comer_ficha()`: Captura fichas rivales
- `mover_ficha_comida()`: Re-entrada desde barra
- `sacar_ficha()`: Bearing off
- `es_destino_legal()`: Verifica si un punto está bloqueado

---

### 2.4. Clase `BackgammonGame`

**Responsabilidad:** Orquestar el flujo completo del juego.

**Por qué existe:**
- Coordina las interacciones entre `Board`, `Dice` y `Player`
- Gestiona los turnos y el estado del juego
- Implementa la lógica de alto nivel (¿hay ganador?, ¿hay movimientos posibles?)
- Delega las validaciones específicas a las clases especializadas

**Decisión de diseño:**
Esta clase sigue el patrón **Facade**: presenta una interfaz simple para operaciones complejas que involucran múltiples objetos.

**Métodos principales:**
- `mover_ficha()`: Método principal que coordina:
  1. Validar si hay dados disponibles
  2. Verificar fichas en barra
  3. Delegar movimiento a `Board`
  4. Consumir dado usado
  5. Actualizar fichas sacadas

- `tiene_movimientos_posibles()`: Evita que el jugador quede atascado sin poder jugar

- `get_ganador()`: Detecta condición de victoria (15 fichas sacadas)

**Atributos clave:**
- `__fichas_sacadas_blancas__` / `__fichas_sacadas_negras__`: Listas que registran fichas que salieron del tablero
- `__turno__`: String que indica qué color juega ("Blancas" o "Negras")

**Nota sobre refactorización:**
Originalmente existía una clase `Checker` que fue eliminada (ver `prompts/desarrollo.md`). Se decidió manejar las fichas sacadas como listas simples en `BackgammonGame` porque:
- Las fichas no tienen comportamiento individual
- Solo importa la cantidad de fichas sacadas
- Simplifica el diseño 

---

### 2.5. Clase `BackgammonCLI`

**Responsabilidad:** Proporcionar interfaz de usuario por consola.

**Por qué existe:**
- Separa la lógica de presentación de la lógica de negocio
- Facilita crear otras interfaces (GUI, web) sin modificar el core
- Cumple con **Separación de Responsabilidades**

**Decisión de diseño:**
La CLI solo se comunica con `BackgammonGame`, nunca accede directamente a `Board` o `Dice`. Esto garantiza el **Principio de Ocultación de Información**.

---

### 2.6. Clase `PygameUI`

**Responsabilidad:** Proporcionar interfaz gráfica de usuario con Pygame.

**Por qué existe:**
- Ofrece una alternativa visual e interactiva a la CLI
- Permite jugar con clicks del mouse en lugar de comandos de texto
- Mantiene la separación de responsabilidades (UI vs lógica de juego)
- Demuestra la extensibilidad del diseño (múltiples interfaces sin cambiar el core)

**Decisión de diseño:**
Similar a `BackgammonCLI`, `PygameUI` solo se comunica con `BackgammonGame`. No tiene acceso directo a `Board` o `Dice`, respetando el encapsulamiento.

**Características principales:**
- Pantalla de inicio para ingresar nombres de jugadores
- Interfaz gráfica del tablero con fichas visuales
- Click para tirar dados
- Click en ficha para seleccionar origen
- Click en destino para mover
- Mensajes de error visuales
- Detección automática de ganador

**Ejecución:**
```bash
python -m pygame_ui.ui
```

---

### 2.7. Clase `BoardRenderer`

**Responsabilidad:** Renderizar visualmente el tablero de Backgammon.

**Por qué existe:**
- Separa la lógica de dibujado de la lógica de UI
- Encapsula toda la geometría y cálculos de posiciones
- Facilita mantener y modificar el aspecto visual sin tocar el juego
- Cumple con **Single Responsibility Principle** (solo dibuja, no decide)

**Decisión de diseño:**
Se creó una clase separada del `PygameUI` para seguir el patrón **Separation of Concerns**:
- `PygameUI` maneja eventos, clicks, flujo del juego
- `BoardRenderer` solo dibuja (tablero, fichas, barras)

**Métodos clave:**
- `dibujar_tablero()`: Dibuja los 24 triángulos y barras
- `dibujar_fichas()`: Posiciona fichas según el estado del juego
- `dibujar_barra()`: Muestra fichas comidas en la barra central
- `dibujar_barra_lateral()`: Contador de fichas sacadas
- `obtener_punto_desde_click()`: Mapea clicks a puntos del tablero
- `obtener_punto_desde_click_en_ficha()`: Detecta click en ficha superior

**Geometría implementada:**
```python
# Tablero dividido en zonas
self.ancho_triangulo = self.ancho // 14  # 6 + barra + 6 por lado
self.ancho_barra = self.ancho_triangulo
self.alto_triangulo = self.alto // 2
self.radio_ficha = self.ancho_triangulo // 3
```

**Paleta de colores:**
- Triángulos: tonos pastel (rosa/beige) alternados
- Fichas: blanco y negro con borde
- Barras: color madera
- Mensajes de error: rojo
- Fondo: verde claro

**Ventajas de separar el renderer:**
- Si quiero cambiar colores, solo modifico `BoardRenderer`
- Si quiero otra UI (ej: web con canvas), reutilizo la lógica de mapeo

---

## 3. Justificación de Atributos

### 3.1. Atributos Privados (Encapsulamiento)

**Todos los atributos internos usan doble guion bajo (`__atributo__`) para indicar privacidad:**

```python
class BackgammonGame:
    def __init__(self, nombre_blancas, nombre_negras):
        self.__board__ = Board()              # Privado
        self.__turno__ = "Blancas"            # Privado
        self.__dado__ = Dice()                # Privado
        self.__jugador_blancas__ = Player()   # Privado
        self.__jugador_negras__ = Player()    # Privado
        self.__fichas_sacadas_blancas__ = []  # Privado
        self.__fichas_sacadas_negras__ = []   # Privado
```

**Por qué:**
- Evita acceso directo desde fuera de la clase
- Obliga a usar getters/setters (control de acceso)
- Facilita cambios internos sin romper código externo
- Cumple con **Encapsulamiento** (pilar de POO)

### 3.2. Atributos en `Dice`

```python
self.__dado1__ = 0
self.__dado2__ = 0
self.__movimientos__ = []
```

- `__dado1__`, `__dado2__`: Valores individuales para debugging y visualización
- `__movimientos__`: Lista que se modifica durante el turno (se consumen valores al mover)

**Ventaja de usar lista:**
- Los dados dobles se representan naturalmente: `[4, 4, 4, 4]`
- Fácil verificar disponibilidad: `if valor in self.__movimientos__`
- Fácil consumir: `self.__movimientos__.remove(valor)`

### 3.3. Atributos en `Board`

```python
self.__board__ = [[] for _ in range(28)]
```

**Por qué lista de listas:**
- Cada posición es una lista de fichas (permite apilar)
- Fácil contar fichas: `len(self.__board__[pos])`
- Fácil verificar color: `self.__board__[pos][0]`
- Fácil añadir/quitar: `.append()` / `.pop()`

**Alternativas consideradas y descartadas:**
- ❌ Diccionario: Más verboso, sin ventajas claras
- ❌ Clase `Point` separada: Sobreingeniería para este proyecto
- ✅ Lista de listas: Simple, eficiente, legible

---

## 4. Decisiones de Diseño Relevantes

### 4.1. Sistema de Excepciones Personalizadas

**Problema inicial:**
El código original usaba `ValueError` genérico para todos los errores, dificultando el debugging y testing.

**Solución:**
Se creó una jerarquía de excepciones en `core/exceptions.py`:

```python
BackgammonError (base)
├── MovimientoInvalidoError
├── FichaEnBarError
├── DadoNoDisponibleError
├── PuntoOcupadoError
├── DireccionInvalidaError
├── MovimientoFueraDeRangoError
└── DadosNoTiradosError
```

**Ventajas:**
- **Testing específico**: `self.assertRaises(DadoNoDisponibleError)`
- **Mensajes claros**: Cada excepción describe exactamente qué falló
- **Debugging rápido**: El tipo de excepción indica la categoría del error
- **Manejo diferenciado**: La CLI puede responder distinto a cada error

**Ejemplo de uso:**
```python
try:
    game.mover_ficha(13, 10)
except FichaEnBarError:
    print("❌ Debes mover primero las fichas de la barra")
except DadoNoDisponibleError as e:
    print(f"❌ Movimiento de {e.movimiento} no disponible")
except PuntoOcupadoError:
    print("❌ Ese punto está bloqueado por el oponente")
```

### 4.2. Delegación de Responsabilidades

**Patrón aplicado:**

```
BackgammonGame.mover_ficha()
    ↓ valida dados disponibles
    ↓ verifica barra
    ↓ delega a ───→ Board.movimiento_valido()
    ↓ delega a ───→ Board.mover_ficha() / comer_ficha() / sacar_ficha()
    ↓ actualiza fichas sacadas
    ↓ consume dado
```

**Por qué:**
- `BackgammonGame` no necesita saber *cómo* se valida un movimiento
- `Board` no necesita saber *cuándo* cambiar de turno
- Cada clase tiene una responsabilidad clara 
- Fácil de testear cada componente por separado

### 4.3. Método `tiene_movimientos_posibles()`

**Por qué existe:**
En Backgammon, si un jugador no tiene movimientos legales, pierde su turno automáticamente.

**Implementación:**
- Itera sobre todas las fichas del jugador
- Para cada dado disponible, verifica si existe un destino legal
- Maneja casos especiales: barra, bearing off

**Importancia:**
- Evita que el juego se quede en deadlock
- Mejora UX: el jugador sabe si puede mover o no
- Cumple con las reglas oficiales de Backgammon

### 4.4. Separación CLI vs Core

**Estructura:**
```
cli/cli.py        ← Solo presentación (texto)
    ↓ llama a
core/backgammongame.py ← Lógica de juego
    ↑ llama a
pygame_ui/ui.py   ← Solo presentación (gráfica)
```

**Ventajas:**
- Puedo crear `pygame_ui/` sin tocar el core ✅ (implementado)
- Los tests del core no dependen de la CLI
- Cumple con **Separación de Responsabilidades**
- Facilita mantenimiento y extensión

**Evidencia de extensibilidad:**
Este proyecto demuestra el principio en acción:
- **CLI** (`cli/cli.py`): Interfaz por consola
- **Pygame UI** (`pygame_ui/ui.py`): Interfaz gráfica
- **Core** (`core/`): Lógica compartida sin modificaciones

Ambas interfaces usan exactamente la misma API de `BackgammonGame`:
```python
# Ambas CLI y PygameUI hacen lo mismo:
game = BackgammonGame(nombre1, nombre2)
game.tirar_dados()
game.mover_ficha(origen, destino)
game.get_jugador_actual()
game.estado_actual()
game.get_ganador()
```

### 4.5. Arquitectura de PygameUI

**Patrón implementado: MVC simplificado**

```
PygameUI (Controlador)
    ↓ maneja eventos
    ↓ llama a → BackgammonGame (Modelo)
    ↓ obtiene estado
    ↓ delega a → BoardRenderer (Vista)
```

**Flujo de un click:**
1. Usuario hace click en posición (x, y)
2. `PygameUI._handle_click()` procesa el evento
3. `BoardRenderer.obtener_punto_desde_click()` mapea coordenadas a punto
4. `PygameUI` valida que sea ficha del jugador actual
5. Si es válido, llama a `game.mover_ficha(origen, destino)`
6. `BackgammonGame` valida y ejecuta (o lanza excepción)
7. `PygameUI` captura excepción o éxito
8. `PygameUI._draw()` redibuja todo
9. `BoardRenderer.dibujar_*()` pinta el nuevo estado

**Ventajas de esta arquitectura:**
- Fácil agregar más UIs (web, mobile)
- Fácil testear el core sin UI
- Cambios visuales no afectan lógica
- Cambios de reglas no afectan UI

---

## 5. Excepciones y Manejo de Errores

### 5.1. Excepciones Definidas

| Excepción | Cuándo se lanza | Por qué existe |
|-----------|----------------|----------------|
| `BackgammonError` | Nunca (clase base) | Permite capturar cualquier error del juego |
| `MovimientoInvalidoError` | Movimiento genérico inválido | Error catch-all para casos no específicos |
| `FichaEnBarError` | Intenta mover fichas normales teniendo fichas en barra | Regla obligatoria de Backgammon |
| `DadoNoDisponibleError` | El movimiento requiere un dado que no está disponible | Evita trampas con los dados |
| `PuntoOcupadoError` | Intenta aterrizar en punto bloqueado (2+ fichas enemigas) | Regla básica de Backgammon |
| `DireccionInvalidaError` | Mueve en dirección incorrecta (Blancas hacia adelante, etc.) | Cada color tiene dirección fija |
| `MovimientoFueraDeRangoError` | Intenta mover fuera del tablero (< 0 o > 24) | Previene errores de índice |
| `DadosNoTiradosError` | Intenta mover sin haber tirado dados | Evita movimientos sin dados |

### 5.2. Estrategia de Manejo

**En el Core:**
- Las excepciones se **lanzan** cuando se detecta un error
- No se capturan dentro del core (dejan que la CLI las maneje)
- Cada excepción incluye información útil (origen, destino, dado requerido, etc.)

**En la CLI:**
- Se capturan **todas** las excepciones específicas
- Se muestran mensajes amigables al usuario
- Se permite reintentar el movimiento

**En los Tests:**
- Se usa `assertRaises()` para verificar que se lanzan correctamente
- Se verifica el mensaje de error cuando es relevante

**Ejemplo completo:**

```python
# En core/backgammongame.py
def mover_ficha(self, origen, destino):
    if not self.get_dados():
        raise DadosNoTiradosError("Debes tirar los dados primero")
    
    if mov not in dados_disponibles:
        raise DadoNoDisponibleError(
            f"Movimiento {mov} no disponible. Dados: {dados_disponibles}"
        )

# En cli/cli.py
try:
    self.game.mover_ficha(origen, destino)
    print("✓ Ficha movida exitosamente")
except DadosNoTiradosError as e:
    print(f"❌ {e}")
except DadoNoDisponibleError as e:
    print(f"❌ {e}")

# En tests/tests_backgammon.py
def test_mover_sin_dados_lanza_error(self):
    game = BackgammonGame("Gabi", "Gabo")
    with self.assertRaises(DadosNoTiradosError):
        game.mover_ficha(13, 10)
```

---

## 6. Estrategias de Testing y Cobertura

### 6.1. Cobertura Actual

**Reporte de Coverage:**
```
Name                     Stmts   Miss Branch BrPart  Cover
------------------------------------------------------------
cli\cli.py                 105      7     42      5    92%
core\backgammongame.py     136      2     60      2    98%
core\board.py              122      2     62      3    97%
core\dice.py                22      0      2      0   100%
core\player.py              10      0      0      0   100%
------------------------------------------------------------
TOTAL                      395     11    166     10    96%
```

**Objetivo alcanzado:** 96% de cobertura total

### 6.2. Estrategia por Módulo

#### **tests_dice.py**
- **Cobertura:** 100%
- **Estrategia:** Testing con mocks usando `@patch`

**Aprendizaje clave:**
- Uso de `@patch('random.randint')` para controlar aleatoriedad
- `side_effect=[5, 2]` para simular dados simples
- `return_value=4` para simular dados dobles
- Verificación de `call_count` para asegurar que se llamó 2 veces

**Tests implementados:**
- Tiradas válidas (rango 1-6)
- Dados dobles generan 4 movimientos
- Dados simples generan 2 movimientos
- Reinicio de dados
- Manejo de excepciones

#### **tests_player.py**
- **Cobertura:** 100%
- **Estrategia:** Testing de getters y construcción

**Por qué es simple:**
`Player` no tiene lógica compleja, solo encapsula datos. Los tests verifican:
- Construcción correcta
- Getters funcionan
- Representación en string

#### **tests_board.py**
- **Cobertura:** 96%
- **Estrategia:** Testing exhaustivo de reglas de Backgammon

**Casos críticos testeados:**
- ✅ Posiciones iniciales correctas
- ✅ Movimientos en dirección correcta (Blancas ←, Negras →)
- ✅ Movimientos fuera de rango lanzan error
- ✅ Apilar fichas propias
- ✅ Captura de fichas enemigas (solo si hay 1)
- ✅ Puntos bloqueados (2+ fichas enemigas)
- ✅ Re-entrada desde barra a home board enemigo
- ✅ Bearing off solo con todas las fichas en home
- ✅ Bearing off con dado mayor al punto

**Casos edge:**
- Barra vacía vs barra con fichas
- Destino vacío vs destino con 1 ficha vs destino con 2+ fichas
- Fichas del mismo color vs color diferente

**Cómo se logró 96%:**
- Se identificaron ramas no cubiertas con `coverage html`
- Se agregaron tests específicos para cada rama (ej: `test_comer_ficha_destino_una`)
- Se testearon casos donde condiciones son False (no solo True)

#### **tests_backgammon.py**
- **Cobertura:** 98%
- **Estrategia:** Testing de integración y orquestación

**Tests de flujo completo:**
- ✅ Turnos: Blancas empieza, cambio de turnos funciona
- ✅ Dados: Tirar, usar, validar disponibilidad
- ✅ Movimientos: Desde barra, normales, bearing off
- ✅ Ganador: Detección cuando se sacan 15 fichas
- ✅ Movimientos posibles: Detecta cuando el jugador está atascado

**Tests de excepciones:**
- ✅ Mover sin tirar dados → `DadosNoTiradosError`
- ✅ Mover ficha normal con fichas en barra → `FichaEnBarError`
- ✅ Usar dado no disponible → `DadoNoDisponibleError`
- ✅ Sacar ficha con fichas fuera de home → error

**Testing de `tiene_movimientos_posibles()`:**
Este método es crítico y se testeó exhaustivamente:
- Puede mover normalmente
- Atascado en barra (todos los destinos bloqueados)
- Puede salir de barra (al menos un destino libre)
- Atascado en tablero normal (sin movimientos legales)
- Puede hacer bearing off
- No puede hacer bearing off aún (fichas fuera de home)

#### **tests_cli.py**
- **Cobertura:** 92%
- **Estrategia:** Testing con mocks de `input` y `BackgammonGame`

**Desafío:**
La CLI depende de `input()` (bloquea ejecución). Solución: `@patch('builtins.input')`

**Tests implementados:**
- ✅ Validación de nombres vacíos
- ✅ Flujo completo: tirar dados, mover, cambiar turno
- ✅ Captura de excepciones y mensajes de error
- ✅ Opción rendirse
- ✅ Opción ver estado
- ✅ Detección de ganador
- ✅ Manejo de "no hay movimientos posibles"

**Técnica clave:**
```python
@patch('builtins.input', side_effect=['Gabi', 'Gabo', 's', '1', '13', '10', '3'])
def test_main_tira_dados_y_mueve(self, mock_input):
    # Simula secuencia completa de inputs
```

### 6.3. ¿Por qué 96% y no 100%?

**Líneas no cubiertas:**

1. **cli.py (92%):** 
   - Algunas ramas de error difíciles de simular con mocks
   - Código defensivo para casos edge muy raros

2. **backgammongame.py (98%):**
   - 1 línea en `tiene_movimientos_posibles()` (caso extremo raro)
   - 1 línea en bearing off con condiciones muy específicas

3. **board.py (97%):**
   - 2 líneas en validaciones de bearing off con múltiples condiciones

**Decisión:**
- 96% es excelente cobertura profesional
- Las líneas no cubiertas son casos extremadamente raros

### 6.4. Lecciones Aprendidas en Testing

**Del prompt `testing.md`:**

1. **Uso de `@patch`:**
   - Controlar aleatoriedad en `random.randint`
   - Verificar número de llamadas con `call_count`
   - Diferencia entre `side_effect` y `return_value`

2. **Coverage y ramas:**
   - Coverage marca líneas "parciales" cuando solo se testea True y no False
   - Usar `with self.assertRaises():` en vez de `assertRaises()` mejora detección
   - Revisar reporte HTML para identificar ramas faltantes

3. **Testing de CLI:**
   - Mockear `input()` con `side_effect` para simular secuencias
   - Mockear `print()` para verificar mensajes mostrados
   - Usar `MagicMock` para objetos complejos

---

## 7. Principios SOLID

### 7.1. Single Responsibility Principle (SRP)

**✅ Cumplimiento:** Cada clase tiene UNA responsabilidad claramente definida.

| Clase | Responsabilidad Única |
|-------|-----------------------|
| `Player` | Datos del jugador |
| `Dice` | Lógica de dados |
| `Board` | Estado del tablero y reglas de movimiento |
| `BackgammonGame` | Orquestación del juego |
| `BackgammonCLI` | Interfaz de usuario |

**Ejemplo de violación evitada:**
- ❌ Poner lógica de dados dentro de `BackgammonGame`
- ✅ Separar en clase `Dice` independiente

**Evidencia:**
- Cada clase puede cambiar por una sola razón
- Las modificaciones en una clase raramente afectan a otras

### 7.2. Open/Closed Principle (OCP)

**✅ Cumplimiento:** El sistema es extensible sin modificar código existente.

**Ejemplos:**

1. **Nuevas interfaces:**
   ```python
   # Se puede crear pygame_ui/ui.py sin tocar core/
   from core.backgammongame import BackgammonGame
   
   class BackgammonGUI:
       def __init__(self):
           self.game = BackgammonGame("P1", "P2")
       # ... lógica gráfica
   ```

2. **Nuevas excepciones:**
   ```python
   # Se pueden agregar más excepciones sin modificar las existentes
   class TrampaDetectadaError(BackgammonError):
       pass
   ```

3. **Extensión de funcionalidad:**
   ```python
   # Se puede heredar para agregar características
   class BackgammonGameConEstadisticas(BackgammonGame):
       def __init__(self, *args):
           super().__init__(*args)
           self.movimientos_totales = 0
   ```

### 7.3. Liskov Substitution Principle (LSP)

**✅ Cumplimiento:** Las excepciones son sustituibles por su clase base.

```python
try:
    game.mover_ficha(13, 10)
except BackgammonError as e:  # Captura CUALQUIER excepción del juego
    print(f"Error: {e}")
```

**Por qué funciona:**
- Todas las excepciones heredan de `BackgammonError`
- Todas tienen mensaje descriptivo
- Todas pueden ser capturadas genéricamente o específicamente

**Contrato:**
- Si el código espera `BackgammonError`, cualquier subclase funciona
- No se rompen suposiciones del código cliente

### 7.4. Interface Segregation Principle (ISP)

**✅ Cumplimiento:** Las clases no dependen de métodos que no usan.

**Ejemplo:**
- `CLI` solo usa métodos públicos de `BackgammonGame`
- No necesita conocer `Board`, `Dice` o `Player` directamente
- Interfaz mínima necesaria:
  ```python
  game.tirar_dados()
  game.mover_ficha(origen, destino)
  game.get_jugador_actual()
  game.estado_actual()
  game.get_ganador()
  ```

**Evidencia:**
```python
# cli/cli.py NUNCA hace esto:
self.game.__board__.mover_ficha()  # ❌ Acceso directo prohibido

# Siempre usa la interfaz pública:
self.game.mover_ficha(origen, destino)  # ✅ Correcto
```

### 7.5. Dependency Inversion Principle (DIP)

**✅ Cumplimiento parcial:** Las clases de alto nivel no dependen directamente de las de bajo nivel.

**Aplicación:**
- `BackgammonGame` depende de abstracciones (`Board`, `Dice`, `Player`)
- Estas clases podrían ser reemplazadas por otras implementaciones
- `CLI` depende de `BackgammonGame`, no de sus componentes internos
- `PygameUI` también depende de `BackgammonGame`, no de `Board` o `Dice`

**Ejemplo conceptual:**
```python
# Podría crear interfaces abstractas (aunque Python no lo requiere):
class IBoard(ABC):
    @abstractmethod
    def mover_ficha(self, origen, destino, color):
        pass

# Y luego:
class BackgammonGame:
    def __init__(self, board: IBoard):  # Depende de abstracción
        self.board = board
```

**Por qué no se implementó completamente:**
- Python es dinámico (duck typing)
- Para este proyecto, la abstracción formal sería sobreingeniería
- El diseño actual ya facilita testing con mocks

**Evidencia de cumplimiento:**
- Todos los tests usan `MagicMock` para simular clases
- Las clases se pueden mockear fácilmente (indicio de bajo acoplamiento)
- Dos UIs diferentes (CLI y Pygame) usan la misma abstracción de `BackgammonGame`

---

## 8. Decisiones de IA y Asistencia

**Este proyecto utilizó asistencia de IA documentada en:**
- `prompts/testing.md` - Tests con `@patch`, coverage, debugging
- `prompts/desarrollo.md` - Diseño de clases, excepciones, refactorización
- `prompts/documentacion.md` - Reglas de Backgammon

**Herramientas usadas:**
- Claude.ai (Claude 3.5 Sonnet)
- ChatGPT (GPT-4)
- GitHub Copilot
- DeepSeek

**Criterio de uso:**
- ✅ La IA sugiere soluciones, yo decido si aplicarlas
- ✅ Todo el código fue revisado y entendido antes de commitear
- ✅ Las sugerencias fueron modificadas para ajustarse al proyecto
- ❌ Nunca se copió código sin entender qué hace

**Ejemplos de modificaciones:**

1. **Sistema de excepciones (Claude):**
   - Sugerido: 7 excepciones
   - Aplicado: 8 (agregué `DadosNoTiradosError`)
   - Modificado: Mensajes en español, atributos adicionales

2. **Tests de CLI (Copilot):**
   - Sugerido: Tests básicos con mocks
   - Aplicado: Tests mejorados con secuencias complejas de input
   - Modificado: Agregué tests de excepciones específicas

3. **Refactorización de `Checker` (Copilot):**
   - Sugerido: Eliminar clase completa
   - Aplicado: Eliminé y moví lógica a `BackgammonGame`
   - Decisión personal: Usar listas simples en vez de diccionarios

4. **Interfaz Pygame (propia decisión):**
   - No sugerido por IA
   - Demuestra que el diseño del core permite extensiones
   - Aplicación práctica de los principios SOLID

---

## 9. Anexos

### 9.1. Diagrama de Clases Principal

Este diagrama muestra las clases core y sus relaciones:

```
┌─────────────────────────────────────────┐
│        BackgammonGame                   │  (Coordinador)
├─────────────────────────────────────────┤
│ - __board__: Board                      │
│ - __turno__: str                        │
│ - __dado__: Dice                        │
│ - __jugador_blancas__: Player           │
│ - __jugador_negras__: Player            │
│ - __fichas_sacadas_blancas__: list      │
│ - __fichas_sacadas_negras__: list       │
├─────────────────────────────────────────┤
│ + tirar_dados()                         │
│ + mover_ficha(origen, destino)          │
│ + cambio_turnos()                       │
│ + tiene_movimientos_posibles()          │
│ + get_ganador()                         │
└──────────────┬──────────────────────────┘
               │ usa (composición)
       ┌─────── ┼───────┬─────────┐
       ▼       ▼       ▼         ▼
    ┌─────┐ ┌──────┐ ┌──────┐ ┌─────────────┐
    │Board│ │ Dice │ │Player│ │ Exceptions  │
    └─────┘ └──────┘ └──────┘ └─────────────┘
       ▲                              ▲
       │                              │
       └───── usa (BackgammonGame) ───┘
              │                   │
              │                   │
┌─────────────┴────┐     ┌────────┴──────┐
│BackgammonCLI     │     │  PygameUI     │
│(Consola)         │     │(Gráfica)      │
└──────────────────┘     └───────┬───────┘
                                 │ usa
                                 ▼
                         ┌──────────────┐
                         │BoardRenderer │
                         └──────────────┘
```

**Clases Core:**
- 📦 **BackgammonGame**: Coordinador principal (Facade)
- 👤 **Player**: Datos del jugador (nombre, color)
- 🎲 **Dice**: Generación y gestión de dados
- 📋 **Board**: Tablero y reglas de movimiento
- ⚠️ **Exceptions**: 8 excepciones personalizadas

**Interfaces:**
- 💻 **BackgammonCLI**: Interfaz por consola
- 🎮 **PygameUI**: Interfaz gráfica con Pygame
- 🖼️ **BoardRenderer**: Renderizador visual del tablero

**Relaciones:**
- **Composición**: BackgammonGame contiene Board, Dice, Players
- **Uso**: CLI y PygameUI usan BackgammonGame (no acceden directamente a Board/Dice)
- **Separación**: Renderer solo dibuja, PygameUI maneja eventos

**Ventajas:**
- ✅ Separación de responsabilidades (core vs UI)
- ✅ Testeable (tests del core sin UI)
- ✅ Extensible (múltiples UIs sin cambiar core)
- ✅ Mantenible (cambios en UI no afectan lógica)

---

### 9.2. Jerarquía de Excepciones

```
        BackgammonError (base)
                │
    ┌───────────┼───────────┬───────────────┐
    │           │           │               │
FichaEnBar  DadoNo    PuntoOcupado  MovimientoInvalido
Error       Disponible    Error         Error
            Error
    │           │
Direccion   MovimientoFuera   DadosNoTirados
InvalidaError  DeRangoError      Error
```

**Total: 8 excepciones** que permiten manejo específico de errores.

---

### 9.3. Flujo de un Movimiento

```
Usuario → CLI/PygameUI
           ↓
    game.mover_ficha(13, 10)
           ↓
    BackgammonGame
    ├─ Validar dados disponibles
    ├─ Verificar barra
    ├─ board.movimiento_valido()
    ├─ board.mover_ficha()
    └─ usar_dados()
           ↓
    ✅ Movimiento exitoso
    o
    ❌ Excepción específica
```

---

## 10. Conclusión

Este proyecto demuestra:

✅ **Diseño orientado a objetos sólido** con clases bien delimitadas  
✅ **Principios SOLID aplicados** en la arquitectura  
✅ **Sistema de excepciones robusto** que facilita debugging y UX  
✅ **Testing exhaustivo** con 96% de cobertura  
✅ **Separación de responsabilidades** entre lógica y presentación  
✅ **Código mantenible y extensible** listo para nuevas features  
✅ **Documentación completa** de decisiones y prompts de IA  

**Métricas finales:**
- **395 líneas** de código core
- **~500 líneas** de código UI (CLI + Pygame)
- **96% cobertura** de tests (core)
- **8 excepciones** personalizadas
- **5 clases** core + 3 UI (CLI + Pygame UI + Renderer)
- **0 violaciones críticas** de pylint
- **100% reglas de Backgammon** implementadas
- **2 interfaces completas** (texto y gráfica)

**Próximos pasos potenciales:**
- [ ] Implementar sonidos en Pygame UI
- [ ] Agregar animaciones de movimiento de fichas
- [ ] Agregar guardado/carga de partidas
- [ ] Implementar cubo doblador
- [ ] IA para jugar contra la computadora
- [ ] Modo multijugador en red
- [ ] Estadísticas de partidas jugadas
- [ ] Tests para PygameUI

---

**Repositorio:** [um-computacion/computacion-2025-backgammon-gabiivz](https://github.com/um-computacion/computacion-2025-backgammon-gabiivz)  
**Documentación de prompts:** Ver carpeta `prompts/`