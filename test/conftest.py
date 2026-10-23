import pytest
from red_social.usuario import Usuario
from red_social.red import RedSocial


@pytest.fixture
def ana():
    return Usuario("Ana","@ana")

@pytest.fixture
def luis():
    return Usuario("Luis","@luis")

@pytest.fixture
def red(ana, luis):
    marta = Usuario("Marta","@marta")
    red_social = RedSocial()
    red_social.añadir(ana)
    red_social.añadir(luis)
    red_social.añadir(marta)
    return red_social