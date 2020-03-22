from PyQt5.QtCore import QSize
from PyQt5.QtWidgets import QWidget, QListWidgetItem, QMessageBox

from UI.QQuestionItem import QAnswerItem
from Question import Question
from UI.Ui_AddQuestionDialog import Ui_AddQuestionDialog


class AddQuestionDialog(QWidget, Ui_AddQuestionDialog):
    def __init__(self, parent=None):
        super(AddQuestionDialog, self).__init__(parent)
        self.setupUi(self)

        self.answer_items = []
        for index in range(4):
            item = QListWidgetItem()
            item.setSizeHint(QSize(418, 60))
            self.listWidget_2.addItem(item)
            answer_item = QAnswerItem()
            self.listWidget_2.setItemWidget(item, answer_item)
            self.answer_items.append(answer_item)

        self.pushButton.clicked.connect(self.on_add_question)

    def on_add_question(self):
        # conn = sqlite3.connect('test.db')

        msg_box = ''
        if not self.textEdit.toPlainText():
            msg_box = '题目不能为空！！！'

        correct_answer = -1
        for index, item in enumerate(self.answer_items):
            if not item.textEdit.toPlainText():
                msg_box = '选项不能为空'
                break
            if item.radioButton.isChecked():
                correct_answer = index

        if correct_answer < 0:
            msg_box = '正确答案不能为空'
        if msg_box:
            QMessageBox.information(self, ' ', msg_box, QMessageBox.Yes)
            return

        q = Question()
        q.question = self.textEdit.toPlainText()
        q.correct_answer.append(correct_answer)
        for index, item in enumerate(self.answer_items):
            q.answer_option.append(item.textEdit.toPlainText())

        success = Question.save_question_to_txt_with_tag('question.txt', q)
        if success:
            QMessageBox.information(self, ' ', '添加成功', QMessageBox.Yes)
        else:
            QMessageBox.information(self, ' ', '添加失败', QMessageBox.Yes)

    def get_question_count(self):
        question_count = 0
        with open('question.txt', mode='r') as f:
            while True:
                line = f.readline()
                if not line:
                    break
                if line.startswith('###'):
                    question_count += 1
        return question_count
