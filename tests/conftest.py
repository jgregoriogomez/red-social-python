import pytest

from red_social.red import RedSocial
from red_social.usuario import Usuario


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
    red_social.anadir(ana)
    red_social.anadir(luis)
    red_social.anadir(marta)
    return red_social