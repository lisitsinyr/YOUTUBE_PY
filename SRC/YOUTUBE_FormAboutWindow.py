"""
 =======================================================
 Copyright (c) 2023
 Author:
     Lisitsin Y.R.
 Project:
     YOUTUBE_PY
     Python (PROJECTS)
 Module:
     YOUTUBE_FormMainWindow.py

 =======================================================
"""

#------------------------------------------
# БИБЛИОТЕКИ python
#------------------------------------------
import os
import sys
import time
import datetime

#------------------------------------------
# БИБЛИОТЕКИ сторонние
#------------------------------------------
from  PySide6 import QtCore

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt, QObject, QThread, Signal, Slot,
    QStringListModel, QModelIndex)

from PySide6.QtGui import (QAction, QBrush, QColor, QConicalGradient,
    QCursor, QFont, QFontDatabase, QGradient,
    QIcon, QImage, QKeySequence, QLinearGradient,
    QPainter, QPalette, QPixmap, QRadialGradient,
    QTransform,
    QClipboard)

from PySide6.QtWidgets import (
    QAbstractScrollArea, QApplication, QFrame, QHBoxLayout, QVBoxLayout,
    QListView, QMainWindow, QMenu, QMenuBar, QDialog,
    QPlainTextEdit, QScrollArea, QSizePolicy, QSplitter,
    QStatusBar, QTextEdit, QToolBar, QVBoxLayout,
    QSizePolicy, QPushButton,
    QWidget, QLabel)

#------------------------------------------
# БИБЛИОТЕКИ LU
#------------------------------------------
import LULog
import LUFile
import LUProc
import LUos
import LUObjectsYT
import LUDateTime
import LUStrUtils
import LUDecotators
import LUSheduler
import LUConsole
import LUQTimer

#------------------------------------------
# БИБЛИОТЕКИ PROJECT
#------------------------------------------
import YOUTUBE_Proc
import YOUTUBE_Params
import YOUTUBE_Consts
import YOUTUBE_widgetYT

from ui_YOUTUBE_FormMain import Ui_FormMainWindow

from ui_YOUTUBE_widget import Ui_YT_widget
from YOUTUBE_widgetYT import YOUTUBEwidget
from ui_YOUTUBE_About import Ui_FormAbout
from ui_YOUTUBE_Setup import Ui_FormSetup

# ------------------------------------
# FormAbout(QDialog)
# ------------------------------------
class FormAbout (QDialog):
    """FormAbout"""
    luClassName = 'FormAbout'
    def __init__(self, parent=None):
    #beginfunction
        super().__init__(parent=parent)
        self.ui = Ui_FormAbout()
        self.ui.setupUi(self)

        # self.buttonBox.accepted.connect (FormAbout.accept)
        # self.buttonBox.rejected.connect (FormAbout.reject)

    #endfunction
    #--------------------------------------------------
    # destructor
    #--------------------------------------------------
    def __del__ (self):
        """__del__"""
    #beginfunction
        LClassName = self.__class__.__name__
        s = '{} уничтожен'.format(LClassName)
        #print (s)
    #endfunction

    def submitclose(self):
        #do whatever you need with self.roiGroups
        self.accept()
#endclass

#------------------------------------------
#
#------------------------------------------
def main ():
#beginfunction
    ...
#endfunction

#------------------------------------------
#
#------------------------------------------
#beginmodule
if __name__ == "__main__":
    main()
#endif

#endmodule
