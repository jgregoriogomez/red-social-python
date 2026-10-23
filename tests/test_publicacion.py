import pytest

from red_social.publicacion import Publicacion


@pytest.mark.parametrize("texto, esperado", 
                         [("Hola #Python", ["#python"]),
                          ("#python #pytest", ["#python", "#pytest"]),
                          ("Hola mundo", []),
                          ("#Python #PYTHON", ["#python"]),])
def test_extraer_hashtags(texto, esperado):
    assert Publicacion.extraer_hashtags(texto) == esperado

@pytest.mark.parametrize("texto", ["", "  ", "a" *281,],)
def test_texto_invalido_lanza_error(ana, texto):
    from red_social.publicacion import Tweet
    with pytest.raises(ValueError):
        Tweet(ana, texto)

def test_retweet_comparte_el_texto_del_original(ana, luis):
    from red_social.publicacion import Retweet, Tweet
    original = Tweet(ana, "Hola mundo #python")
    retweet = Retweet(luis, original)
    assert retweet.texto == original.texto
    assert retweet.original is original