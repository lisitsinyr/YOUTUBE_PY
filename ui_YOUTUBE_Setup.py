# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'YOUTUBE_Setup.ui'
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
from PySide6.QtWidgets import (QAbstractButton, QApplication, QCheckBox, QDialog,
    QDialogButtonBox, QFormLayout, QGridLayout, QGroupBox,
    QLabel, QLayout, QLineEdit, QSizePolicy,
    QTabWidget, QToolButton, QVBoxLayout, QWidget)

class Ui_FormSetup(object):
    def setupUi(self, FormSetup):
        if not FormSetup.objectName():
            FormSetup.setObjectName(u"FormSetup")
        FormSetup.resize(640, 480)
        FormSetup.setSizeGripEnabled(False)
        FormSetup.setModal(True)
        self.buttonBox = QDialogButtonBox(FormSetup)
        self.buttonBox.setObjectName(u"buttonBox")
        self.buttonBox.setGeometry(QRect(10, 440, 621, 32))
        self.buttonBox.setOrientation(Qt.Horizontal)
        self.buttonBox.setStandardButtons(QDialogButtonBox.Cancel|QDialogButtonBox.Ok)
        self.tabWidget = QTabWidget(FormSetup)
        self.tabWidget.setObjectName(u"tabWidget")
        self.tabWidget.setGeometry(QRect(0, 0, 631, 431))
        self.tab_1 = QWidget()
        self.tab_1.setObjectName(u"tab_1")
        self.groupBox_Sheduler = QGroupBox(self.tab_1)
        self.groupBox_Sheduler.setObjectName(u"groupBox_Sheduler")
        self.groupBox_Sheduler.setGeometry(QRect(0, 230, 225, 170))
        self.gridLayout_3 = QGridLayout(self.groupBox_Sheduler)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.formLayout = QFormLayout()
        self.formLayout.setObjectName(u"formLayout")
        self.label_4 = QLabel(self.groupBox_Sheduler)
        self.label_4.setObjectName(u"label_4")

        self.formLayout.setWidget(0, QFormLayout.LabelRole, self.label_4)

        self.lineEdit_MIN = QLineEdit(self.groupBox_Sheduler)
        self.lineEdit_MIN.setObjectName(u"lineEdit_MIN")
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lineEdit_MIN.sizePolicy().hasHeightForWidth())
        self.lineEdit_MIN.setSizePolicy(sizePolicy)
        self.lineEdit_MIN.setMinimumSize(QSize(0, 22))
        self.lineEdit_MIN.setMaximumSize(QSize(16777215, 22))

        self.formLayout.setWidget(0, QFormLayout.FieldRole, self.lineEdit_MIN)

        self.label_5 = QLabel(self.groupBox_Sheduler)
        self.label_5.setObjectName(u"label_5")

        self.formLayout.setWidget(1, QFormLayout.LabelRole, self.label_5)

        self.lineEdit_HH = QLineEdit(self.groupBox_Sheduler)
        self.lineEdit_HH.setObjectName(u"lineEdit_HH")
        self.lineEdit_HH.setMinimumSize(QSize(0, 22))
        self.lineEdit_HH.setMaximumSize(QSize(16777215, 22))

        self.formLayout.setWidget(1, QFormLayout.FieldRole, self.lineEdit_HH)

        self.label_6 = QLabel(self.groupBox_Sheduler)
        self.label_6.setObjectName(u"label_6")

        self.formLayout.setWidget(2, QFormLayout.LabelRole, self.label_6)

        self.lineEdit_DD = QLineEdit(self.groupBox_Sheduler)
        self.lineEdit_DD.setObjectName(u"lineEdit_DD")
        self.lineEdit_DD.setMinimumSize(QSize(0, 22))
        self.lineEdit_DD.setMaximumSize(QSize(16777215, 22))

        self.formLayout.setWidget(2, QFormLayout.FieldRole, self.lineEdit_DD)

        self.label_7 = QLabel(self.groupBox_Sheduler)
        self.label_7.setObjectName(u"label_7")

        self.formLayout.setWidget(3, QFormLayout.LabelRole, self.label_7)

        self.lineEdit_DN = QLineEdit(self.groupBox_Sheduler)
        self.lineEdit_DN.setObjectName(u"lineEdit_DN")
        self.lineEdit_DN.setMinimumSize(QSize(0, 22))
        self.lineEdit_DN.setMaximumSize(QSize(16777215, 22))

        self.formLayout.setWidget(3, QFormLayout.FieldRole, self.lineEdit_DN)

        self.label_8 = QLabel(self.groupBox_Sheduler)
        self.label_8.setObjectName(u"label_8")

        self.formLayout.setWidget(4, QFormLayout.LabelRole, self.label_8)

        self.lineEdit_MM = QLineEdit(self.groupBox_Sheduler)
        self.lineEdit_MM.setObjectName(u"lineEdit_MM")
        self.lineEdit_MM.setMinimumSize(QSize(0, 22))
        self.lineEdit_MM.setMaximumSize(QSize(16777215, 22))

        self.formLayout.setWidget(4, QFormLayout.FieldRole, self.lineEdit_MM)


        self.gridLayout_3.addLayout(self.formLayout, 0, 0, 1, 1)

        self.groupBox_Checkbox = QGroupBox(self.tab_1)
        self.groupBox_Checkbox.setObjectName(u"groupBox_Checkbox")
        self.groupBox_Checkbox.setGeometry(QRect(240, 230, 230, 170))
        self.widget = QWidget(self.groupBox_Checkbox)
        self.widget.setObjectName(u"widget")
        self.widget.setGeometry(QRect(20, 20, 202, 136))
        self.verticalLayout = QVBoxLayout(self.widget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.checkBox_CheckBoxCliboard = QCheckBox(self.widget)
        self.checkBox_CheckBoxCliboard.setObjectName(u"checkBox_CheckBoxCliboard")
        self.checkBox_CheckBoxCliboard.setMinimumSize(QSize(200, 22))
        self.checkBox_CheckBoxCliboard.setMaximumSize(QSize(200, 22))
        self.checkBox_CheckBoxCliboard.setChecked(True)

        self.verticalLayout.addWidget(self.checkBox_CheckBoxCliboard)

        self.checkBox_CheckBoxAutoDownload = QCheckBox(self.widget)
        self.checkBox_CheckBoxAutoDownload.setObjectName(u"checkBox_CheckBoxAutoDownload")
        self.checkBox_CheckBoxAutoDownload.setMinimumSize(QSize(200, 22))
        self.checkBox_CheckBoxAutoDownload.setMaximumSize(QSize(200, 22))
        self.checkBox_CheckBoxAutoDownload.setChecked(True)

        self.verticalLayout.addWidget(self.checkBox_CheckBoxAutoDownload)

        self.checkBox_CheckBoxAutoDelete = QCheckBox(self.widget)
        self.checkBox_CheckBoxAutoDelete.setObjectName(u"checkBox_CheckBoxAutoDelete")
        self.checkBox_CheckBoxAutoDelete.setMinimumSize(QSize(200, 22))
        self.checkBox_CheckBoxAutoDelete.setMaximumSize(QSize(200, 22))
        self.checkBox_CheckBoxAutoDelete.setChecked(True)

        self.verticalLayout.addWidget(self.checkBox_CheckBoxAutoDelete)

        self.checkBox_CheckBoxSkipExists = QCheckBox(self.widget)
        self.checkBox_CheckBoxSkipExists.setObjectName(u"checkBox_CheckBoxSkipExists")
        self.checkBox_CheckBoxSkipExists.setMinimumSize(QSize(200, 22))
        self.checkBox_CheckBoxSkipExists.setMaximumSize(QSize(200, 22))
        self.checkBox_CheckBoxSkipExists.setChecked(True)

        self.verticalLayout.addWidget(self.checkBox_CheckBoxSkipExists)

        self.checkBox_CheckBoxChunk = QCheckBox(self.widget)
        self.checkBox_CheckBoxChunk.setObjectName(u"checkBox_CheckBoxChunk")
        self.checkBox_CheckBoxChunk.setMinimumSize(QSize(200, 22))
        self.checkBox_CheckBoxChunk.setMaximumSize(QSize(200, 22))
        self.checkBox_CheckBoxChunk.setChecked(True)

        self.verticalLayout.addWidget(self.checkBox_CheckBoxChunk)

        self.layoutWidget = QWidget(self.tab_1)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.layoutWidget.setGeometry(QRect(10, 160, 551, 48))
        self.verticalLayout_4 = QVBoxLayout(self.layoutWidget)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.label_PathYoutubeLoad = QLabel(self.layoutWidget)
        self.label_PathYoutubeLoad.setObjectName(u"label_PathYoutubeLoad")

        self.verticalLayout_4.addWidget(self.label_PathYoutubeLoad)

        self.gridLayout_4 = QGridLayout()
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.toolButton_PathYoutubeLoad = QToolButton(self.layoutWidget)
        self.toolButton_PathYoutubeLoad.setObjectName(u"toolButton_PathYoutubeLoad")

        self.gridLayout_4.addWidget(self.toolButton_PathYoutubeLoad, 0, 1, 1, 1)

        self.lineEdit_PathYoutubeLoad = QLineEdit(self.layoutWidget)
        self.lineEdit_PathYoutubeLoad.setObjectName(u"lineEdit_PathYoutubeLoad")

        self.gridLayout_4.addWidget(self.lineEdit_PathYoutubeLoad, 0, 0, 1, 1)


        self.verticalLayout_4.addLayout(self.gridLayout_4)

        self.widget1 = QWidget(self.tab_1)
        self.widget1.setObjectName(u"widget1")
        self.widget1.setGeometry(QRect(11, 111, 551, 48))
        self.verticalLayout_3 = QVBoxLayout(self.widget1)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.label_PathStoreError = QLabel(self.widget1)
        self.label_PathStoreError.setObjectName(u"label_PathStoreError")

        self.verticalLayout_3.addWidget(self.label_PathStoreError)

        self.gridLayout_03 = QGridLayout()
        self.gridLayout_03.setObjectName(u"gridLayout_03")
        self.toolButton_PathStoreError = QToolButton(self.widget1)
        self.toolButton_PathStoreError.setObjectName(u"toolButton_PathStoreError")

        self.gridLayout_03.addWidget(self.toolButton_PathStoreError, 0, 1, 1, 1)

        self.lineEdit_PathStoreError = QLineEdit(self.widget1)
        self.lineEdit_PathStoreError.setObjectName(u"lineEdit_PathStoreError")

        self.gridLayout_03.addWidget(self.lineEdit_PathStoreError, 0, 0, 1, 1)


        self.verticalLayout_3.addLayout(self.gridLayout_03)

        self.widget2 = QWidget(self.tab_1)
        self.widget2.setObjectName(u"widget2")
        self.widget2.setGeometry(QRect(10, 60, 551, 48))
        self.verticalLayout_2 = QVBoxLayout(self.widget2)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.label_PathStoreOut = QLabel(self.widget2)
        self.label_PathStoreOut.setObjectName(u"label_PathStoreOut")

        self.verticalLayout_2.addWidget(self.label_PathStoreOut)

        self.gridLayout_02 = QGridLayout()
        self.gridLayout_02.setObjectName(u"gridLayout_02")
        self.toolButton_PathStoreOut = QToolButton(self.widget2)
        self.toolButton_PathStoreOut.setObjectName(u"toolButton_PathStoreOut")

        self.gridLayout_02.addWidget(self.toolButton_PathStoreOut, 0, 1, 1, 1)

        self.lineEdit_PathStoreOut = QLineEdit(self.widget2)
        self.lineEdit_PathStoreOut.setObjectName(u"lineEdit_PathStoreOut")

        self.gridLayout_02.addWidget(self.lineEdit_PathStoreOut, 0, 0, 1, 1)


        self.verticalLayout_2.addLayout(self.gridLayout_02)

        self.widget3 = QWidget(self.tab_1)
        self.widget3.setObjectName(u"widget3")
        self.widget3.setGeometry(QRect(11, 11, 551, 48))
        self.verticalLayout_1 = QVBoxLayout(self.widget3)
        self.verticalLayout_1.setObjectName(u"verticalLayout_1")
        self.verticalLayout_1.setContentsMargins(0, 0, 0, 0)
        self.label_PathStore = QLabel(self.widget3)
        self.label_PathStore.setObjectName(u"label_PathStore")

        self.verticalLayout_1.addWidget(self.label_PathStore)

        self.gridLayout_01 = QGridLayout()
        self.gridLayout_01.setObjectName(u"gridLayout_01")
        self.gridLayout_01.setSizeConstraint(QLayout.SetMinAndMaxSize)
        self.lineEdit_PathStore = QLineEdit(self.widget3)
        self.lineEdit_PathStore.setObjectName(u"lineEdit_PathStore")
        sizePolicy.setHeightForWidth(self.lineEdit_PathStore.sizePolicy().hasHeightForWidth())
        self.lineEdit_PathStore.setSizePolicy(sizePolicy)
        self.lineEdit_PathStore.setMinimumSize(QSize(300, 0))

        self.gridLayout_01.addWidget(self.lineEdit_PathStore, 0, 0, 1, 1)

        self.toolButton_PathStore = QToolButton(self.widget3)
        self.toolButton_PathStore.setObjectName(u"toolButton_PathStore")

        self.gridLayout_01.addWidget(self.toolButton_PathStore, 0, 1, 1, 1)


        self.verticalLayout_1.addLayout(self.gridLayout_01)

        self.tabWidget.addTab(self.tab_1, "")
        self.tab_2 = QWidget()
        self.tab_2.setObjectName(u"tab_2")
        self.groupBox_3 = QGroupBox(self.tab_2)
        self.groupBox_3.setObjectName(u"groupBox_3")
        self.groupBox_3.setGeometry(QRect(20, 20, 341, 321))
        self.widget4 = QWidget(self.groupBox_3)
        self.widget4.setObjectName(u"widget4")
        self.widget4.setGeometry(QRect(51, 71, 202, 126))
        self.gridLayout = QGridLayout(self.widget4)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.checkBox_CheckBoxCliboard_2 = QCheckBox(self.widget4)
        self.checkBox_CheckBoxCliboard_2.setObjectName(u"checkBox_CheckBoxCliboard_2")
        self.checkBox_CheckBoxCliboard_2.setMinimumSize(QSize(200, 0))
        self.checkBox_CheckBoxCliboard_2.setMaximumSize(QSize(200, 16777215))

        self.gridLayout.addWidget(self.checkBox_CheckBoxCliboard_2, 0, 0, 1, 1)

        self.checkBox_CheckBoxAutoDownload_2 = QCheckBox(self.widget4)
        self.checkBox_CheckBoxAutoDownload_2.setObjectName(u"checkBox_CheckBoxAutoDownload_2")
        self.checkBox_CheckBoxAutoDownload_2.setMinimumSize(QSize(200, 0))
        self.checkBox_CheckBoxAutoDownload_2.setMaximumSize(QSize(200, 16777215))

        self.gridLayout.addWidget(self.checkBox_CheckBoxAutoDownload_2, 1, 0, 1, 1)

        self.checkBox_CheckBoxAutoDelete_2 = QCheckBox(self.widget4)
        self.checkBox_CheckBoxAutoDelete_2.setObjectName(u"checkBox_CheckBoxAutoDelete_2")
        self.checkBox_CheckBoxAutoDelete_2.setMinimumSize(QSize(200, 0))
        self.checkBox_CheckBoxAutoDelete_2.setMaximumSize(QSize(200, 16777215))

        self.gridLayout.addWidget(self.checkBox_CheckBoxAutoDelete_2, 2, 0, 1, 1)

        self.checkBox_CheckBoxSkipExists_2 = QCheckBox(self.widget4)
        self.checkBox_CheckBoxSkipExists_2.setObjectName(u"checkBox_CheckBoxSkipExists_2")
        self.checkBox_CheckBoxSkipExists_2.setMinimumSize(QSize(200, 0))
        self.checkBox_CheckBoxSkipExists_2.setMaximumSize(QSize(200, 16777215))

        self.gridLayout.addWidget(self.checkBox_CheckBoxSkipExists_2, 3, 0, 1, 1)

        self.checkBox_CheckBoxChunk_2 = QCheckBox(self.widget4)
        self.checkBox_CheckBoxChunk_2.setObjectName(u"checkBox_CheckBoxChunk_2")
        self.checkBox_CheckBoxChunk_2.setMinimumSize(QSize(200, 0))
        self.checkBox_CheckBoxChunk_2.setMaximumSize(QSize(200, 16777215))

        self.gridLayout.addWidget(self.checkBox_CheckBoxChunk_2, 4, 0, 1, 1)

        self.tabWidget.addTab(self.tab_2, "")

        self.retranslateUi(FormSetup)
        self.buttonBox.accepted.connect(FormSetup.accept)
        self.buttonBox.rejected.connect(FormSetup.reject)

        self.tabWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(FormSetup)
    # setupUi

    def retranslateUi(self, FormSetup):
        FormSetup.setWindowTitle(QCoreApplication.translate("FormSetup", u"Dialog", None))
        self.groupBox_Sheduler.setTitle(QCoreApplication.translate("FormSetup", u"Sheduler", None))
        self.label_4.setText(QCoreApplication.translate("FormSetup", u"\u041c\u0438\u043d\u0443\u0442\u044b", None))
        self.label_5.setText(QCoreApplication.translate("FormSetup", u"\u0427\u0430\u0441\u044b", None))
        self.label_6.setText(QCoreApplication.translate("FormSetup", u"\u0414\u043d\u0438", None))
        self.label_7.setText(QCoreApplication.translate("FormSetup", u"\u0414\u043d\u0438 \u043d\u0435\u0434\u0435\u043b\u0438", None))
        self.label_8.setText(QCoreApplication.translate("FormSetup", u"\u041c\u0435\u0441\u044f\u0446\u044b", None))
        self.groupBox_Checkbox.setTitle(QCoreApplication.translate("FormSetup", u"Checkbox", None))
        self.checkBox_CheckBoxCliboard.setText(QCoreApplication.translate("FormSetup", u"CheckBoxCliboard", None))
        self.checkBox_CheckBoxAutoDownload.setText(QCoreApplication.translate("FormSetup", u"CheckBoxAutoDownload", None))
        self.checkBox_CheckBoxAutoDelete.setText(QCoreApplication.translate("FormSetup", u"CheckBoxAutoDelete", None))
        self.checkBox_CheckBoxSkipExists.setText(QCoreApplication.translate("FormSetup", u"CheckBoxSkipExists", None))
        self.checkBox_CheckBoxChunk.setText(QCoreApplication.translate("FormSetup", u"CheckBoxChunk", None))
        self.label_PathYoutubeLoad.setText(QCoreApplication.translate("FormSetup", u"PathYoutubeLoad", None))
        self.toolButton_PathYoutubeLoad.setText(QCoreApplication.translate("FormSetup", u"...", None))
        self.label_PathStoreError.setText(QCoreApplication.translate("FormSetup", u"PathStoreError", None))
        self.toolButton_PathStoreError.setText(QCoreApplication.translate("FormSetup", u"...", None))
        self.label_PathStoreOut.setText(QCoreApplication.translate("FormSetup", u"PathStoreOut", None))
        self.toolButton_PathStoreOut.setText(QCoreApplication.translate("FormSetup", u"...", None))
        self.label_PathStore.setText(QCoreApplication.translate("FormSetup", u"PathStore", None))
        self.toolButton_PathStore.setText(QCoreApplication.translate("FormSetup", u"...", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_1), QCoreApplication.translate("FormSetup", u"\u0423\u0441\u0442\u0430\u043d\u043e\u0432\u043e\u0447\u043d\u044b\u0435 \u043f\u0430\u0440\u0430\u043c\u0435\u0442\u0440\u044b", None))
        self.groupBox_3.setTitle(QCoreApplication.translate("FormSetup", u"GroupBox", None))
        self.checkBox_CheckBoxCliboard_2.setText(QCoreApplication.translate("FormSetup", u"CheckBoxCliboard", None))
        self.checkBox_CheckBoxAutoDownload_2.setText(QCoreApplication.translate("FormSetup", u"CheckBoxAutoDownload", None))
        self.checkBox_CheckBoxAutoDelete_2.setText(QCoreApplication.translate("FormSetup", u"CheckBoxAutoDelete", None))
        self.checkBox_CheckBoxSkipExists_2.setText(QCoreApplication.translate("FormSetup", u"CheckBoxSkipExists", None))
        self.checkBox_CheckBoxChunk_2.setText(QCoreApplication.translate("FormSetup", u"CheckBoxChunk", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), QCoreApplication.translate("FormSetup", u"\u041d\u0430\u0441\u0442\u0440\u043e\u0439\u043a\u0430 YOUTUBE", None))
    # retranslateUi

