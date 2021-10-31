# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'interfese_egisso.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(905, 692)
        MainWindow.setStyleSheet("background-color: #f8fafc ;")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(290, 0, 261, 20))
        self.label_7.setStyleSheet("font-size: 15px;\n"
"color: #254d8a;;\n"
"font-weight: 900;\n"
"\n"
"")
        self.label_7.setObjectName("label_7")
        self.label_8 = QtWidgets.QLabel(self.centralwidget)
        self.label_8.setGeometry(QtCore.QRect(290, 240, 251, 20))
        self.label_8.setStyleSheet("font-size: 15px;\n"
"color: #254d8a;\n"
"font-weight: 900;")
        self.label_8.setObjectName("label_8")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(460, 280, 141, 31))
        self.pushButton.setStyleSheet(".QPushButton {\n"
"color: #0f3161;\n"
"background-color: #c0d3ea;\n"
"text-transform: none;\n"
"font-weight: bold;\n"
"text-transform: none;\n"
"font-weight: bold;\n"
"border-radius: 8px;\n"
"}\n"
".QPushButton:hover{\n"
"cursor: pointer;\n"
"color: black;\n"
"background-color: #f5f5f5;\n"
"border: 2px solid #0f3161;\n"
"}\n"
"\n"
"")
        self.pushButton.setObjectName("pushButton")
        self.formLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.formLayoutWidget.setGeometry(QtCore.QRect(0, 40, 431, 181))
        self.formLayoutWidget.setObjectName("formLayoutWidget")
        self.formLayout = QtWidgets.QFormLayout(self.formLayoutWidget)
        self.formLayout.setContentsMargins(0, 0, 0, 0)
        self.formLayout.setObjectName("formLayout")
        self.label = QtWidgets.QLabel(self.formLayoutWidget)
        self.label.setStyleSheet("font-weight: 700;")
        self.label.setObjectName("label")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label)
        self.lineEdit = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.lineEdit.setStyleSheet("")
        self.lineEdit.setObjectName("lineEdit")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.lineEdit)
        self.lineEdit_2 = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.lineEdit_2)
        self.label_2 = QtWidgets.QLabel(self.formLayoutWidget)
        self.label_2.setStyleSheet("font-weight: 700;")
        self.label_2.setObjectName("label_2")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.label_2)
        self.lineEdit_3 = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.lineEdit_3)
        self.label_3 = QtWidgets.QLabel(self.formLayoutWidget)
        self.label_3.setStyleSheet("font-weight: 700;")
        self.label_3.setObjectName("label_3")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.label_3)
        self.lineEdit_4 = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.FieldRole, self.lineEdit_4)
        self.label_4 = QtWidgets.QLabel(self.formLayoutWidget)
        self.label_4.setStyleSheet("font-weight: 700;")
        self.label_4.setObjectName("label_4")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.LabelRole, self.label_4)
        self.label_5 = QtWidgets.QLabel(self.formLayoutWidget)
        self.label_5.setStyleSheet("font-weight: 700;")
        self.label_5.setObjectName("label_5")
        self.formLayout.setWidget(5, QtWidgets.QFormLayout.LabelRole, self.label_5)
        self.lineEdit_5 = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.lineEdit_5.setObjectName("lineEdit_5")
        self.formLayout.setWidget(5, QtWidgets.QFormLayout.FieldRole, self.lineEdit_5)
        self.label_6 = QtWidgets.QLabel(self.formLayoutWidget)
        self.label_6.setStyleSheet("font-weight: 700;")
        self.label_6.setObjectName("label_6")
        self.formLayout.setWidget(6, QtWidgets.QFormLayout.LabelRole, self.label_6)
        self.dateEdit_6 = QtWidgets.QDateEdit(self.formLayoutWidget)
        self.dateEdit_6.setObjectName("dateEdit_6")
        self.formLayout.setWidget(6, QtWidgets.QFormLayout.FieldRole, self.dateEdit_6)
        self.formLayoutWidget_2 = QtWidgets.QWidget(self.centralwidget)
        self.formLayoutWidget_2.setGeometry(QtCore.QRect(0, 290, 431, 181))
        self.formLayoutWidget_2.setObjectName("formLayoutWidget_2")
        self.formLayout_2 = QtWidgets.QFormLayout(self.formLayoutWidget_2)
        self.formLayout_2.setContentsMargins(0, 0, 0, 0)
        self.formLayout_2.setObjectName("formLayout_2")
        self.lineEdit_7 = QtWidgets.QLineEdit(self.formLayoutWidget_2)
        self.lineEdit_7.setObjectName("lineEdit_7")
        self.formLayout_2.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.lineEdit_7)
        self.label_9 = QtWidgets.QLabel(self.formLayoutWidget_2)
        self.label_9.setStyleSheet("font-weight: 700;")
        self.label_9.setObjectName("label_9")
        self.formLayout_2.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_9)
        self.lineEdit_8 = QtWidgets.QLineEdit(self.formLayoutWidget_2)
        self.lineEdit_8.setObjectName("lineEdit_8")
        self.formLayout_2.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.lineEdit_8)
        self.label_10 = QtWidgets.QLabel(self.formLayoutWidget_2)
        self.label_10.setStyleSheet("font-weight: 700;")
        self.label_10.setObjectName("label_10")
        self.formLayout_2.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.label_10)
        self.lineEdit_9 = QtWidgets.QLineEdit(self.formLayoutWidget_2)
        self.lineEdit_9.setObjectName("lineEdit_9")
        self.formLayout_2.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.lineEdit_9)
        self.label_11 = QtWidgets.QLabel(self.formLayoutWidget_2)
        self.label_11.setStyleSheet("font-weight: 700;")
        self.label_11.setObjectName("label_11")
        self.formLayout_2.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.label_11)
        self.lineEdit_10 = QtWidgets.QLineEdit(self.formLayoutWidget_2)
        self.lineEdit_10.setObjectName("lineEdit_10")
        self.formLayout_2.setWidget(4, QtWidgets.QFormLayout.FieldRole, self.lineEdit_10)
        self.label_12 = QtWidgets.QLabel(self.formLayoutWidget_2)
        self.label_12.setStyleSheet("font-weight: 700;")
        self.label_12.setObjectName("label_12")
        self.formLayout_2.setWidget(4, QtWidgets.QFormLayout.LabelRole, self.label_12)
        self.lineEdit_11 = QtWidgets.QLineEdit(self.formLayoutWidget_2)
        self.lineEdit_11.setObjectName("lineEdit_11")
        self.formLayout_2.setWidget(5, QtWidgets.QFormLayout.FieldRole, self.lineEdit_11)
        self.label_13 = QtWidgets.QLabel(self.formLayoutWidget_2)
        self.label_13.setStyleSheet("font-weight: 700;")
        self.label_13.setObjectName("label_13")
        self.formLayout_2.setWidget(5, QtWidgets.QFormLayout.LabelRole, self.label_13)
        self.label_14 = QtWidgets.QLabel(self.formLayoutWidget_2)
        self.label_14.setStyleSheet("font-weight: 700;")
        self.label_14.setObjectName("label_14")
        self.formLayout_2.setWidget(6, QtWidgets.QFormLayout.LabelRole, self.label_14)
        self.dateEdit_7 = QtWidgets.QDateEdit(self.formLayoutWidget_2)
        self.dateEdit_7.setObjectName("dateEdit_7")
        self.formLayout_2.setWidget(6, QtWidgets.QFormLayout.FieldRole, self.dateEdit_7)
        self.splitter = QtWidgets.QSplitter(self.centralwidget)
        self.splitter.setGeometry(QtCore.QRect(450, 40, 322, 79))
        self.splitter.setOrientation(QtCore.Qt.Vertical)
        self.splitter.setObjectName("splitter")
        self.layoutWidget = QtWidgets.QWidget(self.splitter)
        self.layoutWidget.setObjectName("layoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.layoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label_16 = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_16.setFont(font)
        self.label_16.setObjectName("label_16")
        self.horizontalLayout.addWidget(self.label_16)
        self.dateEdit_5 = QtWidgets.QDateEdit(self.layoutWidget)
        self.dateEdit_5.setObjectName("dateEdit_5")
        self.horizontalLayout.addWidget(self.dateEdit_5)
        self.label_15 = QtWidgets.QLabel(self.splitter)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_15.setFont(font)
        self.label_15.setObjectName("label_15")
        self.layoutWidget1 = QtWidgets.QWidget(self.splitter)
        self.layoutWidget1.setObjectName("layoutWidget1")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.layoutWidget1)
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label_17 = QtWidgets.QLabel(self.layoutWidget1)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_17.setFont(font)
        self.label_17.setObjectName("label_17")
        self.horizontalLayout_3.addWidget(self.label_17)
        self.dateEdit_3 = QtWidgets.QDateEdit(self.layoutWidget1)
        self.dateEdit_3.setObjectName("dateEdit_3")
        self.horizontalLayout_3.addWidget(self.dateEdit_3)
        self.label_18 = QtWidgets.QLabel(self.layoutWidget1)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_18.setFont(font)
        self.label_18.setObjectName("label_18")
        self.horizontalLayout_3.addWidget(self.label_18)
        self.dateEdit_4 = QtWidgets.QDateEdit(self.layoutWidget1)
        self.dateEdit_4.setObjectName("dateEdit_4")
        self.horizontalLayout_3.addWidget(self.dateEdit_4)
        self.layoutWidget2 = QtWidgets.QWidget(self.splitter)
        self.layoutWidget2.setObjectName("layoutWidget2")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.layoutWidget2)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_19 = QtWidgets.QLabel(self.layoutWidget2)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_19.setFont(font)
        self.label_19.setObjectName("label_19")
        self.horizontalLayout_2.addWidget(self.label_19)
        self.lineEdit_16 = QtWidgets.QLineEdit(self.layoutWidget2)
        self.lineEdit_16.setObjectName("lineEdit_16")
        self.horizontalLayout_2.addWidget(self.lineEdit_16)
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(670, 340, 161, 31))
        self.pushButton_2.setStyleSheet(".QPushButton {\n"
"color: #0f3161;\n"
"background-color: #c0d3ea;\n"
"text-transform: none;\n"
"font-weight: bold;\n"
"text-transform: none;\n"
"font-weight: bold;\n"
"border-radius: 8px;\n"
"}\n"
".QPushButton:hover{\n"
"cursor: pointer;\n"
"color: black;\n"
"background-color: #f5f5f5;\n"
"border: 2px solid #0f3161;\n"
"}")
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setGeometry(QtCore.QRect(460, 340, 141, 31))
        self.pushButton_3.setStyleSheet(".QPushButton {\n"
"color: #0f3161;\n"
"background-color: #c0d3ea;\n"
"text-transform: none;\n"
"font-weight: bold;\n"
"text-transform: none;\n"
"font-weight: bold;\n"
"border-radius: 8px;\n"
"}\n"
".QPushButton:hover{\n"
"cursor: pointer;\n"
"color: black;\n"
"background-color: #f5f5f5;\n"
"border: 2px solid #0f3161;\n"
"}")
        self.pushButton_3.setObjectName("pushButton_3")
        self.progressBar = QtWidgets.QProgressBar(self.centralwidget)
        self.progressBar.setGeometry(QtCore.QRect(450, 440, 421, 23))
        self.progressBar.setProperty("value", 24)
        self.progressBar.setObjectName("progressBar")
        self.pushButton_4 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_4.setGeometry(QtCore.QRect(670, 280, 161, 31))
        self.pushButton_4.setStyleSheet(".QPushButton {\n"
"color: #0f3161;\n"
"background-color: #c0d3ea;\n"
"text-transform: none;\n"
"font-weight: bold;\n"
"text-transform: none;\n"
"font-weight: bold;\n"
"border-radius: 8px;\n"
"}\n"
".QPushButton:hover{\n"
"cursor: pointer;\n"
"color: black;\n"
"background-color: #f5f5f5;\n"
"border: 2px solid #0f3161;\n"
"}")
        self.pushButton_4.setObjectName("pushButton_4")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.action = QtWidgets.QAction(MainWindow)
        self.action.setObjectName("action")

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label_7.setText(_translate("MainWindow", "Персональные данные родителя"))
        self.label_8.setText(_translate("MainWindow", "Персональные данные ребенка"))
        self.pushButton.setText(_translate("MainWindow", "Загрузить в БД ЕГИССО"))
        self.label.setText(_translate("MainWindow", "Введите СНИЛС родителя"))
        self.label_2.setText(_translate("MainWindow", "Введите фамилию родителя"))
        self.label_3.setText(_translate("MainWindow", "Введите имя  родителя"))
        self.label_4.setText(_translate("MainWindow", "Введите отчество  родителя"))
        self.label_5.setText(_translate("MainWindow", "Укажите пол родителя"))
        self.label_6.setText(_translate("MainWindow", "Укажите дату рождения родителя"))
        self.label_9.setText(_translate("MainWindow", "Введите СНИЛС ребенка"))
        self.label_10.setText(_translate("MainWindow", "Введите фамилию ребенка"))
        self.label_11.setText(_translate("MainWindow", "Введите имя  ребенка"))
        self.label_12.setText(_translate("MainWindow", "Введите отчество  ребенка"))
        self.label_13.setText(_translate("MainWindow", "Укажите пол ребенка"))
        self.label_14.setText(_translate("MainWindow", "Укажите дату рождения ребенка"))
        self.label_16.setText(_translate("MainWindow", "Введите дату назначения МСЗ"))
        self.label_15.setText(_translate("MainWindow", " Период действия МСЗ"))
        self.label_17.setText(_translate("MainWindow", "С"))
        self.label_18.setText(_translate("MainWindow", "ПО"))
        self.label_19.setText(_translate("MainWindow", "Укажите сумму МСЗ"))
        self.pushButton_2.setText(_translate("MainWindow", "Выгрузить в CSV всю БД"))
        self.pushButton_3.setText(_translate("MainWindow", "Экспорт из CSV в БД"))
        self.pushButton_4.setText(_translate("MainWindow", "Отчистить БД"))
        self.action.setText(_translate("MainWindow", "Настройки БД"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
