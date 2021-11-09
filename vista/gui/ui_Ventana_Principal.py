# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Ventana_PrincipalqAfLuR.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(991, 554)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.horizontalLayout = QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.frame = QFrame(self.centralwidget)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.frame)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.frame_3 = QFrame(self.frame)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.verticalLayout = QVBoxLayout(self.frame_3)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.lbl_libros = QLabel(self.frame_3)
        self.lbl_libros.setObjectName(u"lbl_libros")

        self.verticalLayout.addWidget(self.lbl_libros)

        self.lv_libros = QListView(self.frame_3)
        self.lv_libros.setObjectName(u"lv_libros")

        self.verticalLayout.addWidget(self.lv_libros)

        self.pb_crearLibro = QPushButton(self.frame_3)
        self.pb_crearLibro.setObjectName(u"pb_crearLibro")

        self.verticalLayout.addWidget(self.pb_crearLibro)

        self.pb_eliminarLibro = QPushButton(self.frame_3)
        self.pb_eliminarLibro.setObjectName(u"pb_eliminarLibro")

        self.verticalLayout.addWidget(self.pb_eliminarLibro)


        self.horizontalLayout_2.addWidget(self.frame_3)

        self.f_secciones = QFrame(self.frame)
        self.f_secciones.setObjectName(u"f_secciones")
        self.f_secciones.setEnabled(True)
        self.f_secciones.setFrameShape(QFrame.StyledPanel)
        self.f_secciones.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.f_secciones)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.lbl_secciones = QLabel(self.f_secciones)
        self.lbl_secciones.setObjectName(u"lbl_secciones")

        self.verticalLayout_2.addWidget(self.lbl_secciones)

        self.lv_secciones = QListView(self.f_secciones)
        self.lv_secciones.setObjectName(u"lv_secciones")

        self.verticalLayout_2.addWidget(self.lv_secciones)

        self.pb_crearSeccion = QPushButton(self.f_secciones)
        self.pb_crearSeccion.setObjectName(u"pb_crearSeccion")

        self.verticalLayout_2.addWidget(self.pb_crearSeccion)

        self.pb_eliminarSeccion = QPushButton(self.f_secciones)
        self.pb_eliminarSeccion.setObjectName(u"pb_eliminarSeccion")

        self.verticalLayout_2.addWidget(self.pb_eliminarSeccion)


        self.horizontalLayout_2.addWidget(self.f_secciones)

        self.f_paginas = QFrame(self.frame)
        self.f_paginas.setObjectName(u"f_paginas")
        self.f_paginas.setEnabled(True)
        self.f_paginas.setFrameShape(QFrame.StyledPanel)
        self.f_paginas.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.f_paginas)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.lbl_paginas = QLabel(self.f_paginas)
        self.lbl_paginas.setObjectName(u"lbl_paginas")

        self.verticalLayout_3.addWidget(self.lbl_paginas)

        self.lv_paginas = QListView(self.f_paginas)
        self.lv_paginas.setObjectName(u"lv_paginas")

        self.verticalLayout_3.addWidget(self.lv_paginas)

        self.pb_crearPagina = QPushButton(self.f_paginas)
        self.pb_crearPagina.setObjectName(u"pb_crearPagina")

        self.verticalLayout_3.addWidget(self.pb_crearPagina)

        self.pb_eliminarPagina = QPushButton(self.f_paginas)
        self.pb_eliminarPagina.setObjectName(u"pb_eliminarPagina")

        self.verticalLayout_3.addWidget(self.pb_eliminarPagina)


        self.horizontalLayout_2.addWidget(self.f_paginas)

        self.f_notass = QFrame(self.frame)
        self.f_notass.setObjectName(u"f_notass")
        self.f_notass.setFrameShape(QFrame.StyledPanel)
        self.f_notass.setFrameShadow(QFrame.Raised)
        self.verticalLayout_6 = QVBoxLayout(self.f_notass)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.lbl_notass = QLabel(self.f_notass)
        self.lbl_notass.setObjectName(u"lbl_notass")

        self.verticalLayout_6.addWidget(self.lbl_notass)

        self.lv_notass = QListView(self.f_notass)
        self.lv_notass.setObjectName(u"lv_notass")

        self.verticalLayout_6.addWidget(self.lv_notass)

        self.pushButton = QPushButton(self.f_notass)
        self.pushButton.setObjectName(u"pushButton")

        self.verticalLayout_6.addWidget(self.pushButton)

        self.pushButton_2 = QPushButton(self.f_notass)
        self.pushButton_2.setObjectName(u"pushButton_2")

        self.verticalLayout_6.addWidget(self.pushButton_2)


        self.horizontalLayout_2.addWidget(self.f_notass)


        self.horizontalLayout.addWidget(self.frame)

        self.q_frameNota = QFrame(self.centralwidget)
        self.q_frameNota.setObjectName(u"q_frameNota")
        self.q_frameNota.setFrameShape(QFrame.StyledPanel)
        self.q_frameNota.setFrameShadow(QFrame.Raised)
        self.verticalLayout_4 = QVBoxLayout(self.q_frameNota)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.f_nota = QFrame(self.q_frameNota)
        self.f_nota.setObjectName(u"f_nota")
        self.f_nota.setFrameShape(QFrame.StyledPanel)
        self.f_nota.setFrameShadow(QFrame.Raised)
        self.verticalLayout_5 = QVBoxLayout(self.f_nota)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.lbl_nota = QLabel(self.f_nota)
        self.lbl_nota.setObjectName(u"lbl_nota")

        self.verticalLayout_5.addWidget(self.lbl_nota)

        self.txt_nota = QTextEdit(self.f_nota)
        self.txt_nota.setObjectName(u"txt_nota")

        self.verticalLayout_5.addWidget(self.txt_nota)


        self.verticalLayout_4.addWidget(self.f_nota)

        self.pb_archivar = QPushButton(self.q_frameNota)
        self.pb_archivar.setObjectName(u"pb_archivar")

        self.verticalLayout_4.addWidget(self.pb_archivar)


        self.horizontalLayout.addWidget(self.q_frameNota)

        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.lbl_libros.setText(QCoreApplication.translate("MainWindow", u"Libros", None))
        self.pb_crearLibro.setText(QCoreApplication.translate("MainWindow", u"Crear Libro", None))
        self.pb_eliminarLibro.setText(QCoreApplication.translate("MainWindow", u"Eliminar Libro", None))
        self.lbl_secciones.setText(QCoreApplication.translate("MainWindow", u"Secciones", None))
        self.pb_crearSeccion.setText(QCoreApplication.translate("MainWindow", u"Crear Secci\u00f3n", None))
        self.pb_eliminarSeccion.setText(QCoreApplication.translate("MainWindow", u"Eliminar Secci\u00f3n", None))
        self.lbl_paginas.setText(QCoreApplication.translate("MainWindow", u"P\u00e1ginas", None))
        self.pb_crearPagina.setText(QCoreApplication.translate("MainWindow", u"Crear P\u00e1gina", None))
        self.pb_eliminarPagina.setText(QCoreApplication.translate("MainWindow", u"Eliminar P\u00e1gina", None))
        self.lbl_notass.setText(QCoreApplication.translate("MainWindow", u"Notas", None))
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"Crear Nota", None))
        self.pushButton_2.setText(QCoreApplication.translate("MainWindow", u"Eliminar Nota", None))
        self.lbl_nota.setText(QCoreApplication.translate("MainWindow", u"Nota", None))
        self.pb_archivar.setText(QCoreApplication.translate("MainWindow", u"Archivar Nota", None))
    # retranslateUi

