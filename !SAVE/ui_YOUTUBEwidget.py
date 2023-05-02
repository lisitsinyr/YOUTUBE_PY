# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'YOUTUBEwidget.ui'
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

class Ui_YOUTUBEwidget(object):
    def setupUi(self, YOUTUBEwidget):
        if not YOUTUBEwidget.objectName():
            YOUTUBEwidget.setObjectName(u"YOUTUBEwidget")
        YOUTUBEwidget.resize(560, 71)
        YOUTUBEwidget.setStyleSheet(u"background-color: red;")
        self.graphicsView = QGraphicsView(YOUTUBEwidget)
        self.graphicsView.setObjectName(u"graphicsView")
        self.graphicsView.setGeometry(QRect(10, 10, 51, 51))
        self.label = QLabel(YOUTUBEwidget)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(110, 10, 49, 16))
        self.toolButton = QToolButton(YOUTUBEwidget)
        self.toolButton.setObjectName(u"toolButton")
        self.toolButton.setGeometry(QRect(70, 30, 22, 22))
        self.progressBar = QProgressBar(YOUTUBEwidget)
        self.progressBar.setObjectName(u"progressBar")
        self.progressBar.setGeometry(QRect(110, 30, 281, 23))
        self.progressBar.setValue(24)
        self.toolButton_2 = QToolButton(YOUTUBEwidget)
        self.toolButton_2.setObjectName(u"toolButton_2")
        self.toolButton_2.setGeometry(QRect(70, 30, 22, 22))
        self.progressBar_2 = QProgressBar(YOUTUBEwidget)
        self.progressBar_2.setObjectName(u"progressBar_2")
        self.progressBar_2.setGeometry(QRect(110, 30, 281, 23))
        self.progressBar_2.setValue(24)
        self.toolButton_3 = QToolButton(YOUTUBEwidget)
        self.toolButton_3.setObjectName(u"toolButton_3")
        self.toolButton_3.setGeometry(QRect(400, 30, 22, 22))
        self.toolButton_4 = QToolButton(YOUTUBEwidget)
        self.toolButton_4.setObjectName(u"toolButton_4")
        self.toolButton_4.setGeometry(QRect(430, 30, 22, 22))

        self.retranslateUi(YOUTUBEwidget)

        QMetaObject.connectSlotsByName(YOUTUBEwidget)
    # setupUi

    def retranslateUi(self, YOUTUBEwidget):
        YOUTUBEwidget.setWindowTitle(QCoreApplication.translate("YOUTUBEwidget", u"Form", None))
        self.label.setText(QCoreApplication.translate("YOUTUBEwidget", u"TextLabel", None))
        self.toolButton.setText(QCoreApplication.translate("YOUTUBEwidget", u"...", None))
        self.toolButton_2.setText(QCoreApplication.translate("YOUTUBEwidget", u"...", None))
        self.toolButton_3.setText(QCoreApplication.translate("YOUTUBEwidget", u"...", None))
        self.toolButton_4.setText(QCoreApplication.translate("YOUTUBEwidget", u"...", None))
    # retranslateUi

