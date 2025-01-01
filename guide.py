# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'guide.ui'
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
from PySide6.QtWidgets import (QApplication, QDialog, QFrame, QHBoxLayout,
    QLabel, QPushButton, QSizePolicy, QVBoxLayout,
    QWidget)

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(1061, 731)
        Dialog.setStyleSheet(u"background-color: #E9E9E9")
        self.horizontalLayout = QHBoxLayout(Dialog)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.frame = QFrame(Dialog)
        self.frame.setObjectName(u"frame")
        self.frame.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.frame.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout = QVBoxLayout(self.frame)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.label_guide_title = QLabel(self.frame)
        self.label_guide_title.setObjectName(u"label_guide_title")
        self.label_guide_title.setMaximumSize(QSize(16777215, 250))
        self.label_guide_title.setLayoutDirection(Qt.LayoutDirection.RightToLeft)
        self.label_guide_title.setStyleSheet(u"font: 20pt;\n"
"background-color: #FFFFFF;\n"
"\n"
"color: #0095FF;\n"
"border-radius: 10px;\n"
"border: 2px solid #94D3FE;")
        self.label_guide_title.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.label_guide_title.setWordWrap(True)

        self.verticalLayout.addWidget(self.label_guide_title)

        self.label_guide_dozc = QLabel(self.frame)
        self.label_guide_dozc.setObjectName(u"label_guide_dozc")
        self.label_guide_dozc.setStyleSheet(u"font: 16pt;\n"
"background-color: #FFFFFF;\n"
"color: #151716;\n"
"border-radius: 5px;\n"
"border: 2px solid #B0B0B0;")
        self.label_guide_dozc.setAlignment(Qt.AlignmentFlag.AlignJustify|Qt.AlignmentFlag.AlignVCenter)
        self.label_guide_dozc.setWordWrap(True)

        self.verticalLayout.addWidget(self.label_guide_dozc)

        self.label_guide_ppd = QLabel(self.frame)
        self.label_guide_ppd.setObjectName(u"label_guide_ppd")
        self.label_guide_ppd.setStyleSheet(u"font: 16pt;\n"
"background-color: #FFFFFF;\n"
"color: #151716;\n"
"border-radius: 5px;\n"
"border: 2px solid #B0B0B0;")

        self.verticalLayout.addWidget(self.label_guide_ppd)

        self.pushButton_fun = QPushButton(self.frame)
        self.pushButton_fun.setObjectName(u"pushButton_fun")
        self.pushButton_fun.setStyleSheet(u"QPushButton{ \n"
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

        self.verticalLayout.addWidget(self.pushButton_fun)


        self.horizontalLayout.addWidget(self.frame)


        self.retranslateUi(Dialog)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Dialog", None))
        self.label_guide_title.setText(QCoreApplication.translate("Dialog", u"\u0417\u0434\u0435\u0441\u044c \u0431\u0443\u0434\u0435\u0442 \u043d\u0430\u043f\u0438\u0441\u0430\u043d\u0430 \u043f\u043e\u0434\u0441\u043a\u0430\u0437\u043a\u0430 \u0434\u043b\u044f \u043f\u0440\u043e\u0432\u0435\u0434\u0435\u043d\u0438\u044f \u0438\u0437\u043c\u0435\u0440\u0435\u043d\u0438\u0439 \u043d\u0430 \u0434\u043e\u0437\u043a\u0430\u043b\u0438\u0431\u0440\u0430\u0442\u043e\u0440\u0435, \u0430 \u0442\u0430\u043a\u0436\u0435 \u043f\u043e\u0434\u0441\u043a\u0430\u0437\u043a\u0430 \u043f\u043e \u043f\u043e\u043b\u044c\u0437\u043e\u0432\u0430\u043d\u0438\u044e \u044d\u0442\u0438\u043c \u043f\u0440\u0438\u043b\u043e\u0436\u0435\u043d\u0438\u0438.", None))
        self.label_guide_dozc.setText(QCoreApplication.translate("Dialog", u"\n"
"\u0418\u043d\u0441\u0442\u0440\u0443\u043a\u0446\u0438\u044f \u043f\u043e \u0438\u0437\u043c\u0435\u0440\u0435\u043d\u0438\u044e \u043d\u0430 \u0434\u043e\u0437\u043a\u0430\u043b\u0438\u0431\u0440\u0430\u0442\u043e\u0440\u0435:\n"
"1) \u0432\u043a\u043b\u044e\u0447\u0438\u0442\u044c \u043f\u0440\u0438\u0431\u043e\u0440 (\u043a\u043d\u043e\u043f\u043a\u0430 \u0441\u0437\u0430\u0434\u0438)\n"
"2) \u0434\u0430\u0442\u044c \u0435\u043c\u0443 \u043f\u0440\u043e\u0433\u0440\u0435\u0442\u044c\u0441\u044f 10-15 \u043c\u0438\u043d\u0443\u0442, \n"
"3) \u043d\u0430\u0436\u0430\u0442\u044c \u043a\u043d\u043e\u043f\u043a\u0443 OTHER, \u0443\u0431\u0435\u0434\u0438\u0442\u0441\u044f \u0447\u0442\u043e \u043a\u043e\u044d\u0444\u0444\u0438\u0446\u0438\u0435\u043d\u0442 \u0434\u043b\u044f \u0440\u0430\u0441\u043f\u0430\u0434\u0430\u044e\u0449\u0438\u0445\u0441\u044f \u043f\u0440\u043e\u0431 11,3; \u0434\u043b\u044f \u0440\u0430\u0432\u043d\u043e\u0432\u0435\u0441\u043d\u043e\u0433\u043e \u0440\u0430\u0441\u0442\u0432\u043e"
                        "\u0440\u0430 11,5\n"
"4) \u043f\u043e\u0441\u0442\u0430\u0432\u0438\u0442\u044c \u043f\u0440\u043e\u0431\u0443 \u043d\u0430 \u043f\u043e\u043b\u043e\u0447\u043a\u0443 \u043f\u0440\u043e\u0431\u043e\u0434\u0435\u0440\u0436\u0430\u0442\u0435\u043b\u044f, \u043e\u043f\u0443\u0441\u0442\u0438\u0442\u044c \u043f\u0440\u043e\u0431\u0443 \u0432 \u043a\u0430\u043c\u0435\u0440\u0443 \u0434\u043e\u0437\u043a\u0430\u043b\u0438\u0431\u0440\u0430\u0442\u043e\u0440\u0430, \u0437\u0430\u043f\u0438\u0441\u0430\u0442\u044c \u0432\u0440\u0435\u043c\u044f \u0438\u0437\u043c\u0435\u0440\u0435\u043d\u0438\u044f \u0438 \u0437\u043d\u0430\u0447\u0435\u043d\u0438\u0435 \n"
"5) \u0437\u0430\u0441\u0435\u0447\u044c 2 \u043c\u0438\u043d\u0443\u0442\u044b, \u0437\u0430\u043f\u0438\u0441\u0430\u0442\u044c \u0437\u043d\u0430\u0447\u0435\u043d\u0438\u0435 \u043f\u043e \u0438\u0441\u0442\u0435\u0447\u0435\u043d\u0438\u044e \u0442\u0430\u0439\u043c\u0435\u0440\u0430, \u043f\u043e\u0432\u0442\u043e\u0440\u0438\u0442\u044c \u043f.5 \u043f\u044f"
                        "\u0442\u044c \u0440\u0430\u0437. \n"
"6) \u0437\u0430\u043d\u0435\u0441\u0442\u0438 \u0434\u0430\u043d\u043d\u044b\u0435 \u0432 \u0436\u0443\u0440\u043d\u0430\u043b, \u0433\u0434\u0435 \u043e\u0431\u043e\u0437\u043d\u0430\u0447\u0438\u0442\u044c \u0434\u0430\u0442\u0443/\u0432\u0440\u0435\u043c\u044f \u0440\u0430\u0437\u0434\u0435\u043b\u0435\u043d\u0438\u044f, \u043d\u043e\u043c\u0435\u0440 \u043f\u0440\u043e\u0431\u044b, \u0442\u0438\u043f \u043f\u0440\u0438\u0431\u043e\u0440\u0430, \u0432\u0440\u0435\u043c\u044f \u043a\u0430\u0436\u0434\u043e\u0433\u043e \u0438\u0437\u043c\u0435\u0440\u0435\u043d\u0438\u044f (\u0438\u043b\u0438 \u044d\u043a\u0441\u043f\u043e\u0437\u0438\u0446\u0438\u044e), \u0437\u043d\u0430\u0447\u0435\u043d\u0438\u044f \u0430\u043a\u0442\u0438\u0432\u043d\u043e\u0441\u0442\u0438\n"
"7)\u043f\u0440\u043e\u0432\u0435\u0441\u0442\u0438 \u0440\u0430\u0441\u0447\u0451\u0442 \u0432 Excel \u0444\u0430\u0439\u043b\u0435 (\u043f\u0430\u043f\u043a\u0430 \u0433\u0435\u0440\u043c\u0430\u043d\u0438\u0439"
                        "68/\u043a\u0430\u043b\u0438\u0431\u0440\u043e\u0432\u043a\u0438 \u043f\u0440\u043e\u0431\u0438\u0440\u043a\u0430 5\u043c\u043b) \n"
"8) (\u043e\u043f\u0446\u0438\u043e\u043d\u0430\u043b\u044c\u043d\u043e) \u043e\u0441\u0442\u0430\u0432\u0438\u0442\u044c \u0442\u043e\u0432\u0430\u0440\u0438\u0449\u0430\u043c\u0438 \u0441\u043f\u0435\u043a\u0442\u0440\u043e\u043c\u0435\u0442\u0440\u0438\u0441\u0442\u0430\u043c \u0434\u043b\u044f \u0440\u0430\u0441\u0447\u0451\u0442\u0430\n"
"", None))
        self.label_guide_ppd.setText(QCoreApplication.translate("Dialog", u"\u0418\u043d\u0441\u0442\u0440\u0443\u043a\u0446\u0438\u044f \u043f\u043e \u0438\u0437\u043c\u0435\u0440\u0435\u043d\u0438\u044e \u043d\u0430 \u041f\u041f\u0414:\n"
" 1) \u0411\u0443\u0434\u0435\u0442 \u043e\u043f\u0438\u0441\u0430\u043d\u043e \u043f\u043e\u0437\u0436\u0435, \u043c\u043d\u043e\u0433\u043e \u0442\u0435\u043a\u0441\u0442\u0430 + \u043d\u044e\u0430\u043d\u0441\u043e\u0432.", None))
        self.pushButton_fun.setText(QCoreApplication.translate("Dialog", u"\u0414\u0430\u0439 \u0430\u043d\u0435\u043a\u0434\u043e\u0442, \u0445\u043e\u0447\u0443 \u0441\u043c\u0435\u044f\u0442\u044c\u0441\u044f 5 \u043c\u0438\u043d\u0443\u0442.", None))
    # retranslateUi

