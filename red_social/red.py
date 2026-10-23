import json
from collections import Counter

from .usuario import Usuario


class RedSocial:

    def __init__ (self):
        self.usuarios = {}
        self.publicaciones= []

    def anadir(self, usuario):
        if usuario.alias in self.usuarios:
            raise ValueError("El alias ya existe")

        self.usuarios[usuario.alias] =usuario 
        return usuario

    def registrar (self, nombre, alias):
        usuario = Usuario(nombre, alias)
        return self.anadir(usuario)

    def publicar (self, publicacion):
        self.publicaciones.append(publicacion)
        return publicacion

    def timeline (self, usuario):
        return [publicacion for publicacion in reversed(self.publicaciones)
                if usuario.sigue_a(publicacion.autor) and publicacion.autor != usuario]

    def tendencias (self, n=3):
        contador = Counter()
        for publicacion in self.publicaciones:
            contador.update(publicacion.hashtags)
            
        return contador.most_common(n)

    def mostrar_timeline(self, alias):
        usuario = self.usuarios[alias]
        publicaciones = self.timeline(usuario)
        print(f"\nTimeline de {usuario}:")
        for publicacion in publicaciones:
            print(publicacion)

    @classmethod
    def desde_json(cls, ruta):
        with open(ruta, encoding="utf-8") as fichero:
            datos = json.load(fichero)

        red = cls()
        for datos_usuario in datos["usuarios"]:
            usuario = Usuario.desde_dict(datos_usuario)
            red.anadir(usuario)
        for quien_sigue, a_quien in datos["seguimientos"]:
            seguidor = red.usuarios[quien_sigue]
            seguido = red.usuarios[a_quien]
            seguidor.seguir(seguido)

        return red

    def __len__(self):
        return len(self.usuarios)

    def __iter__(self):
        return iter(sorted(self.usuarios.values(),
                           key=lambda usuario: usuario.alias))

    def __contains__(self, alias):
        return alias in self.usuarios

    def __getitem__(self, alias):
        return self.usuarios[alias]

    def __delitem__(self, alias):
        del self.usuarios[alias]
        
    