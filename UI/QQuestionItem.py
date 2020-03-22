from PyQt5.QtWidgets import QWidget

from UI.Ui_AnswerItem import Ui_AnswerItem


class QAnswerItem(QWidget, Ui_AnswerItem):
    def __init__(self):
        super(QAnswerItem, self).__init__()
        self.setupUi(self)
