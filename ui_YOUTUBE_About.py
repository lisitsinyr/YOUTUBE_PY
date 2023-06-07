# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'YOUTUBE_About.ui'
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

class Ui_FormAbout(object):
    def setupUi(self, FormAbout):
        if not FormAbout.objectName():
            FormAbout.setObjectName(u"FormAbout")
        FormAbout.resize(400, 300)
        self.buttonBox = QDialogButtonBox(FormAbout)
        self.buttonBox.setObjectName(u"buttonBox")
        self.buttonBox.setGeometry(QRect(30, 240, 341, 32))
        self.buttonBox.setOrientation(Qt.Horizontal)
        self.buttonBox.setStandardButtons(QDialogButtonBox.Cancel|QDialogButtonBox.Ok)

        self.retranslateUi(FormAbout)
        self.buttonBox.accepted.connect(FormAbout.accept)
        self.buttonBox.rejected.connect(FormAbout.reject)

        QMetaObject.connectSlotsByName(FormAbout)
    # setupUi

    def retranslateUi(self, FormAbout):
        FormAbout.setWindowTitle(QCoreApplication.translate("FormAbout", u"Dialog", None))
    # retranslateUi

