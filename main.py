import sys

from random import choice

from PyQt5.QtCore import QPoint
from PyQt5.QtGui import QPainter, QColor
from PyQt5.QtWidgets import QWidget, QApplication, QPushButton


class Example(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.a, self.b, self.c = choice(range(255)), choice(range(255)), choice(range(255))
        self.setGeometry(300, 300, 500, 500)
        self.setWindowTitle('Рисование')
        self.btn = QPushButton('Рисовать', self)
        self.btn.move(200, 400)
        self.do_paint = False
        self.btn.clicked.connect(self.paint)

    def paintEvent(self, event):
        if self.do_paint:
            qp = QPainter()
            qp.begin(self)
            self.draw_flag(qp)

            qp.end()

    def paint(self):
        self.do_paint = True
        self.a, self.b, self.c = choice(range(255)), choice(range(255)), choice(range(255))
        self.btn.setStyleSheet(
            f'background: rgb({self.a}, {self.b}, {self.c})')
        self.repaint()

    def draw_flag(self, qp):
        r = choice(range(100))
        x, y = choice(range(400)), choice(range(400))
        qp.setBrush(QColor(self.a, self.b, self.c))
        qp.drawEllipse(x, y, r, r)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    ex.show()
    sys.exit(app.exec())
