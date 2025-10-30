from core.backgammongame import BackgammonGame
from core.exceptions import (
    BackgammonError, MovimientoFueraDeRangoError, MovimientoInvalidoError,
    FichaEnBarError, DadoNoDisponibleError, DadosNoTiradosError,
    SinMovimientosPosiblesError, DireccionInvalidaError, TurnoInvalidoError, PuntoOcupadoError
)
"""ejecutar con esto:python -m cli.cli"""
class BackgammonCLI:
    def __init__(self):
        nombre_blancas = input("Nombre jugador blancas: ")
        nombre_negras = input("Nombre jugador negras: ")
        self.__game__ = BackgammonGame(nombre_blancas, nombre_negras)
        self.__board__ = self.__game__.get_board()

    # En: cli/cli.py
    def main(self):
        print("¡Bienvenido al juego de Backgammon!")
        print(f"Jugador 1 (Blancas): {self.__game__.get_jugador_blancas().get_nombre()}")
        print(f"Jugador 2 (Negras): {self.__game__.get_jugador_negras().get_nombre()}")
        print("¡Buena suerte!")

        while not self.__game__.get_ganador():
            estado = self.__game__.estado_actual()
            print("\n--- Estado actual ---")
            print(f"Barra Negras (0): {estado['fichas_negras_en_bar']} fichas")
            print(f"Barra Blancas (25): {estado['fichas_blancas_en_bar']} fichas")
            print(f"Fichas blancas sacadas: {estado['fichas_blancas_sacadas']}")
            print(f"Fichas negras sacadas: {estado['fichas_negras_sacadas']}")
            
            print("Tablero:")
            for pos in range(1, 26): 
                fichas = estado["tablero"][pos] 
                print(f"{pos}: {fichas}")

            print(f"\nTurno de: {self.__game__.get_jugador_actual().get_nombre()}")

            if not self.__game__.get_dados():
                tirar = input("¿Querés tirar los dados? (s/n): ")
                if tirar.lower() == "s":
                    dados = self.__game__.tirar_dados()
                    print(f"Dados tirados: {dados}")
                else:
                    print("Debés tirar los dados para jugar.")
                    continue

            print(f"Movimientos disponibles: {self.__game__.get_dados()}")
            print("Opciones:")
            print("1: Mover ficha")
            print("2: Ver estado del juego")
            print("3: Rendirse")
            print("4: Finalizar juego")
            opcion = input("Opción: ")

            try:
                if opcion == "1":
                    origen = int(input("Mover ficha desde: "))
                    destino = int(input("Hasta: "))
                    
                    barra_rival_antes = 0
                    rival_name = ""
                    ficha_actual = self.__game__.get_jugador_actual().__color__

                    if ficha_actual == "Blancas":
                        rival_name = self.__game__.get_jugador_negras().get_nombre()
                        barra_rival_antes = len(self.__board__.get_bar_negras())
                    else:
                        rival_name = self.__game__.get_jugador_blancas().get_nombre()
                        barra_rival_antes = len(self.__board__.get_bar_blancas())

                    self.__game__.mover_ficha(origen, destino)

                    print(f"Ficha movida de {origen} a {destino}")

                    barra_rival_despues = 0
                    if ficha_actual == "Blancas":
                        barra_rival_despues = len(self.__board__.get_bar_negras())
                    else:
                        barra_rival_despues = len(self.__board__.get_bar_blancas())

                    if barra_rival_despues > barra_rival_antes:
                        print(f"¡{self.__game__.get_jugador_actual().get_nombre()} comió la ficha de {rival_name}!")
                elif opcion == "2":
                    print("Estado actual del juego:")
                    estado = self.__game__.estado_actual()
                    print(f"Barra Negras (0): {estado['fichas_negras_en_bar']} fichas")
                    print(f"Barra Blancas (25): {estado['fichas_blancas_en_bar']} fichas")
                    print("Tablero:")
                    for pos, fichas in estado["tablero"].items():
                        print(f"{pos}: {fichas}")
                    
                    print(f"Turno: {estado['turno']}")
                    print(f"Fichas blancas sacadas: {estado['fichas_blancas_sacadas']}")
                    print(f"Fichas negras sacadas: {estado['fichas_negras_sacadas']}")
                    print(f"Movimientos disponibles: {estado['dados']}")
                
                elif opcion == "3":
                    print("¡Te rendiste! Fin del juego.")
                    break
                elif opcion == "4":
                    print(f"Juego finalizado por {self.__game__.get_jugador_actual().get_nombre()}.")
                    break
                else:
                    print("Opción no válida.")
            
            except (FichaEnBarError, DadoNoDisponibleError, DadosNoTiradosError, MovimientoInvalidoError, SinMovimientosPosiblesError, PuntoOcupadoError, DireccionInvalidaError, MovimientoFueraDeRangoError) as e:
                print(f"Error: {e}")
                continue
            print(f"Movimientos restantes: {self.__game__.get_dados()}")
            if not self.__game__.get_dados():
                self.__game__.cambio_turnos()

        ganador = self.__game__.get_ganador()
        if ganador:
            print(f"\nGanó {ganador}!")

if __name__ == "__main__":
    cli = BackgammonCLI()
    cli.main()