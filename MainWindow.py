import sys

from PyQt5.QtCore import QSize
from PyQt5.QtWidgets import QApplication, QMainWindow, QListWidgetItem, QMessageBox

from AddQuestionDialog import AddQuestionDialog
from QuestionItem import QQuestionItem
from Question import Question
from UI.Ui_MainWindow import Ui_MainWindow


class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        self.setupUi(self)
        self.init_ui()
        self.load_question_from_txt()
        self.paper_question_list = []

    def init_ui(self):
        #设置窗口属性
        self.setWindowTitle('组卷系统')
        self.init_menu_action()
        self.SavePaperToWord.clicked.connect(self.save_paper_to_word)
        self.SavePaperToTXT.clicked.connect(self.save_paper_to_txt)

    def init_menu_action(self):
        self.add_question_action.triggered.connect(self.on_trigger_add_question_action)
        self.import_from_word_action.triggered.connect(self.on_trigger_import_from_word_action)

    def on_trigger_add_question_action(self):
        self.w = AddQuestionDialog()
        self.w.show()

    def on_trigger_import_from_word_action(self):
        pass

    def load_question_from_txt(self):
        question_list = Question.load_question_from_txt('question.txt')
        for question in question_list:
            item = QListWidgetItem()
            item.setSizeHint(QSize(400, 370))
            self.listWidget.addItem(item)
            question_item = QQuestionItem(question, add_cb=self.on_add_question_to_paper)
            self.listWidget.setItemWidget(item, question_item)

    def load_question_from_word(self):
        pass

    def add_one_question_to_paper(self, question):
        item = QListWidgetItem()
        item.setSizeHint(QSize(400, 370))
        self.listWidget_2.addItem(item)
        question_item = QQuestionItem(question, delete_cb=self.on_delete_question_from_paper)
        self.listWidget_2.setItemWidget(item, question_item)

    def on_add_question_to_paper(self, question):
        self.add_one_question_to_paper(question)
        self.paper_question_list.append(question)

    def update_paper_question_list(self):
        self.listWidget_2.clear()
        for question in self.paper_question_list:
            self.add_one_question_to_paper(question)

    def on_delete_question_from_paper(self, question):
        self.paper_question_list.remove(question)
        self.update_paper_question_list()

    def save_paper_to_word(self):
        for question in self.paper_question_list:
            pass

    def save_paper_to_txt(self):
        Question.save_question_to_txt('paper.txt', self.paper_question_list)
        QMessageBox.information(self, ' ', '添加成功', QMessageBox.Yes)


if __name__ == '__main__':
    app = QApplication(sys.argv[1:])

    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
