# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ppd_window.ui'
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
from PySide6.QtWidgets import (QApplication, QComboBox, QDateEdit, QDialog,
    QFrame, QGridLayout, QHBoxLayout, QHeaderView,
    QLabel, QLayout, QLineEdit, QPushButton,
    QSizePolicy, QTableView, QTimeEdit, QVBoxLayout,
    QWidget)

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(1014, 776)
        Dialog.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        Dialog.setStyleSheet(u"background-color: #E9E9E9")
        self.gridLayout_2 = QGridLayout(Dialog)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.frame = QFrame(Dialog)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.frame)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setSizeConstraint(QLayout.SizeConstraint.SetMaximumSize)
        self.date_ppd_mes = QDateEdit(self.frame)
        self.date_ppd_mes.setObjectName(u"date_ppd_mes")
        self.date_ppd_mes.setMaximumSize(QSize(150, 80))
        self.date_ppd_mes.setStyleSheet(u"font: 16pt;\n"
"background-color: #D6D6D6;\n"
"color: #151716;\n"
"border: 2px solid #5c5c5c;\n"
"border-radius: 5px;\n"
"\n"
"")

        self.horizontalLayout_2.addWidget(self.date_ppd_mes)

        self.comboBox_ppd_seria = QComboBox(self.frame)
        self.comboBox_ppd_seria.addItem("")
        self.comboBox_ppd_seria.addItem("")
        self.comboBox_ppd_seria.setObjectName(u"comboBox_ppd_seria")
        self.comboBox_ppd_seria.setMaximumSize(QSize(150, 80))
        self.comboBox_ppd_seria.setStyleSheet(u"QComboBox{\n"
"font-size: 16pt;\n"
"color: #FFFFFF;}\n"
"\n"
"QComboBox {\n"
"background-color: #0095FF}\n"
"\n"
"QComboBox:item{\n"
"color: FFFFF;}\n"
"")

        self.horizontalLayout_2.addWidget(self.comboBox_ppd_seria)

        self.comboBox_ppd_geom = QComboBox(self.frame)
        self.comboBox_ppd_geom.addItem("")
        self.comboBox_ppd_geom.addItem("")
        self.comboBox_ppd_geom.addItem("")
        self.comboBox_ppd_geom.addItem("")
        self.comboBox_ppd_geom.setObjectName(u"comboBox_ppd_geom")
        self.comboBox_ppd_geom.setMaximumSize(QSize(150, 80))
        self.comboBox_ppd_geom.setContextMenuPolicy(Qt.ContextMenuPolicy.DefaultContextMenu)
        self.comboBox_ppd_geom.setStyleSheet(u"QComboBox{\n"
"font-size: 16pt;\n"
"color: #FFFFFF;}\n"
"\n"
"QComboBox {\n"
"background-color: #0095FF}\n"
"\n"
"QComboBox:item{\n"
"color: FFFFF;}")

        self.horizontalLayout_2.addWidget(self.comboBox_ppd_geom)

        self.label_ppd_timesep = QLabel(self.frame)
        self.label_ppd_timesep.setObjectName(u"label_ppd_timesep")
        self.label_ppd_timesep.setMaximumSize(QSize(150, 80))
        self.label_ppd_timesep.setStyleSheet(u"font: 16pt;\n"
"\n"
"color: #151716;;\n"
"border-radius: 5px;\n"
"border: 2px solid #B0B0B0;\n"
"width: 80px;\n"
"height: 50px\n"
"")
        self.label_ppd_timesep.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout_2.addWidget(self.label_ppd_timesep)

        self.timeEdit_ppd__timesep = QTimeEdit(self.frame)
        self.timeEdit_ppd__timesep.setObjectName(u"timeEdit_ppd__timesep")
        self.timeEdit_ppd__timesep.setMaximumSize(QSize(100, 80))
        self.timeEdit_ppd__timesep.setStyleSheet(u"font: 16pt;\n"
"background-color: #D6D6D6;\n"
"color: #151716;\n"
"border: 2px solid #5c5c5c;\n"
"border-radius: 5px;\n"
"width: 80px;\n"
"height: 50px\n"
"\n"
"")

        self.horizontalLayout_2.addWidget(self.timeEdit_ppd__timesep)


        self.verticalLayout_2.addLayout(self.horizontalLayout_2)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.label_ppd_exp = QLabel(self.frame)
        self.label_ppd_exp.setObjectName(u"label_ppd_exp")
        self.label_ppd_exp.setMaximumSize(QSize(150, 80))
        self.label_ppd_exp.setStyleSheet(u"font: 16pt;\n"
"\n"
"color: #151716;;\n"
"border-radius: 5px;\n"
"border: 2px solid #B0B0B0;\n"
"")
        self.label_ppd_exp.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout.addWidget(self.label_ppd_exp)

        self.lineEdit_ppd_expos = QLineEdit(self.frame)
        self.lineEdit_ppd_expos.setObjectName(u"lineEdit_ppd_expos")
        self.lineEdit_ppd_expos.setMaximumSize(QSize(150, 80))
        self.lineEdit_ppd_expos.setStyleSheet(u"font: 16pt;\n"
"color: #151716;\n"
"background-color: #FFFFFF;\n"
"border-radius: 10px;\n"
"border: 1px solid #B0B0B0;\n"
"width: 80px;\n"
"height: 50px")
        self.lineEdit_ppd_expos.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout.addWidget(self.lineEdit_ppd_expos)

        self.label_ppd_timemesh = QLabel(self.frame)
        self.label_ppd_timemesh.setObjectName(u"label_ppd_timemesh")
        self.label_ppd_timemesh.setMaximumSize(QSize(350, 50))
        self.label_ppd_timemesh.setStyleSheet(u"font: 16pt;\n"
"\n"
"color: #151716;;\n"
"border-radius: 5px;\n"
"border: 2px solid #B0B0B0;\n"
"")
        self.label_ppd_timemesh.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout.addWidget(self.label_ppd_timemesh)

        self.timeEdit_ppd_timemesh = QTimeEdit(self.frame)
        self.timeEdit_ppd_timemesh.setObjectName(u"timeEdit_ppd_timemesh")
        self.timeEdit_ppd_timemesh.setMaximumSize(QSize(150, 80))
        self.timeEdit_ppd_timemesh.setStyleSheet(u"font: 16pt;\n"
"background-color: #D6D6D6;\n"
"color: #151716;\n"
"border: 2px solid #5c5c5c;\n"
"border-radius: 5px;\n"
"\n"
"")

        self.horizontalLayout.addWidget(self.timeEdit_ppd_timemesh)

        self.label_ppd_dt = QLabel(self.frame)
        self.label_ppd_dt.setObjectName(u"label_ppd_dt")
        self.label_ppd_dt.setMaximumSize(QSize(100, 16777215))
        self.label_ppd_dt.setStyleSheet(u"font: 16pt;\n"
"\n"
"color: #151716;;\n"
"border-radius: 5px;\n"
"border: 2px solid #B0B0B0;\n"
"width: 80px;\n"
"height: 50px")
        self.label_ppd_dt.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout.addWidget(self.label_ppd_dt)

        self.lineEdit_ppd_dt = QLineEdit(self.frame)
        self.lineEdit_ppd_dt.setObjectName(u"lineEdit_ppd_dt")
        self.lineEdit_ppd_dt.setMaximumSize(QSize(150, 16777215))
        self.lineEdit_ppd_dt.setStyleSheet(u"font: 16pt;\n"
"color: #151716;\n"
"background-color: #FFFFFF;\n"
"border-radius: 10px;\n"
"border: 1px solid #B0B0B0;\n"
"width: 80px;\n"
"height: 50px")

        self.horizontalLayout.addWidget(self.lineEdit_ppd_dt)


        self.verticalLayout_2.addLayout(self.horizontalLayout)

        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setSizeConstraint(QLayout.SizeConstraint.SetMinimumSize)
        self.lineEdit_ppd_data_1 = QLineEdit(self.frame)
        self.lineEdit_ppd_data_1.setObjectName(u"lineEdit_ppd_data_1")
        self.lineEdit_ppd_data_1.setStyleSheet(u"font: 16pt;\n"
"color: #151716;\n"
"background-color: #FFFFFF;\n"
"border-radius: 10px;\n"
"border: 1px solid #B0B0B0;\n"
"\n"
"height: 80px")
        self.lineEdit_ppd_data_1.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout.addWidget(self.lineEdit_ppd_data_1)

        self.lineEdit_ppd_data_2 = QLineEdit(self.frame)
        self.lineEdit_ppd_data_2.setObjectName(u"lineEdit_ppd_data_2")
        self.lineEdit_ppd_data_2.setStyleSheet(u"font: 16pt;\n"
"color: #151716;\n"
"background-color: #FFFFFF;\n"
"border-radius: 10px;\n"
"border: 1px solid #B0B0B0;\n"
"\n"
"height: 80px")
        self.lineEdit_ppd_data_2.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout.addWidget(self.lineEdit_ppd_data_2)

        self.lineEdit_ppd_data_3 = QLineEdit(self.frame)
        self.lineEdit_ppd_data_3.setObjectName(u"lineEdit_ppd_data_3")
        self.lineEdit_ppd_data_3.setStyleSheet(u"font: 16pt;\n"
"color: #151716;\n"
"background-color: #FFFFFF;\n"
"border-radius: 10px;\n"
"border: 1px solid #B0B0B0;\n"
"\n"
"height: 80px")
        self.lineEdit_ppd_data_3.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout.addWidget(self.lineEdit_ppd_data_3)

        self.lineEdit_ppd_data_4 = QLineEdit(self.frame)
        self.lineEdit_ppd_data_4.setObjectName(u"lineEdit_ppd_data_4")
        self.lineEdit_ppd_data_4.setStyleSheet(u"font: 16pt;\n"
"color: #151716;\n"
"background-color: #FFFFFF;\n"
"border-radius: 10px;\n"
"border: 1px solid #B0B0B0;\n"
"\n"
"height: 80px")
        self.lineEdit_ppd_data_4.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout.addWidget(self.lineEdit_ppd_data_4)

        self.pushButton_ppd_calc = QPushButton(self.frame)
        self.pushButton_ppd_calc.setObjectName(u"pushButton_ppd_calc")
        self.pushButton_ppd_calc.setMaximumSize(QSize(16777215, 150))
        self.pushButton_ppd_calc.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.pushButton_ppd_calc.setStyleSheet(u"QPushButton{ \n"
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

        self.verticalLayout.addWidget(self.pushButton_ppd_calc)

        self.tableView_ppd_result = QTableView(self.frame)
        self.tableView_ppd_result.setObjectName(u"tableView_ppd_result")
        self.tableView_ppd_result.setMaximumSize(QSize(16777215, 250))

        self.verticalLayout.addWidget(self.tableView_ppd_result)


        self.verticalLayout_2.addLayout(self.verticalLayout)


        self.gridLayout_2.addWidget(self.frame, 0, 0, 1, 1)


        self.retranslateUi(Dialog)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Dialog", None))
        self.comboBox_ppd_seria.setItemText(0, QCoreApplication.translate("Dialog", u"\u0425-\u0441\u0435\u0440\u0438\u044f", None))
        self.comboBox_ppd_seria.setItemText(1, QCoreApplication.translate("Dialog", u"\u041e\u04133-\u0441\u0435\u0440\u0438\u044f", None))

        self.comboBox_ppd_geom.setItemText(0, QCoreApplication.translate("Dialog", u"250mm", None))
        self.comboBox_ppd_geom.setItemText(1, QCoreApplication.translate("Dialog", u"TOP", None))
        self.comboBox_ppd_geom.setItemText(2, QCoreApplication.translate("Dialog", u"low", None))
        self.comboBox_ppd_geom.setItemText(3, QCoreApplication.translate("Dialog", u"\u0433\u043e\u043b\u043e\u0432\u0430", None))

        self.label_ppd_timesep.setText(QCoreApplication.translate("Dialog", u"TimeSep", None))
        self.label_ppd_exp.setText(QCoreApplication.translate("Dialog", u"\u042d\u043a\u0441\u043f\u043e\u0437\u0438\u0446\u0438\u044f", None))
        self.lineEdit_ppd_expos.setText("")
        self.label_ppd_timemesh.setText(QCoreApplication.translate("Dialog", u"\u0412\u0440\u0435\u043c\u044f \u043d\u0430\u0447\u0430\u043b\u0430 \u0438\u0437\u043c\u0435\u0440\u0435\u043d\u0438\u044f", None))
        self.label_ppd_dt.setText(QCoreApplication.translate("Dialog", u"DT,%", None))
        self.lineEdit_ppd_data_1.setText("")
        self.pushButton_ppd_calc.setText(QCoreApplication.translate("Dialog", u"\u0420\u0430\u0441\u0441\u0447\u0435\u0442", None))
    # retranslateUi

