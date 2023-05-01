# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'YOUTUBE_FormMain.ui'
##
## Created by: Qt User Interface Compiler version 6.5.0
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
from PySide6.QtWidgets import (QAbstractScrollArea, QApplication, QFrame, QGridLayout,
    QHBoxLayout, QListView, QMainWindow, QMenu,
    QMenuBar, QPlainTextEdit, QScrollArea, QSizePolicy,
    QSplitter, QStatusBar, QToolBar, QVBoxLayout,
    QWidget)
import YOUTUBE_images_rc

class Ui_FormMainWindow(object):
    def setupUi(self, FormMainWindow):
        if not FormMainWindow.objectName():
            FormMainWindow.setObjectName(u"FormMainWindow")
        FormMainWindow.resize(755, 600)
        FormMainWindow.setInputMethodHints(Qt.ImhNone)
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
        self.layoutWidget = QWidget(self.centralwidget)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.layoutWidget.setGeometry(QRect(0, 0, 2, 2))
        self.horizontalLayout = QHBoxLayout(self.layoutWidget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout = QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.splitter_2 = QSplitter(self.centralwidget)
        self.splitter_2.setObjectName(u"splitter_2")
        sizePolicy = QSizePolicy(QSizePolicy.MinimumExpanding, QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.splitter_2.sizePolicy().hasHeightForWidth())
        self.splitter_2.setSizePolicy(sizePolicy)
        self.splitter_2.setMaximumSize(QSize(1000, 1505))
        self.splitter_2.setOrientation(Qt.Vertical)
        self.splitter_2.setOpaqueResize(True)
        self.splitter = QSplitter(self.splitter_2)
        self.splitter.setObjectName(u"splitter")
        self.splitter.setMaximumSize(QSize(16777215, 500))
        self.splitter.setOrientation(Qt.Horizontal)
        self.ListViewL = QListView(self.splitter)
        self.ListViewL.setObjectName(u"ListViewL")
        sizePolicy.setHeightForWidth(self.ListViewL.sizePolicy().hasHeightForWidth())
        self.ListViewL.setSizePolicy(sizePolicy)
        self.ListViewL.setMinimumSize(QSize(0, 0))
        self.ListViewL.setMaximumSize(QSize(300, 500))
        self.ListViewL.setSizeIncrement(QSize(0, 0))
        self.splitter.addWidget(self.ListViewL)
        self.ScrollAreaR = QScrollArea(self.splitter)
        self.ScrollAreaR.setObjectName(u"ScrollAreaR")
        self.ScrollAreaR.setLayoutDirection(Qt.LeftToRight)
        self.ScrollAreaR.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 430, 369))
        self.scrollAreaWidgetContents.setLayoutDirection(Qt.LeftToRight)
        self.verticalLayout = QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.frame_3 = QFrame(self.scrollAreaWidgetContents)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setMaximumSize(QSize(398, 50))
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Plain)

        self.verticalLayout.addWidget(self.frame_3)

        self.frame_2 = QFrame(self.scrollAreaWidgetContents)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setMaximumSize(QSize(398, 50))
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Plain)

        self.verticalLayout.addWidget(self.frame_2)

        self.frame = QFrame(self.scrollAreaWidgetContents)
        self.frame.setObjectName(u"frame")
        self.frame.setMaximumSize(QSize(398, 50))
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Plain)

        self.verticalLayout.addWidget(self.frame)

        self.frame_5 = QFrame(self.scrollAreaWidgetContents)
        self.frame_5.setObjectName(u"frame_5")
        self.frame_5.setMaximumSize(QSize(398, 50))
        self.frame_5.setFrameShape(QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QFrame.Plain)

        self.verticalLayout.addWidget(self.frame_5)

        self.frame_4 = QFrame(self.scrollAreaWidgetContents)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setMaximumSize(QSize(398, 50))
        self.frame_4.setFrameShape(QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Plain)

        self.verticalLayout.addWidget(self.frame_4)

        self.frame_6 = QFrame(self.scrollAreaWidgetContents)
        self.frame_6.setObjectName(u"frame_6")
        self.frame_6.setMaximumSize(QSize(398, 50))
        self.frame_6.setFrameShape(QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QFrame.Plain)

        self.verticalLayout.addWidget(self.frame_6)

        self.ScrollAreaR.setWidget(self.scrollAreaWidgetContents)
        self.splitter.addWidget(self.ScrollAreaR)
        self.splitter_2.addWidget(self.splitter)
        self.Memo_Log = QPlainTextEdit(self.splitter_2)
        self.Memo_Log.setObjectName(u"Memo_Log")
        sizePolicy.setHeightForWidth(self.Memo_Log.sizePolicy().hasHeightForWidth())
        self.Memo_Log.setSizePolicy(sizePolicy)
        self.Memo_Log.setMinimumSize(QSize(0, 0))
        self.Memo_Log.setMaximumSize(QSize(1000, 1000))
        font = QFont()
        font.setFamilies([u"Courier New"])
        font.setPointSize(8)
        font.setBold(True)
        self.Memo_Log.setFont(font)
        self.Memo_Log.setAutoFillBackground(True)
        self.Memo_Log.setStyleSheet(u"")
        self.Memo_Log.setInputMethodHints(Qt.ImhHiddenText|Qt.ImhSensitiveData)
        self.Memo_Log.setFrameShape(QFrame.StyledPanel)
        self.Memo_Log.setFrameShadow(QFrame.Plain)
        self.Memo_Log.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOn)
        self.Memo_Log.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOn)
        self.Memo_Log.setSizeAdjustPolicy(QAbstractScrollArea.AdjustToContents)
        self.Memo_Log.setLineWrapMode(QPlainTextEdit.NoWrap)
        self.Memo_Log.setReadOnly(True)
        self.Memo_Log.setBackgroundVisible(False)
        self.splitter_2.addWidget(self.Memo_Log)

        self.gridLayout.addWidget(self.splitter_2, 0, 0, 1, 1)

        FormMainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(FormMainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 755, 22))
        self.menu_File = QMenu(self.menubar)
        self.menu_File.setObjectName(u"menu_File")
        self.menu_Edit = QMenu(self.menubar)
        self.menu_Edit.setObjectName(u"menu_Edit")
        self.menu = QMenu(self.menubar)
        self.menu.setObjectName(u"menu")
        self.menu_Help = QMenu(self.menubar)
        self.menu_Help.setObjectName(u"menu_Help")
        FormMainWindow.setMenuBar(self.menubar)
        self.StatusBar_P1_P2 = QStatusBar(FormMainWindow)
        self.StatusBar_P1_P2.setObjectName(u"StatusBar_P1_P2")
        FormMainWindow.setStatusBar(self.StatusBar_P1_P2)
        self.toolBar = QToolBar(FormMainWindow)
        self.toolBar.setObjectName(u"toolBar")
        FormMainWindow.addToolBar(Qt.TopToolBarArea, self.toolBar)
        QWidget.setTabOrder(self.ListViewL, self.Memo_Log)

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
    # retranslateUi

