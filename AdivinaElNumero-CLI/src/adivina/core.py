import random
from dataclasses import dataclass

RANGO_MIN = 1
RANGO_MAX = 100

@dataclass
class EstadoJuego:
    secreto: int
    intentos: int = 0
    terminado: bool = False

def nuevo_juego(seed: int | None = None) -> EstadoJuego:

    rng = random.Random(seed)
    secreto = rng.randint(RANGO_MIN, RANGO_MAX)
    return EstadoJuego(secreto=secreto)

def evaluar_intento(estado: EstadoJuego, intento: int) -> str:

    if estado.terminado:
        return "terminado"

    estado.intentos += 1

    if intento < estado.secreto:
        return "mas_alto"
    if intento > estado.secreto:
        return "mas_bajo"

    estado.terminado = True
    return "correcto"

def validar_intento(texto: str) -> int:

    try:
        n = int(texto)
    except ValueError:
        raise ValueError("Debes ingresar un número entero.")

    if n < RANGO_MIN or n > RANGO_MAX:
        raise ValueError(f"El número debe estar entre {RANGO_MIN} y {RANGO_MAX}.")

    return n