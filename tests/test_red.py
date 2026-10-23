import json

from red_social.publicacion import Tweet


def test_timeline_solo_tiene_publicaciones_de_lo_seguidos(red):
    ana = red.usuarios["@ana"]
    luis = red.usuarios["@luis"]
    marta = red.usuarios["@marta"]
    marta.seguir(ana)
    marta.seguir(luis)
    publicacion_ana = Tweet(ana, "Hola desde Ana")
    publicacion_luis = Tweet(luis, "Hola desde Luis")

    red.publicar(publicacion_ana)
    red.publicar(publicacion_luis)
    timeline = red.timeline(marta)

    assert publicacion_ana in timeline
    assert publicacion_luis in timeline
    assert len(timeline) == 2
    assert all(publicacion.autor in marta.seguidos 
               for publicacion in timeline)


def test_desde_json_construye_usuarios_y_seguimientos(mocker):
    from red_social.red import RedSocial

    datos = {
        "usuarios": [
            {"nombre": "Ana", "alias": "@ana"},
            {"nombre": "Luis", "alias": "@luis"},
            {"nombre": "Marta", "alias": "@marta"}
        ],
        "seguimientos": [
            ["@luis", "@ana"],
            ["@marta", "@ana"],
            ["@marta", "@luis"]
        ]
        }
    mocker.patch("builtins.open", mocker.mock_open(read_data=json.dumps(datos)),)

    red = RedSocial.desde_json("archivo_mock.json")
    assert len(red) == 3
    assert red["@ana"].nombre == "Ana"
    assert red["@luis"].nombre == "Luis"
    assert red["@marta"].nombre == "Marta"
    assert red["@ana"] in red["@luis"].seguidos
    assert red["@ana"] in red["@marta"].seguidos
    assert red["@luis"] in red["@marta"].seguidos


   