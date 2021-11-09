class AnotadorError(Exception):
    pass

class ElementoExistenteError(AnotadorError):
    """
    Representa una excepcion que indica que el elemento (libro, seccion, pagina o nota) ya existe

    Atrributes:
    titulo: Indica el titulo del elemnto que ya existe
    mensaje: contiene el mensaje de error


    """
    def __init__(self, titulo: str, msg:str):
        self.titulo = titulo
        self.msg = msg


class ElementoNoExistenteError(AnotadorError):
    """
    Representa una excepcion que indica que el elemento (libro, seccion, pagina o nota) No existe

    Atrributes:
    titulo: Indica el titulo del elemnto que No existe
    mensaje: contiene el mensaje de error


    """

    def __init__(self, titulo: str, msg: str):
        self.titulo = titulo
        self.msg = msg
