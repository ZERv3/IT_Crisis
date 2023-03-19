from PyQt5 import QtCore, QtGui, QtWidgets
import sqlite3

import bd

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setFixedSize(810, 448)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setGeometry(QtCore.QRect(0, 0, 811, 421))
        self.tabWidget.setObjectName("tabWidget")
        self.tabWidget.setStyleSheet("background-color: rgb(66, 37, 143);")
        font = QtGui.QFont('Raleway')
        font.setPointSize(13)
        font.setBold(True)
        font.setWeight(75)
        self.tabWidget.setFont(font)
        self.Fly_task = QtWidgets.QWidget()
        self.Fly_task.setObjectName("Fly_task")
        self.label = QtWidgets.QLabel(self.Fly_task)
        self.label.setGeometry(QtCore.QRect(0, 0, 800, 400))
        self.label.setText("")
        self.label.setObjectName("label")
        self.label.setStyleSheet("background-image: url(fon_cos.jpg);")
        self.tochki = QtWidgets.QPlainTextEdit(self.Fly_task)
        self.tochki.setGeometry(QtCore.QRect(70, 20, 661, 281))
        self.tochki.setObjectName("tochki")
        self.tochki.setStyleSheet("background-color: rgb(216, 209, 241, 0.7);" "border-radius: 15px;")
        font = QtGui.QFont('Raleway')
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.tochki.setFont(font)
        self.btn = QtWidgets.QPushButton(self.Fly_task)
        self.btn.setGeometry(QtCore.QRect(540, 320, 191, 41))
        self.btn.setObjectName("btn")
        self.btn.setStyleSheet("background-color: rgb(216, 209, 241, 0.7);" "border-radius: 15px;")
        font = QtGui.QFont('Raleway')
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.btn.setFont(font)
        self.btn2 = QtWidgets.QPushButton(self.Fly_task)
        self.btn2.setGeometry(QtCore.QRect(340, 320, 191, 41))
        self.btn2.setObjectName("btn2")
        self.btn2.setStyleSheet("background-color: rgb(216, 209, 241, 0.7);" "border-radius: 15px;")
        font = QtGui.QFont('Raleway')
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.btn2.setFont(font)
        self.tabWidget.addTab(self.Fly_task, "")
        self.Stat = QtWidgets.QWidget()
        self.Stat.setObjectName("Stat")
        self.fon2 = QtWidgets.QLabel(self.Stat)
        self.fon2.setGeometry(QtCore.QRect(0, 0, 800, 400))
        self.fon2.setText("")
        self.fon2.setObjectName("fon2")
        self.fon2.setStyleSheet("background-image: url(fon_cos.jpg);")
        self.rez_stat = QtWidgets.QPlainTextEdit(self.Stat)
        self.rez_stat.setGeometry(QtCore.QRect(70, 10, 661, 361))
        self.rez_stat.setObjectName("rez_stat")
        self.rez_stat.setStyleSheet("background-color: rgb(216, 209, 241, 0.7);" "border-radius: 15px;")
        font = QtGui.QFont('Raleway')
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.rez_stat.setFont(font)
        self.tabWidget.addTab(self.Stat, "")
        MainWindow.setCentralWidget(self.centralwidget)
        # self.menubar = QtWidgets.QMenuBar(MainWindow)
        # self.menubar.setGeometry(QtCore.QRect(0, 0, 810, 21))
        # self.menubar.setObjectName("menubar")
        # MainWindow.setMenuBar(self.menubar)
        # self.statusbar = QtWidgets.QStatusBar(MainWindow)
        # self.statusbar.setObjectName("statusbar")
        # MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        self.btns()


    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "CosmFerm"))
        self.btn.setText(_translate("MainWindow", "Refresh Task"))
        self.btn2.setText(_translate("MainWindow", "Download Task"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.Fly_task), _translate("MainWindow", "Fly Task"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.Stat), _translate("MainWindow", "Stat"))

    def btns(self):
        self.btn2.clicked.connect(lambda: self.basa())
        self.btn.clicked.connect(lambda: self.refresh())

    def basa(self):
        db = sqlite3.connect('predprof.db')
        cursor = db.cursor()
        rows = cursor.execute('''SELECT * FROM polet''').fetchall()
        rows_idnew = []
        for i in rows:
            rows_idnew.append(i)

        print(rows_idnew)


    #def refresh(self):

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
