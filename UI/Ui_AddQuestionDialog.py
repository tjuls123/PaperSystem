# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'AddQuestionDialog.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_AddQuestionDialog(object):
    def setupUi(self, AddQuestionDialog):
        AddQuestionDialog.setObjectName("AddQuestionDialog")
        AddQuestionDialog.resize(843, 587)
        self.horizontalLayout = QtWidgets.QHBoxLayout(AddQuestionDialog)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.widget = QtWidgets.QWidget(AddQuestionDialog)
        self.widget.setMinimumSize(QtCore.QSize(120, 0))
        self.widget.setMaximumSize(QtCore.QSize(120, 16777215))
        self.widget.setBaseSize(QtCore.QSize(300, 0))
        self.widget.setObjectName("widget")
        self.groupBox = QtWidgets.QGroupBox(self.widget)
        self.groupBox.setGeometry(QtCore.QRect(0, 0, 121, 431))
        self.groupBox.setAlignment(QtCore.Qt.AlignCenter)
        self.groupBox.setObjectName("groupBox")
        self.listWidget = QtWidgets.QListWidget(self.groupBox)
        self.listWidget.setGeometry(QtCore.QRect(0, 20, 121, 401))
        self.listWidget.setObjectName("listWidget")
        item = QtWidgets.QListWidgetItem()
        self.listWidget.addItem(item)
        self.horizontalLayout.addWidget(self.widget)
        self.widget_2 = QtWidgets.QWidget(AddQuestionDialog)
        self.widget_2.setObjectName("widget_2")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.widget_2)
        self.verticalLayout.setObjectName("verticalLayout")
        self.widget_3 = QtWidgets.QWidget(self.widget_2)
        self.widget_3.setObjectName("widget_3")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.widget_3)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.textEdit = QtWidgets.QTextEdit(self.widget_3)
        self.textEdit.setMaximumSize(QtCore.QSize(16777215, 300))
        self.textEdit.setObjectName("textEdit")
        self.horizontalLayout_2.addWidget(self.textEdit)
        self.verticalLayout.addWidget(self.widget_3)
        self.listWidget_2 = QtWidgets.QListWidget(self.widget_2)
        self.listWidget_2.setMinimumSize(QtCore.QSize(0, 0))
        self.listWidget_2.setMaximumSize(QtCore.QSize(16777215, 300))
        self.listWidget_2.setObjectName("listWidget_2")
        self.verticalLayout.addWidget(self.listWidget_2)
        self.widget_4 = QtWidgets.QWidget(self.widget_2)
        self.widget_4.setMinimumSize(QtCore.QSize(0, 30))
        self.widget_4.setObjectName("widget_4")
        self.pushButton = QtWidgets.QPushButton(self.widget_4)
        self.pushButton.setGeometry(QtCore.QRect(500, 0, 75, 23))
        self.pushButton.setObjectName("pushButton")
        self.verticalLayout.addWidget(self.widget_4)
        self.horizontalLayout.addWidget(self.widget_2)

        self.retranslateUi(AddQuestionDialog)
        QtCore.QMetaObject.connectSlotsByName(AddQuestionDialog)

    def retranslateUi(self, AddQuestionDialog):
        _translate = QtCore.QCoreApplication.translate
        AddQuestionDialog.setWindowTitle(_translate("AddQuestionDialog", "添加题目"))
        self.groupBox.setTitle(_translate("AddQuestionDialog", "题目类型"))
        __sortingEnabled = self.listWidget.isSortingEnabled()
        self.listWidget.setSortingEnabled(False)
        item = self.listWidget.item(0)
        item.setText(_translate("AddQuestionDialog", "单选题"))
        self.listWidget.setSortingEnabled(__sortingEnabled)
        self.pushButton.setText(_translate("AddQuestionDialog", "确认添加"))
