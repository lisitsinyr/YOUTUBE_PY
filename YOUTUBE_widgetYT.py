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
from time import sleep
import enum

# from gevent import sleep

#------------------------------------------
# БИБЛИОТЕКИ сторонние
#------------------------------------------
from PySide6 import QtCore

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
    QListView, QMainWindow, QMenu, QMenuBar,
    QPlainTextEdit, QScrollArea, QSizePolicy, QSplitter,
    QStatusBar, QTextEdit, QToolBar, QVBoxLayout,
    QSizePolicy, QPushButton,
    QWidget, QLabel)

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
import LUObjectsYT
import LUThread
import LUStrUtils

#------------------------------------------
# БИБЛИОТЕКИ PROJECT
#------------------------------------------
import YOUTUBE_Proc
import YOUTUBE_Params
import YOUTUBE_Consts

from ui_YOUTUBE_widget import Ui_YT_widget

@enum.unique
class TStatWidget(enum.Enum):
    """TStatWidget"""
    swNew = enum.auto ()
    swGetInfo = enum.auto ()
    swQueue = enum.auto ()
    swDownload = enum.auto ()
    swDownloaded = enum.auto ()
#endclass
CStatWidget = {
    TStatWidget.swNew: 'Новый виджет',
    TStatWidget.swGetInfo: 'swGetInfo',
    TStatWidget.swQueue: 'swQueue',
    TStatWidget.swDownload: 'swDownload',
    TStatWidget.swDownloaded: 'swDownloaded',
    }

# ------------------------------------
# GetInfoStraem_YOUTUBE
# ------------------------------------
class GetInfoStream_YOUTUBE(QThread):
    """GetInfoStream_YOUTUBE"""
    luClassName = 'GetInfoStream_YOUTUBE'

    #----------------------------------------------
    # СИГНАЛ
    #----------------------------------------------
    S1_YT_Caption = QtCore.Signal (str)
    # S1_YT_StatWidget = QtCore.Signal (str)

    def __init__(self, AYouTubeObject: LUObjectsYT.TYouTubeObject, AMaxRes: ()):
    #beginfunction
        super().__init__()
        self.FYouTubeObject = AYouTubeObject
        self.FMaxRes = AMaxRes
        self.FStartThread = False
    #endfunction

    @QtCore.Slot (int, str, name = 'run')
    def run(self):
    #beginfunction
        s = 'GetInfoStream_YOUTUBE.run...'
        # LULog.LoggerTOOLS.debug (s)
        self.FStartThread = True
        self.FYouTubeObject.SetStream (self.FMaxRes)

        # self.S1_YT_Caption_InfoStream.emit (self.FYouTubeObject.StreamInfo['default_filename'])
        self.S1_YT_Caption.emit (s)
    #endfunction
#endclass

# ------------------------------------
# Downloader_YOUTUBE(QThread)
# ------------------------------------
class Downloader_YOUTUBE (QThread):
    """Downloader_YOUTUBE"""
    luClassName = 'Downloader_YOUTUBE'

    #----------------------------------------------
    # СИГНАЛ
    #----------------------------------------------
    S1_YT_Caption = QtCore.Signal (str)
    S1_ProgressMax = QtCore.Signal (int)
    S1_ProgressValue = QtCore.Signal (int)

    def __init__ (self, AYouTubeObject: LUObjectsYT.TYouTubeObject, AMaxRes: ()):
        #beginfunction
        super ().__init__ ()
        self.FYouTubeObject = AYouTubeObject
        self.FYouTubeObject.FONprogress = self.ONprogress
        # self.FYouTubeObject.FONcomplete = self.ONcomplete
        self.FMaxRes = AMaxRes
        self.FStartThread = False
    #endfunction

    @QtCore.Slot (int, str, name = 'ONprogress')
    def ONprogress (self, AStream: pytube.Stream, AChunk: bytes, Abytes_remaining: int):
    #beginfunction
        s = 'Downloader_YOUTUBE.ONprogress...'
        if not AStream is None:
            self.FYouTubeObject.FProgressMax = AStream.filesize
            self.FYouTubeObject.FProgressLeft = Abytes_remaining
            self.FYouTubeObject.FProgressValue = self.FYouTubeObject.FProgressMax - self.FYouTubeObject.FProgressLeft
            self.S1_ProgressValue.emit (self.FYouTubeObject.FProgressValue)
        #endif
        QCoreApplication.processEvents ()
    #endfunction

    @QtCore.Slot (int, str, name = 'run')
    def run (self):
        """"""
    #beginfunction
        s = 'Downloader_YOUTUBE.run...'
        # LULog.LoggerTOOLS.debug (s)
        self.FStartThread = True

        # self.FYouTubeObject.SetStream (self.FMaxRes)
        try:
            self.S1_YT_Caption.emit (self.FYouTubeObject.StreamInfo['default_filename'])
        except:
            self.S1_YT_Caption.emit ('Error! default_filename')
        #endtry
        try:
            self.S1_ProgressMax.emit (self.FYouTubeObject.StreamInfo ['filesize'])
        except:
            self.S1_ProgressMax.emit (0)
        #endtry
        CPATH = 'd:\\work'
        Lfilename_prefix = ''
        self.FYouTubeObject.DownloadURL (CPATH, ADownload = True, Achunk = False, skip_existing = False)
    #endfunction

#endclass

'''
# ------------------------------------
# worker_YOUTUBE (QtCore.QObject)
# ------------------------------------
class worker_YOUTUBE (QtCore.QObject):
    """worker_YOUTUBE"""
    luClassName = 'worker_YOUTUBE'

    # log_event = QtCore.Signal(str)

    #----------------------------------------------
    # СИГНАЛ
    #----------------------------------------------
    SCaptionText = QtCore.Signal(str)
    SProgressMax = QtCore.Signal(int)
    SProgressValue = QtCore.Signal(int)

    def __init__(self, AYouTubeObject: LUObjectsYT.TYouTubeObject, AMaxRes: (), parent):
    #beginfunction
        QtCore.QObject.__init__(self)
        self.parent = parent
        self.idle = False

        self.FYouTubeObject = AYouTubeObject
        self.FYouTubeObject.FONprogress = self.ONprogress
        # self.FYouTubeObject.FONcomplete = self.ONcomplete

        self.FMaxRes = AMaxRes
    #endfunction

    @QtCore.Slot (int,str, name = 'ONprogress')
    def ONprogress (self, AStream: pytube.Stream, AChunk: bytes, Abytes_remaining: int):
    #beginfunction
        s = 'worker_YOUTUBE.ONprogress...'
        if not AStream is None:
            self.FYouTubeObject.FProgressMax = AStream.filesize
            self.FYouTubeObject.FProgressLeft = Abytes_remaining
            self.FYouTubeObject.FProgressValue = self.FYouTubeObject.FProgressMax - self.FYouTubeObject.FProgressLeft

            self.SProgressValue.emit (self.FYouTubeObject.FProgressValue)
        #endif
        QCoreApplication.processEvents ()
    #endfunction

    @QtCore.Slot (int,str, name = 'DownloadURL')
    def DownloadURL (self):
    #beginfunction
        s = 'worker_YOUTUBE.DownloadURL...'
        # LULog.LoggerTOOLS.debug (s)

        # self.FYouTubeObject.SetStream (self.FMaxRes)

        self.SCaptionText.emit (self.FYouTubeObject.StreamInfo['default_filename'])
        self.SProgressMax.emit (self.FYouTubeObject.StreamInfo['filesize'])

        CPATH = 'd:\\work'
        Lfilename_prefix = ''
        self.FYouTubeObject.DownloadURL (CPATH, ADownload = True, Achunk = False, skip_existing = False)
        QCoreApplication.processEvents ()
    #endfunction
#endclass
'''

# ------------------------------------
# YOUTUBEwidget(QWidget)
# ------------------------------------
class YOUTUBEwidget(QWidget):
    """YOUTUBEwidget"""
    luClassName = 'YOUTUBEwidget'

    #----------------------------------------------
    # СИГНАЛ
    #----------------------------------------------
    SDownloadURL = QtCore.Signal(str)
    S1_YT_StatWidget = QtCore.Signal (str)

    #----------------------------------------------
    # Коннектор - сюда приходит signalHandlerCaptionText(str)
    #----------------------------------------------
    def signalHandler_YT_Caption(self, text):
    #beginfunction
        self.ui.YT_Caption.setText(text)
    #endfunction
    #----------------------------------------------
    # Коннектор - сюда приходит signalHandlerCaptionText(str)
    #----------------------------------------------
    def signalHandler_YT_StatWidget(self, text):
    #beginfunction
        self.ui.YT_StatWidget.setText(text)
    #endfunction
    #----------------------------------------------
    # Коннектор - сюда приходит signalHandlerProgressMax(int)
    #----------------------------------------------
    def signalHandler_ProgressMax(self, value):
    #beginfunction
        self.ui.YT_ProgressBar.setMaximum (value)
    #endfunction
    #----------------------------------------------
    # Коннектор - сюда приходит signalHandlerProgressValue(int)
    #----------------------------------------------
    def signalHandler_ProgressValue(self, value):
    #beginfunction
        self.ui.YT_ProgressBar.setValue(value)
        # if self.ui.YT_ProgressBar.value() < 80:
        #     self.ui.YT_ProgressBar.setStyleSheet(self.safe)
        # else:
        #     self.ui.YT_ProgressBar.setStyleSheet(self.danger)
    #endfunction

    def __init__(self, AYouTubeObject: LUObjectsYT.TYouTubeObject, AMaxRes, parent):
    #beginfunction
        super().__init__(parent)
        self.ui = Ui_YT_widget()
        self.ui.setupUi(self)

        self.FStatWidget: TStatWidget = TStatWidget.swNew

        self.FYouTubeObject = AYouTubeObject
        # self.FYouTubeObject.FONprogress = self.ONprogress
        self.FYouTubeObject.FONcomplete = self.ONcomplete
        self.FMaxRes = AMaxRes
        s = AYouTubeObject.URLInfo ['thumbnail_url']
        s = AYouTubeObject.URLInfo ['author']

        # self.setObjectName (u"widget_X")
        # self.setMinimumSize (QSize (400, 40))
        # self.setMaximumSize (QSize (400, 40))
        # self.setMinimumSize (QSize (0, 40))
        # self.setMinimumSize (QSize (0, 800))
        # self.setMaximumSize (QSize (16777215, 16777215))
        # self.setStyleSheet (u"background-color: rgb(0, 0, 255);")
        # self.setSizePolicy(QSizePolicy.Maximum, QSizePolicy.Maximum)


        # sizePolicy2 = QSizePolicy (QSizePolicy.Expanding, QSizePolicy.Preferred)
        # sizePolicy2.setHorizontalStretch (0)
        # sizePolicy2.setVerticalStretch (0)
        # sizePolicy2.setHeightForWidth (self.ui.YT_ProgressBar.sizePolicy ().hasHeightForWidth ())
        # self.ui.YT_ProgressBar.setSizePolicy (sizePolicy2)
        # self.ui.YT_ProgressBar.setAlignment (Qt.AlignBottom | Qt.AlignHCenter)
        # self.ui.YT_ProgressBar.setOrientation (Qt.Horizontal)
        # self.ui.YT_ProgressBar.setMinimumSize (QSize (40, 800))
        # self.ui.YT_ProgressBar.setMaximumSize (QSize (16777215, 16777215))
        self.ui.YT_ProgressBar.setMinimum (0)
        self.ui.YT_ProgressBar.setMaximum (100)
        # self.ui.YT_ProgressBar.setRange (0, 100)
        self.ui.YT_ProgressBar.setValue (0)
        self.ui.YT_ProgressBar.hide()

        #======================================================
        self.danger = 'QProgressBar::chunk {background: QLinearGradient(\
            x1: 0, y1: 0, x2: 1, y2: 0,stop: 0 #FF0350,stop: 0.4999 #00d920,stop: 0.5\
            #FF0019,stop: 1 #ff0000 );border-bottom-right-radius: 5px;border-bottom-\
            left-radius: 5px;border: .px solid black;}'
        self.safe = 'QProgressBar::chunk {background: QLinearGradient(\
            x1: 0, y1: 0, x2: 1, y2: 0,stop: 0 #78d,stop: 0.4999 #46a,stop: 0.5\
            #45a,stop: 1 #238 );border-bottom-right-radius: 7px;border-bottom-left-\
            radius: 7px;border: 1px solid black;}'
        # self.ui.YT_ProgressBar.setStyleSheet (self.safe)
        #======================================================

        # #----------------------------------------------
        # # 1 вариант
        # #----------------------------------------------
        # self.FQThread = QtCore.QThread ()
        # #----------------------------------------------
        # # Отправитель - отсюда исходят сигналы - int и str
        # #----------------------------------------------
        # self.Fworker_YOUTUBE = worker_YOUTUBE (AYouTubeObject, AMaxRes, None)
        # self.Fworker_YOUTUBE.moveToThread (self.FQThread)
        # # сигналы
        # self.Fworker_YOUTUBE.SCaptionText.connect (self.signalHandlerCaptionText)
        # self.Fworker_YOUTUBE.SProgressMax.connect (self.signalHandlerProgressMax)
        # self.Fworker_YOUTUBE.SProgressValue.connect (self.signalHandlerProgressValue)
        # # функция запуска
        # self.FQThread.started.connect (self.Fworker_YOUTUBE.DownloadURL)

        #----------------------------------------------
        # 2 вариант
        #----------------------------------------------
        self.FDownloader_YOUTUBE = Downloader_YOUTUBE (AYouTubeObject, AMaxRes)
        # сигналы
        self.FDownloader_YOUTUBE.S1_YT_Caption.connect(self.signalHandler_YT_Caption)
        self.FDownloader_YOUTUBE.S1_ProgressMax.connect (self.signalHandler_ProgressMax)
        self.FDownloader_YOUTUBE.S1_ProgressValue.connect (self.signalHandler_ProgressValue)
        self.FDownloader_YOUTUBE.finished.connect (self.qthreadFinished_Downloader_YOUTUBE)

        self.FGetInfoStream_YOUTUBE = GetInfoStream_YOUTUBE (AYouTubeObject, AMaxRes)
        # сигналы
        self.FGetInfoStream_YOUTUBE.S1_YT_Caption.connect (self.signalHandler_YT_Caption)
        self.FGetInfoStream_YOUTUBE.finished.connect (self.qthreadFinished_GetInfoStream_YOUTUBE)




        self.S1_YT_StatWidget.connect (self.signalHandler_YT_StatWidget)

        self.signalHandler_YT_Caption (AYouTubeObject.URL)
        # self.ui.YT_Caption.setText (AYouTubeObject.URL)
        s = CStatWidget[self.FStatWidget]
        self.signalHandler_YT_StatWidget (s)
        # self.ui.YT_StatWidget.setText (AYouTubeObject.URL)

        self.ui.YT_StatWidget.show ()

    #endfunction
    def ONcomplete (self, AStream: pytube.Stream, AFilePath: str):
    #beginfunction
        s = 'YOUTUBEwidget.ONcomplete...'
        # LULog.LoggerTOOLS.debug (s)
        QCoreApplication.processEvents ()
        if not AStream is None:
            LProgressMax = AStream.filesize
            LProgressLeft = 0
            LProgressValue = LProgressMax - LProgressLeft
            if not AFilePath is None:
                LFileName = LUStrUtils.PrintableStr (AFilePath)
                # LULog.LoggerTOOLS.debug ('Файл ' + LFileName + ' загружен')
            #endif
        #endif
    #endfunction

    @QtCore.Slot (str, name = 'qthreadFinished_Downloader_YOUTUBE')
    def qthreadFinished_Downloader_YOUTUBE(self):
    #beginfunction
        s = 'YOUTUBEwidget.qthreadFinished_Downloader_YOUTUBE...'
        # LULog.LoggerTOOLS.debug (s)
        s = self.FYouTubeObject.URL

        self.SDownloadURL.emit (self.FYouTubeObject.URL)

        self.FStatWidget = TStatWidget.swDownloaded

        # self.label.setText("Файл загружен!")
        # # Сброс кнопки.
        # self.button.setEnabled(True)
        # Удаление потока после его использования.
        del self.FDownloader_YOUTUBE
    #endfunction

    def run_Downloader(self):
        """run_Downloader"""
    #beginfunction
        s = 'YOUTUBEwidget.run_Downloader...'
        # LULog.LoggerTOOLS.debug (s)
        """
        # LMaxRes = LUObjectsYT.cMaxRes480p
        # LMaxRes = self.FMaxRes
        # self.FYouTubeObject.SetStream (LMaxRes)
        # self.ui.YT_ProgressBar.setMaximum (self.FYouTubeObject.FProgressMax)
        """
        """
        # CPATH = 'd:\\work'
        # Lfilename_prefix = ''
        # self.FYouTubeObject.DownloadURL (CPATH, ADownload = True, Achunk = False, skip_existing = False)
        # self.FYouTubeObject.StartYouTubeThread(CPATH, ADownload=True, Achunk=False, skip_existing = True,
        #                                    filename_prefix=Lfilename_prefix)
        """
        """
        self.FQThread.start ()
        """

        self.ui.YT_StatWidget.hide ()

        self.ui.YT_ProgressBar.show()
        self.FDownloader_YOUTUBE.start ()
    #endfunction

    @QtCore.Slot (str, name = 'qthreadFinished_GetInfoStream_YOUTUBE')
    def qthreadFinished_GetInfoStream_YOUTUBE (self):
        #beginfunction
        s = 'YOUTUBEwidget.qthreadFinished_GetInfoStream_YOUTUBE...'
        # LULog.LoggerTOOLS.debug (s)
        s = self.FYouTubeObject.URL
        # self.SDownloadURL.emit (self.FYouTubeObject.URL)
        self.FStatWidget = TStatWidget.swGetInfo
        s = CStatWidget [self.FStatWidget]
        s = 'Получена информация...'
        self.S1_YT_StatWidget.emit (s)

        # Удаление потока, после его использования.
        del self.FGetInfoStream_YOUTUBE
    #endfunction

    def run_GetInfoStream(self):
        """run_GetInfoStream"""
    #beginfunction
        s = 'YOUTUBEwidget.run_GetInfoStream...'
        # LULog.LoggerTOOLS.debug (s)

        self.ui.YT_StatWidget.show ()
        self.FGetInfoStream_YOUTUBE.start ()
    #endfunction

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
