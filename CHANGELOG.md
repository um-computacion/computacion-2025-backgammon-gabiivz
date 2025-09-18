# CHANGELOG

Este archivo registra todos los cambios realizados en el proyecto Backgammon.

El formato sigue Keep a Changelog y el proyecto utiliza Semantic Versioning.

## [UNRELEASED]

### Added
- Se agregaron tests unitarios para la clase BackgammonGame, cubriendo turnos, jugadores y métodos de dados.
- Se implementaron tests para los métodos get_board, get_jugador_blancas, get_jugador_negras y cambio_turnos.
- Se añadieron tests para la clase Dice usando patch para controlar los valores de los dados.
- Se agregaron tests para la clase Player y Checker, verificando getters y representación en string.
- Se ampliaron los tests en la clase Board para cubrir movimientos válidos, inválidos y casos de comer ficha.
- Se agregaron tests para asegurar la cobertura de los métodos de distancia y validación de movimientos en Board.

### Changed
- Se mejoró la estructura de los tests dividiéndolos en funciones pequeñas y específicas.
- Se ajustaron los tests para acceder correctamente a los atributos privados de las clases.
- Se actualizaron los tests de Dice para cubrir casos de dobles, valores distintos y errores en randint.

### Fixed
- Se corrigieron errores en los tests que no accedían correctamente a los atributos privados.
- Se solucionaron problemas de cobertura en los métodos de Board y Dice.
- Se ajustaron los tests para contemplar correctamente los casos de excepción en movimientos inválidos.

### Removed
- Se eliminaron tests redundantes y se consolidaron casos similares para simplificar la suite de pruebas.

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