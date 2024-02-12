# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'conversor.ui'
##
## Created by: Qt User Interface Compiler version 6.6.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QComboBox, QFrame, QHBoxLayout,
    QLabel, QLineEdit, QMainWindow, QPlainTextEdit,
    QPushButton, QSizePolicy, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.horizontalLayout = QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.main_container = QFrame(self.centralwidget)
        self.main_container.setObjectName(u"main_container")
        self.main_container.setFrameShape(QFrame.StyledPanel)
        self.main_container.setFrameShadow(QFrame.Raised)
        self.titulo = QLabel(self.main_container)
        self.titulo.setObjectName(u"titulo")
        self.titulo.setGeometry(QRect(-10, -10, 801, 91))
        self.titulo.setStyleSheet(u"*{\n"
"	background-color: rgb(255, 255, 0);\n"
"	background-color: rgb(255, 238, 53);\n"
"	border:none;\n"
"}")
        self.frame = QFrame(self.main_container)
        self.frame.setObjectName(u"frame")
        self.frame.setGeometry(QRect(0, 82, 781, 501))
        self.frame.setStyleSheet(u"background-color: rgb(15, 15, 15);")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.box_base = QComboBox(self.frame)
        self.box_base.setObjectName(u"box_base")
        self.box_base.setGeometry(QRect(400, 70, 111, 21))
        self.box_base.setStyleSheet(u"*{\n"
"	background-color: rgb(255, 255, 255);\n"
"	border:none;\n"
"}")
        self.moeda_base = QLabel(self.frame)
        self.moeda_base.setObjectName(u"moeda_base")
        self.moeda_base.setGeometry(QRect(200, 60, 101, 41))
        self.moeda_base.setStyleSheet(u"*{\n"
"	color: rgb(255, 255, 255);\n"
"	border:none;\n"
"}")
        self.box_alvo = QComboBox(self.frame)
        self.box_alvo.setObjectName(u"box_alvo")
        self.box_alvo.setGeometry(QRect(400, 160, 111, 21))
        self.box_alvo.setStyleSheet(u"*{\n"
"	background-color: rgb(255, 255, 255);\n"
"	border:none;\n"
"}")
        self.moeda_alvo = QLabel(self.frame)
        self.moeda_alvo.setObjectName(u"moeda_alvo")
        self.moeda_alvo.setGeometry(QRect(200, 150, 101, 41))
        self.moeda_alvo.setStyleSheet(u"*{\n"
"	color: rgb(255, 255, 255);\n"
"	border:none;\n"
"}")
        self.resultado = QLabel(self.frame)
        self.resultado.setObjectName(u"resultado")
        self.resultado.setGeometry(QRect(200, 330, 101, 41))
        self.resultado.setStyleSheet(u"*{\n"
"	color: rgb(255, 255, 255);\n"
"	border:none;\n"
"}")
        self.box_resultado = QPlainTextEdit(self.frame)
        self.box_resultado.setObjectName(u"box_resultado")
        self.box_resultado.setGeometry(QRect(390, 330, 261, 61))
        self.box_resultado.setStyleSheet(u"*{\n"
"	font: 75 12pt \"MS Shell Dlg 2\";\n"
"	background-color: rgb(255, 255, 255);\n"
"	border:none;\n"
"}")
        self.converter_btn = QPushButton(self.frame)
        self.converter_btn.setObjectName(u"converter_btn")
        self.converter_btn.setGeometry(QRect(200, 420, 341, 23))
        self.converter_btn.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.quantidade = QLabel(self.frame)
        self.quantidade.setObjectName(u"quantidade")
        self.quantidade.setGeometry(QRect(200, 250, 101, 41))
        self.quantidade.setStyleSheet(u"*{\n"
"	color: rgb(255, 255, 255);\n"
"	border:none;\n"
"}")
        self.box_quantidade = QLineEdit(self.frame)
        self.box_quantidade.setObjectName(u"box_quantidade")
        self.box_quantidade.setGeometry(QRect(400, 260, 101, 20))
        self.box_quantidade.setStyleSheet(u"background-color: rgb(255, 255, 255);")

        self.horizontalLayout.addWidget(self.main_container)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.titulo.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:24pt; font-weight:600;\">Conversor de moedas</span></p></body></html>", None))
        self.moeda_base.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:12pt;\">Moeda base</span></p></body></html>", None))
        self.moeda_alvo.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:12pt;\">Moeda alvo</span></p></body></html>", None))
        self.resultado.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:12pt;\">Resultado</span></p></body></html>", None))
        self.converter_btn.setText(QCoreApplication.translate("MainWindow", u"Converter", None))
        self.quantidade.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:12pt;\">Quantidade</span></p></body></html>", None))
    # retranslateUi

