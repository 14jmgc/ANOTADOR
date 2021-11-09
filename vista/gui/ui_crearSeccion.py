# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'crearSeccionwjyAmO.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_DialogCrearSeccion(object):
    def setupUi(self, DialogCrearSeccion):
        if not DialogCrearSeccion.objectName():
            DialogCrearSeccion.setObjectName(u"DialogCrearSeccion")
        DialogCrearSeccion.resize(395, 140)
        self.verticalLayout = QVBoxLayout(DialogCrearSeccion)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.frame = QFrame(DialogCrearSeccion)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.formLayout = QFormLayout(self.frame)
        self.formLayout.setObjectName(u"formLayout")
        self.lbl_tituloSeccion = QLabel(self.frame)
        self.lbl_tituloSeccion.setObjectName(u"lbl_tituloSeccion")

        self.formLayout.setWidget(0, QFormLayout.LabelRole, self.lbl_tituloSeccion)

        self.lbl_fechaSeccion = QLabel(self.frame)
        self.lbl_fechaSeccion.setObjectName(u"lbl_fechaSeccion")

        self.formLayout.setWidget(1, QFormLayout.LabelRole, self.lbl_fechaSeccion)

        self.le_tituloSeccion = QLineEdit(self.frame)
        self.le_tituloSeccion.setObjectName(u"le_tituloSeccion")

        self.formLayout.setWidget(0, QFormLayout.FieldRole, self.le_tituloSeccion)

        self.de_fechaSeccion = QDateEdit(self.frame)
        self.de_fechaSeccion.setObjectName(u"de_fechaSeccion")

        self.formLayout.setWidget(1, QFormLayout.FieldRole, self.de_fechaSeccion)


        self.verticalLayout.addWidget(self.frame)

        self.botones_crearSeccion = QDialogButtonBox(DialogCrearSeccion)
        self.botones_crearSeccion.setObjectName(u"botones_crearSeccion")
        self.botones_crearSeccion.setOrientation(Qt.Horizontal)
        self.botones_crearSeccion.setStandardButtons(QDialogButtonBox.Cancel|QDialogButtonBox.Ok)

        self.verticalLayout.addWidget(self.botones_crearSeccion)


        self.retranslateUi(DialogCrearSeccion)
        self.botones_crearSeccion.accepted.connect(DialogCrearSeccion.accept)
        self.botones_crearSeccion.rejected.connect(DialogCrearSeccion.reject)

        QMetaObject.connectSlotsByName(DialogCrearSeccion)
    # setupUi

    def retranslateUi(self, DialogCrearSeccion):
        DialogCrearSeccion.setWindowTitle(QCoreApplication.translate("DialogCrearSeccion", u"Dialog", None))
        self.lbl_tituloSeccion.setText(QCoreApplication.translate("DialogCrearSeccion", u"Titulo:", None))
        self.lbl_fechaSeccion.setText(QCoreApplication.translate("DialogCrearSeccion", u"Fecha:", None))
        self.le_tituloSeccion.setPlaceholderText(QCoreApplication.translate("DialogCrearSeccion", u"Obligatorio*", None))
    # retranslateUi

