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
from PySide6.QtWidgets import (QAbstractButton, QApplication, QDialog, QDialogButtonBox,
    QSizePolicy, QWidget)

class Ui_FormSetup(object):
    def setupUi(self, FormSetup):
        if not FormSetup.objectName():
            FormSetup.setObjectName(u"FormSetup")
        FormSetup.resize(640, 480)
        self.buttonBox = QDialogButtonBox(FormSetup)
        self.buttonBox.setObjectName(u"buttonBox")
        self.buttonBox.setGeometry(QRect(10, 440, 621, 32))
        self.buttonBox.setOrientation(Qt.Horizontal)
        self.buttonBox.setStandardButtons(QDialogButtonBox.Cancel|QDialogButtonBox.Ok)

        self.retranslateUi(FormSetup)
        self.buttonBox.accepted.connect(FormSetup.accept)
        self.buttonBox.rejected.connect(FormSetup.reject)

        QMetaObject.connectSlotsByName(FormSetup)
    # setupUi

    def retranslateUi(self, FormSetup):
        FormSetup.setWindowTitle(QCoreApplication.translate("FormSetup", u"Dialog", None))
    # retranslateUi

