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
import time
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
class TStatWidgetObject(enum.Enum):
    """TStatWidget"""
    swNew = enum.auto ()
    swGetInfo = enum.auto ()
    swQueue = enum.auto ()
    swDownload = enum.auto ()
    swDownloaded = enum.auto ()
#endclass
CStatWidgetObject = {
    TStatWidgetObject.swNew: 'Новый виджет',
    TStatWidgetObject.swGetInfo: 'swGetInfo',
    TStatWidgetObject.swQueue: 'swQueue',
    TStatWidgetObject.swDownload: 'swDownload',
    TStatWidgetObject.swDownloaded: 'swDownloaded',
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
    signal_YT_Caption = QtCore.Signal (str)
    # S1_YT_StatWidget = QtCore.Signal (str)

    def __init__(self, AYouTubeObject: LUObjectsYT.TYouTubeObject, AMaxRes: ()):
    #beginfunction
        super().__init__()
        self.__FYouTubeObject = AYouTubeObject
        self.__FMaxRes = AMaxRes
        self.__FStartDownload = False
    #endfunction

    #--------------------------------------------------
    # @property StartDownload
    #--------------------------------------------------
    # getter
    @property
    def StartDownload (self) -> bool:
    #beginfunction
        return self.__FStartDownload
    #endfunction
    @StartDownload.setter
    def StartDownload (self, Value: bool):
    #beginfunction
        self.__FStartDownload = Value
    #endfunction

    @QtCore.Slot (int, str, name = 'GetInfoStream_YOUTUBE.run')
    def run(self):
    #beginfunction
        s = 'GetInfoStream_YOUTUBE.run...'
        # LULog.LoggerTOOLS.debug (s)
        self.__FStartDownload = True
        self.__FYouTubeObject.SetStream (self.__FMaxRes)
        self.signal_YT_Caption.emit (s)
    #endfunction
#endclass

# ------------------------------------
# TDownloader_YOUTUBESignals
# ------------------------------------
class TDownloader_YOUTUBE_Signals(QObject):
    signal_YT_Caption = QtCore.Signal (str)
    signal_ProgressMax = QtCore.Signal (int)
    signal_ProgressValue = QtCore.Signal (int)
#endclass

# ------------------------------------
# Downloader_YOUTUBE(QThread)
# ------------------------------------
class Downloader_YOUTUBE (QThread):
    """Downloader_YOUTUBE"""
    luClassName = 'Downloader_YOUTUBE'

    #--------------------------------------------------
    # constructor
    #--------------------------------------------------
    def __init__ (self, AYouTubeObject: LUObjectsYT.TYouTubeObject, AMaxRes, parent = None):
    #beginfunction
        QThread.__init__ (self, parent = parent)
        self.__FYouTubeObject = AYouTubeObject
        self.__FMaxRes = AMaxRes
        self.__FYouTubeObject.ONprogress = self.ONprogress
        # self.__FYouTubeObject.ONcomplete = self.ONcomplete
        self.__FStartDownload_01 = False
        self.__FDownloader_YOUTUBE_Signals = TDownloader_YOUTUBE_Signals()
    #endfunction

    #--------------------------------------------------
    # @property Downloader_YOUTUBE_Signals
    #--------------------------------------------------
    # getter
    @property
    def Downloader_YOUTUBE_Signals (self) -> TDownloader_YOUTUBE_Signals:
    #beginfunction
        return self.__FDownloader_YOUTUBE_Signals
    #endfunction

    #--------------------------------------------------
    # @property StartDownload_01
    #--------------------------------------------------
    # getter
    @property
    def StartDownload_01 (self) -> bool:
    #beginfunction
        return self.__FStartDownload_01
    #endfunction
    @StartDownload_01.setter
    def StartDownload_01 (self, Value: bool):
    #beginfunction
        self.__FStartDownload_01 = Value
    #endfunction

    # @QtCore.Slot (int, str, name = 'ONprogress')
    def ONprogress (self, AStream: pytube.Stream, AChunk: bytes, Abytes_remaining: int):
    #beginfunction
        s = 'Downloader_YOUTUBE.ONprogress...'
        # LULog.LoggerTOOLS.debug (s)

        if not AStream is None:
            # self.__FYouTubeObject.ONprogressObject(AStream, AChunk, Abytes_remaining)
            self.__FYouTubeObject.FProgressMax = AStream.filesize
            self.__FYouTubeObject.FProgressLeft = Abytes_remaining
            self.__FYouTubeObject.FProgressValue = self.__FYouTubeObject.FProgressMax - self.__FYouTubeObject.FProgressLeft

            if not AChunk is None:
                if not self.__FYouTubeObject.FFilechunk is None:
                    self.__FYouTubeObject.FFilechunk.write (AChunk)
                #endif
            #endif

            self.Downloader_YOUTUBE_Signals.signal_ProgressValue.emit (self.__FYouTubeObject.FProgressValue)
        #endif
    #endfunction

    @QtCore.Slot (int, str, name = 'Downloader_YOUTUBE.run')
    def run (self):
        """run"""
    #beginfunction
        s = 'Downloader_YOUTUBE.run...'
        # LULog.LoggerTOOLS.debug (s)
        try:
            self.Downloader_YOUTUBE_Signals.signal_YT_Caption.emit (self.__FYouTubeObject.StreamInfo['default_filename'])
        except:
            self.Downloader_YOUTUBE_Signals.signal_YT_Caption.emit ('Error! default_filename')
        #endtry
        try:
            self.Downloader_YOUTUBE_Signals.signal_ProgressMax.emit (self.__FYouTubeObject.StreamInfo ['filesize'])
        except:
            self.Downloader_YOUTUBE_Signals.signal_ProgressMax.emit (0)
        #endtry
        self.__FYouTubeObject.DownloadURL (ADownload = True, skip_existing = self.__FYouTubeObject.Fskip_existing)
    #endfunction
#endclass

# ------------------------------------
# TYOUTUBEwidgetSignals - СИГНАЛЫ
# ------------------------------------
class TYOUTUBEwidgetSignals(QObject):
    signal_DownloadedURL = QtCore.Signal (str)
    signal_YT_StatWidget = QtCore.Signal (str)
    signal_ChangeStatWidgetObject = QtCore.Signal (TStatWidgetObject, int)
#endclass

# ------------------------------------
# YOUTUBEwidget(QWidget)
# ------------------------------------
class YOUTUBEwidget(QWidget):
    """YOUTUBEwidget"""
    luClassName = 'YOUTUBEwidget'

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
        #
        self.__FYOUTUBEwidgetSignals = TYOUTUBEwidgetSignals()
        self.__FStatWidgetObject: TStatWidgetObject = TStatWidgetObject.swNew
        # Состояние Widget
        self.__FStatWidget: LUProc.TStatWidget = LUProc.TStatWidget.swRunning
        # FYouTubeObject
        self.__FYouTubeObject = AYouTubeObject
        # self.__FYouTubeObject.ONprogress = self.ONprogress
        self.__FYouTubeObject.ONcomplete = self.ONcomplete
        s = AYouTubeObject.URLInfo ['thumbnail_url']
        s = AYouTubeObject.URLInfo ['author']
        self.__FMaxRes = AMaxRes
        self.setObjectName (u"Widget_X")
        """
        # self.setMinimumSize (QSize (400, 40))
        # self.setMaximumSize (QSize (400, 40))
        # self.setMinimumSize (QSize (0, 40))
        # self.setMinimumSize (QSize (0, 800))
        # self.setMaximumSize (QSize (16777215, 16777215))
        # self.setStyleSheet (u"background-color: rgb(0, 0, 255);")
        # self.setSizePolicy(QSizePolicy.Maximum, QSizePolicy.Maximum)
        """
        #----------------------------------------------
        # 2 вариант
        #----------------------------------------------
        self.FDownloader_YOUTUBE = Downloader_YOUTUBE (AYouTubeObject, AMaxRes)
        # сигналы
        self.FDownloader_YOUTUBE.Downloader_YOUTUBE_Signals.signal_YT_Caption.connect(self.signalHandler_YT_Caption)
        self.FDownloader_YOUTUBE.Downloader_YOUTUBE_Signals.signal_ProgressMax.connect (self.signalHandler_ProgressMax)
        self.FDownloader_YOUTUBE.Downloader_YOUTUBE_Signals.signal_ProgressValue.connect (self.signalHandler_ProgressValue)
        self.FDownloader_YOUTUBE.finished.connect (self.qthreadFinished_Downloader_YOUTUBE)

        self.FGetInfoStream_YOUTUBE = GetInfoStream_YOUTUBE (AYouTubeObject, AMaxRes)
        # сигналы
        self.FGetInfoStream_YOUTUBE.signal_YT_Caption.connect (self.signalHandler_YT_Caption)
        self.FGetInfoStream_YOUTUBE.finished.connect (self.qthreadFinished_GetInfoStream_YOUTUBE)

        self.YOUTUBEwidgetSignals.signal_YT_StatWidget.connect (self.signalHandler_YT_StatWidget)

        self.signalHandler_YT_Caption (AYouTubeObject.URL)
        # self.ui.YT_Caption.setText (AYouTubeObject.URL)

        s = CStatWidgetObject[self.__FStatWidgetObject]
        self.signalHandler_YT_StatWidget (s)
        # self.ui.YT_StatWidget.setText (AYouTubeObject.URL)
        self.ui.YT_StatWidget.show ()
        #-----------------------------------------------------------
        self.__WidgetCreate ()
        self.__WidgetActivate ()
    #endfunction

    #--------------------------------------------------
    # @property YOUTUBEwidgetSignals
    #--------------------------------------------------
    # getter
    @property
    def YOUTUBEwidgetSignals (self) -> TYOUTUBEwidgetSignals:
    #beginfunction
        return self.__FYOUTUBEwidgetSignals
    #endfunction

    #--------------------------------------------------
    # @property StatWidgetObject
    #--------------------------------------------------
    # getter
    @property
    def StatWidgetObject (self) -> TStatWidgetObject:
    #beginfunction
        return self.__FStatWidgetObject
    #endfunction
    @StatWidgetObject.setter
    def StatWidgetObject(self, Value: TStatWidgetObject):
    #beginfunction
        self.__FStatWidgetObject = Value
    #endfunction

    #--------------------------------------------------
    # @property YouTubeObject
    #--------------------------------------------------
    # getter
    @property
    def YouTubeObject (self) -> LUObjectsYT.TYouTubeObject:
    #beginfunction
        return self.__FYouTubeObject
    #endfunction

    def __WidgetCreate (self):
        """__WidgetCreate"""
    #beginfunction
        s = '__WidgetCreate...'
        # LULog.LoggerAPPS.info (s)
        # 00.__SetYT_ProgressBar
        self.__SetYT_ProgressBar()
        # 00.__SetActions
        self.__SetActions()
    #endfunction

    def SetStatWidgetObject (self):
        """SetStatWidgetObject"""
    #beginfunction
        if self.__FStatWidgetObject == TStatWidgetObject.swNew:
            self.ui.pushButton_Start_Stop.setEnabled (False)
            self.ui.pushButton_Delete.setEnabled (True)
        #endif
        if self.__FStatWidgetObject == TStatWidgetObject.swQueue:
            self.ui.pushButton_Start_Stop.setEnabled (False)
            self.ui.pushButton_Delete.setEnabled (True)
        #endif
        if self.__FStatWidgetObject == TStatWidgetObject.swGetInfo:
            self.ui.action_Start_Stop.setEnabled (False)
            # self.ui.pushButton_Start_Stop.hide()
            self.ui.pushButton_Start_Stop.setEnabled (False)
            self.ui.pushButton_Delete.setEnabled (False)
        #endif
        if self.__FStatWidgetObject == TStatWidgetObject.swDownload:
            self.ui.action_Start_Stop.setEnabled (True)
            # self.ui.pushButton_Start_Stop.show()
            self.ui.pushButton_Start_Stop.setEnabled (True)
            self.ui.pushButton_Delete.setEnabled (True)
        #endif
    #endfunction

    def __SetStatWidget (self, AStatWidget: LUProc.TStatWidget):
        """__SetStatWidget"""
    #beginfunction
        self.__FStatWidget = AStatWidget
        self.ui.action_Start_Stop.setEnabled(True)
        if self.__FStatWidget == LUProc.TStatWidget.swRunning:
            self.ui.action_Start_Stop.setIcon (self.__FiconStop)
            self.ui.pushButton_Start_Stop.setIcon (self.__FiconStop)
            self.SetStatWidgetObject()
        #endif
        if self.__FStatWidget == LUProc.TStatWidget.swBreak:
            self.ui.action_Start_Stop.setIcon (self.__FiconStart)
            self.ui.pushButton_Start_Stop.setIcon (self.__FiconStart)
            self.SetStatWidgetObject()
        #endif
    #endfunction

    def StartWidget (self):
        """StartWidget"""
    #beginfunction
        s = 'StartWidget...'
        # LULog.LoggerAPPS.info (s)
        self.__SetStatWidget (LUProc.TStatWidget.swRunning)
        self.FDownloader_YOUTUBE.StartDownload_01 = True
    #endfunction
    def StopWidget (self):
        """StopWidget"""
    #beginfunction
        s = 'StopWidget...'
        # LULog.LoggerAPPS.info (s)
        self.__SetStatWidget (LUProc.TStatWidget.swBreak)
        self.FDownloader_YOUTUBE.StartDownload_01 = False
    #endfunction

    @QtCore.Slot (name = '__Action_Start_Stop')
    def __Action_Start_Stop (self):
        """__Action_Start_Stop"""
    #beginfunction
        s = '__Action_Start_Stop...'
        LULog.LoggerAPPS.info (s)
        if self.__FStatWidget == LUProc.TStatWidget.swBreak:

            if self.__FStatWidgetObject == TStatWidgetObject.swNew:
                # Получить информацию о потоке
                self.run_GetInfoStream ()
            #endif
            #
            while self.__FStatWidgetObject == TStatWidgetObject.swGetInfo:
                QCoreApplication.processEvents ()
            #endwhile
            #
            if self.__FStatWidgetObject == TStatWidgetObject.swQueue:
                # Запустить загрузку
                self.__FYouTubeObject.Fis_paused = False
                self.run_Downloader ()
            #endif

            if self.__FStatWidgetObject == TStatWidgetObject.swDownload:
                # Продолжить загрузку
                self.__FYouTubeObject.Fis_paused = False
            #endif
        else:
            if self.__FStatWidget == LUProc.TStatWidget.swRunning:
                # Приостановить загрузку
                self.__FYouTubeObject.Fis_paused = True
                self.StopWidget()
            #endif
        #endif
    #endfunction

    @QtCore.Slot (name = '__Action_Delete')
    def __Action_Delete (self):
        """__Action_Delete"""
    #beginfunction
        s = '__Action_Delete...'
        LULog.LoggerAPPS.info (s)

        self.YOUTUBEwidgetSignals.signal_ChangeStatWidgetObject.emit (self.__FStatWidgetObject, -1)

        self.YouTubeObject.Fis_cancelled = True

        if not self.__FStatWidgetObject == TStatWidgetObject.swDownload:
            # Удаление Widget
            LURL = self.__FYouTubeObject.URL
            self.YOUTUBEwidgetSignals.signal_DownloadedURL.emit (LURL)
        #endif
    #endfunction

    #--------------------------------------------------
    # 00.__SetYT_ProgressBar
    #--------------------------------------------------
    def __SetYT_ProgressBar (self):
        """__SetYT_ProgressBar"""
    #beginfunction
        s = '__SetYT_ProgressBar...'
        # LULog.LoggerAPPS.info (s)
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
    #endfunction

    #--------------------------------------------------
    # 00.__SetActions
    #--------------------------------------------------
    def __SetActions (self):
        """__SetActions"""
    #beginfunction
        s = '00.__SetActions...'
        # LULog.LoggerAPPS.info (s)

        self.ui.pushButton_Start_Stop.addAction(self.ui.action_Start_Stop)
        self.ui.pushButton_Start_Stop.clicked.connect(self.__Action_Start_Stop)
        self.ui.pushButton_Delete.addAction(self.ui.action_Delete)
        self.ui.pushButton_Delete.clicked.connect(self.__Action_Delete)

        self.ui.action_Start_Stop.triggered.connect(self.__Action_Start_Stop)
        self.ui.action_Delete.triggered.connect(self.__Action_Delete)

        self.__FiconStart = QIcon()
        self.__FiconStart.addFile(u":/ICONS/run.png", QSize(), QIcon.Normal, QIcon.Off)
        self.__FiconStop = QIcon()
        self.__FiconStop.addFile(u":/ICONS/stop.png", QSize(), QIcon.Normal, QIcon.Off)
        self.__FiconDelete = QIcon()
        self.__FiconDelete.addFile(u":/ICONS/delete.png", QSize(), QIcon.Normal, QIcon.Off)

        self.ui.pushButton_Delete.setIcon (self.__FiconDelete)

    #endfunction

    def __WidgetActivate (self):
        """__WidgetActivate"""
    #beginfunction
        s = '__WidgetActivate...'
        # LULog.LoggerAPPS.info (s)
    #endfunction

    def ONcomplete (self, AStream: pytube.Stream, AFilePath: str):
    #beginfunction
        s = 'YOUTUBEwidget.ONcomplete...'
        # LULog.LoggerTOOLS.debug (s)

        if not AStream is None:
            # self.__FYouTubeObject.ONcompleteObject (AStream, AFilePath)

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
        LULog.LoggerTOOLS.debug (s)

        # Приостановить загрузку
        # self.__FYouTubeObject.Fis_paused = True

        self.StopWidget ()

        # swDownload - 1
        self.YOUTUBEwidgetSignals.signal_ChangeStatWidgetObject.emit (self.__FStatWidgetObject, -1)
        if not self.YouTubeObject.Fis_cancelled:
            # swDownloaded + 1
            self.__FStatWidgetObject = TStatWidgetObject.swDownloaded
            self.YOUTUBEwidgetSignals.signal_ChangeStatWidgetObject.emit (self.__FStatWidgetObject, 1)
            s = 'Загружено ... (swDownloaded)'
            self.YOUTUBEwidgetSignals.signal_YT_StatWidget.emit (s)
        else:
            s = 'is_cancelled ...'
            self.YOUTUBEwidgetSignals.signal_YT_StatWidget.emit (s)
        #endif

        # Удаление Widget
        LURL = self.__FYouTubeObject.URL
        self.YOUTUBEwidgetSignals.signal_DownloadedURL.emit (LURL)

        # Удаление потока, после его использования.
        del self.FDownloader_YOUTUBE
    #endfunction

    def run_Downloader_01(self):
        """run_Downloader_01"""
    #beginfunction
        # swQueue - 1
        self.YOUTUBEwidgetSignals.signal_ChangeStatWidgetObject.emit (self.__FStatWidgetObject, -1)
        # swDownload + 1
        self.__FStatWidgetObject = TStatWidgetObject.swDownload
        self.YOUTUBEwidgetSignals.signal_ChangeStatWidgetObject.emit (self.__FStatWidgetObject, 1)
    #endfunction

    def run_Downloader(self):
        """run_Downloader"""
    #beginfunction
        s = 'YOUTUBEwidget.run_Downloader...'
        LULog.LoggerTOOLS.debug (s)

        self.SetStatWidgetObject()

        self.ui.YT_StatWidget.hide ()
        self.ui.YT_ProgressBar.show()
        s = 'Загрузка потока ... (swDownload)'
        self.YOUTUBEwidgetSignals.signal_YT_StatWidget.emit (s)
        self.run_Downloader_01()
        self.StartWidget ()
        self.FDownloader_YOUTUBE.start ()
    #endfunction

    @QtCore.Slot (str, name = 'qthreadFinished_GetInfoStream_YOUTUBE')
    def qthreadFinished_GetInfoStream_YOUTUBE (self):
    #beginfunction
        s = 'YOUTUBEwidget.qthreadFinished_GetInfoStream_YOUTUBE...'
        LULog.LoggerTOOLS.debug (s)
        self.StopWidget ()
        # swGetInfo - 1
        self.YOUTUBEwidgetSignals.signal_ChangeStatWidgetObject.emit (self.__FStatWidgetObject, -1)
        # swQueue + 1
        self.__FStatWidgetObject = TStatWidgetObject.swQueue
        self.YOUTUBEwidgetSignals.signal_ChangeStatWidgetObject.emit (self.__FStatWidgetObject, 1)
        s = 'Получена информация... (swQueue)'
        self.YOUTUBEwidgetSignals.signal_YT_StatWidget.emit (s)

        self.SetStatWidgetObject ()

        # Удаление потока, после его использования.
        del self.FGetInfoStream_YOUTUBE
    #endfunction

    def run_GetInfoStream_01(self):
        """run_GetInfoStream_01"""
    #beginfunction
        # swNew - 1
        self.YOUTUBEwidgetSignals.signal_ChangeStatWidgetObject.emit (self.__FStatWidgetObject, -1)
        # swGetInfo + 1
        self.__FStatWidgetObject = TStatWidgetObject.swGetInfo
        self.YOUTUBEwidgetSignals.signal_ChangeStatWidgetObject.emit (self.__FStatWidgetObject, 1)
    #endfunction

    def run_GetInfoStream(self):
        """run_GetInfoStream"""
    #beginfunction
        s = 'YOUTUBEwidget.run_GetInfoStream...'
        LULog.LoggerTOOLS.debug (s)

        self.SetStatWidgetObject()

        self.ui.YT_StatWidget.show ()
        s = 'Получение информации о потоке ... (swGetInfo)'
        self.YOUTUBEwidgetSignals.signal_YT_StatWidget.emit (s)
        self.run_GetInfoStream_01()
        self.StartWidget ()
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
