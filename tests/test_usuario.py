import pytest


def test_seguirse_a_si_mismo_lanza_error(ana):
    with pytest.raises(ValueError):
        ana.seguir(ana)


def test_seguir_añade_otro_usuario(ana, luis):
    ana.seguir(luis)

    assert luis in ana.seguidos
    assert luis.numero_seguidos == 0
    assert ana.numero_seguidos == 1