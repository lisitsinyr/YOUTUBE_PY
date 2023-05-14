"""
 =======================================================
 Copyright (c) 2023
 Author:
     Lisitsin Y.R.
 Project:
     YOUTUBE_PY
     Python (PROJECTS)
 Module:
     YOUTUBE_widgetYT.py

 =======================================================
"""

#------------------------------------------
# БИБЛИОТЕКИ python
#------------------------------------------
import os
import sys

#------------------------------------------
# БИБЛИОТЕКИ сторонние
#------------------------------------------
from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt,
    QStringListModel, QModelIndex)
from PySide6.QtGui import (QAction, QBrush, QColor, QConicalGradient,
    QCursor, QFont, QFontDatabase, QGradient,
    QIcon, QImage, QKeySequence, QLinearGradient,
    QPainter, QPalette, QPixmap, QRadialGradient,
    QTransform,
    QClipboard)
from PySide6.QtWidgets import (QAbstractScrollArea, QApplication, QFrame, QGridLayout,
    QHBoxLayout, QListView, QMainWindow, QMenu,
    QMenuBar, QPlainTextEdit, QScrollArea, QSizePolicy,
    QSplitter, QStatusBar, QToolBar, QVBoxLayout,
    QWidget,
    QLabel)



# from PyQt6.QtWidgets import QApplication, QMainWindow, QWidget, QLabel, QPushButton, QVBoxLayout, QProgressBar
# from PyQt6.QtCore import QThread, QObject, pyqtSignal as Signal, pyqtSlot as Slot

import pytube
import pytube.exceptions

#------------------------------------------
# БИБЛИОТЕКИ LU
#------------------------------------------
import LULog
import LUFile
import LUProc
import LUos
# import LUParserARG
import LUYouTube
from LUObjectsYT import *
import LUThread

#------------------------------------------
# БИБЛИОТЕКИ PROJECT
#------------------------------------------
import YOUTUBE_Proc
import YOUTUBE_Params
import YOUTUBE_Consts

from ui_YOUTUBE_widget import Ui_YT_widget

# ------------------------------------
# YOUTUBE(QObject)
# ------------------------------------
class worker_YOUTUBE(QObject):
    """worker_YOUTUBE"""
    luClassName = 'worker_YOUTUBE'

    def __init__(self, A):
    #beginfunction
        super().__init__()
        self.FA = A
        ...
    #endfunction
#endclass

# ------------------------------------
# YOUTUBEwidget(QWidget)
# ------------------------------------
class YOUTUBEwidget(QWidget):
    """YOUTUBEwidget"""
    luClassName = 'YOUTUBEwidget'

    def __init__(self, parent=None):
    #beginfunction
        super().__init__(parent)
        self.ui = Ui_YT_widget()
        self.ui.setupUi(self)
        self.FA = worker_YOUTUBE(None)

        # self.FA.moveToThread()
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
