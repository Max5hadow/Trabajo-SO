from .core import nuevo_juego, evaluar_intento, validar_intento, RANGO_MIN, RANGO_MAX

def main():
    print("=====================================")
    print(" Adivina el Número (1 a 100) - CLI ")
    print("=====================================")
    print("Escribe 'salir' para terminar el juego.")
    print()

    estado = nuevo_juego()

    while not estado.terminado:
        entrada = input(f"Ingresa tu intento [{RANGO_MIN}-{RANGO_MAX}]: ").strip()

        if entrada.lower() == "salir":
            print("Juego terminado por el jugador.")
            return

        try:
            intento = validar_intento(entrada)
        except ValueError as e:
            print(f"Entrada inválida: {e}")
            continue

        pista = evaluar_intento(estado, intento)

        if pista == "mas_alto":
            print("Más alto ⬆️")
        elif pista == "mas_bajo":
            print("Más bajo ⬇️")
        elif pista == "correcto":
            print(f"¡Correcto! El número era {estado.secreto}.")
            print(f"Intentos usados: {estado.intentos}")
        else:
            print("El juego ya terminó.")

if __name__ == "__main__":
    main()
