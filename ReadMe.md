# 🎲 Backgammon

**Alumno:** Ivañez Gabriela  
**Carrera:** Ingeniería en Informática  
**Ciclo lectivo:** 2025

---

## 📋 Descripción

Este proyecto implementa una versión completa del juego **Backgammon** en Python, con soporte para juego por consola y una base preparada para interfaz gráfica.

### Clases principales

* **`BackgammonGame`**: Coordina la lógica completa de una partida, gestiona turnos y determina ganadores.
* **`Board`**: Representa el tablero, implementa reglas de movimiento, validaciones y gestiona el bar (banco de fichas comidas).
* **`Player`**: Representa a los jugadores con su nombre y color de fichas.
* **`Dice`**: Maneja la tirada de dados y los movimientos disponibles, incluyendo dados dobles.
* **`Checker`**: Gestiona las fichas y su interacción en el tablero, incluyendo fichas sacadas.
* **`Exceptions`**: Define excepciones personalizadas para manejar errores específicos del juego.

### Estructura adicional

* **`cli/`**: Interfaz por línea de comandos para jugar en terminal.
* **`htmlcov/`**: Reportes de cobertura de código en formato HTML.
* **`prompts/`**: Documentación del proceso de desarrollo con IA.
* **`tests/`**: Suite completa de tests unitarios para cada módulo.

---

## 🚀 Instalación

### 1. Clonar el repositorio

```bash
git clone https://github.com/usuario/backgammon-gabiivz.git
cd backgammon-gabiivz
```

### 2. Crear un entorno virtual

**Linux/Mac:**
```bash
python3 -m venv venv
source venv/bin/activate
```

**Windows:**
```bash
python -m venv venv
venv\Scripts\activate
```

### 3. Instalar dependencias

```bash
pip install -r requirements.txt
```

---

## 🎮 Uso

### Jugar en modo consola

```bash
python -m cli.cli
```

### Ejecutar tests

**Todos los tests:**
```bash
python -m unittest discover tests
```

**Tests específicos:**
```bash
python -m unittest tests.tests_backgammon
python -m unittest tests.tests_board
python -m unittest tests.tests_checker
python -m unittest tests.tests_dice
python -m unittest tests.tests_player
```

### Generar reporte de cobertura

```bash
coverage run -m unittest discover tests
coverage report
coverage html
```

Luego abrir `htmlcov/index.html` en un navegador para ver el reporte detallado.

---

## 📁 Estructura del Proyecto

```
backgammon-gabiivz/
│
├── cli/
│   └── cli.py                    # Interfaz de línea de comandos
│
├── core/
│   ├── __init__.py
│   ├── backgammongame.py         # Lógica principal del juego
│   ├── board.py                  # Tablero y validaciones
│   ├── checker.py                # Gestión de fichas
│   ├── dice.py                   # Sistema de dados
│   ├── exceptions.py             # Excepciones personalizadas
│   └── player.py                 # Representación de jugadores
│
├── htmlcov/                      # Reportes de cobertura HTML
│
├── prompts/
│   ├── desarrollo.md             # Prompts de desarrollo
│   ├── documentacion.md          # Prompts de documentación
│   └── testing.md                # Prompts de testing
│
├── tests/
│   ├── __init__.py
│   ├── tests_backgammon.py       # Tests del juego principal
│   ├── tests_board.py            # Tests del tablero
│   ├── tests_checker.py          # Tests de fichas
│   ├── tests_dice.py             # Tests de dados
│   └── tests_player.py           # Tests de jugadores
│
├── venv/                         # Entorno virtual
│
├── .coverage                     # Datos de cobertura
├── .coveragerc                   # Configuración de coverage
├── .pylintrc                     # Configuración de pylint
├── CHANGELOG.md                  # Historial de cambios
├── coverage_report.txt           # Reporte de cobertura en texto
├── coverage.xml                  # Reporte de cobertura en XML
├── pylint_report.txt             # Reporte de pylint
├── README.md                     # Este archivo
└── requirements.txt              # Dependencias del proyecto
```

---

## 🧪 Testing

El proyecto cuenta con una suite completa de tests unitarios con las siguientes coberturas:

| Módulo | Cobertura |
|--------|-----------|
| `backgammongame.py` | 90%+ |
| `board.py` | 98% |
| `checker.py` | 100% |
| `dice.py` | 100% |
| `player.py` | 100% |
| **Total** | **~95%** |

### Excepciones personalizadas

El juego implementa las siguientes excepciones para manejar situaciones específicas:

* `BackgammonError`: Excepción base
* `MovimientoInvalidoError`: Movimiento no válido según las reglas
* `FichaEnBarError`: Intento de mover sin resolver fichas en el bar
* `DadoNoDisponibleError`: El dado necesario no está disponible
* `PuntoOcupadoError`: El punto destino está bloqueado
* `DireccionInvalidaError`: Dirección de movimiento incorrecta
* `MovimientoFueraDeRangoError`: Movimiento fuera del tablero
* `SinMovimientosPosiblesError`: No hay movimientos legales
* `TurnoInvalidoError`: Jugador incorrecto intenta mover
* `DadosNoTiradosError`: Intento de mover sin tirar dados
* `PartidaFinalizadaError`: La partida ya terminó

---

## 🎯 Reglas del Backgammon

El Backgammon es un juego de mesa para dos jugadores que combina estrategia y suerte. Cada jugador tiene 15 fichas que debe mover alrededor del tablero según el resultado de dos dados.

### Objetivo

Ser el primero en mover todas tus fichas a tu casa (cuadrante final) y luego sacarlas del tablero.

### Movimientos básicos

1. Se tiran dos dados al inicio de cada turno
2. Cada dado representa un movimiento independiente
3. Si salen dados dobles, se juega cada número dos veces (4 movimientos)
4. Las blancas se mueven en sentido horario (1→24)
5. Las negras se mueven en sentido antihorario (24→1)

### Reglas especiales

* **Bar (fichas comidas)**: Si una ficha es capturada, debe reingresar desde el bar antes de poder mover otras fichas
* **Bloqueo**: Un punto con 2 o más fichas del oponente está bloqueado
* **Captura**: Solo se puede capturar si el punto tiene exactamente una ficha del oponente

---

## 🛠️ Tecnologías utilizadas

* **Python 3.12+**
* **unittest**: Framework de testing
* **coverage**: Análisis de cobertura de código
* **pylint**: Linter para calidad de código

---

## 📝 Notas de desarrollo

Este proyecto fue desarrollado siguiendo buenas prácticas de programación:

* **Arquitectura modular**: Separación clara de responsabilidades
* **Testing exhaustivo**: Cobertura superior al 90%
* **Manejo de excepciones**: Errores específicos y descriptivos
* **Documentación**: Código comentado y documentado
* **Control de versiones**: Uso de Git con commits descriptivos

---

## 📄 Licencia

Este proyecto es parte del curso de Ingeniería en Informática - 2025

---

## 👥 Autor

**Gabriela Ivañez**  
Estudiante de Ingeniería en Informática  
Universidad Tecnológica Nacional

---

## 🔗 Enlaces útiles

* [Reglas oficiales del Backgammon](https://bkgm.com/rules.html)
* [Documentación de unittest](https://docs.python.org/3/library/unittest.html)
* [Coverage.py docs](https://coverage.readthedocs.io/)