from PyQt5.QtCore import QSize
from PyQt5.QtWidgets import QWidget, QListWidgetItem

from UI.QQuestionItem import QAnswerItem
from UI.Ui_QuestionItem import Ui_QuestionItem


class QQuestionItem(QWidget, Ui_QuestionItem):

    def __init__(self, question, delete_cb=None, add_cb=None):
        super(QQuestionItem, self).__init__()
        self.setupUi(self)
        self.question = question
        self.delete_cb = delete_cb
        self.add_cb = add_cb
        if self.delete_cb:
            self.pushButton_2.setText('删除')
        if self.add_cb:
            self.pushButton_2.setText('添加')
        assert not (self.delete_cb and self.add_cb)
        self.pushButton_2.clicked.connect(self.on_clicked)
        self.init_question()

    def get_answer_item(self):
        answer_item = QAnswerItem()
        return answer_item

    def init_question(self):
        q = self.question
        self.textEdit.setText(q.question)
        for index, answer in enumerate(q.answer_option):
            item = QListWidgetItem()
            item.setSizeHint(QSize(360, 80))
            answer_item = QAnswerItem()
            answer_item.textEdit.setText(answer)
            answer_item.radioButton.setChecked(index in q.correct_answer)
            self.listWidget.addItem(item)
            self.listWidget.setItemWidget(item, answer_item)

    def on_clicked(self):
        if self.delete_cb:
            self.delete_cb(self.question)
        if self.add_cb:
            self.add_cb(self.question)
