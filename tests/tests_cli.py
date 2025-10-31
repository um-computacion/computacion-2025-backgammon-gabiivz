import unittest
from unittest.mock import patch, MagicMock, call
from cli.cli import BackgammonCLI
from core.backgammongame import (
    BackgammonGame, 
    MovimientoInvalidoError as MovimientoInvalido, 
    FichaEnBarError
)
from core.dice import Dice


class TestBackgammonCLI(unittest.TestCase):
    
    def setUp(self):
        """Este setup se usa para mockear el 'estado' base del juego."""
        self.mock_game = MagicMock(spec=BackgammonGame)
        
        jugador_blancas = MagicMock()
        jugador_blancas.get_nombre.return_value = 'Gabi'
        jugador_blancas.get_color.return_value = 'Blancas'
        jugador_negras = MagicMock()
        jugador_negras.get_nombre.return_value = 'Gabo'
        jugador_negras.get_color.return_value = 'Negras'

        self.mock_game.get_jugador_blancas.return_value = jugador_blancas
        self.mock_game.get_jugador_negras.return_value = jugador_negras
        self.mock_game.get_jugador_actual.return_value = jugador_blancas

        self.fake_estado = {
            'fichas_negras_en_bar': 0,
            'fichas_blancas_en_bar': 0,
            'fichas_blancas_sacadas': 0,
            'fichas_negras_sacadas': 0,
            'tablero': {i: [] for i in range(1, 25)},
            'dados': []
        }
        self.mock_game.estado_actual.return_value = self.fake_estado
        self.mock_game.get_ganador.return_value = None
        self.mock_game.get_dados.return_value = []

    def _make_get_dados(self, sequence):
        """Helper para crear un side_effect robusto para get_dados."""
        seq = list(sequence)
        def _f():
            if not seq:
                return []
            if len(seq) == 1:
                return seq[0]
            return seq.pop(0)
        return _f

    @patch('builtins.print')
    @patch('builtins.input', side_effect=['', 'Gabi', '', 'Gabo'])
    @patch('cli.cli.BackgammonGame')
    def test_init_valida_nombres_vacios(self, mock_BackgammonGame_class, mock_input, mock_print):
        """Testea que el __init__ insiste si el nombre está vacío."""
        mock_BackgammonGame_class.return_value = self.mock_game
        cli = BackgammonCLI()
        error_msg = "Error: El nombre no puede estar vacío. Intenta de nuevo."
        self.assertIn(call(error_msg), mock_print.call_args_list)
        mock_BackgammonGame_class.assert_called_with('Gabi', 'Gabo')

    @patch('builtins.print')
    @patch('cli.cli.BackgammonGame')
    def test_main_tira_dados_y_mueve(self, mock_BackgammonGame_class, mock_print):
        """Testea el camino feliz: tirar, mover y luego rendirse para salir."""
        inputs_simulados = ['Gabi', 'Gabo', 's', '1', '13', '10', 's', '3']

        shared = {'mov': []}
        self.mock_game.get_dados.side_effect = lambda: shared['mov']

        def tirar():
            shared['mov'] = [3, 4]
            return (3, 4)
        self.mock_game.tirar_dados.side_effect = tirar

        def mover_side_effect(origen, destino):
            if shared['mov']:
                shared['mov'].pop(0)
        self.mock_game.mover_ficha.side_effect = mover_side_effect

        self.mock_game.tiene_movimientos_posibles.return_value = True
        mock_BackgammonGame_class.return_value = self.mock_game

        with patch('builtins.input', side_effect=inputs_simulados):
            cli = BackgammonCLI()
            cli.main()

        self.mock_game.mover_ficha.assert_called_with(13, 10)
        self.assertIn(call("Ficha movida de 13 a 10"), mock_print.call_args_list)
        self.assertIn(call("¡Te rendiste! Fin del juego."), mock_print.call_args_list)

    @patch('builtins.print')
    @patch('cli.cli.BackgammonGame')
    def test_main_tira_dados_y_no_hay_movimientos(self, mock_BackgammonGame_class, mock_print):
        """Testea que el CLI maneja 'tiene_movimientos_posibles' = False y usa los dados."""
        inputs_simulados = ['Gabi', 'Gabo', 's', 's', '3']

        shared = {'mov': []}
        self.mock_game.get_dados.side_effect = lambda: shared['mov']

        def tirar():
            shared['mov'] = [1, 1]
            return (1, 1)
        self.mock_game.tirar_dados.side_effect = tirar

        def usar_dados(val):
            try:
                shared['mov'].remove(val)
            except ValueError:
                pass
        self.mock_game.usar_dados.side_effect = usar_dados

        self.mock_game.tiene_movimientos_posibles.side_effect = [False, True]
        mock_BackgammonGame_class.return_value = self.mock_game

        with patch('builtins.input', side_effect=inputs_simulados):
            cli = BackgammonCLI()
            cli.main()

        self.assertIn(call("!! No hay movimientos posibles. Turno perdido. !!"), mock_print.call_args_list)
        self.assertTrue(self.mock_game.usar_dados.call_count >= 1)

    @patch('builtins.print')
    @patch('cli.cli.BackgammonGame')
    def test_main_captura_movimiento_invalido(self, mock_BackgammonGame_class, mock_print):
        """Testea que el 'try...except' captura un MovimientoInvalidoError."""
        inputs_simulados = ['Gabi', 'Gabo', 's', '1', '24', '20', '3']
        self.mock_game.get_dados.return_value = [4]
        self.mock_game.tiene_movimientos_posibles.return_value = True
        self.mock_game.mover_ficha.side_effect = MovimientoInvalido("Punto bloqueado")
        mock_BackgammonGame_class.return_value = self.mock_game

        with patch('builtins.input', side_effect=inputs_simulados):
            cli = BackgammonCLI()
            cli.main()

        self.mock_game.mover_ficha.assert_called_with(24, 20)
        self.assertIn(call("Error: Punto bloqueado"), mock_print.call_args_list)

    @patch('builtins.print')
    @patch('cli.cli.BackgammonGame')
    def test_main_captura_value_error(self, mock_BackgammonGame_class, mock_print):
        """Testea que el CLI maneja un input no numérico para origen/destino."""
        inputs_simulados = ['Gabi', 'Gabo', 's', '1', 'abc', '3']
        self.mock_game.get_dados.return_value = [4]
        self.mock_game.tiene_movimientos_posibles.return_value = True
        mock_BackgammonGame_class.return_value = self.mock_game

        with patch('builtins.input', side_effect=inputs_simulados):
            cli = BackgammonCLI()
            cli.main()

        self.assertIn(call("¡Te rendiste! Fin del juego."), mock_print.call_args_list)

    @patch('builtins.print')
    @patch('cli.cli.BackgammonGame')
    def test_main_opcion_3_rendirse(self, mock_BackgammonGame_class, mock_print):
        """Testea que la opción 3 (Rendirse) funciona."""
        inputs_simulados = ['Gabi', 'Gabo', 's', '3']
        self.mock_game.get_dados.return_value = [1]
        self.mock_game.tiene_movimientos_posibles.return_value = True
        mock_BackgammonGame_class.return_value = self.mock_game

        with patch('builtins.input', side_effect=inputs_simulados):
            cli = BackgammonCLI()
            cli.main()

        self.assertIn(call("¡Te rendiste! Fin del juego."), mock_print.call_args_list)

    @patch('builtins.print')
    @patch('cli.cli.BackgammonGame')
    def test_main_opcion_invalida(self, mock_BackgammonGame_class, mock_print):
        """Testea que el CLI maneja una opción de menú inválida."""
        inputs_simulados = ['Gabi', 'Gabo', 's', '9', '3']
        self.mock_game.get_dados.return_value = [1]
        self.mock_game.tiene_movimientos_posibles.return_value = True
        mock_BackgammonGame_class.return_value = self.mock_game

        with patch('builtins.input', side_effect=inputs_simulados):
            cli = BackgammonCLI()
            cli.main()

        self.assertIn(call("Opción no válida."), mock_print.call_args_list)

    @patch('builtins.print')
    @patch('cli.cli.BackgammonGame')
    def test_main_termina_al_ganar(self, mock_BackgammonGame_class, mock_print):
        """Testea que el bucle 'while' termina y muestra al ganador."""
        inputs_simulados = ['Gabi', 'Gabo', '3']
        self.mock_game.get_ganador.side_effect = [None, "Gabi"]
        self.mock_game.get_dados.return_value = [1]
        mock_BackgammonGame_class.return_value = self.mock_game

        with patch('builtins.input', side_effect=inputs_simulados):
            cli = BackgammonCLI()
            cli.main()

        self.assertIn(call("\nGanó Gabi!"), mock_print.call_args_list)

    @patch('builtins.print')
    @patch('cli.cli.BackgammonGame')
    def test_main_opcion_2_ver_estado(self, mock_BackgammonGame_class, mock_print):
        """Testea la opción 2: ver estado del juego."""
        inputs = ['Gabi', 'Gabo', '2', '3']
        self.mock_game.get_dados.return_value = [1]
        self.mock_game.tiene_movimientos_posibles.return_value = True
        fake_estado = dict(self.fake_estado)
        fake_estado['dados'] = [1]
        fake_estado['turno'] = 'Blancas'
        self.mock_game.estado_actual.return_value = fake_estado
        mock_BackgammonGame_class.return_value = self.mock_game

        with patch('builtins.input', side_effect=inputs):
            cli = BackgammonCLI()
            cli.main()

        self.assertIn(call("Estado actual del juego:"), mock_print.call_args_list)
        self.assertIn(call(f"Movimientos disponibles: {fake_estado['dados']}"), mock_print.call_args_list)

    @patch('builtins.print')
    @patch('cli.cli.BackgammonGame')
    def test_main_opcion_4_finalizar(self, mock_BackgammonGame_class, mock_print):
        """Testea la opción 4: finalizar juego."""
        inputs = ['Gabi', 'Gabo', '4']
        self.mock_game.get_dados.return_value = [1]
        self.mock_game.tiene_movimientos_posibles.return_value = True
        mock_BackgammonGame_class.return_value = self.mock_game

        with patch('builtins.input', side_effect=inputs):
            cli = BackgammonCLI()
            cli.main()

        self.assertIn(call(f"Juego finalizado por {self.mock_game.get_jugador_actual().get_nombre()}."), mock_print.call_args_list)

    @patch('builtins.print')
    @patch('cli.cli.BackgammonGame')
    def test_tirar_n_no_tira(self, mock_BackgammonGame_class, mock_print):
        """Testea que responder 'n' al preguntar si se quieren tirar los dados muestra el mensaje correcto."""
        inputs = ['Gabi', 'Gabo', 'n']
        self.mock_game.get_ganador.side_effect = [None, "Gabi", "Gabi"]
        self.mock_game.get_dados.return_value = []
        mock_BackgammonGame_class.return_value = self.mock_game

        with patch('builtins.input', side_effect=inputs):
            cli = BackgammonCLI()
            cli.main()

        self.assertIn(call("Debés tirar los dados para jugar."), mock_print.call_args_list)

    @patch('builtins.print')
    @patch('cli.cli.BackgammonGame')
    def test_main_captura_ficha_en_bar(self, mock_BackgammonGame_class, mock_print):
        """Testea captura de FichaEnBarError al intentar mover desde sitio incorrecto."""
        inputs = ['Gabi', 'Gabo', 's', '1', '12', '8', '3']

        shared = {'mov': []}
        self.mock_game.get_dados.side_effect = lambda: shared['mov']

        def tirar():
            shared['mov'] = [4]
            return (4, 4)
        self.mock_game.tirar_dados.side_effect = tirar

        self.mock_game.mover_ficha.side_effect = FichaEnBarError("Ficha en bar")
        self.mock_game.tiene_movimientos_posibles.return_value = True
        mock_BackgammonGame_class.return_value = self.mock_game

        with patch('builtins.input', side_effect=inputs):
            cli = BackgammonCLI()
            cli.main()

        self.assertIn(call("Error: Ficha en bar"), mock_print.call_args_list)

if __name__ == '__main__':
    unittest.main()