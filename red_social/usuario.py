class Usuario:

    def __init__ (self, nombre, alias):
        self.nombre = nombre
        if not alias.startswith("@"):
            alias = "@"+alias

        self.alias = alias
        self.seguidos = []

    @classmethod
    def desde_dict(cls, datos):  
        return cls(datos ["nombre"], datos ["alias"])

    @property
    def numero_seguidos(self):
        return len(self.seguidos)
    
    def seguir (self, otro):
        if self == otro:
            raise ValueError("Un usuario no puede seguirse a si mismo")
        
        if self.sigue_a(otro):
            raise ValueError("El usuario ya sigue a esta persona")
        self.seguidos.append(otro)

    def sigue_a (self, otro): 
        return otro in self.seguidos

    def a_dict(self):
        return {
            "nombre": self.nombre,
            "alias":self.alias
        }

    def __str__(self):
        
        return f"{self.nombre} ({self.alias})"

    def __eq__(self, otro):

        if not isinstance (otro, Usuario):
            return NotImplemented
        
        return self.alias == otro.alias

