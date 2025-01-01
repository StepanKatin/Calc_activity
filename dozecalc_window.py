# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'dozecalc_window.ui'
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
from PySide6.QtWidgets import (QApplication, QComboBox, QDateEdit, QDateTimeEdit,
    QDialog, QFrame, QGridLayout, QHBoxLayout,
    QHeaderView, QLabel, QLineEdit, QPushButton,
    QSizePolicy, QTableView, QTimeEdit, QVBoxLayout,
    QWidget)

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(698, 681)
        Dialog.setStyleSheet(u"background-color: #E9E9E9;")
        self.gridLayout_2 = QGridLayout(Dialog)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.frame = QFrame(Dialog)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout = QVBoxLayout(self.frame)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.date_dozc_day = QDateEdit(self.frame)
        self.date_dozc_day.setObjectName(u"date_dozc_day")
        self.date_dozc_day.setEnabled(True)
        self.date_dozc_day.setMaximumSize(QSize(250, 80))
        self.date_dozc_day.setStyleSheet(u"font: 16pt;\n"
"background-color: #D6D6D6;\n"
"color: #151716;\n"
"border: 2px solid #5c5c5c;\n"
"border-radius: 5px;\n"
"\n"
"")
        self.date_dozc_day.setDateTime(QDateTime(QDate(2024, 7, 31), QTime(18, 0, 0)))
        self.date_dozc_day.setCurrentSection(QDateTimeEdit.Section.DaySection)

        self.horizontalLayout.addWidget(self.date_dozc_day)

        self.label_dozc_timsep = QLabel(self.frame)
        self.label_dozc_timsep.setObjectName(u"label_dozc_timsep")
        self.label_dozc_timsep.setMaximumSize(QSize(250, 80))
        self.label_dozc_timsep.setStyleSheet(u"font: 16pt;\n"
"\n"
"color: #151716;;\n"
"border-radius: 5px;\n"
"border: 2px solid #B0B0B0;")
        self.label_dozc_timsep.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout.addWidget(self.label_dozc_timsep)

        self.timeEdit_dozc_timesep = QTimeEdit(self.frame)
        self.timeEdit_dozc_timesep.setObjectName(u"timeEdit_dozc_timesep")
        self.timeEdit_dozc_timesep.setMaximumSize(QSize(250, 80))
        self.timeEdit_dozc_timesep.setStyleSheet(u"font: 16pt;\n"
"background-color: #D6D6D6;\n"
"color: #151716;\n"
"border: 2px solid #5c5c5c;\n"
"border-radius: 5px;\n"
"")
        self.timeEdit_dozc_timesep.setKeyboardTracking(True)
        self.timeEdit_dozc_timesep.setCurrentSection(QDateTimeEdit.Section.MinuteSection)

        self.horizontalLayout.addWidget(self.timeEdit_dozc_timesep)

        self.label_dozc_usil = QLabel(self.frame)
        self.label_dozc_usil.setObjectName(u"label_dozc_usil")
        self.label_dozc_usil.setMaximumSize(QSize(250, 80))
        self.label_dozc_usil.setStyleSheet(u"font: 16pt;\n"
"color: #151716;;\n"
"border-radius: 5px;\n"
"border: 2px solid #B0B0B0;")
        self.label_dozc_usil.setTextFormat(Qt.TextFormat.AutoText)
        self.label_dozc_usil.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout.addWidget(self.label_dozc_usil)

        self.comboBox_dozc_usil = QComboBox(self.frame)
        self.comboBox_dozc_usil.addItem("")
        self.comboBox_dozc_usil.addItem("")
        self.comboBox_dozc_usil.setObjectName(u"comboBox_dozc_usil")
        self.comboBox_dozc_usil.setMaximumSize(QSize(200, 80))
        self.comboBox_dozc_usil.setStyleSheet(u"QComboBox{\n"
"font-size: 16pt;\n"
"color: #FFFFFF;}\n"
"\n"
"QComboBox {\n"
"background-color: #0095FF}\n"
"\n"
"QComboBox:item{\n"
"color: FFFFF:}\n"
"")

        self.horizontalLayout.addWidget(self.comboBox_dozc_usil)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.label_dozc_timestart = QLabel(self.frame)
        self.label_dozc_timestart.setObjectName(u"label_dozc_timestart")
        self.label_dozc_timestart.setMaximumSize(QSize(350, 100))
        self.label_dozc_timestart.setStyleSheet(u"font: 16pt;\n"
"\n"
"color: #151716;;\n"
"border-radius: 5px;\n"
"border: 2px solid #B0B0B0;")
        self.label_dozc_timestart.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout_4.addWidget(self.label_dozc_timestart)

        self.timeEdit_dozc_timestart = QTimeEdit(self.frame)
        self.timeEdit_dozc_timestart.setObjectName(u"timeEdit_dozc_timestart")
        self.timeEdit_dozc_timestart.setMaximumSize(QSize(250, 100))
        self.timeEdit_dozc_timestart.setStyleSheet(u"font: 16pt;\n"
"background-color: #D6D6D6;\n"
"color: #151716;\n"
"border: 2px solid #5c5c5c;\n"
"border-radius: 5px;\n"
"\n"
"")

        self.horizontalLayout_4.addWidget(self.timeEdit_dozc_timestart)

        self.label_dozc_timeplus = QLabel(self.frame)
        self.label_dozc_timeplus.setObjectName(u"label_dozc_timeplus")
        self.label_dozc_timeplus.setMaximumSize(QSize(250, 100))
        self.label_dozc_timeplus.setStyleSheet(u"font: 16pt;\n"
"\n"
"color: #151716;;\n"
"border-radius: 5px;\n"
"border: 2px solid #B0B0B0;")
        self.label_dozc_timeplus.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout_4.addWidget(self.label_dozc_timeplus)

        self.timeEdit_dozc_timeplus = QTimeEdit(self.frame)
        self.timeEdit_dozc_timeplus.setObjectName(u"timeEdit_dozc_timeplus")
        self.timeEdit_dozc_timeplus.setMaximumSize(QSize(250, 100))
        self.timeEdit_dozc_timeplus.setStyleSheet(u"font: 16pt;\n"
"background-color: #D6D6D6;\n"
"color: #151716;\n"
"border: 2px solid #5c5c5c;\n"
"border-radius: 5px;\n"
"\n"
"")
        self.timeEdit_dozc_timeplus.setCurrentSection(QDateTimeEdit.Section.HourSection)

        self.horizontalLayout_4.addWidget(self.timeEdit_dozc_timeplus)


        self.verticalLayout.addLayout(self.horizontalLayout_4)

        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.lineEdit_dozc_data_5 = QLineEdit(self.frame)
        self.lineEdit_dozc_data_5.setObjectName(u"lineEdit_dozc_data_5")
        self.lineEdit_dozc_data_5.setStyleSheet(u"font: 16pt;\n"
"color: #151716;\n"
"background-color: #FFFFFF;\n"
"border-radius: 10px;\n"
"border: 1px solid #B0B0B0;")

        self.gridLayout.addWidget(self.lineEdit_dozc_data_5, 5, 0, 1, 1)

        self.tableView_dozcalc_result = QTableView(self.frame)
        self.tableView_dozcalc_result.setObjectName(u"tableView_dozcalc_result")
        self.tableView_dozcalc_result.setMaximumSize(QSize(16777215, 250))
        self.tableView_dozcalc_result.setStyleSheet(u"")

        self.gridLayout.addWidget(self.tableView_dozcalc_result, 8, 0, 1, 1)

        self.lineEdit_dozc_data_4 = QLineEdit(self.frame)
        self.lineEdit_dozc_data_4.setObjectName(u"lineEdit_dozc_data_4")
        self.lineEdit_dozc_data_4.setStyleSheet(u"font: 16pt;\n"
"color: #151716;\n"
"background-color: #FFFFFF;\n"
"border-radius: 10px;\n"
"border: 1px solid #B0B0B0;\n"
"height: 35px;")
        self.lineEdit_dozc_data_4.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout.addWidget(self.lineEdit_dozc_data_4, 4, 0, 1, 1)

        self.lineEdit_dozc_data_1 = QLineEdit(self.frame)
        self.lineEdit_dozc_data_1.setObjectName(u"lineEdit_dozc_data_1")
        self.lineEdit_dozc_data_1.setStyleSheet(u"font: 16pt;\n"
"color: #151716;\n"
"background-color: #FFFFFF;\n"
"border-radius: 10px;\n"
"border: 1px solid #B0B0B0;\n"
"height: 35px;")
        self.lineEdit_dozc_data_1.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout.addWidget(self.lineEdit_dozc_data_1, 1, 0, 1, 1)

        self.lineEdit_dozc_data_3 = QLineEdit(self.frame)
        self.lineEdit_dozc_data_3.setObjectName(u"lineEdit_dozc_data_3")
        self.lineEdit_dozc_data_3.setStyleSheet(u"font: 16pt;\n"
"color: #151716;\n"
"background-color: #FFFFFF;\n"
"border-radius: 10px;\n"
"border: 1px solid #B0B0B0;\n"
"height: 35px;")
        self.lineEdit_dozc_data_3.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout.addWidget(self.lineEdit_dozc_data_3, 3, 0, 1, 1)

        self.pushButton_dozc_calc = QPushButton(self.frame)
        self.pushButton_dozc_calc.setObjectName(u"pushButton_dozc_calc")
        self.pushButton_dozc_calc.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.pushButton_dozc_calc.setStyleSheet(u"QPushButton{ \n"
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

        self.gridLayout.addWidget(self.pushButton_dozc_calc, 6, 0, 1, 1)

        self.lineEdit_dozc_data_2 = QLineEdit(self.frame)
        self.lineEdit_dozc_data_2.setObjectName(u"lineEdit_dozc_data_2")
        self.lineEdit_dozc_data_2.setStyleSheet(u"font: 16pt;\n"
"color: #151716;\n"
"background-color: #FFFFFF;\n"
"border-radius: 10px;\n"
"border: 1px solid #B0B0B0;\n"
"height: 35px;")
        self.lineEdit_dozc_data_2.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout.addWidget(self.lineEdit_dozc_data_2, 2, 0, 1, 1)

        self.pushButton_dozc_addline = QPushButton(self.frame)
        self.pushButton_dozc_addline.setObjectName(u"pushButton_dozc_addline")
        self.pushButton_dozc_addline.setStyleSheet(u"QPushButton{ \n"
"background-color: #0095FF;\n"
"font: 18pt;\n"
"font-weight: bold;\n"
"color: #FFFFFF;\n"
"border-radius: 10px;\n"
"font-color: #151716;\n"
"border: 2px solid #FFFFFF;\n"
"width: 400px;\n"
"height: 50px;\n"
"}\n"
"\n"
"QPushButton:hover { \n"
"background-color: rgba(0,149,255, 100);\n"
"}\n"
"QPushButton:pressed { \n"
"background-color:  rgba(0,149,255, 70);\n"
"}\n"
"")

        self.gridLayout.addWidget(self.pushButton_dozc_addline, 7, 0, 1, 1)


        self.verticalLayout.addLayout(self.gridLayout)


        self.gridLayout_2.addWidget(self.frame, 0, 0, 1, 1)


        self.retranslateUi(Dialog)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Dialog", None))
        self.label_dozc_timsep.setText(QCoreApplication.translate("Dialog", u"TimeSep", None))
        self.label_dozc_usil.setText(QCoreApplication.translate("Dialog", u"\u0423\u0441\u0438\u043b\u0435\u043d\u0438\u0435", None))
        self.comboBox_dozc_usil.setItemText(0, QCoreApplication.translate("Dialog", u"11,3", None))
        self.comboBox_dozc_usil.setItemText(1, QCoreApplication.translate("Dialog", u"11,5", None))

        self.label_dozc_timestart.setText(QCoreApplication.translate("Dialog", u"\u0412\u0440\u0435\u043c\u044f \u043d\u0430\u0447\u0430\u043b\u0430 \u0438\u0437\u043c\u0435\u0440\u0435\u043d\u0438\u044f", None))
        self.label_dozc_timeplus.setText(QCoreApplication.translate("Dialog", u"+t, min", None))
        self.lineEdit_dozc_data_1.setText("")
        self.pushButton_dozc_calc.setText(QCoreApplication.translate("Dialog", u"\u0420\u0430\u0441\u0441\u0447\u0435\u0442", None))
        self.pushButton_dozc_addline.setText(QCoreApplication.translate("Dialog", u"\u0414\u043e\u0431\u0430\u0432\u0438\u0442\u044c \u0438\u0437\u043c\u0435\u0440\u0435\u043d\u0438\u0435", None))
    # retranslateUi

