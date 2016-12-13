# -*- coding: utf-8 -*-

import sys
from PyQt5 import QtWidgets, QtCore
from pyomo import paths

class Main(QtWidgets.QMainWindow):
    def __init__(self, flags, *args, **kwargs):

        super().__init__(flags, *args, **kwargs)
        self.resize(500, 500)
        self.central_widget = QtWidgets.QFrame()
        self.setCentralWidget(self.central_widget)


if __name__ == '__main__':
    style_name = 'style.css'
    app = QtWidgets.QApplication(sys.argv)
    app.setStyleSheet(open(paths.css_file(style_name), "r").read())
    main = Main(None, (QtCore.Qt.Window))
    main.show()
    sys.exit(app.exec_())