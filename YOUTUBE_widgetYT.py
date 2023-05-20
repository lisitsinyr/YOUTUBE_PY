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

# ------------------------------------
# Downloader_YOUTUBE(QThread)
# ------------------------------------
class Downloader_YOUTUBE(QThread):
    """Downloader_YOUTUBE"""
    luClassName = 'Downloader_YOUTUBE'

    S1CaptionText = QtCore.Signal (str)
    S1ProgressMax = QtCore.Signal (int)
    S1ProgressValue = QtCore.Signal (int)

    def __init__(self, AYouTubeObject: LUObjectsYT.TYouTubeObject, AMaxRes: ()):
    #beginfunction
        super().__init__()
        self.FYouTubeObject = AYouTubeObject
        self.FYouTubeObject.FONprogress = self.ONprogress
        # self.FYouTubeObject.FONcomplete = self.ONcomplete
        self.FMaxRes = AMaxRes
    #endfunction

    @QtCore.Slot (int,str, name = 'ONprogress')
    def ONprogress (self, AStream: pytube.Stream, AChunk: bytes, Abytes_remaining: int):
    #beginfunction
        s = 'Downloader_YOUTUBE.ONprogress...'
        QCoreApplication.processEvents ()
        if not AStream is None:
            self.FYouTubeObject.FProgressMax = AStream.filesize
            self.FYouTubeObject.FProgressLeft = Abytes_remaining
            self.FYouTubeObject.FProgressValue = self.FYouTubeObject.FProgressMax - self.FYouTubeObject.FProgressLeft
            self.S1ProgressValue.emit (self.FYouTubeObject.FProgressValue)
        #endif
    #endfunction

    @QtCore.Slot (int, str, name = 'run')
    def run(self):
    #beginfunction
        # # Открываем  URL.
        # with urlopen(self._url) as r:
        #     with open(self._filename, "wb") as f:
        #         # Чтение содержимого и запись его в новый файл.
        #         f.write(r.read())
        QCoreApplication.processEvents ()
        LULog.LoggerTOOLS.debug ('worker_YOUTUBE.DownloadURL...')
        self.FYouTubeObject.SetStream (self.FMaxRes)
        # self.FCaptionText.emit (self.FYouTubeObject.StreamInfo['default_filename'])
        self.S1ProgressMax.emit (self.FYouTubeObject.StreamInfo['filesize'])
        CPATH = 'd:\\work'
        Lfilename_prefix = ''
        self.FYouTubeObject.DownloadURL (CPATH, ADownload = True, Achunk = False, skip_existing = False)
    #endfunction
#endclass

# ------------------------------------
# worker_YOUTUBE (QtCore.QObject)
# ------------------------------------
class worker_YOUTUBE (QtCore.QObject):
    """worker_YOUTUBE"""
    luClassName = 'worker_YOUTUBE'

    log_event = QtCore.Signal(str)

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
        QCoreApplication.processEvents ()
        if not AStream is None:
            self.FYouTubeObject.FProgressMax = AStream.filesize
            self.FYouTubeObject.FProgressLeft = Abytes_remaining
            self.FYouTubeObject.FProgressValue = self.FYouTubeObject.FProgressMax - self.FYouTubeObject.FProgressLeft

            self.SProgressValue.emit (self.FYouTubeObject.FProgressValue)
        #endif
    #endfunction

    @QtCore.Slot (int,str, name = 'DownloadURL')
    def DownloadURL (self):
    #beginfunction
        QCoreApplication.processEvents ()
        LULog.LoggerTOOLS.debug ('worker_YOUTUBE.DownloadURL...')
        self.FYouTubeObject.SetStream (self.FMaxRes)

        self.SCaptionText.emit (self.FYouTubeObject.StreamInfo['default_filename'])
        self.SProgressMax.emit (self.FYouTubeObject.StreamInfo['filesize'])

        CPATH = 'd:\\work'
        Lfilename_prefix = ''
        self.FYouTubeObject.DownloadURL (CPATH, ADownload = True, Achunk = False, skip_existing = False)
    #endfunction
    def run(self):
    #beginfunction
        ...
    #endfunction
    def run_idle(self):
    #beginfunction
        self.idle = True
        self.log_event.emit('running idle... ')
        while self.idle:
            sleep(0.00001)
    #endfunction
    def process_single(self):
    #beginfunction
        self.log_event.emit('Processing item...')
        self.run_idle()
    #endfunction
#endclass

# ------------------------------------
# YOUTUBEwidget(QWidget)
# ------------------------------------
class YOUTUBEwidget(QWidget):
    """YOUTUBEwidget"""
    luClassName = 'YOUTUBEwidget'

    SDownloadURL = QtCore.Signal(str)

    #----------------------------------------------
    # Коннектор - сюда приходит signalHandlerCaptionText(str)
    #----------------------------------------------
    def signalHandlerCaptionText(self, text):
    #beginfunction
        self.ui.YT_Caption.setText(text)
    #endfunction
    #----------------------------------------------
    # Коннектор - сюда приходит signalHandlerProgressMax(int)
    #----------------------------------------------
    def signalHandlerProgressMax(self, value):
    #beginfunction
        self.ui.YT_ProgressBar.setMaximum (value)
    #endfunction
    #----------------------------------------------
    # Коннектор - сюда приходит signalHandlerProgressValue(int)
    #----------------------------------------------
    def signalHandlerProgressValue(self, value):
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

        self.FYouTubeObject = AYouTubeObject
        # self.FYouTubeObject.FONprogress = self.ONprogress
        self.FYouTubeObject.FONcomplete = self.ONcomplete
        self.FMaxRes = AMaxRes

        self.setObjectName (u"widget_X")
        self.setMinimumSize (QSize (400, 40))
        self.setMaximumSize (QSize (400, 40))
        # self.widget_X.setSizePolicy(QSizePolicy.Maximum, QSizePolicy.Maximum)
        self.ui.YT_Caption.setText (AYouTubeObject.URLInfo ['title'])
        s = AYouTubeObject.URLInfo ['thumbnail_url']
        s = AYouTubeObject.URLInfo ['author']
        self.ui.YT_ProgressBar.setMinimum (0)
        self.ui.YT_ProgressBar.setMaximum (100)
        # self.ui.YT_ProgressBar.setRange (0, 100)
        self.ui.YT_ProgressBar.setValue (0)

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
        self.FDownloader_YOUTUBE.S1CaptionText.connect(self.signalHandlerCaptionText)
        self.FDownloader_YOUTUBE.S1ProgressMax.connect (self.signalHandlerProgressMax)
        self.FDownloader_YOUTUBE.S1ProgressValue.connect (self.signalHandlerProgressValue)
        self.FDownloader_YOUTUBE.finished.connect (self.downloadFinished)

        #======================================================
        # self.timer = QtCore.QTimer (self)
        # self.timer.timeout.connect (self.close)
        # self.timer.start (17000)
        #======================================================
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

        # self.SDownloadURL.emit (self.FYouTubeObject.URL)

        # self.deleteLater ()

    #endfunction

    def downloadFinished(self):
    #beginfunction
        s = 'YOUTUBEwidget.downloadFinished...'
        # LULog.LoggerTOOLS.debug (s)
        print (s)
        s = self.FYouTubeObject.URL
        # LULog.LoggerTOOLS.debug (s)
        # print (s)

        self.SDownloadURL.emit (self.FYouTubeObject.URL)

        # self.label.setText("Файл загружен!")
        # # Сброс кнопки.
        # self.button.setEnabled(True)
        # Удаление потока после его использования.
        del self.FDownloader_YOUTUBE
    #endfunction

    def run(self):
    #beginfunction
        LULog.LoggerTOOLS.debug ('YOUTUBEwidget.run...')

        # LMaxRes = LUObjectsYT.cMaxRes480p
        # LMaxRes = self.FMaxRes
        # self.FYouTubeObject.SetStream (LMaxRes)
        # self.ui.YT_ProgressBar.setMaximum (self.FYouTubeObject.FProgressMax)

        # CPATH = 'd:\\work'
        # Lfilename_prefix = ''
        # self.FYouTubeObject.DownloadURL (CPATH, ADownload = True, Achunk = False, skip_existing = False)
        # self.FYouTubeObject.StartYouTubeThread(CPATH, ADownload=True, Achunk=False, skip_existing = True,
        #                                    filename_prefix=Lfilename_prefix)

        # self.FQThread.start ()
        self.FDownloader_YOUTUBE.start ()

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
