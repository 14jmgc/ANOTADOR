# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'crearLibrokHnlPy.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_DialogCrearLibro(object):
    def setupUi(self, DialogCrearLibro):
        if not DialogCrearLibro.objectName():
            DialogCrearLibro.setObjectName(u"DialogCrearLibro")
        DialogCrearLibro.resize(392, 136)
        self.verticalLayout = QVBoxLayout(DialogCrearLibro)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.frame = QFrame(DialogCrearLibro)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.formLayout = QFormLayout(self.frame)
        self.formLayout.setObjectName(u"formLayout")
        self.lbl_tituloLibro = QLabel(self.frame)
        self.lbl_tituloLibro.setObjectName(u"lbl_tituloLibro")

        self.formLayout.setWidget(0, QFormLayout.LabelRole, self.lbl_tituloLibro)

        self.lbl_fechaLibro = QLabel(self.frame)
        self.lbl_fechaLibro.setObjectName(u"lbl_fechaLibro")

        self.formLayout.setWidget(1, QFormLayout.LabelRole, self.lbl_fechaLibro)

        self.le_tituloLibro = QLineEdit(self.frame)
        self.le_tituloLibro.setObjectName(u"le_tituloLibro")

        self.formLayout.setWidget(0, QFormLayout.FieldRole, self.le_tituloLibro)

        self.dateEdit = QDateEdit(self.frame)
        self.dateEdit.setObjectName(u"dateEdit")

        self.formLayout.setWidget(1, QFormLayout.FieldRole, self.dateEdit)


        self.verticalLayout.addWidget(self.frame)

        self.botones_crearLibro = QDialogButtonBox(DialogCrearLibro)
        self.botones_crearLibro.setObjectName(u"botones_crearLibro")
        self.botones_crearLibro.setOrientation(Qt.Horizontal)
        self.botones_crearLibro.setStandardButtons(QDialogButtonBox.Cancel|QDialogButtonBox.Ok)

        self.verticalLayout.addWidget(self.botones_crearLibro)


        self.retranslateUi(DialogCrearLibro)
        self.botones_crearLibro.accepted.connect(DialogCrearLibro.accept)
        self.botones_crearLibro.rejected.connect(DialogCrearLibro.reject)

        QMetaObject.connectSlotsByName(DialogCrearLibro)
    # setupUi

    def retranslateUi(self, DialogCrearLibro):
        DialogCrearLibro.setWindowTitle(QCoreApplication.translate("DialogCrearLibro", u"Dialog", None))
        self.lbl_tituloLibro.setText(QCoreApplication.translate("DialogCrearLibro", u"Titulo:", None))
        self.lbl_fechaLibro.setText(QCoreApplication.translate("DialogCrearLibro", u"Fecha:", None))
        self.le_tituloLibro.setPlaceholderText(QCoreApplication.translate("DialogCrearLibro", u"Obligatorio*", None))
    # retranslateUi

