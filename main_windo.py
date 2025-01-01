# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main_windo.ui'
##
## Created by: Qt User Interface Compiler version 6.8.1
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
from PySide6.QtWidgets import (QApplication, QFrame, QLabel, QMainWindow,
    QPushButton, QSizePolicy, QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(800, 611)
        MainWindow.setStyleSheet(u"background-color: #E9E9E9")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout_3 = QVBoxLayout(self.centralwidget)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.frame = QFrame(self.centralwidget)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.frame)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.label_menu = QLabel(self.frame)
        self.label_menu.setObjectName(u"label_menu")
        self.label_menu.setStyleSheet(u"font: 25pt;\n"
"font-weight: bold;\n"
"border: true;\n"
"border-radius: 10px;\n"
"font-color: #151716;\n"
"border: 2px solid #B0B0B0;\n"
"width: 700px;\n"
"height: 300px;")
        self.label_menu.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout.addWidget(self.label_menu)

        self.pushButton_ppd = QPushButton(self.frame)
        self.pushButton_ppd.setObjectName(u"pushButton_ppd")
        self.pushButton_ppd.setStyleSheet(u"QPushButton{ \n"
"background-color: #0095FF;\n"
"font: 18pt;\n"
"font-weight: bold;\n"
"color: #FFFFFF;\n"
"border-radius: 10px;\n"
"font-color: #151716;\n"
"border: 2px solid #FFFFFF;\n"
"width: 400px;\n"
"height: 100px\n"
"}\n"
"\n"
"QPushButton:hover { \n"
"background-color: rgba(0,149,255, 100);\n"
"}\n"
"QPushButton:pressed { \n"
"background-color:  rgba(0,149,255, 70);\n"
"}\n"
"")

        self.verticalLayout.addWidget(self.pushButton_ppd)

        self.pushButton_menu_dozcal = QPushButton(self.frame)
        self.pushButton_menu_dozcal.setObjectName(u"pushButton_menu_dozcal")
        self.pushButton_menu_dozcal.setStyleSheet(u"QPushButton{ \n"
"background-color: #0095FF;\n"
"font: 18pt;\n"
"font-weight: bold;\n"
"color: #FFFFFF;\n"
"border-radius: 10px;\n"
"font-color: #151716;\n"
"border: 2px solid #FFFFFF;\n"
"width: 400px;\n"
"height: 100px\n"
"}\n"
"\n"
"QPushButton:hover { \n"
"background-color: rgba(0,149,255, 99);\n"
"}\n"
"QPushButton:pressed { \n"
"background-color:  rgba(0,149,255, 70);\n"
"}\n"
"")

        self.verticalLayout.addWidget(self.pushButton_menu_dozcal)

        self.pushButton_menu_guide = QPushButton(self.frame)
        self.pushButton_menu_guide.setObjectName(u"pushButton_menu_guide")
        self.pushButton_menu_guide.setStyleSheet(u"QPushButton{ \n"
"background-color: #E9E9E9;\n"
"font: 18pt;\n"
"color: #0095ff;\n"
"border-radius: 10px;\n"
"border: 2px solid #94D3FE;\n"
"width: 400px;\n"
"height: 100px;\n"
"}\n"
"QPushButton:hover { \n"
"color: rgba(0,149,255, 99);\n"
"border: 2px solid rgba(148,211,254, 99);\n"
"}\n"
"QPushButton:pressed { \n"
"color: rgba(0,149,255, 70);\n"
"border: 2px solid rgba(148,211,254, 70);\n"
"}\n"
"")

        self.verticalLayout.addWidget(self.pushButton_menu_guide)


        self.verticalLayout_2.addLayout(self.verticalLayout)


        self.verticalLayout_3.addWidget(self.frame)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.label_menu.setText(QCoreApplication.translate("MainWindow", u"\u041d\u0430 \u0447\u0435\u043c \u0438\u0437\u043c\u0435\u0440\u044f\u0435\u043c?", None))
        self.pushButton_ppd.setText(QCoreApplication.translate("MainWindow", u"\u041f\u041f\u0414 \u0441\u043f\u0435\u043a\u0442\u0440\u043e\u043c\u0435\u0442\u0440", None))
        self.pushButton_menu_dozcal.setText(QCoreApplication.translate("MainWindow", u"\u0414\u043e\u0437\u043a\u0430\u043b\u0438\u0431\u0440\u0430\u0442\u043e\u0440", None))
        self.pushButton_menu_guide.setText(QCoreApplication.translate("MainWindow", u"\u041f\u043e\u0434\u0441\u043a\u0430\u0437\u043a\u0430", None))
    # retranslateUi

