
class BackgammonError(Exception):
    """Clase base para todas las excepciones del juego."""
    pass


class MovimientoInvalidoError(BackgammonError):
    """Error para un movimiento no permitido por las reglas."""
    pass


class FichaEnBarError(BackgammonError):
    """Error cuando hay fichas en el bar que deben moverse primero."""
    pass


class DadoNoDisponibleError(BackgammonError):
    """Error cuando el dado necesario no está disponible."""
    pass


class PuntoOcupadoError(BackgammonError):
    """Error cuando el punto de destino está bloqueado por el oponente."""
    pass


class DireccionInvalidaError(BackgammonError):
    """Error cuando el movimiento va en dirección incorrecta."""
    pass


class MovimientoFueraDeRangoError(BackgammonError):
    """Error cuando se intenta mover fuera de las posiciones válidas."""
    pass


class DadosNoTiradosError(BackgammonError):
    """Error cuando se intenta mover sin haber tirado los dados."""
    pass
