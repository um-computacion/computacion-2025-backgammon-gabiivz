# Prompts de Desarrollo - Backgammon Game

---

## Prompt: Configuración inicial del Board en Backgammon

### Modelo/Herramienta utilizada:
- ChatGPT (GPT-4)
- DeepSeek

### Texto exacto del Prompt:
"Cambiame esto teniendo en cuenta lo que puse arriba, lo de abajo lo use cuando iba de 0 a 23 mi tablero.

Para que veas bien como lo pensé:
def __init__(self):
    self.__board__ = [None] * 26  #de 0 a 25, 2 demas, (0) que se va a referir al bar, donde van las fichas "comidas" 
                                  # y luego 25 que se va a referir a donde salen las fichas 

    self.__board__[5] = ['Blancas'] * 5
    self.__board__[0] = ['Negras'] * 2
    self.__board__[7] = ['Blancas'] * 3
    self.__board__[11] = ['Negras'] * 5
    self.__board__[12] = ['Blancas'] * 5
    self.__board__[16] = ['Negras'] * 3
    self.__board__[23] = ['Blancas'] * 2
    self.__board__[18] = ['Negras'] * 5

### Instrucciones del sistema:
No se aplicaron instrucciones de sistema personalizadas.

### Respuesta completa de la IA:

¡Entiendo perfectamente tu estructura! Te dejo la versión corregida:

El tablero debe inicializarse con 26 posiciones (0–25):

0 → bar (fichas comidas).

1–24 → tablero principal.

25 → salida (fichas que ya terminaron).

El bar (0) y la salida (25) deben empezar vacíos.

La configuración inicial estándar es:

Blancas: punto 24(2), punto 13(5), punto 8(3), punto 6(5).

Negras: punto 1(2), punto 12(5), punto 17(3), punto 19(5).

Se añadieron métodos para:

Sentido de movimiento por color.

Dirección de movimiento (+1 / -1).

Validar puntos.

Obtener bar, salida o un punto específico.

**Código sugerido:**
```python
class Board:
    def __init__(self):
        self.__board__ = [[] for _ in range(26)]
        
        # Posiciones iniciales Blancas
        self.__board__[24] = ['Blancas'] * 2
        self.__board__[13] = ['Blancas'] * 5
        self.__board__[8] = ['Blancas'] * 3
        self.__board__[6] = ['Blancas'] * 5
        
        # Posiciones iniciales Negras
        self.__board__[1] = ['Negras'] * 2
        self.__board__[12] = ['Negras'] * 5
        self.__board__[17] = ['Negras'] * 3
        self.__board__[19] = ['Negras'] * 5
```

### Resultado obtenido:
**Usado sin cambios**

El código fue implementado exactamente como se sugirió en `core/board.py`.

### Referencias a archivos finales:
- `core/board.py` (líneas 1-20) - Inicialización del tablero

---

## Prompt: Diseño completo de BackgammonGame

### Modelo/Herramienta utilizada:
ChatGPT (GPT-4) / Claude.ai (Claude 3.5 Sonnet)

### Texto exacto del Prompt:

"Estoy desarrollando un juego de Backgammon en Python siguiendo principios de POO. 
Actualmente tengo implementadas las siguientes clases base:

- **Checker**: Representa una ficha individual
- **Player**: Gestiona la información del jugador
- **Board**: Representa el tablero con sus 24 puntos
- **Dice**: Maneja el lanzamiento y estado de los dados

## Objetivo

Necesito diseñar completamente la clase **BackgammonGame** que orquestará 
toda la lógica del juego. Esta clase debe encargarse del flujo completo de una 
partida, incluyendo turnos, validaciones y condiciones de victoria.

## Métodos ya identificados (pero necesito que me ayudes a refinarlos):

### Métodos básicos actuales:
1. `iniciar_juego()` - Configuración inicial del tablero y fichas
2. `tirar_dados()` - Generar valores aleatorios y gestionar dados dobles (4 movimientos)
3. `usar_dado(valor)` - Marcar un dado como usado tras un movimiento
4. `puede_mover(jugador)` - Validar si existen movimientos legales disponibles
5. `mover_ficha(origen, destino)` - Ejecutar movimiento y consumir dado
6. `jugar_turno()` - Coordinar la secuencia completa de un turno
7. `estado_actual()` - Retornar snapshot del estado del juego
8. `fin_de_partida()` / `get_ganador()` - Detectar condiciones de victoria

## Lo que necesito de ti:

### 1. Análisis de completitud
- ¿Falta algún método crítico para el flujo del juego?
- ¿Hay funcionalidades de Backgammon que no estoy contemplando?

### 2. Reglas específicas de Backgammon a considerar:
- Capturas (enviar fichas oponentes a la barra)
- Movimientos desde la barra (entrada obligatoria)
- Bearing off (sacar fichas cuando todas están en home)
- Prioridad de movimientos forzados
- Validación de movimientos legales según posición de fichas

### 3. Arquitectura sugerida:
- ¿Cómo estructurarías `jugar_turno()` para gestionar interrupciones 
  (ej: captura que obliga a re-entrar)?
- ¿Deberían algunos métodos ser privados vs públicos?
- ¿Qué validaciones críticas deben hacerse antes de cada movimiento?

### 4. Gestión de estados:
- ¿Cómo representarías el estado de "dados disponibles"?
- ¿Necesito un método para "deshacer movimiento" (por si el jugador 
  se da cuenta que hay mejor secuencia)?

### 5. Entrega esperada:
Por favor, proporcióname:
- Lista completa de métodos recomendados (incluyendo los que faltan)
- Firma de cada método con tipos de datos esperados
- Breve descripción de la responsabilidad de cada uno
- Orden sugerido de implementación (por dependencias)

## Restricciones técnicas:
- Python 3.8+
- Sin dependencias externas complejas (solo stdlib)
- Diseño que facilite testing unitario
- Separación clara entre lógica de juego y presentación (para futura UI)

## Ejemplo de formato de respuesta esperado:
```python
class BackgammonGame:
    def iniciar_juego(self) -> None:
        """Configura posición inicial de fichas según reglas estándar"""
        pass
    
    def validar_movimiento_desde_barra(self, jugador: Player, destino: int) -> bool:
        """Verifica si un jugador puede entrar desde la barra al punto destino"""
        pass
    
    # ... etc
```"

### Instrucciones del sistema:
No se aplicaron instrucciones de sistema personalizadas.

### Respuesta completa de la IA:

La IA proporcionó un análisis detallado y diseño completo:

**1. Análisis de completitud:**
Falta agregar:
- `validar_movimiento_desde_barra()` - Manejo específico de re-entrada
- `puede_hacer_bearing_off()` - Verificar si todas las fichas están en home
- `validar_movimientos_disponibles()` - Verificar movimientos legales con dados actuales
- `tiene_movimientos_validos()` - Determinar si debe perder turno

**2. Métodos recomendados con firmas:**

```python
class BackgammonGame:
    def __init__(self, nombre_blancas: str, nombre_negras: str) -> None:
        """Inicializa el juego con dos jugadores"""
        
    def tirar_dados(self) -> List[int]:
        """Tira dados y retorna lista de movimientos disponibles (2 o 4)"""
        
    def mover_ficha(self, origen: int, destino: int) -> bool:
        """Ejecuta movimiento, valida y consume dado. Retorna True si exitoso"""
        
    def cambio_turnos(self) -> None:
        """Cambia al siguiente jugador"""
        
    def get_jugador_actual(self) -> Player:
        """Retorna el jugador del turno actual"""
        
    def fin_de_partida(self) -> bool:
        """Verifica si el juego terminó"""
        
    def get_ganador(self) -> Optional[Player]:
        """Retorna el jugador ganador o None si no hay"""
        
    def estado_actual(self) -> Dict[str, Any]:
        """Retorna diccionario con estado completo del juego"""
        
    def puede_hacer_bearing_off(self, color: str) -> bool:
        """Verifica si todas las fichas del jugador están en home board"""
        
    def tiene_movimientos_validos(self) -> bool:
        """Verifica si existen movimientos legales con dados actuales"""
```

**3. Arquitectura de `jugar_turno()`:**
```python
def jugar_turno(self):
    self.tirar_dados()
    
    while self.__dado__.movimientos:  # Mientras haya dados disponibles
        if not self.tiene_movimientos_validos():
            break  # No puede jugar, pierde turno
            
        # Esperar input del jugador (CLI/GUI)
        # Validar y ejecutar movimiento
        # mover_ficha() consume el dado automáticamente
        
    self.cambio_turnos()
```

**4. Orden de implementación sugerido:**
1. Constructor y getters básicos
2. `tirar_dados()` y manejo de dados
3. `cambio_turnos()`
4. `mover_ficha()` con validaciones básicas
5. `tiene_movimientos_validos()`
6. `puede_hacer_bearing_off()`
7. `fin_de_partida()` y `get_ganador()`
8. `estado_actual()`
9. `jugar_turno()` (orquestación completa)

### Resultado obtenido:
**Usado con modificaciones**

Se implementó la clase siguiendo la estructura sugerida, con las siguientes modificaciones:
- Se simplificó `jugar_turno()` para que sea más adecuada para CLI
- Se agregó manejo de excepciones personalizadas en lugar de solo booleanos
- Se eliminó `puede_hacer_bearing_off()` y se integró en la lógica de `mover_ficha()`

### Referencias a archivos finales:
- `core/backgammongame.py` - Clase completa implementada

---

## Prompt: BackgammonGame con Excepciones Personalizadas

### Modelo/Herramienta utilizada:
Claude.ai (Claude 3.5 Sonnet)

### Texto exacto del Prompt:

"Estoy desarrollando un juego de Backgammon en Python. Tengo las clases: Checker, Player, Board, Dice y BackgammonGame.

## Código actual de `mover_ficha()` con problemas:
```python
def mover_ficha(self, origen, destino):
    origen = int(origen)
    destino = int(destino)
    jugador = self.get_jugador_actual()
    color = Player.get_color()  # ❌ ERROR: Método de clase en vez de instancia
    
    # Código duplicado para calcular distancia (aparece 2 veces)
    if len(self.__board__.get_bar()) > 0:
        if origen != 0:
            raise ValueError("Debes mover primero las fichas del bar.")
        if not self.__board__.mover_ficha_comida(destino, color):
            raise ValueError("No puedes ingresar la ficha del bar en ese punto.")
        
        if color == "Blancas":
            movida = self.__board__.distancia_blancas(origen, destino)
        else:
            movida = self.__board__.distancia_negras(origen, destino)
        
        if movida not in self.__dado__.movimientos:
            raise ValueError("El movimiento no coincide con los dados.")
        self.__dado__.movimientos.remove(movida)
        return True
    
    self.__board__.movimiento_valido(origen, destino, color)
    
    # Código duplicado otra vez
    if color == "Blancas":
        movida = self.__board__.distancia_blancas(origen, destino)
    else:
        movida = self.__board__.distancia_negras(origen, destino)
    
    if movida not in self.__dado__.movimientos:
        raise ValueError("Movimiento no válido según los dados.")
    
    if self.__board__.comer_ficha(destino, origen, color, None):
        self.__dado__.movimientos.remove(movida)
        return True
    
    if self.__board__.mover_ficha(origen, destino, color):
        self.__dado__.movimientos.remove(movida)
        return True
    
    raise ValueError("No se pudo mover la ficha.")
Problemas a resolver:

Error crítico: Player.get_color() debe ser jugador.get_color()
Código duplicado: Cálculo de distancia repetido 2 veces
ValueError genérico: No permite distinguir tipos de errores (bar, dados, punto bloqueado, etc.)
Falta delegación: Lógica de distancia debería estar en Board


Lo que necesito:
1️⃣ Sistema completo de excepciones (core/exceptions.py)
Diseña excepciones personalizadas para:

Fichas en el bar (deben moverse primero)
Dados no disponibles
Punto de destino bloqueado
Movimiento en dirección incorrecta
Movimiento fuera de rango
Bearing-off sin cumplir condiciones
No hay movimientos posibles

Incluye:

Clase base BackgammonError
Jerarquía de excepciones específicas
Docstrings explicativos
Atributos útiles (origen, destino, dados_disponibles, etc.)

2️⃣ Refactorización completa de mover_ficha()
Que incluya:

Corrección del error Player.get_color()
Eliminación de código duplicado
Uso de excepciones personalizadas
Métodos auxiliares privados (_calcular_distancia(), _mover_desde_bar(), etc.)
Código legible y mantenible

3️⃣ Método en Board para delegar responsabilidad
pythondef calcular_distancia(self, origen, destino, color):
    """Calcula distancia según dirección del jugador"""
    # Implementación que elimine el if/else duplicado
4️⃣ Ejemplos de manejo de excepciones
Muestra cómo capturar estas excepciones en:

CLI/Consola: Con mensajes amigables
Testing: Verificar que se lancen correctamente
GUI (opcional): Con diálogos/notificaciones

5️⃣ Tabla comparativa antes/después
Mostrando ventajas específicas del nuevo diseño.

Preguntas adicionales:

¿Es mejor usar ficha (objeto) en vez de color (string)?
¿Agregar atributos como self.origen y self.destino a las excepciones?
¿Excepción diferente para "no hay movimientos" vs "movimiento específico inválido"?


Requisitos:

Python 3.8+
PEP 8
Sin dependencias externas
Código autodocumentado

Objetivo:
Código profesional con excepciones semánticas, sin duplicación, fácil de testear y mantener."

### Instrucciones del sistema:
No se aplicaron instrucciones de sistema personalizadas.

### Respuesta completa de la IA:

Claude proporcionó un sistema completo de excepciones y refactorización:

**1. Sistema de excepciones (`core/exceptions.py`):**

```python
class BackgammonError(Exception):
    """Clase base para todas las excepciones del juego"""
    pass

class FichasEnBarError(BackgammonError):
    """Se lanzacuando hay fichas en la barra que deben moverse primero"""
    def __init__(self, color: str):
        self.color = color
        super().__init__(f"Debes mover primero las fichas de {color} desde la barra")

class DadoNoDisponibleError(BackgammonError):
    """El movimiento requiere un dado que no está disponible"""
    def __init__(self, movimiento: int, dados_disponibles: List[int]):
        self.movimiento = movimiento
        self.dados_disponibles = dados_disponibles
        super().__init__(
            f"Movimiento de {movimiento} no disponible. "
            f"Dados: {dados_disponibles}"
        )

class PuntoBloqueadoError(BackgammonError):
    """El destino está bloqueado por el oponente"""
    def __init__(self, destino: int, fichas_oponente: int):
        self.destino = destino
        self.fichas_oponente = fichas_oponente
        super().__init__(
            f"Punto {destino} bloqueado ({fichas_oponente} fichas del oponente)"
        )

class MovimientoInvalidoError(BackgammonError):
    """Movimiento genérico inválido"""
    def __init__(self, origen: int, destino: int, razon: str = ""):
        self.origen = origen
        self.destino = destino
        super().__init__(
            f"Movimiento inválido de {origen} a {destino}. {razon}"
        )
```

**2. Refactorización de `mover_ficha()`:**

```python
def mover_ficha(self, origen: int, destino: int) -> bool:
    origen, destino = int(origen), int(destino)
    jugador = self.get_jugador_actual()
    color = jugador.get_color()  # ✅ Corregido
    
    # Validar fichas en barra
    if len(self.__board__.get_bar()) > 0:
        if origen != 0:
            raise FichasEnBarError(color)
        return self._mover_desde_bar(destino, color)
    
    # Validar movimiento
    self.__board__.movimiento_valido(origen, destino, color)
    
    # Calcular distancia (delegado a Board)
    movida = self.__board__.calcular_distancia(origen, destino, color)
    
    # Validar dado disponible
    if movida not in self.__dado__.movimientos:
        raise DadoNoDisponibleError(movida, self.__dado__.movimientos[:])
    
    # Intentar movimiento
    if self.__board__.comer_ficha(destino, origen, color, None):
        self.__dado__.movimientos.remove(movida)
        return True
    
    if self.__board__.mover_ficha(origen, destino, color):
        self.__dado__.movimientos.remove(movida)
        return True
    
    raise MovimientoInvalidoError(origen, destino, "No se pudo ejecutar")

def _mover_desde_bar(self, destino: int, color: str) -> bool:
    """Método auxiliar privado para movimientos desde barra"""
    if not self.__board__.mover_ficha_comida(destino, color):
        raise PuntoBloqueadoError(destino, 
            len(self.__board__.get_punto(destino)))
    
    movida = self.__board__.calcular_distancia(0, destino, color)
    
    if movida not in self.__dado__.movimientos:
        raise DadoNoDisponibleError(movida, self.__dado__.movimientos[:])
    
    self.__dado__.movimientos.remove(movida)
    return True
```

**3. Método en Board para delegación:**

```python
def calcular_distancia(self, origen: int, destino: int, color: str) -> int:
    """Calcula distancia según dirección del jugador"""
    if color == "Blancas":
        return self.distancia_blancas(origen, destino)
    else:
        return self.distancia_negras(origen, destino)
```

**4. Manejo en CLI:**

```python
try:
    game.mover_ficha(origen, destino)
    print("✓ Movimiento exitoso")
except FichasEnBarError as e:
    print(f"❌ {e}")
except DadoNoDisponibleError as e:
    print(f"❌ {e}")
    print(f"   Dados disponibles: {e.dados_disponibles}")
except PuntoBloqueadoError as e:
    print(f"❌ {e}")
except MovimientoInvalidoError as e:
    print(f"❌ {e}")
```

**5. Ventajas del nuevo diseño:**

| Aspecto | Antes | Después |
|---------|-------|---------|
| **Errores** | ValueError genérico | Excepciones específicas |
| **Debugging** | Mensaje string | Atributos tipados |
| **Testing** | `assertRaises(ValueError)` | `assertRaises(DadoNoDisponibleError)` |
| **Código duplicado** | Cálculo de distancia 2 veces | Método delegado 1 vez |
| **Mantenibilidad** | Difícil rastrear errores | Clara jerarquía de excepciones |

### Resultado obtenido:
**Usado con modificaciones**

Se implementó el sistema de excepciones completo y se refactorizó `mover_ficha()`:
- Archivo `core/exceptions.py` creado con todas las excepciones
- Método `mover_ficha()` refactorizado en `core/backgammongame.py`
- Método `calcular_distancia()` añadido a `core/board.py`
- CLI actualizada para manejar excepciones específicas en `cli/cli.py`

**Modificaciones realizadas:**
- Se agregó `OrigenInvalidoError` para validar posición de origen
- Se simplificó la lógica de bearing-off usando excepciones
- Se añadieron docstrings en español

### Referencias a archivos finales:
- `core/exceptions.py` - Sistema completo de excepciones
- `core/backgammongame.py` (método `mover_ficha`, líneas 65-95)
- `core/board.py` (método `calcular_distancia`, líneas 110-115)
- `cli/cli.py` (manejo de excepciones, líneas 45-75)

---

## Prompt: Mejoras y Conflictos en Backgammon CLI

### Modelo/Herramienta utilizada:
ChatGPT (GPT-4)

### Texto exacto del Prompt:

"Estoy desarrollando un juego de Backgammon en Python y quiero mejorar mi CLI para que sea más clara y completa, pero sin complicarla.
Quiero que me guies para agregar que en cada turno se muestre el estado del juego: movimientos disponibles, fichas en el bar, fichas sacadas y el tablero.
Además, tuve problemas de conflicto de merge con archivos como .coverage, coverage.xml y __pycache__/*.pyc después de hacer pull y checkout.
Necesito una explicación breve de cómo resolver estos conflictos y dejar todo como mi versión local, sin perder los archivos de reporte que pide la entrega."

### Instrucciones del sistema:
No se aplicaron instrucciones de sistema personalizadas.

### Respuesta completa de la IA:

**1. Mejoras para la CLI:**

ChatGPT sugirió agregar un método `mostrar_estado()` en la clase CLI:

```python
def mostrar_estado(self, game):
    print("\n" + "="*60)
    print(f"Turno de: {game.get_jugador_actual().get_nombre()} ({game.get_jugador_actual().get_color()})")
    print("="*60)
    
    # Movimientos disponibles
    movimientos = game.get_dados().movimientos
    print(f"Dados disponibles: {movimientos if movimientos else 'Ninguno'}")
    
    # Fichas en barra
    bar = game.get_board().get_bar()
    if bar:
        print(f"Fichas en barra: {bar}")
    
    # Fichas sacadas
    blancas_sacadas = len(game._BackgammonGame__fichas_sacadas_blancas__)
    negras_sacadas = len(game._BackgammonGame__fichas_sacadas_negras__)
    print(f"Fichas sacadas - Blancas: {blancas_sacadas}, Negras: {negras_sacadas}")
    
    # Tablero
    self.mostrar_tablero(game.get_board())
    print("="*60 + "\n")
```

**2. Sobre conflictos de merge:**

ChatGPT explicó:

**Archivos que NUNCA deben commitearse:**
- `.coverage`
- `coverage.xml`
- `__pycache__/*.pyc`
- `htmlcov/`

**Solución:**
1. Agregar a `.gitignore`:
```
# Coverage
.coverage
coverage.xml
htmlcov/

# Python cache
__pycache__/
*.pyc
*.pyo
```

2. Resolver conflictos:
```bash
# Si ya están en staging/conflicto
git rm --cached .coverage coverage.xml
git rm --cached -r __pycache__/

# Volver a tu versión local en conflictos
git checkout --ours archivo_en_conflicto.py

# O aceptar la versión remota
git checkout --theirs archivo_en_conflicto.py
```

3. Para reportes de entrega:
```bash
# Generar reportes limpios antes de entregar
coverage run -m pytest
coverage report
coverage xml
```

### Resultado obtenido:
**Usado con modificaciones**

Se implementaron las mejoras en la CLI:
- Método `mostrar_estado()` agregado con formato simplificado
- Se actualizó `.gitignore` para excluir archivos de coverage
- Se creó script `generate_reports.py` para generar reportes antes de entregar

**Modificaciones realizadas:**
- Se simplificó el formato visual del estado
- Se agregó validación para no mostrar fichas en barra si está vacía
- Se mejoró el método `mostrar_tablero()` para mejor visualización

### Referencias a archivos finales:
- `cli/cli.py` (método `mostrar_estado`, líneas 25-50)
- `.gitignore` (líneas 1-10)
- `generate_reports.py` - Script para generar reportes

---

## Prompt: Refactorización de Clases (Checker vs Game)

### Modelo/Herramienta utilizada:
GitHub Copilot (GPT-4)

### Texto exacto del Prompt:

"creo que quiero mover fichas sacadas a game tiene sentido? hace falta eliminar checker?"

### Contexto proporcionado:

El usuario tenía este código:
class BackgammonGame:
    def __init__(self, ...):
        # ...
        self.__fichas_blancas__ = Checker("Blancas", ...)
        self.__fichas_negras__ = Checker("Negras", ...)
    
    def get_ganador(self):
        blancas_sacadas = len(self.__fichas_blancas__.get_fichas_sacadas_blancas())
        #...
El enunciado del proyecto (Punto 5.1) especifica: Checker → Representa cada ficha. El diseño actual del usuario es confuso.

Solicitud del usuario
"creo que quiero mover fichas sacadas a game tiene sentido?"  "hace falta eliminar checker?"

Problema identificado
El diseño de la clase Checker del usuario no se alinea con la responsabilidad definida en el enunciado, creando una clase confusa que solo se usa para mantener un contador. La lógica de "fichas sacadas" es un estado del juego (BackgammonGame), no de una entidad Checker separada.

Tarea
Validar la intuición del usuario ("Sí, tiene muchísimo sentido").

Explicar por qué es una buena idea (centraliza el estado, limpia el diseño).

Proporcionar el código refactorizado para BackgammonGame.py:

Modificar __init__ para usar self.__fichas_sacadas_blancas__ = [].

Modificar mover_ficha para usar .append() en esa lista.

Modificar get_ganador y estado_actual para usar len() de esa lista.

Aconsejar firmemente (en rol de "profe") la eliminación de los archivos core/checker.py y tests/tests_checker.py por ser "código muerto" y mala práctica.

Actualizar el archivo de tests tests_backgammongame.py para que refleje los cambios (ej. en test_get_ganador_blancas).

Estilo de respuesta esperado
Actuar como un guía/profesor que valida una buena idea de diseño.

Ser claro sobre por qué la refactorización es correcta.

