# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'YOUTUBE_FormMain.ui'
##
## Created by: Qt User Interface Compiler version 6.4.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QAction, QBrush, QColor, QConicalGradient,
    QCursor, QFont, QFontDatabase, QGradient,
    QIcon, QImage, QKeySequence, QLinearGradient,
    QPainter, QPalette, QPixmap, QRadialGradient,
    QTransform)
from PySide6.QtWidgets import (QApplication, QMainWindow, QMenu, QMenuBar,
    QSizePolicy, QStatusBar, QToolBar, QWidget)
import YOUTUBE_images_rc

class Ui_FormMainWindow(object):
    def setupUi(self, FormMainWindow):
        if not FormMainWindow.objectName():
            FormMainWindow.setObjectName(u"FormMainWindow")
        FormMainWindow.resize(734, 509)
        self.action_CreateYoutube = QAction(FormMainWindow)
        self.action_CreateYoutube.setObjectName(u"action_CreateYoutube")
        self.action_CreateYoutube.setCheckable(True)
        self.action_CreateYoutube.setChecked(True)
        icon = QIcon()
        icon.addFile(u"icons8-\u043e\u0431\u0441\u043b\u0443\u0436\u0438\u0432\u0430\u043d\u0438\u0435-48.png", QSize(), QIcon.Normal, QIcon.Off)
        self.action_CreateYoutube.setIcon(icon)
        self.action_Exit = QAction(FormMainWindow)
        self.action_Exit.setObjectName(u"action_Exit")
        self.action_Exit.setCheckable(True)
        icon1 = QIcon()
        icon1.addFile(u":/test/sign_out_32px.png", QSize(), QIcon.Normal, QIcon.Off)
        self.action_Exit.setIcon(icon1)
        self.action_Exit.setProperty("clicked()", False)
        self.action_Action_Cut = QAction(FormMainWindow)
        self.action_Action_Cut.setObjectName(u"action_Action_Cut")
        self.action_Action_Copy = QAction(FormMainWindow)
        self.action_Action_Copy.setObjectName(u"action_Action_Copy")
        self.action_Action_Paste = QAction(FormMainWindow)
        self.action_Action_Paste.setObjectName(u"action_Action_Paste")
        self.action_Setup = QAction(FormMainWindow)
        self.action_Setup.setObjectName(u"action_Setup")
        icon2 = QIcon()
        iconThemeName = u"applications-engineering"
        if QIcon.hasThemeIcon(iconThemeName):
            icon2 = QIcon.fromTheme(iconThemeName)
        else:
            icon2.addFile(u":/test/sign_out_32px.png", QSize(), QIcon.Normal, QIcon.On)

        self.action_Setup.setIcon(icon2)
        self.action_Setup.setVisible(True)
        self.centralwidget = QWidget(FormMainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        FormMainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(FormMainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 734, 22))
        self.menu_File = QMenu(self.menubar)
        self.menu_File.setObjectName(u"menu_File")
        self.menu_Edit = QMenu(self.menubar)
        self.menu_Edit.setObjectName(u"menu_Edit")
        self.menu = QMenu(self.menubar)
        self.menu.setObjectName(u"menu")
        self.menu_Help = QMenu(self.menubar)
        self.menu_Help.setObjectName(u"menu_Help")
        FormMainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(FormMainWindow)
        self.statusbar.setObjectName(u"statusbar")
        FormMainWindow.setStatusBar(self.statusbar)
        self.toolBar = QToolBar(FormMainWindow)
        self.toolBar.setObjectName(u"toolBar")
        FormMainWindow.addToolBar(Qt.TopToolBarArea, self.toolBar)
        self.toolBar_2 = QToolBar(FormMainWindow)
        self.toolBar_2.setObjectName(u"toolBar_2")
        FormMainWindow.addToolBar(Qt.TopToolBarArea, self.toolBar_2)

        self.menubar.addAction(self.menu_File.menuAction())
        self.menubar.addAction(self.menu_Edit.menuAction())
        self.menubar.addAction(self.menu.menuAction())
        self.menubar.addAction(self.menu_Help.menuAction())
        self.menu_File.addAction(self.action_CreateYoutube)
        self.menu_File.addAction(self.action_Exit)
        self.menu_Edit.addAction(self.action_Action_Cut)
        self.menu_Edit.addAction(self.action_Action_Copy)
        self.menu_Edit.addAction(self.action_Action_Paste)
        self.menu.addAction(self.action_Setup)
        self.toolBar.addAction(self.action_Exit)
        self.toolBar.addAction(self.action_CreateYoutube)
        self.toolBar.addAction(self.action_Setup)

        self.retranslateUi(FormMainWindow)
        self.action_Exit.triggered.connect(FormMainWindow.close)

        QMetaObject.connectSlotsByName(FormMainWindow)
    # setupUi

    def retranslateUi(self, FormMainWindow):
        FormMainWindow.setWindowTitle(QCoreApplication.translate("FormMainWindow", u"FormMainWindow", None))
        self.action_CreateYoutube.setText(QCoreApplication.translate("FormMainWindow", u"\u0421\u043e\u0437\u0434\u0430\u0442\u044c Youtube", None))
#if QT_CONFIG(tooltip)
        self.action_CreateYoutube.setToolTip(QCoreApplication.translate("FormMainWindow", u"\u0421\u043e\u0437\u0434\u0430\u0442\u044c Youtube", None))
#endif // QT_CONFIG(tooltip)
        self.action_Exit.setText(QCoreApplication.translate("FormMainWindow", u"\u0412\u044b\u0445\u043e\u0434", None))
        self.action_Action_Cut.setText(QCoreApplication.translate("FormMainWindow", u"Action_Cut", None))
        self.action_Action_Copy.setText(QCoreApplication.translate("FormMainWindow", u"Action_Copy", None))
        self.action_Action_Paste.setText(QCoreApplication.translate("FormMainWindow", u"Action_Paste", None))
        self.action_Setup.setText(QCoreApplication.translate("FormMainWindow", u"\u041d\u0430\u0441\u0442\u0440\u043e\u0439\u043a\u0430", None))
        self.menu_File.setTitle(QCoreApplication.translate("FormMainWindow", u"File", None))
        self.menu_Edit.setTitle(QCoreApplication.translate("FormMainWindow", u"Edit", None))
        self.menu.setTitle(QCoreApplication.translate("FormMainWindow", u"\u041d\u0430\u0441\u0442\u0440\u043e\u0439\u043a\u0430", None))
        self.menu_Help.setTitle(QCoreApplication.translate("FormMainWindow", u"\u0421\u043f\u0440\u0430\u0432\u043a\u0430 \u043f\u043e \u043f\u0440\u043e\u0433\u0440\u0430\u043c\u043c\u0435", None))
        self.toolBar.setWindowTitle(QCoreApplication.translate("FormMainWindow", u"toolBar", None))
        self.toolBar_2.setWindowTitle(QCoreApplication.translate("FormMainWindow", u"toolBar_2", None))
    # retranslateUi

