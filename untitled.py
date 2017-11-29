# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'untitled.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(400, 200)
        MainWindow.setMinimumSize(QtCore.QSize(400, 200))
        MainWindow.setMaximumSize(QtCore.QSize(400, 200))
        font = QtGui.QFont()
        font.setBold(False)
        font.setItalic(False)
        font.setUnderline(False)
        font.setWeight(50)
        font.setStrikeOut(False)
        MainWindow.setFont(font)
        MainWindow.setMouseTracking(False)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("icon.ico"), QtGui.QIcon.Normal, QtGui.QIcon.On)
        MainWindow.setWindowIcon(icon)
        MainWindow.setIconSize(QtCore.QSize(25, 25))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(350, 180, 41, 20))
        self.label_3.setObjectName("label_3")
        self.widget = QtWidgets.QWidget(self.centralwidget)
        self.widget.setGeometry(QtCore.QRect(60, 80, 297, 63))
        self.widget.setObjectName("widget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.widget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.valor1 = QtWidgets.QLineEdit(self.widget)
        self.valor1.setObjectName("valor1")
        self.horizontalLayout_2.addWidget(self.valor1)
        self.valor2 = QtWidgets.QLineEdit(self.widget)
        self.valor2.setObjectName("valor2")
        self.horizontalLayout_2.addWidget(self.valor2)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.btn1 = QtWidgets.QPushButton(self.widget)
        self.btn1.setObjectName("btn1")
        self.horizontalLayout.addWidget(self.btn1)
        self.btn2 = QtWidgets.QPushButton(self.widget)
        self.btn2.setObjectName("btn2")
        self.horizontalLayout.addWidget(self.btn2)
        self.btn3 = QtWidgets.QPushButton(self.widget)
        self.btn3.setObjectName("btn3")
        self.horizontalLayout.addWidget(self.btn3)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.widget1 = QtWidgets.QWidget(self.centralwidget)
        self.widget1.setGeometry(QtCore.QRect(61, 51, 291, 23))
        self.widget1.setObjectName("widget1")
        self.gridLayout = QtWidgets.QGridLayout(self.widget1)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.label = QtWidgets.QLabel(self.widget1)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.widget1)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 0, 1, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Conversor"))
        self.label_3.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\">V 1.0</p></body></html>"))
        self.btn1.setText(_translate("MainWindow", "calcular"))
        self.btn2.setText(_translate("MainWindow", "limpiar"))
        self.btn3.setText(_translate("MainWindow", "salir"))
        self.label.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:10pt; font-weight:600;\">Mts * Seg</span></p></body></html>"))
        self.label_2.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:10pt; font-weight:600;\">Km*H</span></p></body></html>"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

