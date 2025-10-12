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

        while not self.game.get_ganador():
            estado = self.game.estado_actual()
            print("\n--- Estado actual ---")
            print("Tablero:")
            for pos, fichas in estado["tablero"].items():
                print(f"{pos}: {fichas}")
            print(f"\nTurno de: {self.game.get_jugador_actual().get_nombre()}")
            if not self.game.get_dados():
                tirar = input("¿Querés tirar los dados? (si/no): ")
                if tirar.lower() == "si":
                    dados = self.game.tirar_dados()
                    print(f"Dados tirados: {dados}")
                else:
                    print("Debés tirar los dados para jugar.")
                    continue
            print(f"Movimientos disponibles: {self.game.get_dados()}")
            print("Opciones:")
            print("1: Mover ficha")
            print("2: Ver estado del juego")
            print("3: Rendirse")
            print("4: Finalizar juego")
            opcion = input("Opción: ")

            if opcion == "1":
                try:
                    print(f"Movimientos disponibles este turno: {self.game.get_dados()}")
                    origen = int(input("Mover ficha desde: "))
                    destino = int(input("Hasta: "))
                    self.game.mover_ficha(origen, destino)
                    print(f"Ficha movida de {origen} a {destino}")
                    print(f"Movimientos restantes: {self.game.get_dados()}")  
            # SOLO CAMBIAR TURNO SI YA NO QUEDAN MOVIMIENTOS
                    if not self.game.get_dados():
                        self.game.cambio_turnos()
                except (FichaEnBarError, DadoNoDisponibleError, DadosNoTiradosError, MovimientoInvalidoError, SinMovimientosPosiblesError) as e:
                    print(f"Error: {e}")
                    self.game.cambio_turnos()
                    continue
            elif opcion == "2":
                print("Estado actual del juego:")
                print(self.game.estado_actual())
            elif opcion == "3":
                print("¡Te rendiste! Fin del juego.")
                break
            elif opcion == "4":
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