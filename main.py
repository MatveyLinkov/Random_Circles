import sys
from random import randint

from PyQt5 import QtWidgets, QtCore
from PyQt5.QtGui import QPainter, QColor
from PyQt5.QtWidgets import QApplication, QMainWindow


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(591, 300)
        self.generateButton = QtWidgets.QPushButton(Form)
        self.generateButton.setGeometry(QtCore.QRect(230, 10, 131, 23))
        self.generateButton.setObjectName("generateButton")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Желтые окружности"))
        self.generateButton.setText(_translate("Form", "Генерация окружностей"))


class Circles(QMainWindow, Ui_Form):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.do_paint = False
        self.generateButton.clicked.connect(self.paint)

    def paintEvent(self, event):
        if self.do_paint:
            qp = QPainter()
            qp.begin(self)
            self.draw_circle(qp)
            qp.end()

    def paint(self):
        self.do_paint = True
        self.repaint()

    def draw_circle(self, qp):
        for i in range(3):
            qp.setBrush(QColor(randint(0, 255), randint(0, 255), randint(0, 255)))
            diameter = randint(5, 175)
            qp.drawEllipse(30 + i * 175, 70, diameter, diameter)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Circles()
    ex.show()
    sys.exit(app.exec())