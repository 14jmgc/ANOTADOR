# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'crearNotalTfUjQ.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_DialogCrearNota(object):
    def setupUi(self, DialogCrearNota):
        if not DialogCrearNota.objectName():
            DialogCrearNota.setObjectName(u"DialogCrearNota")
        DialogCrearNota.resize(358, 167)
        self.verticalLayout = QVBoxLayout(DialogCrearNota)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.frame = QFrame(DialogCrearNota)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.formLayout = QFormLayout(self.frame)
        self.formLayout.setObjectName(u"formLayout")
        self.lbl_tituloNota = QLabel(self.frame)
        self.lbl_tituloNota.setObjectName(u"lbl_tituloNota")

        self.formLayout.setWidget(0, QFormLayout.LabelRole, self.lbl_tituloNota)

        self.le_tituloNota = QLineEdit(self.frame)
        self.le_tituloNota.setObjectName(u"le_tituloNota")

        self.formLayout.setWidget(0, QFormLayout.FieldRole, self.le_tituloNota)

        self.lbl_fechaNota = QLabel(self.frame)
        self.lbl_fechaNota.setObjectName(u"lbl_fechaNota")

        self.formLayout.setWidget(1, QFormLayout.LabelRole, self.lbl_fechaNota)

        self.lbl_etiquetaNota = QLabel(self.frame)
        self.lbl_etiquetaNota.setObjectName(u"lbl_etiquetaNota")

        self.formLayout.setWidget(2, QFormLayout.LabelRole, self.lbl_etiquetaNota)

        self.de_fechaNota = QDateEdit(self.frame)
        self.de_fechaNota.setObjectName(u"de_fechaNota")

        self.formLayout.setWidget(1, QFormLayout.FieldRole, self.de_fechaNota)

        self.le_etiquetaNota = QLineEdit(self.frame)
        self.le_etiquetaNota.setObjectName(u"le_etiquetaNota")

        self.formLayout.setWidget(2, QFormLayout.FieldRole, self.le_etiquetaNota)


        self.verticalLayout.addWidget(self.frame)

        self.botones_crearNota = QDialogButtonBox(DialogCrearNota)
        self.botones_crearNota.setObjectName(u"botones_crearNota")
        self.botones_crearNota.setOrientation(Qt.Horizontal)
        self.botones_crearNota.setStandardButtons(QDialogButtonBox.Cancel|QDialogButtonBox.Ok)

        self.verticalLayout.addWidget(self.botones_crearNota)


        self.retranslateUi(DialogCrearNota)
        self.botones_crearNota.accepted.connect(DialogCrearNota.accept)
        self.botones_crearNota.rejected.connect(DialogCrearNota.reject)

        QMetaObject.connectSlotsByName(DialogCrearNota)
    # setupUi

    def retranslateUi(self, DialogCrearNota):
        DialogCrearNota.setWindowTitle(QCoreApplication.translate("DialogCrearNota", u"Dialog", None))
        self.lbl_tituloNota.setText(QCoreApplication.translate("DialogCrearNota", u"Titulo", None))
        self.le_tituloNota.setPlaceholderText(QCoreApplication.translate("DialogCrearNota", u"Obligatorio*", None))
        self.lbl_fechaNota.setText(QCoreApplication.translate("DialogCrearNota", u"Fecha", None))
        self.lbl_etiquetaNota.setText(QCoreApplication.translate("DialogCrearNota", u"Etiqueta", None))
        self.le_etiquetaNota.setPlaceholderText(QCoreApplication.translate("DialogCrearNota", u"Obligatorio*", None))
    # retranslateUi

