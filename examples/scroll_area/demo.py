# coding:utf-8
import sys
from qtfluentwidgets import SmoothScrollArea, PixmapLabel
from qtpy.QtCore import QEasingCurve, Qt
from qtpy.QtGui import QPixmap
from qtpy.QtWidgets import QApplication



class Demo(SmoothScrollArea):

    def __init__(self):
        super().__init__()
        self.label = PixmapLabel(self)
        self.label.setPixmap(QPixmap("resource/shoko.jpg"))

        # customize scroll animation
        self.setScrollAnimation(Qt.Vertical, 400, QEasingCurve.OutQuint)
        self.setScrollAnimation(Qt.Horizontal, 400, QEasingCurve.OutQuint)

        self.horizontalScrollBar().setValue(1900)
        self.setWidget(self.label)
        self.resize(1200, 800)

        with open('resource/demo.qss', encoding='utf-8') as f:
            self.setStyleSheet(f.read())


if __name__ == '__main__':
    app = QApplication(sys.argv)
    w = Demo()
    w.show()
    app.exec_()