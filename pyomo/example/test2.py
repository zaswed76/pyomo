# -*- coding: utf-8 -*

import sys
from PyQt5 import QtWidgets
class Widget(QtWidgets.QLabel):
    def __init__(self):

        super().__init__()
        self.resize(500, 500)
        self.setText('корова')

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    # app.setStyleSheet(open('./etc/{0}.qss'.format('style'), "r").read())
    main = Widget()
    main.show()
    sys.exit(app.exec_())

