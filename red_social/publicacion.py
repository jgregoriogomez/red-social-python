import re
from abc import ABC, abstractmethod

from red_social.usuario import Usuario

LIMITE_CARACTERES = 280

class Publicacion (ABC):

    def __init__ (self, autor, texto):

        if not isinstance (autor, Usuario):
            raise TypeError("El autor debe ser un usuario")
        
        if not texto or not texto.strip():
            raise ValueError("El texto no puede estar vacio")
        
        if len(texto) > LIMITE_CARACTERES:
            raise ValueError (f"El texto no puede superar {LIMITE_CARACTERES} caracteres")

        self.autor = autor
        self.texto = texto
        self.me_gusta = 0  

    @staticmethod
    def extraer_hashtags(texto):
        return [hashtag.lower()
                for hashtag in re.findall(r"#\w+", texto ,flags=re.UNICODE)]

    @staticmethod
    def validar_original(original):
        if not isinstance (original, Publicacion):
            raise TypeError("El publicacion original ser una publicacion")

    @property
    def hashtags(self):
        return self.extraer_hashtags(self.texto)

    def dar_me_gusta(self):
        self.me_gusta += 1

    @abstractmethod
    def __str__(self):
        pass

class Tweet(Publicacion):

    def __init__ (self, autor, texto):
        super().__init__(autor, texto)

    def __str__(self):
        return f"{self.autor.alias}: {self.texto}"


class Respuesta(Publicacion):
    def __init__ (self, autor, texto, original):    
            Publicacion.validar_original(original)
            super().__init__(autor, texto)
            self.original = original

    def __str__(self):
            return f"{self.autor.alias} \u21B5 {self.original.autor.alias}: {self.texto}"

class Retweet(Publicacion):
    def __init__ (self, autor, original):
        Publicacion.validar_original(original)
        super().__init__(autor, original.texto)
        self.original = original  

    def __str__(self):
            return f"{self.autor.alias} \U0001F501 {self.original}"
           
