# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'H:\NEW_ETH_IQ\helpspec.ui'
#
# Created by: PyQt5 UI code generator 5.12.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(495, 150)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Form.sizePolicy().hasHeightForWidth())
        Form.setSizePolicy(sizePolicy)
        Form.setMinimumSize(QtCore.QSize(495, 150))
        Form.setMaximumSize(QtCore.QSize(495, 150))
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(30, 0, 470, 140))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        self.label.setMinimumSize(QtCore.QSize(470, 140))
        self.label.setMaximumSize(QtCore.QSize(470, 140))
        self.label.setObjectName("label")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Оконные функции"))
        self.label.setText(_translate("Form", "<table  border=\"1\">\n"
"\n"
"<tr>\n"
"<th>Название</th>\n"
"<th>Полное название</th>\n"
"<th>Коэфициент</th>\n"
"</tr>\n"
"\n"
"\n"
"<tr>\n"
"<td>gaussian</td>\n"
"<td>Gaussian window</td>\n"
"<td>The standard deviation, sigma, любое значение</td>\n"
"</tr>\n"
"\n"
"<tr>\n"
"<td>kaiser</td>\n"
"<td>Kaiser window</td>\n"
"<td>Shape parameter, рекомендовано [0:14]</td>\n"
"</tr>\n"
"\n"
"<tr>\n"
"<td>blackman</td>\n"
"<td>lackman window</td>\n"
"<td>Не требуется</td>\n"
"</tr>\n"
"\n"
"<tr>\n"
"<td>barthann</td>\n"
"<td>Bartlett-Hann window</td>\n"
"<td>Не требуется</td>\n"
"</tr>\n"
"\n"
"<tr>\n"
"<td>exponential</td>\n"
"<td>exponential (or Poisson) window</td>\n"
"<td>Не требуется</td>\n"
"</tr>\n"
"\n"
"</table>"))


