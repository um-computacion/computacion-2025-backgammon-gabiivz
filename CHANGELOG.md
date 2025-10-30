# CHANGELOG

Este archivo registra todos los cambios realizados en el proyecto Backgammon.

El formato sigue Keep a Changelog y el proyecto utiliza Semantic Versioning.

## [UNRELEASED]

### Added

### Changed

### Fixed

### Removed

## [1.3.0] - Cuarto Sprint

### Added
- Se implementó una interfaz de línea de comandos (CLI) en `main.py` para permitir la interacción del usuario y jugar una partida completa.
- Se completó la lógica de la clase `BackgammonGame`, integrando la gestión de turnos, el lanzamiento de dados, el movimiento de fichas y la detección del ganador.
- Se añadió la lógica para manejar el ciclo de juego completo, desde el inicio hasta que se declara un ganador.
- Se agregaron tests unitarios exhaustivos para `BackgammonGame`, cubriendo escenarios de juego complejos, movimientos desde el bar y el retiro de fichas.
- Se implementaron tests para los métodos `get_board`, `get_jugador_blancas`, `get_jugador_negras` y `cambio_turnos`.
- Se añadieron tests para la clase `Dice` usando `patch` para simular tiradas de dados específicas.
- Se agregaron tests para la clase `Player`, verificando la correcta creación y obtención de sus atributos.

### Changed
- Se refactorizó la clase `BackgammonGame` para centralizar la lógica de las reglas del juego y simplificar la interacción con el `Board`.
- Se modificó la clase `Board` para delegar las validaciones de movimientos complejos a `BackgammonGame`, enfocándose solo en el estado del tablero.
- Se mejoró la legibilidad de todos los tests unitarios añadiendo docstrings descriptivos en español a cada función de prueba.
- Se ajustaron los tests existentes para reflejar la nueva arquitectura y el acceso a los atributos de las clases.

### Fixed
- Se corrigió el acceso a atributos privados en los tests para asegurar que las pruebas sean robustas y no dependan de la implementación interna.
- Se solucionaron problemas de cobertura de código en las clases `Board` y `Dice` mediante la adición de tests para casos borde.
- Se ajustaron los tests de movimientos para contemplar correctamente el lanzamiento de excepciones personalizadas.

### Removed
- Se eliminó la clase `Checker`, ya que su funcionalidad fue absorbida y simplificada dentro de las clases `Board` y `BackgammonGame`.
- Se eliminaron tests redundantes que probaban la misma funcionalidad, consolidándolos en pruebas más completas y específicas.

## [1.2.0] - Tercer Sprint

### Added
- Se implementaron múltiples funcionalidades nuevas en la clase BackgammonGame:
  - Método verificar_fin_juego para detectar cuando un jugador ha retirado todas sus fichas.
  - Método obtener_movimientos_validos que retorna todos los movimientos posibles para el turno actual.
  - Método puede_mover para verificar si un jugador tiene al menos un movimiento legal disponible.
  - Sistema de validación de entrada de usuario para coordenadas del tablero.
- Se agregaron tests exhaustivos para todas las nuevas funcionalidades, aumentando significativamente el coverage del proyecto.
- Se implementaron tests de integración que prueban escenarios completos de juego desde inicio hasta fin.
- Se añadieron tests para casos edge como tableros vacíos, múltiples fichas en el banco y situaciones de bloqueo.

### Changed
- Se refactorizó el método mover_ficha en BackgammonGame para mejorar la legibilidad y mantenibilidad del código.
- Se optimizó el método reingresar_ficha para reducir la complejidad ciclomática.
- Se actualizó la lógica de cambio de turnos para manejar correctamente los casos donde un jugador no puede mover.
- Se mejoró la documentación interna de los métodos en BackgammonGame con docstrings más descriptivos.

### Fixed
- Se corrigió un bug en el método ganador que no detectaba correctamente la victoria cuando la última ficha era retirada.
- Se solucionó un problema en posiciones que no validaba correctamente las fichas en posiciones intermedias antes de permitir retiros.
- Se arreglaron inconsistencias en la gestión del banco cuando múltiples fichas del mismo color eran comidas consecutivamente.

## [1.1.0] - Segundo Sprint

### Added
- Clase 'Board' y sus test: se agregaron las ultimas funciones que necesitaba.
- Clase 'Checker' y sus test: estructura principal, métodos get_movimiento, en_banco, ficha_afuera, __str__.
- Tests para cada clase cubriendo los métodos principales.
- Se agregaron test en la clase Dice vistos en clase para poder testear la herramienta randint.
- Se agregaron test en la clase Board para aumentar el coverage.
- Se comenzó a implementar la clase Backgammon, que relaciona todas las clases.
- Se agregaron test para los métodos implementados en Backgammon.
- Se agregaron funciones y test en la clase Backgammon.
- Se implementó el método mover_ficha en la clase Backgammon.
- Se implementó el método reingresar_ficha en la clase Backgammon.
- Se implementó el método ganador en la clase Backgammon.
- Se implementó el método posiciones en la clase Backgammon, para permitir retirar una ficha.
- Se implementó el método retirar_ficha, la cual saca definitivamente a una ficha del tablero.

### Fixed
- Había líneas en las clases Board y Dice que no eran testeadas.
- En el método devolver_ficha_comida no se respetaba que si se encontraba una sola ficha en cierta posición, el oponente que se encontraba esperando a sacar la ficha del banco, podía comer a su rival.
- Se corrigió el método retirar_ficha, que solo verificaba que una ficha podía ser retirada si el dado coincidía exactamente con la distancia que le faltaba a la ficha para salir.

### Removed
- Se eliminó el método distancia que generaba redundancia y provocaba error en los test.

## [1.0.0] - Primer Sprint

### Added
- Creación de las carpetas y sus archivos.
- Clase 'Player' y sus test: estructura principal, métodos get_nombre y get_ficha.
- Clase 'Dice' y sus test: estructura principal, método movimiento, método tirar, lógica de dobles y valores distintos.
- Clase 'Board' y sus test: estructura principal, método inicializar, banco, distancia, validar_movimiento, ficha_comida, devolver_ficha, mover_ficha, sin_fichas.

### Fixed
- Corrección en los métodos validar_movimiento y mover_ficha para contemplar casos inválidos de destino y origen.
- Ajuste en devolver_ficha_comida para cubrir casos de fichas del mismo color y del color opuesto.
- Agregados tests adicionales en la clase Board para incrementar la cobertura hasta 100%.