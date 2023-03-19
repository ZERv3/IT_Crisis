from PyQt5 import QtCore, QtGui, QtWidgets
import sqlite3
import requests
import ast
from bs4 import BeautifulSoup as bs

import database


import math

def Velocity(mass, voltage = 80):
    # Единица измерения - светововой год / день
    return 2*(voltage/80)*(200/mass)

def Gen(gen_old, k):
    # Новая популяция
    return gen_old*(k+1)

def Koef(temperature, oxygen):
    # Коеффициент
    return math.sin(-(math.pi / 2) + (math.pi/40)*(temperature + oxygen*0.5))

def Energy(temperature):
    s = 0
    for i in range(temperature):
        s += i
    return s

# Каждый день популяция травы увеличивается в 2 раза
# До тех пор пока не будет достаточно для выгрузки на точку + 8
# Если достаточно то энергия тратится только на реактор (80%)

def statistics(dist, SH_value):
    SH_cur = 8
    dist_cur = 0
    stats = []
    while dist_cur < dist:
        flag = 0
        if SH_cur < (SH_value + 8):
            flag = 1
            SH_cur *= 2
        vel = Velocity(mass = 192 + SH_cur)
        dist_cur += vel
        
        line = ""
        if flag == 0:
            line = "\n\t\tEngine: 80% \n\t\tSH_generation: 0%"
        else:
            line = "\n\t\tEngine: 80% \n\t\tSH_generation: 20%"

        stats.append([SH_cur, round(vel*1000)/1000, line, flag])
    
    return stats

def update(data):
    Fuel = 0
    Oxygen = 0

    days = []    
    for target in data:
        stat = statistics(target[2], target[1])
        for i in stat:
            days.append(i)

    with open('output.txt', 'w') as f:
        for i in range(len(days)):
            line = f"Day {i+1}:\n \tSH: {days[i][0]} units;\n \tVelocity: {days[i][1]} ly/d;\n \tPower: {days[i][2]}\n"
            f.write(line+"\n")
            if days[i][-1] == 0:
                Fuel += 80
            else:
                Fuel += 100
                Oxygen += 38*days[i][0]

        f.write(f"\nFuel: {'{:,}'.format(Fuel)} units ({'{:,}'.format(Fuel*20)}₵)\nOxygen: {'{:,}'.format(Oxygen)} units ({'{:,}'.format(Oxygen*7)}₵)\nTotal: {'{:,}'.format(Fuel*20 + Oxygen)}₵")


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

        rows = database.main()
        #print(rows)
        output_string = '(id, SH, Distance)\n'
        for i in rows:
            output_string += f'{i}\n'
        self.tochki.clear()
        self.tochki.insertPlainText(output_string)

    #def refresh(self):
    def refresh(self):
        
        line = self.tochki.toPlainText()

        with open('data.txt',"w") as f:
            f.write(line)
        
        with open('data.txt', 'r') as f:
            data = []
            data_text = f.readlines()[1:]
            print(data_text)
            for line in data_text:
                q = [int(i) for i in line[1:-2].split(", ")]
                data.append(q)
        
        print(data)
        update(data)

        # 
        self.rez_stat.clear()
        f = open('output.txt', 'r')
        for line in f:
            self.rez_stat.insertPlainText(line)

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
