import re


class QuestionType(object):
    SINGLE_CHOICE = 0


class Question(object):
    def __init__(self):
        self.question = ''
        self.answer_option = []
        self.correct_answer = []
        self.question_type = QuestionType.SINGLE_CHOICE

    def correct_answer_to_char(self):
        if len(self.correct_answer) > 0:
            return ','.join([chr(ord('A') + index) for index in self.correct_answer])
        return '()'

    @staticmethod
    def load_question_from_txt(file_name):
        correct_answer_pattern = re.compile('(A-D)')
        question_title_pattern = re.compile('(\d)')
        question_list = []
        question_count = Question.get_question_count(file_name)
        with open(file_name, mode='r') as f:
            for index in range(question_count):
                line = f.readline()
                assert line.startswith('###')
                q = Question()
                q.question = f.readline().strip()
                f.readline()
                print(question_title_pattern.match(line))
                for index in range(4):
                    answer = f.readline()
                    assert answer[0] in 'ABCD'
                    q.answer_option.append(answer[2:].strip())
                print(correct_answer_pattern.match(f.readline()))
                f.readline()
                question_list.append(q)
        return question_list

    @staticmethod
    def save_question_to_txt_with_tag(file_name, question_list):
        question_index = Question.get_question_count(file_name)
        if isinstance(question_list, Question):
            question_list = [question_list]
        with open('question.txt', mode='a+') as f:
            for question in question_list:
                f.write('###{0} 题目({1})：\n'.format(question_index + 1, len(question.answer_option)))
                f.write(question.question + '\n')
                f.write('选项：\n')

                for index, answer in enumerate(question.answer_option):
                    f.write(chr(ord('A') + index) + ': ' + answer + '\n')

                f.write('正确答案：{}\n\n'.format(question.correct_answer_to_char()))
        return True

    @staticmethod
    def save_question_to_txt(fine_name, question_list):
        if isinstance(question_list, Question):
            question_list = [question_list]
        question_count = 1
        with open(fine_name, mode='w+') as f:
            for question in question_list:
                f.write('{}. '.format(question_count) + question.question + '\n')
                question_count += 1
                for index, answer in enumerate(question.answer_option):
                    f.write(chr(ord('A') + index) + ': ' + answer + '\n')
                f.write('\n')
        return True

    @staticmethod
    def get_question_count(file_name):
        question_count = 0
        with open(file_name, mode='r') as f:
            while True:
                line = f.readline()
                if not line:
                    break
                if line.startswith('###'):
                    question_count += 1
        return question_count
