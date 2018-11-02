'''
PyQt GUI version of the Permutation Generator
'''

from itertools import permutations

from PyQt5.QtWidgets import (QFrame, QLineEdit, QTextEdit, QVBoxLayout,
                             QApplication, QGridLayout, QPushButton, QCheckBox)
from PyQt5.QtGui import QIcon


class PermutationApp(QFrame):
    def __init__(self):
        super().__init__()
        self.setWindowIcon(QIcon("Permutation 3D.ico"))
        self.setWindowTitle("Permutation Generator")
        self.CreateApp()

    def CreateApp(self):
        self.input_layout = QGridLayout()

        self.word1 = QLineEdit()
        self.word2 = QLineEdit()
        self.word3 = QLineEdit()
        self.word4 = QLineEdit()
        self.word5 = QLineEdit()
        self.word6 = QLineEdit()
        self.go = QPushButton("Permutate")
        self.numb = QCheckBox("Numbered")
        self.outputBox = QTextEdit("Enter up to six words in the fields above and click to generate their permutations.")

        self.go.clicked.connect(self.GetPerm)

        self.input_layout.addWidget(self.word1, 0, 0)
        self.input_layout.addWidget(self.word2, 0, 1)
        self.input_layout.addWidget(self.word3, 1, 0)
        self.input_layout.addWidget(self.word4, 1, 1)
        self.input_layout.addWidget(self.word5, 2, 0)
        self.input_layout.addWidget(self.word6, 2, 1)
        self.input_layout.addWidget(self.go, 3, 0)
        self.input_layout.addWidget(self.numb, 3, 1)

        self.mainLayout = QVBoxLayout()

        self.mainLayout.addLayout(self.input_layout)
        self.mainLayout.addWidget(self.outputBox)

        self.setLayout(self.mainLayout)


    def GetPerm(self):
        words = []

        boxes = [self.word1.text(), self.word2.text(), self.word3.text(),
                 self.word4.text(), self.word5.text(), self.word6.text()]

        for content in boxes:
            if content != "":
                words.append(content)


        self.outputBox.setText("")
        i = 1

        if self.numb.isChecked() == True:
            for word in permutations(words):
                self.outputBox.append(str(i) + ". " + " ".join(word))
                i += 1

        else:
            for word in permutations(words):
                self.outputBox.append(" ".join(word))



if __name__ == "__main__":
    import sys

    app = QApplication(sys.argv)

    window = PermutationApp()
    window.show()

    sys.exit(app.exec_())



