# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'crearPaginaWJtRoU.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_DialogCrearPagina(object):
    def setupUi(self, DialogCrearPagina):
        if not DialogCrearPagina.objectName():
            DialogCrearPagina.setObjectName(u"DialogCrearPagina")
        DialogCrearPagina.resize(400, 137)
        self.verticalLayout = QVBoxLayout(DialogCrearPagina)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.frame = QFrame(DialogCrearPagina)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.formLayout = QFormLayout(self.frame)
        self.formLayout.setObjectName(u"formLayout")
        self.lbl_tituloPagina = QLabel(self.frame)
        self.lbl_tituloPagina.setObjectName(u"lbl_tituloPagina")

        self.formLayout.setWidget(0, QFormLayout.LabelRole, self.lbl_tituloPagina)

        self.lbl_fechaPagina = QLabel(self.frame)
        self.lbl_fechaPagina.setObjectName(u"lbl_fechaPagina")

        self.formLayout.setWidget(1, QFormLayout.LabelRole, self.lbl_fechaPagina)

        self.le_tituloPagina = QLineEdit(self.frame)
        self.le_tituloPagina.setObjectName(u"le_tituloPagina")

        self.formLayout.setWidget(0, QFormLayout.FieldRole, self.le_tituloPagina)

        self.de_fechaPagina = QDateEdit(self.frame)
        self.de_fechaPagina.setObjectName(u"de_fechaPagina")

        self.formLayout.setWidget(1, QFormLayout.FieldRole, self.de_fechaPagina)


        self.verticalLayout.addWidget(self.frame)

        self.botones_crearPagina = QDialogButtonBox(DialogCrearPagina)
        self.botones_crearPagina.setObjectName(u"botones_crearPagina")
        self.botones_crearPagina.setOrientation(Qt.Horizontal)
        self.botones_crearPagina.setStandardButtons(QDialogButtonBox.Cancel|QDialogButtonBox.Ok)

        self.verticalLayout.addWidget(self.botones_crearPagina)


        self.retranslateUi(DialogCrearPagina)
        self.botones_crearPagina.accepted.connect(DialogCrearPagina.accept)
        self.botones_crearPagina.rejected.connect(DialogCrearPagina.reject)

        QMetaObject.connectSlotsByName(DialogCrearPagina)
    # setupUi

    def retranslateUi(self, DialogCrearPagina):
        DialogCrearPagina.setWindowTitle(QCoreApplication.translate("DialogCrearPagina", u"Dialog", None))
        self.lbl_tituloPagina.setText(QCoreApplication.translate("DialogCrearPagina", u"Titulo:", None))
        self.lbl_fechaPagina.setText(QCoreApplication.translate("DialogCrearPagina", u"Fecha:", None))
        self.le_tituloPagina.setPlaceholderText(QCoreApplication.translate("DialogCrearPagina", u"Obligatorio*", None))
    # retranslateUi

