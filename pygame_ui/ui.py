import sys
import pygame

from core.backgammongame import BackgammonGame
from core.exceptions import BackgammonError
from pygame_ui.board_game import BoardRenderer 

class PygameUI:
    """Clase que representa la interfaz gráfica del juego de Backgammon usando Pygame."""
    def __init__(self):
        """
        Inicializa Pygame, la pantalla, las fuentes,
        lanza la pantalla de nombres e inicializa el juego.
        Ejecución: python -m pygame_ui.ui
        """
        pygame.init()
        
        self.HEADER_HEIGHT = 50
        self.FOOTER_HEIGHT = 50
        self.ALTO_JUEGO = 550
        
        self.ANCHO_PANTALLA = 1000
        self.ALTO_PANTALLA = self.ALTO_JUEGO + self.HEADER_HEIGHT + self.FOOTER_HEIGHT
        
        self.pantalla = pygame.display.set_mode((self.ANCHO_PANTALLA, self.ALTO_PANTALLA))
        pygame.display.set_caption("Backgammon Gabi")
        
        self.clock = pygame.time.Clock()
        
        self.fuente_header = pygame.font.Font(None, 36)
        self.fuente_footer = pygame.font.Font(None, 28)
        
        self.fuente_titulo = pygame.font.Font(None, 74) 
        self.fuente_input = pygame.font.Font(None, 50)
        self.fuente_info = pygame.font.Font(None, 28)
        self.__nombre_blancas__, self.__nombre_negras__ = self._obtener_nombres()
        
        self.game_surface = pygame.Surface((self.ANCHO_PANTALLA, self.ALTO_JUEGO))
        
        self.game = BackgammonGame(self.__nombre_blancas__, self.__nombre_negras__)
        
        self.renderer = BoardRenderer(self.game_surface, alto_tablero=self.ALTO_JUEGO)

        self.running = True
        self.origen_seleccionado = None
        self.mensaje_ui = f"Turno de {self.game.get_turno()}. ¡Haz clic para tirar!"
        self.dados_tirados = False

    def _dibujar_pantalla_nombres(self, nombre_blancas, nombre_negras, input_activo, mensaje_error=""):
        """Dibuja la pantalla de ingreso de nombres de los jugadores."""
        
        FONDO_AZUL_PASTEL = (200, 220, 240) 
        TEXTO_CELESTE_OSCURO = (70, 100, 120)  
        BORDE_AZUL_OSCURO = (80, 120, 140)  
        FONDO_INPUT = (255, 255, 255) 
        BORDE_ACTIVO = (255, 0, 0) 
        COLOR_ERROR = (200, 0, 0)

        self.pantalla.fill(FONDO_AZUL_PASTEL)
        
        bienvenida_texto = self.fuente_titulo.render("¡Bienvenido al Backgammon!", True, TEXTO_CELESTE_OSCURO)
        self.pantalla.blit(bienvenida_texto, bienvenida_texto.get_rect(center=(self.ANCHO_PANTALLA/2, 150)))
        
        rect_blancas = pygame.Rect(self.ANCHO_PANTALLA/2 - 250, 280, 500, 60)
        pygame.draw.rect(self.pantalla, FONDO_INPUT, rect_blancas, border_radius=5)
        borde_b = 3 if input_activo == 'blancas' else 1
        color_borde_b = BORDE_ACTIVO if input_activo == 'blancas' else BORDE_AZUL_OSCURO
        pygame.draw.rect(self.pantalla, color_borde_b, rect_blancas, borde_b, border_radius=5)
        
        label_b = self.fuente_info.render("Jugador Blancas:", True, TEXTO_CELESTE_OSCURO)
        self.pantalla.blit(label_b, (rect_blancas.x, rect_blancas.y - 30))
        
        input_b = self.fuente_input.render(nombre_blancas, True, TEXTO_CELESTE_OSCURO)
        self.pantalla.blit(input_b, (rect_blancas.x + 15, rect_blancas.y + 15))

        rect_negras = pygame.Rect(self.ANCHO_PANTALLA/2 - 250, 420, 500, 60)
        pygame.draw.rect(self.pantalla, FONDO_INPUT, rect_negras, border_radius=5)
        borde_n = 3 if input_activo == 'negras' else 1
        color_borde_n = BORDE_ACTIVO if input_activo == 'negras' else BORDE_AZUL_OSCURO
        pygame.draw.rect(self.pantalla, color_borde_n, rect_negras, borde_n, border_radius=5)

        label_n = self.fuente_info.render("Jugador Negras:", True, TEXTO_CELESTE_OSCURO)
        self.pantalla.blit(label_n, (rect_negras.x, rect_negras.y - 30))
        
        input_n = self.fuente_input.render(nombre_negras, True, TEXTO_CELESTE_OSCURO)
        self.pantalla.blit(input_n, (rect_negras.x + 15, rect_negras.y + 15))

        info = self.fuente_info.render("Presiona ENTER para ingresar el segundo nombre luego presiona ENTER para comenzar.", True, TEXTO_CELESTE_OSCURO)
        self.pantalla.blit(info, info.get_rect(center=(self.ANCHO_PANTALLA/2, 550)))
        
        if mensaje_error:
            error_texto = self.fuente_info.render(mensaje_error, True, COLOR_ERROR)
            self.pantalla.blit(error_texto, error_texto.get_rect(center=(self.ANCHO_PANTALLA/2, 600)))
        
        pygame.display.flip()

    def _obtener_nombres(self):
        """
        Bucle que se ejecuta antes del juego para pedir y validar los nombres
        de los jugadores. No permite avanzar si los campos están vacíos.
        """
        nombre_blancas = ""
        nombre_negras = ""
        input_activo = "blancas"
        mensaje_error = "" 

        while True:
            for e in pygame.event.get():
                if e.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                
                if e.type == pygame.KEYDOWN:
                    mensaje_error = "" 
                    
                    if e.key == pygame.K_RETURN:
                        if input_activo == 'blancas':
                            if not nombre_blancas.strip(): 
                                mensaje_error = "Por favor, ingresa un nombre para Blancas."
                            else:
                                input_activo = 'negras' 
                        
                        else:
                            if not nombre_blancas.strip():
                                mensaje_error = "¡Espera! Falta el nombre de Blancas."
                                input_activo = 'blancas'
                            
                            elif not nombre_negras.strip():
                                mensaje_error = "Por favor, ingresa un nombre para Negras."
                            
                            else:
                                return nombre_blancas.strip(), nombre_negras.strip()
                    
                    elif e.key == pygame.K_TAB:
                        input_activo = 'negras' if input_activo == 'blancas' else 'blancas'
                    
                    elif e.key == pygame.K_BACKSPACE:
                        if input_activo == 'blancas':
                            nombre_blancas = nombre_blancas[:-1]
                        else:
                            nombre_negras = nombre_negras[:-1]
                    else:
                        if input_activo == 'blancas':
                            nombre_blancas += e.unicode
                        else:
                            nombre_negras += e.unicode

            self._dibujar_pantalla_nombres(nombre_blancas, nombre_negras, input_activo, mensaje_error)
            self.clock.tick(30)

    def _handle_click(self, pos):
        """Gestiona la lógica de un clic en el tablero o barras."""
        mouse_x = pos[0]
        mouse_y = pos[1] - self.HEADER_HEIGHT
        
        if mouse_y < 0 or mouse_y > self.ALTO_JUEGO:
            if not self.dados_tirados:
                 try:
                    dados = self.game.tirar_dados()
                    self.dados_tirados = True
                    self.mensaje_ui = f"Dados: {dados}. Mueve {self.game.get_turno()}"
                    if not self.game.tiene_movimientos_posibles():
                        self.mensaje_ui = "No hay movimientos posibles. Turno perdido."
                        while self.game.get_dados():
                            self.game.usar_dados(self.game.get_dados()[0])
                 except Exception as err:
                    self.mensaje_ui = f"Error: {err}"
            return
        
        pos_ajustado = (mouse_x, mouse_y)

        if not self.dados_tirados:
             self.mensaje_ui = "Error: ¡Haz clic para tirar los dados!"
             return

        estado_tablero = self.game.estado_actual()["tablero"]
        
        origen = self.renderer.obtener_punto_desde_click_en_ficha(pos_ajustado, estado_tablero)
        origen_barra = self.renderer.obtener_punto_desde_click(pos_ajustado)
        if origen_barra in [0, 25]:
            origen = origen_barra  
            
        destino_vacio = self.renderer.obtener_punto_desde_click(pos_ajustado)
        destino_lateral = self.renderer.obtener_barra_lateral_desde_click(pos_ajustado)

        
        if self.origen_seleccionado is None:
            if origen is not None:
                ficha_color = ""
                if origen in estado_tablero:
                    ficha_color = estado_tablero[origen][0]
                elif (origen == 25 and self.game.estado_actual()['fichas_blancas_en_bar'] > 0):
                    ficha_color = "Blancas"
                elif (origen == 0 and self.game.estado_actual()['fichas_negras_en_bar'] > 0):
                     ficha_color = "Negras"
                
                if ficha_color == self.game.get_turno():
                    self.origen_seleccionado = origen
                    self.mensaje_ui = f"Origen seleccionado: {origen}. Elige un destino."
                else:
                    self.mensaje_ui = "Error: ¡Esa no es tu ficha!"
            else:
                self.mensaje_ui = "Error: Haz clic en una de tus fichas (o en la barra) para mover."
        
        else:
            destino = -1
            if destino_lateral == 26:
                destino = 26
            elif destino_vacio is not None:
                destino = destino_vacio
            else:
                self.mensaje_ui = "Error: Clic en un lugar inválido para destino."
                self.origen_seleccionado = None
                return

            try:
                print(f"Intentando mover: {self.origen_seleccionado} -> {destino}")
                self.game.mover_ficha(self.origen_seleccionado, destino)
                self.mensaje_ui = f"Movimiento exitoso: {self.origen_seleccionado} -> {destino}"
            except BackgammonError as err:
                self.mensaje_ui = f"Error: {err}"
            except Exception as e_gen:
                self.mensaje_ui = f"Error inesperado: {e_gen}"
            
            self.origen_seleccionado = None

    def _update_game_state(self):
        """Comprueba si el turno terminó (sin dados) o si hay un ganador."""
        
        if self.dados_tirados and not self.game.get_dados():
            try:
                self.game.cambio_turnos()
                self.dados_tirados = False
                self.origen_seleccionado = None
                self.mensaje_ui = f"Turno de {self.game.get_turno()}. ¡Haz clic para tirar!"
            except Exception as e:
                self.mensaje_ui = f"Error al cambiar turno: {e}"
        
        ganador = self.game.get_ganador()
        if ganador:
            self.mensaje_ui = f"¡GANADOR: {ganador}!"
            self._draw()
            pygame.time.wait(5000)
            self.running = False

    def _draw(self):
        """Dibuja todos los componentes: barras (header/footer) y el tablero de juego."""
        estado_core = self.game.estado_actual()
        
        color_barras = self.renderer.COLOR_HEADER_FOOTER
        color_texto_header = self.renderer.COLOR_TEXTO_HEADER
        
        self.pantalla.fill(color_barras) 
        
        rect_header = pygame.Rect(0, 0, self.ANCHO_PANTALLA, self.HEADER_HEIGHT)
        rect_footer = pygame.Rect(0, self.ALTO_PANTALLA - self.FOOTER_HEIGHT, self.ANCHO_PANTALLA, self.FOOTER_HEIGHT)

        self.renderer.dibujar_tablero()
        self.renderer.dibujar_fichas(estado_core["tablero"])
        self.renderer.dibujar_barra(estado_core)
        self.renderer.dibujar_barra_lateral(estado_core)
        
        self.pantalla.blit(self.game_surface, (0, self.HEADER_HEIGHT))
        
        if estado_core['turno'] == "Blancas":
            turno_str = f"Jugador (Blancas): {self.__nombre_blancas__}"
        else:
            turno_str = f"Jugador (Negras): {self.__nombre_negras__}"
        
        texto_turno = self.fuente_header.render(turno_str, True, color_texto_header)
        rect_turno = texto_turno.get_rect(center=(self.ANCHO_PANTALLA / 2, self.HEADER_HEIGHT / 2))
        self.pantalla.blit(texto_turno, rect_turno)

        mov_str = "Movimientos: " + str(estado_core['dados'])
        texto_mov = self.fuente_footer.render(mov_str, True, color_texto_header)
        rect_mov = texto_mov.get_rect(midleft=(20, self.ALTO_PANTALLA - self.FOOTER_HEIGHT / 2))
        self.pantalla.blit(texto_mov, rect_mov)

        if self.mensaje_ui:
            color = self.renderer.COLOR_MENSAJE_ERROR if "Error" in self.mensaje_ui else self.renderer.COLOR_MENSAJE_INFO
            texto_msg = self.fuente_footer.render(self.mensaje_ui, True, color)
            rect_msg = texto_msg.get_rect(midright=(self.ANCHO_PANTALLA - 20, self.ALTO_PANTALLA - self.FOOTER_HEIGHT / 2))
            self.pantalla.blit(texto_msg, rect_msg)

        pygame.display.flip()

    def run(self):
        """Bucle principal del juego que maneja eventos, actualizaciones y dibujado."""
        while self.running:
            for e in pygame.event.get():
                if e.type == pygame.QUIT:
                    self.running = False
                elif e.type == pygame.KEYDOWN and e.key in (pygame.K_ESCAPE, pygame.K_q):
                    self.running = False
                elif e.type == pygame.MOUSEBUTTONDOWN and e.button == 1:
                    self._handle_click(e.pos)
            
            self._update_game_state()
            self._draw()
            
            self.clock.tick(30)

        pygame.quit()
        sys.exit()

if __name__ == "__main__":
    ui = PygameUI()
    ui.run()