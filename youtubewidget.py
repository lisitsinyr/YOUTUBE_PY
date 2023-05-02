"""
 =======================================================
 Copyright (c) 2023
 Author:
     Lisitsin Y.R.
 Project:
     YOUTUBE_PY
     Python (PROJECTS)
 Module:
     YOUTUBEwidget.py

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
# import PySide6.QtWidgets
# import PySide6.QtGui
# import PySide6.QtCore
# from PySide6.QtGui import QPalette, QColor
# from PySide6.QtWidgets import QStyle

# from PySide6.QtWidgets import QApplication, QMainWindow
# from PySide6.QtUiTools import QUiLoader
# from PySide6.QtCore import QFile, QIODevice

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

from ui_YOUTUBEwidget import Ui_YOUTUBEwidget

#------------------------------------------
#
#------------------------------------------
# Lui_file_name1 = "YOUTUBE_FormMain.ui"
# Lui_file_name2 = "D:/PROJECTS_LYR/CHECK_LIST/05_DESKTOP/02_Python/PROJECTS_PY/YUOTUBE/YOUTUBE/YOUTUBE_FormMain.ui"

# ------------------------------------
# YOUTUBEwidget(QWidget)
# ------------------------------------
class YOUTUBEwidget(QWidget):
    """YOUTUBEwidget"""
    luClassName = 'YOUTUBEwidget'

    def __init__(self, parent=None):
    #beginfunction
        super().__init__(parent)
        self.ui = Ui_YOUTUBEwidget()
        self.ui.setupUi(self)
#endclass

#------------------------------------------
#
#------------------------------------------
def main ():
#beginfunction
    #YOUTUBEwidget = TYOUTUBEwidget()
    #YOUTUBEwidget.show()
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
