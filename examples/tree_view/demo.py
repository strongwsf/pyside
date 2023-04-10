# coding:utf-8
import sys
from qtfluentwidgets import TreeWidget, setTheme, Theme, TreeView
from qtpy.QtCore import Qt
from qtpy.QtWidgets import QApplication, QWidget, QTreeWidgetItem, QFileSystemModel, QHBoxLayout


class Demo(QWidget):
    """ 树形控件演示 """

    def __init__(self):
        super().__init__()
        self.hBoxLayout = QHBoxLayout(self)
        self.setStyleSheet("Demo{background:rgb(255,255,255)}")
        # setTheme(Theme.DARK)

        self.view = TreeView(self)
        model = QFileSystemModel()
        model.setRootPath('.')
        self.view.setModel(model)

        self.hBoxLayout.addWidget(self.view)
        self.hBoxLayout.setContentsMargins(30, 30, 30, 30)
        self.resize(700, 600)


if __name__ == '__main__':
    # enable dpi scale
    QApplication.setHighDpiScaleFactorRoundingPolicy(
        Qt.HighDpiScaleFactorRoundingPolicy.PassThrough)
    QApplication.setAttribute(Qt.AA_EnableHighDpiScaling)
    QApplication.setAttribute(Qt.AA_UseHighDpiPixmaps)

    app = QApplication(sys.argv)
    w = Demo()
    w.show()
    sys.exit(app.exec_())
