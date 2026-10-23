def test_timeline_solo_tiene_publicaciones_de_lo_seguidos(red):
    ana = red.usuarios["@ana"]
    luis = red.usuarios["@luis"]
    marta = red.usuarios["@marta"]
    timeline = red.timeline(marta)

    assert all(publicacion.autor in marta.seguidos 
               for publicacion in timeline)


def test_desde_json_construye_usuarios_y_seguimientos():
    from red_social.red import RedSocial
    red = RedSocial.desde_json("datos/usuarios.json")
    assert len(red) == 3
    assert red["@ana"].usuario == "Ana"
    assert red["@luis"].usuario == "Luis"
    assert red["@marta"].usuario == "Marta"
    assert red["@ana"] in red["@luis"].seguidos
    assert red["@ana"] in red["@marta"].seguidos
    assert red["@luis"] in red["@marta"].seguidos


   