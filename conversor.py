from PyQt5 import QtCore, QtWidgets, QtGui
from untitled import Ui_MainWindow


class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.setupUi(self)

        self.btn2.clicked.connect(self._clear)
        self.btn3.clicked.connect(self.close)
        self.btn1.clicked.connect(self.calcmts)

    def validar(self):
        self.valor1.setValidator(self.validator)


    def _clear(self):
        self.valor1.clear()
        self.valor2.clear()

    def calcmts(self):
        conversion = float(self.valor1.text()) * 3.6
        self.valor2.setText(str(conversion))


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    MainWindow = MainWindow()
    MainWindow.show()
    sys.exit(app.exec_())
