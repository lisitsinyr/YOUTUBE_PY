# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'YOUTUBE_widget.ui'
##
## Created by: Qt User Interface Compiler version 6.5.0
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
from PySide6.QtWidgets import (QApplication, QGraphicsView, QLabel, QProgressBar,
    QSizePolicy, QToolButton, QWidget)
import YOUTUBE_images_rc

class Ui_YT_widget(object):
    def setupUi(self, YT_widget):
        if not YT_widget.objectName():
            YT_widget.setObjectName(u"YT_widget")
        YT_widget.resize(400, 40)
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(YT_widget.sizePolicy().hasHeightForWidth())
        YT_widget.setSizePolicy(sizePolicy)
        YT_widget.setMinimumSize(QSize(400, 40))
        YT_widget.setMaximumSize(QSize(400, 40))
        YT_widget.setStyleSheet(u"")
        self.YT_Image = QGraphicsView(YT_widget)
        self.YT_Image.setObjectName(u"YT_Image")
        self.YT_Image.setGeometry(QRect(0, 0, 40, 40))
        sizePolicy1 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.YT_Image.sizePolicy().hasHeightForWidth())
        self.YT_Image.setSizePolicy(sizePolicy1)
        self.YT_Image.setMinimumSize(QSize(40, 40))
        self.YT_Image.setMaximumSize(QSize(40, 40))
        self.YT_Caption = QLabel(YT_widget)
        self.YT_Caption.setObjectName(u"YT_Caption")
        self.YT_Caption.setGeometry(QRect(40, 0, 360, 20))
        sizePolicy1.setHeightForWidth(self.YT_Caption.sizePolicy().hasHeightForWidth())
        self.YT_Caption.setSizePolicy(sizePolicy1)
        self.YT_Caption.setTextFormat(Qt.RichText)
        self.YT_Stop = QToolButton(YT_widget)
        self.YT_Stop.setObjectName(u"YT_Stop")
        self.YT_Stop.setGeometry(QRect(380, 20, 20, 20))
        self.YT_Start = QToolButton(YT_widget)
        self.YT_Start.setObjectName(u"YT_Start")
        self.YT_Start.setGeometry(QRect(360, 20, 20, 20))
        icon = QIcon()
        iconThemeName = u"call-start"
        if QIcon.hasThemeIcon(iconThemeName):
            icon = QIcon.fromTheme(iconThemeName)
        else:
            icon.addFile(u".", QSize(), QIcon.Normal, QIcon.Off)

        self.YT_Start.setIcon(icon)
        self.YT_ProgressBar = QProgressBar(YT_widget)
        self.YT_ProgressBar.setObjectName(u"YT_ProgressBar")
        self.YT_ProgressBar.setGeometry(QRect(60, 20, 301, 20))
        sizePolicy1.setHeightForWidth(self.YT_ProgressBar.sizePolicy().hasHeightForWidth())
        self.YT_ProgressBar.setSizePolicy(sizePolicy1)
        self.YT_ProgressBar.setValue(24)
        self.YT_Delete = QToolButton(YT_widget)
        self.YT_Delete.setObjectName(u"YT_Delete")
        self.YT_Delete.setGeometry(QRect(40, 20, 20, 20))
        icon1 = QIcon()
        iconThemeName = u"application-exit"
        if QIcon.hasThemeIcon(iconThemeName):
            icon1 = QIcon.fromTheme(iconThemeName)
        else:
            icon1.addFile(u":/test/sign_out_32px.png", QSize(), QIcon.Normal, QIcon.Off)
            icon1.addFile(u":/test/sign_out_32px.png", QSize(), QIcon.Normal, QIcon.On)

        self.YT_Delete.setIcon(icon1)

        self.retranslateUi(YT_widget)

        QMetaObject.connectSlotsByName(YT_widget)
    # setupUi

    def retranslateUi(self, YT_widget):
        YT_widget.setWindowTitle(QCoreApplication.translate("YT_widget", u"Form", None))
        self.YT_Caption.setText(QCoreApplication.translate("YT_widget", u"TextLabel", None))
        self.YT_Stop.setText(QCoreApplication.translate("YT_widget", u"...", None))
        self.YT_Start.setText(QCoreApplication.translate("YT_widget", u"...", None))
        self.YT_Delete.setText("")
    # retranslateUi

