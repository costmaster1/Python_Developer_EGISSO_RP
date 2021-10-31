# Подключаем библиотеку sqlite3
import sqlite3
# Подключаем наш интерфейс программы
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox
from interfese_egisso import Ui_MainWindow  # импорт нашего сгенерированного файла
import sys
# подключаем модуль csv
import csv
import glob
import os

# Обьявляем класс bd_egisso для работы с базой данных
class bd_egisso:
    # Обьявляем метод bd создания БД egisso и таблици fact
    def bd(self):
        con = sqlite3.connect('egisso_db_Kompensaciya_RP')
        # Создаем обьект курсор
        cur = con.cursor()
        # Создаем таблицу fact если ее не существует
        cur.execute('CREATE TABLE if not exists fact(RecType text, LMSZID text, categoryID text, ONMSZCode text, SNILS_recip text, FamilyName_recip text, Name_recip text, Patronymic_recip text, Gender_recip text, BirthDate_recip text, doctype_recip text, doc_Series_recip text, doc_Number_recip text, doc_IssueDate_recip text, doc_Issuer_recip text, SNILS_reason text, FamilyName_reason text, Name_reason text, Patronymic_reason text, Gender_reason text, BirthDate_reason text, doctype_reason text, doc_Series_reason text, doc_Number_reason text, doc_IssueDate_reason text, doc_Issuer_reason text, decision_date text, dateStart text, dateFinish text, usingSign text, criteria text, FormCode text, amount text, measuryCode text, monetization text, content text, comment text, equivalentAmount text)')
        # Создаем таблицу Reason если ее не существует
        cur.execute('CREATE TABLE if not exists Reason(RecType text, LMSZID text, categoryID text, ONMSZCode text, SNILS_recip text, FamilyName_recip text, Name_recip text, Patronymic_recip text, Gender_recip text, BirthDate_recip text, doctype_recip text, doc_Series_recip text, doc_Number_recip text, doc_IssueDate_recip text, doc_Issuer_recip text, SNILS_reason text, FamilyName_reason text, Name_reason text, Patronymic_reason text, Gender_reason text, BirthDate_reason text, doctype_reason text, doc_Series_reason text, doc_Number_reason text, doc_IssueDate_reason text, doc_Issuer_reason text, decision_date text, dateStart text, dateFinish text, usingSign text, criteria text, FormCode text, amount text, measuryCode text, monetization text, content text, comment text, equivalentAmount text)')

    # Обьявляем метод tabal_import для занесения данных в БД ЕГИССО
    def tabal_import(self):
      con = sqlite3.connect('egisso_db_Kompensaciya_RP')
      # Создаем обьект курсор
      cur = con.cursor()
      # Cоздаем стек из данных для таблици fact
      lineEdit = ui.lineEdit.text()
      lineEdit_2 = ui.lineEdit_2.text()
      lineEdit_3 = ui.lineEdit_3.text()
      lineEdit_4 = ui.lineEdit_4.text()
      lineEdit_5 = ui.lineEdit_5.text()
      dateEdit_6 = ui.dateEdit_6.text()
      lineEdit_7 = ui.lineEdit_7.text()
      lineEdit_8 = ui.lineEdit_8.text()
      lineEdit_9 = ui.lineEdit_9.text()
      lineEdit_10 = ui.lineEdit_10.text()
      lineEdit_11 = ui.lineEdit_11.text()
      dateEdit_12 = ui.dateEdit_7.text()
      dateEdit_13 = ui.dateEdit_5.text()
      dateEdit_14 = ui.dateEdit_3.text()
      dateEdit_15 = ui.dateEdit_4.text()
      lineEdit_16 = ui.lineEdit_16.text()

      stek_fact = ["Fact",
              "c1dd4851-19ad-4e2e-aafb-d1ce65286801",
              "20030916-1e10-44a0-9c0f-e041777a1941",
              "6706.000000",
              lineEdit,
              lineEdit_2,
              lineEdit_3,
              lineEdit_4,
              lineEdit_5,
              dateEdit_6,
              "",
              "",
              "",
              "",
              "",
              "",
              "",
              "",
              "",
              "",
              "",
              "",
              "",
              "",
              "",
              "",
              dateEdit_13,
              dateEdit_14,
              dateEdit_15,
              "Да",
              "",
              "01",
              lineEdit_16,
              "01",
              "",
              "",
              "",
              ""]
      # Cоздаем стек из данных для таблици Reason
      stek_Reason = ["Reason",
                     "",
                     "",
                     "",
                     "",
                     "",
                     "",
                     "",
                     "",
                     "",
                     "",
                     "",
                     "",
                     "",
                     "",
                     lineEdit_7,
                     lineEdit_8,
                     lineEdit_9,
                     lineEdit_10,
                     lineEdit_11,
                     dateEdit_12,
                     "",
                     "",
                     "",
                     "",
                     "",
                     "",
                     "",
                     "",
                     "",
                     "",
                     "",
                     "",
                     "",
                     "",
                     "",
                     "",
                     ""]
      # Заносим данные в таблицу fact
      cur.execute("""INSERT INTO fact VALUES(?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)""",stek_fact)
      # Заносим данные в таблицу Reason
      cur.execute( """INSERT INTO fact VALUES(?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)""",stek_Reason)
      # Сохраняе изменения в БД ЕГИССО
      con.commit()

    # Обьявляем метод export_bd для выгрузки данных в csv
    def export_bd(self):
        con = sqlite3.connect('egisso_db_Kompensaciya_RP')
        # Создаем обьект курсор
        cur = con.cursor()
        fact = cur.execute("SELECT * FROM fact")
        # Записываем данные в CSV файл
        with open("export-bd/egisso_db_Kompensaciya_RP.csv", 'w', newline='') as csvfile:
            writer = csv.writer(csvfile, delimiter=';')
            writer.writerows([["RecType", "LMSZID", "categoryID", "ONMSZCode", "SNILS_recip", "FamilyName_recip", "Name_recip", "Patronymic_recip", "Gender_recip", "BirthDate_recip", "doctype_recip", "doc_Series_recip", "doc_Number_recip", "doc_IssueDate_recip", "doc_Issuer_recip", "SNILS_reason", "FamilyName_reason", "Name_reason", "Patronymic_reason", "Gender_reason", "BirthDate_reason", "doctype_reason", "doc_Series_reason", "doc_Number_reason", "doc_IssueDate_reason", "doc_Issuer_reason", "decision_date", "dateStart", "dateFinish", "usingSign", "criteria", "FormCode", "amount", "measuryCode", "monetization", "content", "comment", "equivalentAmount"]])
            writer.writerows(fact)
        print("Данные успешно выгружены в csv файл !")

        msg = QMessageBox()
        msg.setIcon(QMessageBox.Information)
        # msg.setIconPixmap(pixmap)  # Своя картинка

        msg.setWindowTitle("Информация")
        msg.setText("Данные успешно выгружены в csv файл !")

        okButton = msg.addButton('Окей', QMessageBox.AcceptRole)
        msg.addButton('Отмена', QMessageBox.RejectRole)

        msg.exec()
        if msg.clickedButton() == okButton:
            print("Yes")
        else:
            print("No")




    # Обьявляем метод import_csv_bd для занесения данных из CSV файла в БД ЕГИССО
    def import_csv_bd(self):
        # Читаем данные из CSV файла
        with open("import-bd/test.csv", newline='') as csvfile:
            reader = csv.DictReader(csvfile, delimiter=';')
            for row in reader:
                # Создаем стек из прочитанных данных
                test = (row['RecType'], row['LMSZID'], row['categoryID'], row['ONMSZCode'], row['SNILS_recip'],
                        row['FamilyName_recip'], row['Name_recip'], row['Patronymic_recip'], row['Gender_recip'],
                        row['BirthDate_recip'], row['doctype_recip'], row['doc_Series_recip'], row['doc_Number_recip'],
                        row['doc_IssueDate_recip'], row['doc_Issuer_recip'], row['SNILS_reason'],
                        row['FamilyName_reason'], row['Name_reason'], row['Patronymic_reason'], row['Gender_reason'],
                        row['BirthDate_reason'], row['doctype_reason'], row['doc_Series_reason'],
                        row['doc_Number_reason'], row['doc_IssueDate_reason'], row['doc_Issuer_reason'],
                        row['decision_date'], row['dateStart'], row['dateFinish'], row['usingSign'], row['criteria'],
                        row['FormCode'], row['amount'], row['measuryCode'], row['monetization'], row['content'],
                        row['comment'], row['equivalentAmount'])
                # Подключаемся к БД ЕГИССО
                con = sqlite3.connect('egisso_db_Kompensaciya_RP')
                # Создаем обьект курсор
                cur = con.cursor()
                # Заносим данные в таблицу fact
                cur.execute("""INSERT INTO fact VALUES(?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)""",test)
                # Обновляем данные в таблице fact
                cur.execute("""UPDATE fact SET LMSZID='c1dd4851-19ad-4e2e-aafb-d1ce65286801',
                categoryID='20030916-1e10-44a0-9c0f-e041777a1941',
                ONMSZCode='6706.000000', doctype_recip='',
                doc_Series_recip='', doc_Number_recip='', doc_IssueDate_recip='',
                doc_Issuer_recip='', doctype_reason='', doc_Series_reason='',
                doc_Number_reason='', doc_IssueDate_reason='', doc_Issuer_reason='',
                usingSign='Да', criteria='', FormCode='01', measuryCode='01', monetization='',
                content='', comment='', equivalentAmount='' WHERE RecType LIKE 'Fact'""")

                cur.execute("""UPDATE fact SET LMSZID='', categoryID='',ONMSZCode='', doctype_recip='',doc_Series_recip='', doc_Number_recip='', doc_IssueDate_recip='',doc_Issuer_recip='', doctype_reason='', doc_Series_reason='',doc_Number_reason='', doc_IssueDate_reason='', doc_Issuer_reason='',usingSign='', criteria='', FormCode='', measuryCode='', monetization='',content='', comment='', equivalentAmount='' WHERE RecType LIKE 'Reason'""")
                print('Строки таблици fact успешно обновлены !!! ')

                # Сохраняе изменения в БД ЕГИССО
                con.commit()

    # Обьяивляем метод delete_bd для удаления всех записей из таблици fact
    def delete_bd(self):
        # Подключаемся к БД ЕГИССО
        con = sqlite3.connect('egisso_db_Kompensaciya_RP')
        # Создаем обьект курсор
        cur = con.cursor()
        # Удаляем все записи из таблици fact
        cur.execute("""DELETE FROM fact""")
        # Сохраняе изменения в БД ЕГИССО
        con.commit()








# Создаем объект класса bd_egisso под названием method_bd
method_bd = bd_egisso()

# Вызываем метод bd класса bd_egisso при помощи обьекта класса method_bd
method_bd.bd()
# Выводим уведомление в cmd о создании БД ЕГИССО с таблицами fact и Rеason
print('БД ЕГИССО с таблицей fact and Reason успешно созданы !')


app = QtWidgets.QApplication(sys.argv)
MainWindow = QtWidgets.QMainWindow()
ui = Ui_MainWindow()
ui.setupUi(MainWindow)

# Вызываем метод tabal_import класса bd_egisso при помощи обьекта класса method_bd через функцию tabal_import
def tabal_import():
    # Вызываем метод bd.tabal_import()
    method_bd.tabal_import()
    # Отчищаем виджиты lineEdit от текста
    ui.lineEdit.setText("")
    ui.lineEdit_2.setText("")
    ui.lineEdit_3.setText("")
    ui.lineEdit_4.setText("")
    ui.lineEdit_5.setText("")
    ui.lineEdit_7.setText("")
    ui.lineEdit_8.setText("")
    ui.lineEdit_9.setText("")
    ui.lineEdit_10.setText("")
    ui.lineEdit_11.setText("")
    ui.lineEdit_16.setText("")

    # Выводим уведомление в cmd об успешном занесении данных в таблицу fact БД ЕГИССО
    print('Данные в таблицу fact и Reason БД ЕГИССО успешно занесены !')

    msg = QMessageBox()
    msg.setIcon(QMessageBox.Information)
    # msg.setIconPixmap(pixmap)  # Своя картинка

    msg.setWindowTitle("Информация")
    msg.setText("Данные в таблицу fact и Reason БД ЕГИССО успешно занесены !")

    okButton = msg.addButton('Окей', QMessageBox.AcceptRole)
    msg.addButton('Отмена', QMessageBox.RejectRole)

    msg.exec()
    if msg.clickedButton() == okButton:
        print("Yes")
    else:
        print("No")



# Вызываем метод export_bd класса bd_egisso при помощи обьекта класса method_bd через функцию export_bd _post
def export_bd_post():
    method_bd.export_bd()



# Вызываем метод import_csv_bd класса bd_egisso при помощи обьекта класса method_bd через функцию import_csv_bd_post
def import_csv_bd_post():
    method_bd.import_csv_bd()
    print('Данные успешно прочитанны из файла CSV и занесены в БД ЕГИССО !')

    msg = QMessageBox()
    msg.setIcon(QMessageBox.Information)
    # msg.setIconPixmap(pixmap)  # Своя картинка

    msg.setWindowTitle("Информация")
    msg.setText("Данные успешно прочитанны из файла CSV и занесены в БД ЕГИССО !")

    okButton = msg.addButton('Окей', QMessageBox.AcceptRole)
    msg.addButton('Отмена', QMessageBox.RejectRole)

    msg.exec()
    if msg.clickedButton() == okButton:
        print("Yes")
    else:
        print("No")


# Вызываем метод delete_bd класса bd_egisso при помощи обьекта класса method_bd через функцию delete_bd_post
def delete_bd_post():
    method_bd.delete_bd()
    print('Все данные успешно удалены из таблици fact БД ЕГИССО !')
    msg = QMessageBox()
    msg.setIcon(QMessageBox.Information)
    # msg.setIconPixmap(pixmap)  # Своя картинка

    msg.setWindowTitle("Информация")
    msg.setText("Все данные успешно удалены из таблици fact БД ЕГИССО !")

    okButton = msg.addButton('Окей', QMessageBox.AcceptRole)
    msg.addButton('Отмена', QMessageBox.RejectRole)

    msg.exec()
    if msg.clickedButton() == okButton:
        print("Yes")
    else:
        print("No")










# Подключам кнопку pushButton к слоту tabal_import
ui.pushButton.clicked.connect(tabal_import)
# Подключам кнопку pushButton_2 к слоту export_bd_post
ui.pushButton_2.clicked.connect(export_bd_post)
# Подключам кнопку pushButton_3 к слоту redactor_bd_post
ui.pushButton_3.clicked.connect(import_csv_bd_post)
# Подключам кнопку pushButton_4 к слоту delete_bd_post
ui.pushButton_4.clicked.connect(delete_bd_post)





MainWindow.show()
sys.exit(app.exec_())












