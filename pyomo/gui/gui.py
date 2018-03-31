

import sys
from PyQt5 import QtWidgets

class TextLabel(QtWidgets.QLabel):
    def __init__(self, *__args):
        super().__init__(*__args)

class Widget(QtWidgets.QFrame):
    def __init__(self):
        super().__init__()
        self.resize(500, 400)
        self.hbox = QtWidgets.QHBoxLayout(self)
        self.hbox.addWidget()



if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    app.setStyleSheet(open("../css/style.css", "r").read())
    main = Widget()
    main.show()
    sys.exit(app.exec_())