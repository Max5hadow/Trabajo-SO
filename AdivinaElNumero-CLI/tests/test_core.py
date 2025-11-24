from adivina.core import nuevo_juego, evaluar_intento, validar_intento

def test_nuevo_juego_seed_reproducible():
    estado1 = nuevo_juego(seed=123)
    estado2 = nuevo_juego(seed=123)
    assert estado1.secreto == estado2.secreto

def test_evaluar_intento_mas_alto():
    estado = nuevo_juego(seed=1)
    estado.secreto = 50
    assert evaluar_intento(estado, 20) == "mas_alto"

def test_evaluar_intento_mas_bajo():
    estado = nuevo_juego(seed=1)
    estado.secreto = 50
    assert evaluar_intento(estado, 80) == "mas_bajo"

def test_evaluar_intento_correcto():
    estado = nuevo_juego(seed=1)
    estado.secreto = 50
    assert evaluar_intento(estado, 50) == "correcto"
    assert estado.terminado is True

def test_validar_intento_ok():
    assert validar_intento("55") == 55

def test_validar_intento_fuera_rango():
    import pytest
    with pytest.raises(ValueError):
        validar_intento("999")