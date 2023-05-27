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
from PySide6.QtWidgets import (QApplication, QFrame, QGraphicsView, QHBoxLayout,
    QLabel, QProgressBar, QPushButton, QSizePolicy,
    QVBoxLayout, QWidget)
import YOUTUBE_images_rc

class Ui_YT_widget(object):
    def setupUi(self, YT_widget):
        if not YT_widget.objectName():
            YT_widget.setObjectName(u"YT_widget")
        YT_widget.resize(558, 76)
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(YT_widget.sizePolicy().hasHeightForWidth())
        YT_widget.setSizePolicy(sizePolicy)
        YT_widget.setMinimumSize(QSize(0, 76))
        YT_widget.setMaximumSize(QSize(16777215, 76))
        font = QFont()
        font.setPointSize(10)
        font.setBold(True)
        YT_widget.setFont(font)
        YT_widget.setStyleSheet(u"")
        self.horizontalLayout = QHBoxLayout(YT_widget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.frame_L = QFrame(YT_widget)
        self.frame_L.setObjectName(u"frame_L")
        self.frame_L.setMaximumSize(QSize(50, 16777215))
        self.frame_L.setFrameShape(QFrame.StyledPanel)
        self.frame_L.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.frame_L)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.graphicsView = QGraphicsView(self.frame_L)
        self.graphicsView.setObjectName(u"graphicsView")

        self.verticalLayout_3.addWidget(self.graphicsView)


        self.horizontalLayout.addWidget(self.frame_L)

        self.frame_R = QFrame(YT_widget)
        self.frame_R.setObjectName(u"frame_R")
        self.frame_R.setMaximumSize(QSize(30, 16777215))
        self.frame_R.setFrameShape(QFrame.StyledPanel)
        self.frame_R.setFrameShadow(QFrame.Raised)
        self.verticalLayout = QVBoxLayout(self.frame_R)
        self.verticalLayout.setSpacing(5)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.pushButton_Delete = QPushButton(self.frame_R)
        self.pushButton_Delete.setObjectName(u"pushButton_Delete")
        self.pushButton_Delete.setMinimumSize(QSize(25, 25))
        self.pushButton_Delete.setMaximumSize(QSize(25, 25))

        self.verticalLayout.addWidget(self.pushButton_Delete)

        self.pushButton_Stop = QPushButton(self.frame_R)
        self.pushButton_Stop.setObjectName(u"pushButton_Stop")
        self.pushButton_Stop.setMinimumSize(QSize(25, 25))
        self.pushButton_Stop.setMaximumSize(QSize(25, 25))
        icon = QIcon()
        icon.addFile(u":/ICONS/stop.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_Stop.setIcon(icon)

        self.verticalLayout.addWidget(self.pushButton_Stop)


        self.horizontalLayout.addWidget(self.frame_R)

        self.frame = QFrame(YT_widget)
        self.frame.setObjectName(u"frame")
        sizePolicy.setHeightForWidth(self.frame.sizePolicy().hasHeightForWidth())
        self.frame.setSizePolicy(sizePolicy)
        self.frame.setMinimumSize(QSize(0, 0))
        self.frame.setFrameShape(QFrame.Box)
        self.frame.setFrameShadow(QFrame.Raised)
        self.frame.setLineWidth(1)
        self.verticalLayout_2 = QVBoxLayout(self.frame)
        self.verticalLayout_2.setSpacing(5)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(5, 5, 5, 5)
        self.YT_Caption = QLabel(self.frame)
        self.YT_Caption.setObjectName(u"YT_Caption")
        sizePolicy.setHeightForWidth(self.YT_Caption.sizePolicy().hasHeightForWidth())
        self.YT_Caption.setSizePolicy(sizePolicy)
        self.YT_Caption.setMinimumSize(QSize(250, 15))
        self.YT_Caption.setMaximumSize(QSize(16777215, 15))
        font1 = QFont()
        font1.setPointSize(8)
        font1.setBold(True)
        self.YT_Caption.setFont(font1)
        self.YT_Caption.setTextFormat(Qt.RichText)
        self.YT_Caption.setWordWrap(True)

        self.verticalLayout_2.addWidget(self.YT_Caption)

        self.YT_StatWidget = QLabel(self.frame)
        self.YT_StatWidget.setObjectName(u"YT_StatWidget")

        self.verticalLayout_2.addWidget(self.YT_StatWidget)

        self.YT_ProgressBar = QProgressBar(self.frame)
        self.YT_ProgressBar.setObjectName(u"YT_ProgressBar")
        sizePolicy1 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Minimum)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.YT_ProgressBar.sizePolicy().hasHeightForWidth())
        self.YT_ProgressBar.setSizePolicy(sizePolicy1)
        self.YT_ProgressBar.setMinimumSize(QSize(0, 15))
        self.YT_ProgressBar.setMaximumSize(QSize(16777215, 15))
        self.YT_ProgressBar.setFont(font1)
        self.YT_ProgressBar.setValue(24)
        self.YT_ProgressBar.setAlignment(Qt.AlignCenter)

        self.verticalLayout_2.addWidget(self.YT_ProgressBar)

        self.verticalLayout_2.setStretch(0, 3)
        self.verticalLayout_2.setStretch(2, 3)

        self.horizontalLayout.addWidget(self.frame)


        self.retranslateUi(YT_widget)

        QMetaObject.connectSlotsByName(YT_widget)
    # setupUi

    def retranslateUi(self, YT_widget):
        YT_widget.setWindowTitle(QCoreApplication.translate("YT_widget", u"Form", None))
        self.pushButton_Delete.setText("")
        self.pushButton_Stop.setText("")
        self.YT_Caption.setText(QCoreApplication.translate("YT_widget", u"YT_Caption", None))
        self.YT_StatWidget.setText(QCoreApplication.translate("YT_widget", u"YT_StatWidget", None))
    # retranslateUi

