"""
board_renderer.py
Responsabilidad:
- Encargado de dibujar todo lo visual del tablero.
- Dibuja los 24 triángulos (puntos) del Backgammon.
- Dibuja las fichas de los jugadores en la posición correcta.
- No contiene reglas del juego (la lógica sigue en core/).
- Solo “pinta” lo que le dicen que pinte.
"""

import pygame

class BoardRenderer:
    """Clase responsable de renderizar el tablero de Backgammon usando Pygame."""
    def __init__(self, pantalla, alto_tablero=None):
        """Inicializa el renderer del tablero, calculando geometría y paleta de colores."""
        self.pantalla = pantalla
        self.ancho = self.pantalla.get_width()
        self.alto = alto_tablero if alto_tablero else self.pantalla.get_height()
        
        self.ancho_triangulo = self.ancho // 14
        self.ancho_barra = self.ancho_triangulo
        self.alto_triangulo = self.alto // 2
        self.radio_ficha = self.ancho_triangulo // 3
        
        self.COLOR_FONDO_GENERAL = (195, 220, 195)
        self.COLOR_TRI_A = (240, 170, 170)
        self.COLOR_TRI_B = (245, 240, 210)
        self.COLOR_BARRA_CENTRAL = (210, 180, 140) 
        self.COLOR_BARRA_LATERAL = (210, 180, 140)
        
        self.COLOR_BORDE = (80, 80, 80)
        self.COLOR_LINEA_FICHA = (0, 0, 0)
        
        self.COLOR_FICHA_BLANCA = (245, 245, 245)
        self.COLOR_FICHA_NEGRA = (30, 30, 30)
        
        self.COLOR_TEXTO_GENERAL = (0, 0, 0)
        self.COLOR_MENSAJE_ERROR = (200, 0, 0)
        self.COLOR_MENSAJE_INFO = (0, 0, 0)
        self.COLOR_HEADER_FOOTER = (210, 180, 140)
        self.COLOR_TEXTO_HEADER = (0, 0, 0)
        self.COLOR_TEXTO_FOOTER_MSG = (0, 0, 0)
        self.COLOR_TEXTO_FOOTER_ERR = (200, 0, 0)

    def dibujar_tablero(self):
        """Dibuja el fondo, la barra central, las barras laterales y los 24 triángulos."""
        self.pantalla.fill(self.COLOR_FONDO_GENERAL)

        x_barra = (self.ancho / 2) - (self.ancho_barra / 2)
        pygame.draw.rect(self.pantalla, self.COLOR_BARRA_CENTRAL,
                         pygame.Rect(x_barra, 0, self.ancho_barra, self.alto))
        pygame.draw.rect(self.pantalla, self.COLOR_BORDE,
                         pygame.Rect(x_barra, 0, self.ancho_barra, self.alto), 2)

        for i in range(6):
            x = self.ancho_barra // 2 + i * self.ancho_triangulo
            pygame.draw.polygon(self.pantalla, self.COLOR_TRI_A if (i % 2 == 0) else self.COLOR_TRI_B,
                                [(x, 0), (x + self.ancho_triangulo, 0), (x + self.ancho_triangulo // 2, self.alto_triangulo)])
            
            pygame.draw.polygon(self.pantalla, self.COLOR_TRI_B if (i % 2 == 0) else self.COLOR_TRI_A,
                                [(x, self.alto), (x + self.ancho_triangulo, self.alto),
                                 (x + self.ancho_triangulo // 2, self.alto - self.alto_triangulo)])

        for i in range(6):
            x = x_barra + self.ancho_barra + i * self.ancho_triangulo
            pygame.draw.polygon(self.pantalla, self.COLOR_TRI_B if (i % 2 == 0) else self.COLOR_TRI_A,
                                [(x, 0), (x + self.ancho_triangulo, 0), (x + self.ancho_triangulo // 2, self.alto_triangulo)])
            
            pygame.draw.polygon(self.pantalla, self.COLOR_TRI_A if (i % 2 == 0) else self.COLOR_TRI_B,
                                [(x, self.alto), (x + self.ancho_triangulo, self.alto),
                                 (x + self.ancho_triangulo // 2, self.alto - self.alto_triangulo)])

        pygame.draw.rect(self.pantalla, self.COLOR_BARRA_LATERAL,
                         pygame.Rect(0, 0, self.ancho_barra // 2, self.alto))
        pygame.draw.rect(self.pantalla, self.COLOR_BORDE,
                         pygame.Rect(0, 0, self.ancho_barra // 2, self.alto), 2)
        pygame.draw.rect(self.pantalla, self.COLOR_BARRA_LATERAL,
                         pygame.Rect(self.ancho - self.ancho_barra // 2, 0, self.ancho_barra // 2, self.alto))
        pygame.draw.rect(self.pantalla, self.COLOR_BORDE,
                         pygame.Rect(self.ancho - self.ancho_barra // 2, 0, self.ancho_barra // 2, self.alto), 2)

    def dibujar_fichas(self, estado_tablero: dict):
        """Dibuja las fichas en sus respectivos puntos (1-24), apilándolas."""
        fuente = pygame.font.Font(None, 24)
        max_visibles = 5
        
        for punto in range(1, 25):
            fichas = estado_tablero.get(punto)
            if not fichas:
                continue

            color_str = fichas[0]
            color = self.COLOR_FICHA_BLANCA if color_str == "Blancas" else self.COLOR_FICHA_NEGRA
            cantidad = len(fichas)

            if punto <= 12:
                if punto <= 6:
                    x = (6 - punto) * self.ancho_triangulo + self.ancho_triangulo // 2 + self.ancho_barra // 2 + (7 * self.ancho_triangulo)
                else:
                    x = (12 - punto) * self.ancho_triangulo + self.ancho_triangulo // 2 + self.ancho_barra // 2
                y_base = self.radio_ficha
                step = self.radio_ficha * 2
            else:
                if punto <= 18:
                    x = (punto - 13) * self.ancho_triangulo + self.ancho_triangulo // 2 + self.ancho_barra // 2
                else:
                    x = (punto - 19) * self.ancho_triangulo + self.ancho_triangulo // 2 + self.ancho_barra // 2 + (7 * self.ancho_triangulo)
                y_base = self.alto - self.radio_ficha
                step = -self.radio_ficha * 2

            visibles = min(cantidad, max_visibles)
            for i in range(visibles):
                y = y_base + step * i
                pygame.draw.circle(self.pantalla, color, (x, y), self.radio_ficha)
                pygame.draw.circle(self.pantalla, self.COLOR_LINEA_FICHA, (x, y), self.radio_ficha, 2)

            if cantidad > max_visibles:
                restantes = cantidad - max_visibles
                y = y_base + step * (visibles - 1)
                color_texto = self.COLOR_TEXTO_GENERAL if color == self.COLOR_FICHA_BLANCA else self.COLOR_FICHA_BLANCA
                texto = fuente.render(f"+{restantes}", True, color_texto)
                rect = texto.get_rect(center=(x, y))
                self.pantalla.blit(texto, rect)

    def dibujar_barra(self, estado_core: dict):
        """Dibuja las fichas comidas en la barra central."""
        x_centro = self.ancho // 2
        alto_zona = self.alto // 2 - 20
        
        barra_info = {
            "Blanca": estado_core["fichas_blancas_en_bar"],
            "Negra": estado_core["fichas_negras_en_bar"]
        }

        for color, cantidad in barra_info.items():
            if cantidad == 0:
                continue

            radio = max(self.radio_ficha * 0.6, min(self.radio_ficha, alto_zona / (cantidad * 2)))
            step = radio * 2
            color_rgb = self.COLOR_FICHA_BLANCA if color == "Blanca" else self.COLOR_FICHA_NEGRA

            for i in range(cantidad):
                y = (self.alto // 2) - ((i + 1) * step) if color == "Blanca" else (self.alto // 2) + (i * step) + step
                pygame.draw.circle(self.pantalla, color_rgb, (x_centro, int(y)), int(radio))
                pygame.draw.circle(self.pantalla, self.COLOR_LINEA_FICHA, (x_centro, int(y)), int(radio), 2)

            if cantidad > 6:
                texto = pygame.font.Font(None, 28).render(str(cantidad), True, self.COLOR_MENSAJE_ERROR)
                self.pantalla.blit(texto, (x_centro - 8, (self.alto // 2) + (40 if color == "Negra" else -60)))

    def dibujar_barra_lateral(self, estado_core: dict):
        """Dibuja el contador de fichas sacadas en la barra lateral."""
        fuente = pygame.font.Font(None, 36)
        x_centro_barra = self.ancho - self.ancho_barra // 4

        cantidad_blanca = estado_core["fichas_blancas_sacadas"]
        texto_blanca = fuente.render(f"{cantidad_blanca}", True, self.COLOR_TEXTO_GENERAL)
        texto_blanca_rect = texto_blanca.get_rect(center=(x_centro_barra, 40))
        pygame.draw.rect(self.pantalla, self.COLOR_FICHA_BLANCA, texto_blanca_rect.inflate(16, 10), border_radius=6)
        self.pantalla.blit(texto_blanca, texto_blanca_rect)

        cantidad_negra = estado_core["fichas_negras_sacadas"]
        texto_negra = fuente.render(f"{cantidad_negra}", True, self.COLOR_FICHA_BLANCA)
        texto_negra_rect = texto_negra.get_rect(center=(x_centro_barra, self.alto - 40))
        pygame.draw.rect(self.pantalla, self.COLOR_FICHA_NEGRA, texto_negra_rect.inflate(16, 10), border_radius=6)
        self.pantalla.blit(texto_negra, texto_negra_rect)
        
    def dibujar_info_turno(self, estado_core: dict, mensaje: str, nombre_blancas: str, nombre_negras: str):
        """Dibuja el texto del turno actual, dados y mensajes de estado/error."""
        fuente_grande = pygame.font.Font(None, 36)
        fuente_media = pygame.font.Font(None, 28)
        
        if estado_core['turno'] == "Blancas":
            turno_str = f"Jugador (Blancas): {nombre_blancas}"
            color_turno = self.COLOR_MENSAJE_INFO 
        else:
            turno_str = f"Jugador (Negras): {nombre_negras}"
            color_turno = self.COLOR_MENSAJE_INFO 
            
        texto_turno = fuente_grande.render(turno_str, True, color_turno)
        self.pantalla.blit(texto_turno, (self.ancho_barra // 2 + 10, 10))
        
        dados_str = " ".join(map(str, estado_core['dados']))
        texto_dados = fuente_media.render(f"Dados: [{dados_str}]", True, self.COLOR_TEXTO_GENERAL)
        self.pantalla.blit(texto_dados, (self.ancho_barra // 2 + 10, 50))
        
        if mensaje:
            color = self.COLOR_MENSAJE_ERROR if "Error" in mensaje else self.COLOR_MENSAJE_INFO
            texto_msg = fuente_media.render(mensaje, True, color)
            rect_msg = texto_msg.get_rect(midbottom=(self.ancho // 2, self.alto - 10))
            self.pantalla.blit(texto_msg, rect_msg)

    def obtener_punto_desde_click_en_ficha(self, pos, estado_tablero: dict):
        """Retorna el punto (1-24) si el click cae dentro de la ficha SUPERIOR de ese punto."""
        x_click, y_click = pos
        max_visibles = 5 

        for punto in range(1, 25):
            fichas = estado_tablero.get(punto)
            if not fichas:
                continue
            
            cantidad = len(fichas)

            if punto <= 12:
                if punto <= 6:
                    x = (6 - punto) * self.ancho_triangulo + self.ancho_triangulo // 2 + self.ancho_barra // 2 + (7 * self.ancho_triangulo)
                else:
                    x = (12 - punto) * self.ancho_triangulo + self.ancho_triangulo // 2 + self.ancho_barra // 2
                y_base = self.radio_ficha
                step = self.radio_ficha * 2
                i = min(cantidad, max_visibles) - 1
            else:
                if punto <= 18:
                    x = (punto - 13) * self.ancho_triangulo + self.ancho_triangulo // 2 + self.ancho_barra // 2
                else:
                    x = (punto - 19) * self.ancho_triangulo + self.ancho_triangulo // 2 + self.ancho_barra // 2 + (7 * self.ancho_triangulo)
                y_base = self.alto - self.radio_ficha
                step = -self.radio_ficha * 2
                i = min(cantidad, max_visibles) - 1

            y = y_base + step * i
            
            distancia = ((x_click - x)**2 + (y_click - y)**2)**0.5
            if distancia <= self.radio_ficha:
                return punto 
        return None

    def obtener_punto_desde_click(self, pos):
        """Mapea el clic a un punto (triángulo) vacío o de destino (1-24) o barra (0, 25)."""
        x, y = pos
        margen_lateral = self.ancho_barra // 2 
        
        if x < margen_lateral or x > self.ancho - margen_lateral:
            return None 

        x_barra = (self.ancho / 2) - (self.ancho_barra / 2)
        parte_superior = y < self.alto // 2

        ancho_punto = self.ancho_triangulo

        if x > x_barra and x < x_barra + self.ancho_barra:
            if parte_superior:
                return 25
            else:
                return 0
        
        if x > x_barra + self.ancho_barra:
            x_rel = x - (x_barra + self.ancho_barra)
            indice = int(x_rel // ancho_punto) 
            
            if indice >= 6: return None 

            if parte_superior:
                return 6 - indice 
            else:
                return 19 + indice 
        else:
            x_rel = x - margen_lateral
            indice = int(x_rel // ancho_punto) 
            
            if indice >= 6: return None 

            if parte_superior:
                return 12 - indice 
            else:
                return 13 + indice 

    def obtener_barra_lateral_desde_click(self, pos):
        """Devuelve 26 si el clic cae en la zona de sacar fichas (barra lateral derecha)."""
        x, y = pos
        if x > self.ancho - self.ancho_barra // 2:
            return 26
        
        return None