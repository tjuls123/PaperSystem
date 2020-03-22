# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'AnswerItem.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_AnswerItem(object):
    def setupUi(self, AnswerItem):
        AnswerItem.setObjectName("AnswerItem")
        AnswerItem.resize(481, 107)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(AnswerItem)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.widget = QtWidgets.QWidget(AnswerItem)
        self.widget.setObjectName("widget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.widget)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.textEdit = QtWidgets.QTextEdit(self.widget)
        self.textEdit.setObjectName("textEdit")
        self.horizontalLayout.addWidget(self.textEdit)
        self.radioButton = QtWidgets.QRadioButton(self.widget)
        self.radioButton.setObjectName("radioButton")
        self.horizontalLayout.addWidget(self.radioButton)
        self.horizontalLayout_2.addWidget(self.widget)

        self.retranslateUi(AnswerItem)
        QtCore.QMetaObject.connectSlotsByName(AnswerItem)

    def retranslateUi(self, AnswerItem):
        _translate = QtCore.QCoreApplication.translate
        AnswerItem.setWindowTitle(_translate("AnswerItem", "Form"))
        self.radioButton.setText(_translate("AnswerItem", "正确答案"))
