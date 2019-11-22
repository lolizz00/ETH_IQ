# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'H:\NEW_ETH_IQ\helpplot.ui'
#
# Created by: PyQt5 UI code generator 5.12.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(630, 160)
        Form.setMinimumSize(QtCore.QSize(630, 160))
        Form.setMaximumSize(QtCore.QSize(630, 160))
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(40, 20, 550, 120))
        self.label.setMinimumSize(QtCore.QSize(550, 120))
        self.label.setMaximumSize(QtCore.QSize(550, 120))
        self.label.setObjectName("label")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Кнопки работы с графиками"))
        self.label.setText(_translate("Form", "<center>\n"
"    <img src=\"toolbar.png\"></img>\n"
"</center>\n"
"\n"
"<ol>\n"
"    <li>Вернуться к исходному виду</li>\n"
"    <li>Зажатая ЛКМ - перемещение графика. Зажатая ПКМ  - масштабирование осей </li>\n"
"    <li>Зажатая ЛКМ - увеличение в выбранной области. Зажатая ПКМ - уменьшение выбранной области.</li>\n"
"<li>Сохранить график</li>\n"
"    \n"
"</ol>\n"
""))


