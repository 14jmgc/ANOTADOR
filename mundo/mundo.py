from mundo.errores import ElementoExistenteError, ElementoNoExistenteError


class Parte:
    def __init__(self, titulo: str, fecha: str):
        self.titulo = titulo
        self.fecha = fecha


class Libro(Parte):
    def __init__(self, titulo: str, fecha: str):
        Parte.__init__(self, titulo, fecha)

    def __str__(self):
        return f"{self.titulo} [{self.fecha}]"


class Seccion(Parte):
    def __init__(self, titulo: str, fecha: str):
        Parte.__init__(self, titulo, fecha)

    def __str__(self):
        return f"{self.titulo} [{self.fecha}]"


class Pagina(Parte):
    def __init__(self, titulo: str, fecha: str):
        Parte.__init__(self, titulo, fecha)

    def __str__(self):
        return f"{self.titulo} [{self.fecha}]"


class Nota(Parte):
    def __init__(self, titulo: str, fecha: str, etiqueta: str, contenido: str):
        self.contenido = contenido
        self.etiqueta = etiqueta
        Parte.__init__(self, titulo, fecha)

    def __str__(self):
        return f"{self.titulo} [{self.fecha}] #{self.etiqueta} \n {self.contenido}"


class Anotador:
    def __init__(self):
        self.etiquetas = list()
        self.libros = dict()
        self.secciones = dict()
        self.paginas = dict()
        self.notas = dict()

    def buscar_libro(self, titulo_libro: str):

        if titulo_libro in self.libros.keys():
            return self.libros[titulo_libro]
        else:
            return None

    def crear_libro(self, titulo_libro, fecha_libro):
        lib = self.buscar_libro(titulo_libro)
        if lib is None:
            libro = titulo_libro + "     " + "Fecha de creacion: " + fecha_libro
            self.libros[titulo_libro] = fecha_libro
            return libro
        else:
            raise ElementoExistenteError(titulo_libro, f"Ya existe un libro con el titulo {titulo_libro}")

    def eliminar_libro(self, titulo_libro: str):
        lib = self.buscar_libro(titulo_libro)
        if lib is not None:
            del self.libros[titulo_libro]
        else:
            raise ElementoNoExistenteError(titulo_libro, f"No existe un libro con el titulo {titulo_libro}")

    def buscar_seccion(self, titulo_seccion: str):
        if titulo_seccion in self.secciones.keys():
            return self.secciones[titulo_seccion]
        else:
            return None

    def crear_seccion(self, titulo_seccion, fecha_seccion):
        sec = self.buscar_seccion(titulo_seccion)
        if sec is None:
            seccion = titulo_seccion + "     " + "Fecha de creacion: " + fecha_seccion
            self.secciones[titulo_seccion] = fecha_seccion
            return seccion
        else:
            raise ElementoExistenteError(titulo_seccion, f"Ya exíste una sección con el titulo {titulo_seccion}")

    def eliminar_seccion(self, titulo_seccion):
        seccion = self.buscar_seccion(titulo_seccion)
        if Seccion is not None:
            del self.secciones[titulo_seccion]
        else:
            raise ElementoNoExistenteError(titulo_seccion, f"No existe una seccion con el titulo {titulo_seccion}")
            pass

    def buscar_pagina(self, titulo_pagina):
        if titulo_pagina in self.paginas.keys():
            return self.paginas[titulo_pagina]
        else:
            return None

    def crear_pagina(self, titulo_pagina, fecha_pagina):
        pag = self.buscar_pagina(titulo_pagina)
        if pag is None:
            pagina = titulo_pagina + "     " + "Fecha de creacion: " + fecha_pagina
            self.paginas[titulo_pagina] = fecha_pagina
            return pagina
        else:
            raise ElementoExistenteError(titulo_pagina, f"Ya exíste una página con el titulo {titulo_pagina}")

    def eliminar_pagina(self, titulo_pagina):
        pagina = self.buscar_pagina(titulo_pagina)
        if pagina is not None:
            del self.paginas[titulo_pagina]
        else:
            raise ElementoNoExistenteError(titulo_pagina, f"No existe una pagina con el titulo {titulo_pagina}")

    def buscar_nota(self, titulo_nota):
        if titulo_nota in self.notas.keys():
            return self.notas[titulo_nota]
        else:
            return None

    def crear_nota(self, nota: Nota):
        Not = self.buscar_nota(nota.titulo)
        if Not is None:
            self.notas[nota.titulo] = (nota.fecha, nota.etiqueta, nota.contenido)
            self.etiquetas.append(nota.etiqueta)
        else:
            raise ElementoExistenteError(nota.titulo, f"Ya existe una nota con el titulo {nota.titulo}")

    def eliminar_nota(self, titulo_nota):
        nota = self.buscar_nota(titulo_nota)
        if nota is not None:
            del self.notas[titulo_nota]
        else:
            raise ElementoNoExistenteError(titulo_nota, f"No existe una nota con el titulo {titulo_nota}")
            pass

    def archivar_nota(self, nota: Nota):
        Not = self.buscar_nota(nota)
        notas_archivadas = list()
        if Not is not None:
            notas_archivadas.append(nota)
            del self.notas[nota.titulo]
        else:
            raise ElementoNoExistenteError(nota.titulo, f"No existe una nota con el titulo {nota.titulo}")

    def buscar_etiqueta(self, etiqueta: str):
        if etiqueta in self.etiquetas:
            return etiqueta
        else:
            raise ElementoNoExistenteError(etiqueta, f"No existe una etiqueta con el titulo {etiqueta}")
