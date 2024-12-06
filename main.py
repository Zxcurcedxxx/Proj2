# main.py
import sys
from PyQt6.QtWidgets import QApplication, QWidget
from PyQt6.QtCore import Qt, QTimer
from PyQt6.QtGui import QPainter, QColor, QPen
from PyQt6.uic import loadUi

class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        loadUi("UI.ui", self)
        self.button.clicked.connect(self.create_circles)
        self.circles = []
        self.timer = QTimer()
        self.timer.timeout.connect(self.update)
        self.timer.start(10)

    def create_circles(self):
        self.circles.append((self.width() / 2, self.height() / 2, 50 + int(self.width() / 20)))

    def paintEvent(self, event):
        super().paintEvent(event)
        painter = QPainter(self)
        painter.setPen(QPen(QColor(255, 255, 0), 2))
        for x, y, r in self.circles:
            painter.drawEllipse(x - r, y - r, 2 * r, 2 * r)

    def update(self):
        self.update()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
