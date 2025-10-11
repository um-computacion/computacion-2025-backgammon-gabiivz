from core.backgammongame import BackgammonGame
from core.exceptions import (
    BackgammonError, MovimientoFueraDeRangoError, MovimientoInvalidoError,
    FichaEnBarError, DadoNoDisponibleError, DadosNoTiradosError,
    SinMovimientosPosiblesError, DireccionInvalidaError, TurnoInvalidoError
)
"""ejecutar con esto:python -m cli.cli"""
class BackgammonCLI:
    def __init__(self):
        nombre_blancas = input("Nombre jugador blancas: ")
        nombre_negras = input("Nombre jugador negras: ")
        self.game = BackgammonGame(nombre_blancas, nombre_negras)
        self.board = self.game.get_board()

    def main(self):
        print("¡Bienvenido al juego de Backgammon!")
        print(f"Jugador 1 (Blancas): {self.game.get_jugador_blancas().get_nombre()}")
        print(f"Jugador 2 (Negras): {self.game.get_jugador_negras().get_nombre()}")
        print("Instrucciones: ...")
        print("Los jugadores se turnan para mover sus fichas.")
        print("El objetivo es llevar todas tus fichas a tu hogar.")
        print("Los dados determinan cuántas casillas puedes mover.")
        print("Si caes en una casilla ocupada por el oponente, debes 'comer' su ficha.")
        print("¡Buena suerte!")
        print("Tablero inicial:")
        print(self.board)

        while not self.game.get_ganador():
            estado = self.game.estado_actual()
            print("\n--- Estado actual ---")
            print(f"Movimientos disponibles: {self.game.get_dados()}")
            print(f"Fichas blancas en el bar: {estado['fichas_blancas_en_bar']}")
            print(f"Fichas negras en el bar: {estado['fichas_negras_en_bar']}")
            print(f"Fichas blancas sacadas: {estado['fichas_blancas_sacadas']}")
            print(f"Fichas negras sacadas: {estado['fichas_negras_sacadas']}")
            print("Tablero:")
            for pos, fichas in estado["tablero"].items():
                print(f"{pos}: {fichas}")
            print(f"\nTurno de: {self.game.get_jugador_actual().get_nombre()}")
            dados = self.game.tirar_dados()
            print(f"Dados tirados: {dados}")
            print("Opciones:")
            print("1: Mover ficha")
            print("2: Rendirse")
            print("3: Finalizar juego")
            opcion = input("Opción: ")

            if opcion == "1":
                try:
                    print(f"Movimientos disponibles este turno: {self.game.get_dados()}")
                    origen = int(input("Mover ficha desde: "))
                    destino = int(input("Hasta: "))
                    self.game.mover_ficha(origen, destino)
                    print(f"Ficha movida de {origen} a {destino}")
                except (FichaEnBarError, DadoNoDisponibleError, DadosNoTiradosError, MovimientoInvalidoError, SinMovimientosPosiblesError) as e:
                    print(f"Error: {e}")
                    self.game.cambio_turnos()
                    continue
            elif opcion == "2":
                print("¡Te rendiste! Fin del juego.")
                break
            elif opcion == "3":
                print(f"Juego finalizado por {self.game.get_jugador_actual().get_nombre()}.")
                break
            else:
                print("Opción no válida.")

            print("Estado actual del tablero:")
            print(self.game.estado_actual())

        ganador = self.game.get_ganador()
        if ganador:
            print(f"\nGanó {ganador}!")

if __name__ == "__main__":
    cli = BackgammonCLI()
    cli.main()