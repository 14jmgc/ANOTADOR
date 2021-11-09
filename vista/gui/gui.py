import sys

from PySide2.QtGui import QStandardItemModel, QStandardItem
from PySide2.QtWidgets import QMainWindow, QDialog, QApplication, QMessageBox

from mundo.errores import ElementoExistenteError
from mundo.mundo import Anotador
from vista.gui.ui_Ventana_Principal import Ui_MainWindow
from vista.gui.ui_crearLibro import Ui_DialogCrearLibro
from vista.gui.ui_crearPagina import Ui_DialogCrearPagina
from vista.gui.ui_crearSeccion import Ui_DialogCrearSeccion
from vista.gui.ui_crearNota import Ui_DialogCrearNota


class VentanaAnotador(QMainWindow):

    def __init__(self, anotador:Anotador):
        QMainWindow.__init__(self)
        self.anotador = anotador
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self._Configurar()
        self.showMaximized()
        self.show()

    def _Configurar(self):
        self.ui.pb_crearLibro.clicked.connect(self.abrir_dialogo_crear_libro)
        self.ui.lv_libros.setModel(QStandardItemModel())
        self.ui.lv_libros.selectionChanged = self.seleccionar_libro

        self.ui.f_secciones.setEnabled(False)
        self.ui.pb_crearSeccion.clicked.connect(self.abrir_dialogo_crear_seccion)
        self.ui.lv_secciones.setModel(QStandardItemModel())
        self.ui.lv_secciones.selectionChanged = self.seleccionar_seccion

        self.ui.f_paginas.setEnabled(False)
        self.ui.pb_crearPagina.clicked.connect(self.abrir_dialogo_crear_pagina)
        self.ui.lv_paginas.setModel(QStandardItemModel())
        self.ui.lv_paginas.selectionChanged = self.seleccionar_pagina

        self.ui.f_nota.setEnabled(False)

        self.ui.lv_notass.setModel(QStandardItemModel())
        self.ui.f_notass.setEnabled(False)


    def abrir_dialogo_crear_libro(self):
        dialogo = DialogCrearLibro(self)
        resp = dialogo.exec_()
        if resp == QDialog.Accepted:
            titulo_libro = dialogo.ui.le_tituloLibro.text()
            fecha_libro = dialogo.ui.dateEdit.text()

            try:
                libro = self.anotador.crear_libro(titulo_libro,fecha_libro)
            except ElementoExistenteError as err:
                msg_box = QMessageBox(self)
                msg_box.setWindowTitle("Error al crear")
                msg_box.setIcon(QMessageBox.Critical)
                msg_box.setText(err.msg)
                msg_box.setStandardButtons(QMessageBox.Ok)
                msg_box.exec_()
            else:
                self.actualizar_lista_libros(libro)

    def actualizar_lista_libros(self, libro):
        item = QStandardItem(str(libro))
        item.setEditable(False)
        item.libro = libro
        self.ui.lv_libros.model().appendRow(item)

    def seleccionar_libro(self, selected, deselected):
        self.ui.f_paginas.setEnabled(False)
        self.ui.f_nota.setEnabled(False)
        indexes = selected.indexes()
        if len(indexes) > 0:
            item = self.ui.lv_libros.model().itemFromIndex(indexes[0])

            self.ui.f_secciones.setEnabled(True)


            #self.actualizar_lv_seccion()
            #self.actualizar_lv_paginas()
            #self.actualizar_txt_notas()

    def abrir_dialogo_crear_seccion(self):
        dialogo = DialogCrearSeccion(self)
        resp= dialogo.exec_()
        if resp == QDialog.Accepted:
            titulo_seccion= dialogo.ui.le_tituloSeccion.text()
            fecha_seccion= dialogo.ui.de_fechaSeccion.text()

            try:
                seccion = self.anotador.crear_seccion(titulo_seccion, fecha_seccion)
            except ElementoExistenteError as err:
                msg_box = QMessageBox(self)
                msg_box.setWindowTitle("Error al crear")
                msg_box.setIcon(QMessageBox.Critical)
                msg_box.setText(err.msg)
                msg_box.setStandardButtons(QMessageBox.Ok)
                msg_box.exec_()
            else:
                self.actualizar_lista_seccion(seccion)

    def actualizar_lista_seccion(self, seccion):
        item = QStandardItem(str(seccion))
        item.setEditable(False)
        item.seccion = seccion
        self.ui.lv_secciones.model().appendRow(item)

    def seleccionar_seccion(self, selected, deselected):
        self.ui.f_nota.setEnabled(False)
        indexes = selected.indexes()
        if len(indexes) > 0:
            item = self.ui.lv_secciones.model().itemFromIndex(indexes[0])

            self.ui.f_paginas.setEnabled(True)

            self.actualizar_lv_paginas()
            #self.actualizar_txt_notas()


    def actualizar_lv_seccion(self):
        self.ui.lv_secciones.model().clear()
        indexes = self.ui.lv_libros.selectedIndexes()
        item = self.ui.lv_libros.model().itemFromIndex(indexes[0])

        #for seccion in item.libro.secciones:
        #    item = QStandardItem(str(seccion))
        #    item.setEditable(False)
        #    item.seccion = seccion
        #    self.ui.lv_secciones.model.appendRow(item)


    def abrir_dialogo_crear_pagina(self):
        dialogo = DialogCrearPagina(self)
        resp = dialogo.exec_()

        if resp == QDialog.Accepted:
            titulo_pagina = dialogo.ui.le_tituloPagina.text()
            fecha_pagina = dialogo.ui.de_fechaPagina.text()

            try:
                pagina = self.anotador.crear_pagina(titulo_pagina,fecha_pagina)
            except ElementoExistenteError as err:
                msg_box = QMessageBox(self)
                msg_box.setWindowTitle("Error al crear")
                msg_box.setIcon(QMessageBox.Critical)
                msg_box.setText(err.msg)
                msg_box.setStandardButtons(QMessageBox.Ok)
                msg_box.exec_()
            else:
                self.actualizar_lista_paginas(pagina)

    def actualizar_lista_paginas(self, pagina):
        item = QStandardItem(str(pagina))
        item.setEditable(False)
        item.pagina = pagina
        self.ui.lv_paginas.model().appendRow(item)

    def seleccionar_pagina(self, selected, deselected):
        indexes = selected.indexes()
        if len(indexes) > 0:
            item = self.ui.lv_paginas.model().itemFromIndex(indexes[0])

            self.ui.f_notass.setEnabled(True)
            self.actualizar_txt_notas()

    def actualizar_lv_paginas(self):
        self.ui.lv_paginas.model().clear()
        indexes = self.ui.lv_secciones.selectedIndexes()
        item = self.ui.lv_secciones.model().itemFromIndex(indexes[0])

    def actualizar_txt_notas(self):
        self.ui.txt_nota.clear()
        indexes = self.ui.lv_paginas.selectedIndexes()
        item = self.ui.lv_paginas.model().itemFromIndex(indexes[0])




class DialogCrearLibro(QDialog):
    def __init__(self, parent = None):
        QDialog.__init__(self, parent)
        self.ui = Ui_DialogCrearLibro()
        self.ui.setupUi(self)

    def accept(self) -> None:
        if self.ui.le_tituloLibro.text() != "" and self.ui.dateEdit.text() != "":
            super().accept()
        else:
            msg_box = QMessageBox(self)
            msg_box.setWindowTitle("Error de validacion")
            msg_box.setIcon(QMessageBox.Critical)
            msg_box.setText("Debe ingresar todos los campos obligatorios")
            msg_box.setStandardButtons(QMessageBox.Ok)
            msg_box.exec_()


class DialogCrearSeccion(QDialog):
    def __init__(self, parent = None):
        QDialog.__init__(self, parent)
        self.ui = Ui_DialogCrearSeccion()
        self.ui.setupUi(self)

    def accept(self) -> None:
        if self.ui.le_tituloSeccion.text() != "" and self.ui.de_fechaSeccion.text() != "":
            super().accept()
        else:
            msg_box = QMessageBox(self)
            msg_box.setWindowTitle("Error de validacion")
            msg_box.setIcon(QMessageBox.Critical)
            msg_box.setText("Debe ingresar todos los campos obligatorios")
            msg_box.setStandardButtons(QMessageBox.Ok)
            msg_box.exec_()


class DialogCrearPagina(QDialog):
    def __init__(self, parent = None):
        QDialog.__init__(self, parent)
        self.ui = Ui_DialogCrearPagina()
        self.ui.setupUi(self)

    def accept(self) -> None:
        if self.ui.le_tituloPagina.text() != "" and self.ui.de_fechaPagina.text() != "":
            super().accept()
        else:
            msg_box = QMessageBox(self)
            msg_box.setWindowTitle("Error de validacion")
            msg_box.setIcon(QMessageBox.Critical)
            msg_box.setText("Debe ingresar todos los campos obligatorios")
            msg_box.setStandardButtons(QMessageBox.Ok)
            msg_box.exec_()


class DialogCrearNota(QDialog):
    def __init__(self, parent = None):
        QDialog.__init__(self, parent)
        self.ui = Ui_DialogCrearNota
        self.ui.setupUi(self)

    def accept(self) -> None:
        if self.ui.le_tituloNota != "" and self.ui.de_fechaNota.text() != "" and self.ui.le_etiquetaNota.text() != "":
            super().accept()
        else:
            msg_box = QMessageBox(self)
            msg_box.setWindowTitle("Error de validacion")
            msg_box.setIcon(QMessageBox.Critical)
            msg_box.setText("Debe ingresar todos los campos obligatorios")
            msg_box.setStandardButtons(QMessageBox.Ok)
            msg_box.exec_()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    anotador = Anotador()
    window = VentanaAnotador(anotador)
    sys.exit(app.exec_())