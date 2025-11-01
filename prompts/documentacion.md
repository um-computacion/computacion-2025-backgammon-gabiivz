# Prompt: Reglas completas del Backgammon para implementar en código

## Modelo/Herramienta utilizada:
Claude.ai (Claude 3.5 Sonnet)

## Texto exacto del Prompt:

"Necesito implementar un juego de Backgammon en Python y requiero conocer todas las reglas del juego para poder programar la lógica correctamente. ¿Me puedes explicar las reglas completas del Backgammon incluyendo: configuración inicial, movimientos, capturas, bearing off, y condiciones de victoria?"

## Instrucciones del sistema:
No se aplicaron instrucciones de sistema personalizadas.

## Respuesta completa de la IA:

## Respuesta completa de la IA:

Claude proporcionó una explicación detallada de todas las reglas de Backgammon:

### Objetivo del juego
Ser el primer jugador en mover todas sus fichas (checkers) fuera del tablero.

### Configuración inicial
- **Tablero**: 24 puntos (triángulos) numerados del 1 al 24
- **Fichas**: Cada jugador tiene 15 fichas
- **Dados**: 2 dados regulares + 1 dado doblador (opcional)
- **Posición inicial**: 
  - 2 fichas en el punto 24
  - 5 fichas en el punto 13  
  - 3 fichas en el punto 8
  - 5 fichas en el punto 6

### Movimiento básico
1. **Tirar dados**: Cada jugador tira 2 dados por turno
2. **Mover fichas**: Cada dado representa un movimiento separado
3. **Dirección**: Las fichas se mueven en sentido horario hacia el "home board" (puntos 1-6)
4. **Suma de dados**: Si salen 3 y 5, puedes mover una ficha 3 espacios y otra 5 espacios, O una sola ficha 8 espacios

### Dados dobles
- Si salen **dos números iguales** (ej: 4-4), juegas **4 movimientos** de ese número
- Ejemplo: Con doble 4, puedes hacer 4 movimientos de 4 espacios cada uno

### Reglas de movimiento
#### ✅ Movimientos válidos:
- A un punto **vacío**
- A un punto con **tus propias fichas**
- A un punto con **solo 1 ficha enemiga** (blot)

#### ❌ Movimientos inválidos:
- A un punto con **2 o más fichas enemigas**

### Captura (Hit)
- Si mueves a un punto con **1 ficha enemiga**, la capturas
- La ficha capturada va a la **barra central**
- El oponente debe **re-entrar** esa ficha antes de hacer otros movimientos

### Re-entrada desde la barra
- Las fichas en la barra deben entrar por el **home board enemigo** (puntos 19-24 para el jugador que re-entra)
- Solo puedes entrar a puntos **no bloqueados** por el oponente
- Si no puedes re-entrar, **pierdes tu turno**

### Bearing Off (Sacar fichas)
- Solo puedes sacar fichas cuando **todas** tus fichas estén en tu home board (puntos 1-6)
- El número del dado debe **coincidir exactamente** con el punto, O ser **mayor** si no hay fichas en puntos superiores
- Ejemplo: Con dado 6, puedes sacar una ficha del punto 6, o del punto más alto si no hay fichas en el 6

### Uso obligatorio de dados
- **DEBES usar ambos dados** si es posible
- Si solo puedes usar uno, debes usar el **número más alto**
- Si no puedes usar ningún dado, pierdes el turno

### Blocking
- **6 puntos consecutivos** con 2+ fichas cada uno = "Prime" (bloqueo total)
- El oponente no puede pasar ese bloqueo

### Cubo doblador (Doubling cube)
- Empieza en 1, puede doblarse a 2, 4, 8, 16, 32, 64
- El jugador puede **ofrecer doblar** antes de tirar dados
- El oponente puede **aceptar** (continúa el juego por el doble de puntos) o **rendirse** (pierde los puntos actuales)

- Detectar condiciones de victoria

---

## Resultado obtenido:
**Usado como referencia**

La información proporcionada por Claude fue utilizada como documentación de referencia durante todo el desarrollo del proyecto. Se consultó especialmente para:
- Implementar la lógica de movimientos válidos en `Board.movimiento_valido()`
- Validar capturas en `Board.comer_ficha()`
- Implementar bearing off en `Board.sacar_ficha()`
- Verificar condiciones de victoria en `BackgammonGame.get_ganador()`

No se tradujo directamente a código, sino que sirvió como guía para entender las reglas y tomar decisiones de diseño.

## Referencias a archivos finales:
- `core/board.py` - Implementación de reglas de movimiento y captura
- `core/backgammongame.py` - Lógica de juego y condiciones de victoria
- `ReadMe.md` - Documentación del proyecto con reglas resumidas
#### Victoria simple (1 punto):
- Sacas todas tus fichas antes que el oponente

#### Gammon (2 puntos):
- Sacas todas tus fichas Y el oponente no sacó ninguna

#### Backgammon (3 puntos):
- Sacas todas tus fichas Y el oponente tiene fichas en tu home board o en la barra

### Reglas especiales
1. **Crawford Rule**: Cuando un jugador está a 1 punto de ganar un match, no se puede usar el cubo doblador en esa partida
2. **Jacoby Rule**: Gammons y backgammons solo cuentan si se usó el cubo doblador
3. **Pip count**: Suma de espacios que faltan mover para sacar todas las fichas (usado para estrategia)

## Aspectos críticos para implementación en código:

### 🔧 Lógica fundamental:
- **Movimiento básico**: 2 dados = 2 movimientos separados
- **Dados dobles**: Mismo número = 4 movimientos
- **Validación**: Verificar si un punto está bloqueado (2+ fichas enemigas)
- **Captura**: Solo fichas solitarias pueden ser capturadas
- **Re-entrada**: Fichas en barra deben entrar primero
- **Bearing off**: Solo cuando todas las fichas están en home board

### 🎯 Componentes clave a implementar:
1. **Validación de movimientos legales**
2. **Gestión de la barra** 
3. **Detección de bloqueos**
4. **Cálculo de bearing off**
5. **Detección de gammon/backgammon**
6. **Sistema de turnos y uso obligatorio de dados**
7. **Lógica del cubo doblador**

## Lo que necesito:
Ayuda para implementar estas reglas en Python, especialmente los algoritmos para:
- Validar si un movimiento es legal
- Manejar la captura y re-entrada de fichas
- Implementar la lógica de bearing off
- Detectar condiciones de victoria

---
