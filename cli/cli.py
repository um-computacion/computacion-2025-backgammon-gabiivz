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
            print("1: Mover ficha normal")
            print("2: Comer ficha")
            print("3: Mover ficha desde el bar")
            print("4: Sacar ficha")
            print("5: Ver estado del juego")
            print("6: Rendirse")
            print("7: Finalizar juego")
            opcion = input("Opción: ")

            try:
                if opcion == "1":
                    origen = int(input("Mover ficha desde: "))
                    destino = int(input("Hasta: "))
                    self.game.mover_ficha(origen, destino)
                    print(f"Ficha movida de {origen} a {destino}")
                elif opcion == "2":
                    origen = int(input("Comer ficha desde: "))
                    destino = int(input("Hasta: "))
                    self.game.comer_ficha(origen, destino)
                    print(f"Ficha comida de {origen} a {destino}")
                elif opcion == "3":
                    destino = int(input("Mover ficha comida hasta: "))
                    self.game.mover_ficha_desde_bar(destino)
                    print(f"Ficha comida movida hasta {destino}")
                elif opcion == "4":
                    origen = int(input("Sacar ficha desde: "))
                    self.game.sacar_ficha(origen)
                    print(f"Ficha sacada desde {origen}")
                elif opcion == "5":
                    print("Estado actual del juego:")
                    estado = self.game.estado_actual()
                    print("Tablero:")
                    for pos, fichas in estado["tablero"].items():
                        print(f"{pos}: {fichas}")
                    print(f"Turno: {estado['turno']}")
                    print(f"Fichas blancas en el bar: {estado['fichas_blancas_en_bar']}")
                    print(f"Fichas negras en el bar: {estado['fichas_negras_en_bar']}")
                    print(f"Fichas blancas sacadas: {estado['fichas_blancas_sacadas']}")
                    print(f"Fichas negras sacadas: {estado['fichas_negras_sacadas']}")
                    print(f"Movimientos disponibles: {estado['dados']}")
                elif opcion == "6":
                    print("¡Te rendiste! Fin del juego.")
                    break
                elif opcion == "7":
                    print(f"Juego finalizado por {self.game.get_jugador_actual().get_nombre()}.")
                    break
                else:
                    print("Opción no válida.")
            except (FichaEnBarError, DadoNoDisponibleError, DadosNoTiradosError, MovimientoInvalidoError, SinMovimientosPosiblesError) as e:
                print(f"Error: {e}")
                self.game.cambio_turnos()
                continue

            print(f"Movimientos restantes: {self.game.get_dados()}")
            if not self.game.get_dados():
                self.game.cambio_turnos()

        ganador = self.game.get_ganador()
        if ganador:
            print(f"\nGanó {ganador}!")

if __name__ == "__main__":
    cli = BackgammonCLI()
    cli.main()