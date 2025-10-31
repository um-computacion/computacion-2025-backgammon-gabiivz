🎲 Backgammon
Alumno: Gabriela Vaca 
Carrera: Ingeniería en Informática 
Ciclo lectivo: 2025

📋 Descripción
Este proyecto implementa una versión completa del juego Backgammon en Python, con soporte para juego por consola (CLI) y una interfaz gráfica (Pygame) desacoplada de la lógica.

Clases principales
BackgammonGame: Orquestador principal. Coordina la lógica completa de una partida, gestiona los turnos, el estado del juego y determina al ganador.

Board: Representa el tablero. Implementa todas las reglas de movimiento (normal, comer, salir del bar), validaciones de puntos y gestiona el bar (fichas comidas).

Player: Representa a los jugadores con su nombre y color de fichas.

Dice: Maneja la tirada de dados y la lista de movimientos disponibles, incluyendo la lógica de dados dobles.

Exceptions: Define excepciones personalizadas para manejar todos los errores específicos del juego (movimientos inválidos, dados no disponibles, etc.).

Estructura adicional
cli/: Interfaz por línea de comandos para jugar en la terminal.

pygame_ui/: (Opcional si ya lo tienes) Interfaz gráfica con Pygame.

htmlcov/: Reportes de cobertura de código en formato HTML.

prompts/: Documentación del proceso de desarrollo con IA.

tests/: Suite completa de tests unitarios para cada módulo del core.

🚀 Instalación
1. Clonar el repositorio
Bash

git clone https://github.com/usuario/backgammon-gabiivz.git
cd backgammon-gabiivz
2. Crear un entorno virtual
Windows:

Bash

python -m venv venv
venv\Scripts\activate

3. Instalar dependencias
Bash

pip install -r requirements.txt
🎮 Uso
Jugar en modo consola
Bash

python -m cli.cli
Ejecutar tests
Todos los tests:

Bash

python -m unittest discover tests
Tests específicos:

Bash

python -m unittest tests.tests_backgammon
python -m unittest tests.tests_board
python -m unittest tests.tests_dice
python -m unittest tests.tests_player
Generar reporte de cobertura
Bash

coverage run -m unittest discover tests
coverage report
coverage html
Luego abrir htmlcov/index.html en un navegador para ver el reporte detallado.

📁 Estructura del Proyecto
backgammon-gabiivz/
│
├── cli/
│   └── cli.py                 # Interfaz de línea de comandos
│
├── core/
│   ├── __init__.py
│   ├── backgammongame.py      # Lógica principal del juego
│   ├── board.py               # Tablero y validaciones
│   ├── dice.py                # Sistema de dados
│   ├── exceptions.py          # Excepciones personalizadas
│   └── player.py              # Representación de jugadores
│
├── htmlcov/                   # Reportes de cobertura HTML
│
├── prompts/
│   ├── desarrollo.md          # Prompts de desarrollo
│   ├── documentacion.md       # Prompts de documentación
│   └── testing.md             # Prompts de testing
│
├── tests/
│   ├── __init__.py
│   ├── tests_backgammon.py    # Tests del juego principal
│   ├── tests_board.py         # Tests del tablero
│   ├── tests_dice.py          # Tests de dados
│   └── tests_player.py        # Tests de jugadores
│
├── venv/                      # Entorno virtual
│
├── .coverage                  # Datos de cobertura
├── .coveragerc                # Configuración de coverage
├── .pylintrc                  # Configuración de pylint
├── CHANGELOG.md               # Historial de cambios
├── JUSTIFICACION.md           # Justificación de diseño
├── pylint_report.txt          # Reporte de pylint
├── README.md                  # Este archivo
└── requirements.txt           # Dependencias del proyecto
🧪 Testing
El proyecto cuenta con una suite completa de tests unitarios. La cobertura actual del código core es del 98%.

Excepciones personalizadas
El juego implementa las siguientes excepciones para manejar situaciones específicas:

BackgammonError: Excepción base

MovimientoInvalidoError: Movimiento no válido según las reglas

FichaEnBarError: Intento de mover sin resolver fichas en el bar

DadoNoDisponibleError: El dado necesario no está disponible

PuntoOcupadoError: El punto destino está bloqueado

DireccionInvalidaError: Dirección de movimiento incorrecta

MovimientoFueraDeRangoError: Movimiento fuera del tablero

SinMovimientosPosiblesError: No hay movimientos legales

TurnoInvalidoError: Jugador incorrecto intenta mover

DadosNoTiradosError: Intento de mover sin tirar dados

PartidaFinalizadaError: La partida ya terminó

🎯 Reglas del Backgammon
El Backgammon es un juego de mesa para dos jugadores que combina estrategia y suerte. Cada jugador tiene 15 fichas que debe mover alrededor del tablero según el resultado de dos dados.

Objetivo
Ser el primero en mover todas tus fichas a tu casa (cuadrante final) y luego sacarlas del tablero.

Movimientos básicos (Según implementación)
Se tiran dos dados al inicio de cada turno.

Cada dado representa un movimiento independiente.

Si salen dados dobles, se juega cada número dos veces (4 movimientos).

Blancas: Se mueven desde los números altos a los bajos (ej. de 24 a 1). Su casa es el cuadrante 1-6.

Negras: Se mueven desde los números bajos a los altos (ej. de 1 a 24). Su casa es el cuadrante 19-24.

Reglas especiales
Bar (fichas comidas): Si una ficha es capturada, debe reingresar desde el bar antes de poder mover otras fichas.

Bloqueo: Un punto con 2 o más fichas del oponente está bloqueado.

Captura: Solo se puede capturar si el punto tiene exactamente una ficha del oponente.

🛠️ Tecnologías utilizadas
Python 3.12+

unittest: Framework de testing

coverage: Análisis de cobertura de código

pylint: Linter para calidad de código

