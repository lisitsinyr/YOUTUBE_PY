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
import psutil

from  PySide6 import QtCore

from PySide6.QtCore import (
    QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt, QObject, QThread, Signal, Slot,
    QStringListModel, QModelIndex
    )

from PySide6.QtGui import (
    QAction, QBrush, QColor, QConicalGradient,
    QCursor, QFont, QFontDatabase, QGradient,
    QIcon, QImage, QKeySequence, QLinearGradient,
    QPainter, QPalette, QPixmap, QRadialGradient,
    QTransform,
    QClipboard
    )

from PySide6.QtWidgets import (
    QAbstractScrollArea, QApplication, QFrame, QHBoxLayout, QVBoxLayout,
    QFileDialog,
    QListView, QMainWindow, QMenu, QMenuBar, QDialog,
    QPlainTextEdit, QScrollArea, QSizePolicy, QSplitter,
    QStatusBar, QTextEdit, QToolBar, QVBoxLayout,
    QSizePolicy, QPushButton,
    QProgressBar,
    QWidget, QLabel
    )

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

import YOUTUBE_FormAboutWindow
import YOUTUBE_FormSetupWindow

class CustomButton_01 (QPushButton):
    def mousePressEvent (self, event):
    #beginfunction
        event.accept ()
    #endfunction
#endclass

class CustomButton_02 (QPushButton):
    def event (self, event):
    #beginfunction
        event.ignore ()
    #endfunction
#endclass

class TQThread(QtCore.QThread):
    def __init__ (self, parent = None):
    #beginfunction
        super ().__init__ (parent)
        self.__Fstopped = False
    #endfunction

    def stop(self):
    #beginfunction
        self.__Fstopped = True
        print('STOPPING LOOP')

    #endfunction
    def run(self):
    #beginfunction
        self.__Fstopped = False
        counter = 0
        while not self.__Fstopped:
            # counter += 1
            # print(counter)
            # # do some more work...
            self.msleep(1)
        #endwhile
    #endfunction
#endclass

# ------------------------------------
# TAPPSignals - СИГНАЛЫ
# ------------------------------------
class TAPPSignals(QObject):
    StopApplication_event = QtCore.Signal(bool)
    StatApplication_event = QtCore.Signal(str)
    closed_event = QtCore.Signal (bool)
#endclass

# ------------------------------------
# FormSetup(QDialog)
# ------------------------------------
class FormSetup(QDialog):
    """FormAbout"""
    luClassName = 'FormSetup'
    def __init__(self, parent=None):
    #beginfunction
        super().__init__(parent=parent)
        self.ui = Ui_FormSetup()
        self.ui.setupUi(self)
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

#endclass

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

# ------------------------------------
# FormMainWindow(QMainWindow)
# ------------------------------------
class FormMainWindow(QMainWindow):
    """FormMainWindow"""
    luClassName = 'FormMainWindow'

    # #----------------------------------------------
    # # СИГНАЛ
    # #----------------------------------------------
    # StopApplication_event = QtCore.Signal(bool)
    # StatApplication_event = QtCore.Signal(str)
    # closed_event = QtCore.Signal (bool)

    #----------------------------------------------
    # Коннектор - сюда приходит СИГНАЛ StopApplication
    #----------------------------------------------
    def signalHandler_StopApplication(self, Abool):
        """signalHandler_StopApplication"""
    #beginfunction
        s = 'signalHandler_StopApplication...'
        self.__FStopApplicationMain = Abool
    #endfunction

    #----------------------------------------------
    # Коннектор - сюда приходит СИГНАЛ StatApplication_event
    #----------------------------------------------
    def signalHandler_StatApplication(self, text):
        """signalHandler_StatApplication"""
    #beginfunction
        s = 'signalHandler_StatApplication...'
        self.P_StatApplication.setText (text)
    #endfunction

    #----------------------------------------------
    # Коннектор - сюда приходит СИГНАЛ
    #----------------------------------------------
    def signalHandler_DownloadedURL(self, text):
        """signalHandler_DownloadedURL"""
    #beginfunction
        s = 'signalHandler_DownloadedURL...'
        # LULog.LoggerAPPSAdd_debug (s)
        LURL = text
        self.__DelModel (LURL)
        self.__DelListWidget (LURL)
        self.__DelListYouTubeObject (LURL)
    #endfunction

    #----------------------------------------------
    # Коннектор - сюда приходит СИГНАЛ
    #----------------------------------------------
    def signalHandler_ChangeStatWidgetObject(self, AStatWidgetObject, ACount):
        """signalHandler_DownloadedURL"""
    #beginfunction
        s = 'signalHandler_ChangeStatWidgetObject...'
        # LULog.LoggerAPPSAdd_debug (s)
        self.__ChangeCountStatWidgetObject(AStatWidgetObject, ACount)
    #endfunction

    def __init__(self, parent=None):
    #beginfunction
        super().__init__(parent=parent)
        self.ui = Ui_FormMainWindow()
        self.ui.setupUi(self)
        # СИГНЫЛЫ
        self.__FAPPSignals = TAPPSignals ()
        #
        self.__FStopApplicationMain: bool = True
        #
        self.__FMaxThread: int = 5
        #
        self.__FidleApplication = False
        self.__FidleParams = False
        self.__FidleClock = False
        #
        self.__FQTimerApplicationInterval = 1
        self.__FQTimerParamsInterval = 5000
        self.__FQTimerClockInterval = 1000


        # Состояние программы
        self.__FStatApplication: LUProc.TStatApplication = LUProc.TStatApplication.saRunning
        # __FParams
        self.__FParams: YOUTUBE_Params.TParams = YOUTUBE_Params.TParams ()
        # self.APPLog = self.__FParams.FileMemoLog
        self.__FSheduler:LUSheduler.TSheduler = None
        #
        self.__FswNew = 0
        self.__FswGetInfo = 0
        self.__FswQueue = 0
        self.__FswDownload = 0
        self.__FswDownloaded = 0
        #
        self.__FormCreate ()
        self.__FormActivate ()
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

    def closeEvent(self, event):
        """closeEvent"""
    #beginfunction
        super().closeEvent(event)
        # event.ignore()
        event.accept ()
        # self.closed_event.emit(True)
        self.__FAPPSignals.closed_event.emit(True)

        self.StopApplication()
        # self.__Action_Exit()
    #endfunction

    """
    # События
    Обработчик              Событие
    mouseMoveEvent          Мышь переместилась
    mousePressEvent         Кнопка мыши нажата
    mouseReleaseEvent       Кнопка мыши отпущена
    mouseDoubleClickEvent   Обнаружен двойной клик

    # События управления мышью
    Метод                   Возвращает
    .button()               Конкретную кнопку, вызвавшую данное событие
    .buttons()              Состояние всех кнопок мыши (флаги OR)
    .position()             Относительную позицию виджета в виде целого QPoint .

    # Идентификаторы кнопок определяются в пространстве имён Qt:
    Код             Бинарное значение   Описание
    Qt.NoButton     0 (000)             Кнопка не нажата, или событие не связано с нажатием кнопки
    Qt.LeftButton   1 (001)             Левая кнопка нажата
    Qt.RightButton  2 (010)             Правая кнопка нажата
    Qt.MiddleButton 4 (100)             Средняя кнопка [обычно это колёсико мыши] нажата
    """
    # def event (self, event):
    # #beginfunction
    #     # event.ignore ()
    #     ...
    # #endfunction
    def mouseMoveEvent (self, event):
    #beginfunction
        self.P_StatEvents.setText("mouseMoveEvent")
        # event.accept ()
    #endfunction
    def mousePressEvent (self, event):
    #beginfunction
        self.P_StatEvents.setText("mousePressEvent")
        # event.accept ()
        if event.button() == Qt.LeftButton:
            # здесь обрабатываем нажатие левой кнопки
            self.P_StatEvents.setText("mousePressEvent LEFT")
        elif event.button() == Qt.MiddleButton:
            # здесь обрабатываем нажатие средней кнопки.
            self.P_StatEvents.setText("mousePressEvent MIDDLE")
        elif event.button() == Qt.RightButton:
            # здесь обрабатываем нажатие правой кнопки.
            self.P_StatEvents.setText("mousePressEvent RIGHT")
        # super (self, FormMainWindow).contextMenuEvent (event)
    #endfunction
    def mouseReleaseEvent (self, event):
    #beginfunction
        self.P_StatEvents.setText("mouseReleaseEvent")
        # event.accept ()
        if event.button() == Qt.LeftButton:
            self.P_StatEvents.setText("mouseReleaseEvent LEFT")
        elif event.button() == Qt.MiddleButton:
            self.P_StatEvents.setText("mouseReleaseEvent MIDDLE")
        elif event.button() == Qt.RightButton:
            self.P_StatEvents.setText("mouseReleaseEvent RIGHT")
    #endfunction
    def mouseDoubleClickEvent (self, event):
        self.P_StatEvents.setText("mouseDoubleClickEvent")
        # event.accept ()
        if event.button() == Qt.LeftButton:
            self.P_StatEvents.setText("mouseDoubleClickEvent LEFT")
        elif event.button() == Qt.MiddleButton:
            self.P_StatEvents.setText("mouseDoubleClickEvent MIDDLE")
        elif event.button() == Qt.RightButton:
            self.P_StatEvents.setText("mouseDoubleClickEvent RIGHT")
    #endfunction
    #------------------------------------------
    # Контекстные меню
    #------------------------------------------
    def contextMenuEvent (self, event):
    #beginfunction
        context = QMenu (self)
        context.addAction (QAction ("test 1", self))
        context.addAction (QAction ("test 2", self))
        context.addAction (QAction ("test 3", self))
        context.exec (event.globalPos ())
    #endfunction

    def __SetColorGroup (self):
        """__SetColorGroup"""
    #beginfunction
        s = '__SetColorGroup...'
        # LULog.LoggerAPPSAdd_debug (s)

        Lpalette = self.ui.Memo_Log.palette ()
        Lpalette.setCurrentColorGroup (QPalette.Normal)
        Lpalette.setColorGroup (QPalette.Disabled,
                               Lpalette.windowText (), Lpalette.button (),
                               Lpalette.light (), Lpalette.dark (), Lpalette.mid (),
                               Lpalette.text (), Lpalette.brightText (),
                               Lpalette.base (), Lpalette.window (),
                               )
        self.ui.Memo_Log.setPalette (Lpalette)
    #endfunction

    #--------------------------------------------------
    # 01.__SetStylesheetsFor_ALL
    #--------------------------------------------------
    def __SetStylesheetsFor_ALL (self):
        """__SetStylesheetsFor_ALL"""
    #beginfunction
        s = '__SetStylesheetsFor_ALL...'
        # LULog.LoggerAPPSAdd_debug (s)

        # Create Stylesheets
        self.style_light = """
            * {font-family: 'Noto Sans';}  /* REMOVING THIS LINE AVOIDS THE ISSUE, BUT THEN FONTS ARE WRONG INITIALLY */
            QMainWindow {background-color: white;}
            """
        # Create Stylesheets
        self.style_dark = """
            * {font-family: 'Noto Sans';}
            QMainWindow {background-color: gray;}
            """
        # Create Stylesheets
        self.style_light = """
            * QPlainTextEdit {color: rgba(0, 0, 0, .5); background-color: rgb(157, 157, 157); font-weight: bold; font-size: 10px; font: 20pt "Courier New"}
            QPlainTextEdit {color: blue; background-color: rgb(157, 157, 157); font-weight: bold; font-size: 10px; font: 10pt "Courier New"}
            """
        self.setStyleSheet (self.style_light)
    #endfunction
    #--------------------------------------------------
    # 01.__SetColorFor_Memo_Log
    #--------------------------------------------------
    def __SetColorFor_Memo_Log (self):
        """__SetupColorFor_Memo_Log"""
    #beginfunction
        s = '__SetColorFor_Memo_Log...'
        # LULog.LoggerAPPSAdd_debug (s)

        cg = QPalette.ColorGroup (QPalette.Active)
        cg = QPalette.ColorGroup (QPalette.Disabled)
        cg = QPalette.ColorGroup (QPalette.Inactive)

        # foreground
        palette_foreground = QPalette ()
        palette_foreground = self.ui.Memo_Log.palette ()
        fc = QColor('yellow')
        fr = QPalette.ColorRole(QPalette.ColorRole.Text)
        palette_foreground.setColor (fr, fc)
        self.ui.Memo_Log.setPalette (palette_foreground)

        # background
        # gray = #808080 как более жесткий, холодный.
        # grey = #D3D3D3 он более светлый.
        palette_background = QPalette ()
        palette_background = self.ui.Memo_Log.palette ()
        bc = QColor('grey')
        br = QPalette.ColorRole(QPalette.ColorRole.Base)
        palette_background.setColor (br, bc)
        self.ui.Memo_Log.setPalette (palette_background)
    #endfunction
    #--------------------------------------------
    # 01.__SetStylesheetsFor_Memo_Log
    #--------------------------------------------
    def __SetStylesheetsFor_Memo_Log (self):
        """__SetupStylesheetsFor_Memo_Log"""
    #beginfunction
        s = '__SetStylesheetsFor_Memo_Log...'
        # LULog.LoggerAPPSAdd_debug (s)

        # stylesheet
        # color: rgb (0, 0, 0); background-color: rgb (157, 157, 157)
        # RGBA расшифровывается как Red Green Blue Alpha.
        # На W3C объясняется: «В этой спецификации цветовая модель RGB расширена
        # и включает составляющую альфа, позволяющую задать непрозрачность цвета»
        # Это значит, что можно добавить четвертое значение (от 1 до 0),
        # чтобы задать уровень непрозрачности данного RGB-цвета.
        # Для полной непрозрачности используется значение 1, для полной прозрачности - 0.
        ss = 'color: red; background-color: grey; font-weight: bold'
        ss = 'color: black; background-color: grey; font-weight: bold'
        ss = 'color: rgba(0, 0, 0, .5); background-color: rgb(157, 157, 157); font-weight: bold; font-size: 10px; font: 10pt "Courier New"'
        self.ui.Memo_Log.setStyleSheet (ss)
    #endfunction

    #--------------------------------------------------
    # 00.__SetParams
    #--------------------------------------------------
    def __SetParams (self):
        """__SetParams"""
    #beginfunction
        s = '00.__SetParams...'
        # LULog.LoggerAPPSAdd_info (s)

        LULog.LoggerAPPSAdd (LULog.TEXT, self.Params.FileNameINI)
        # # [GENERAL]
        # LULog.LoggerAPPSAdd (LULog.TEXT, 'PathStore='+self.Params.PathStore)
        # LULog.LoggerAPPSAdd (LULog.TEXT, 'PathStoreOut='+self.Params.PathStoreOut)
        # LULog.LoggerAPPSAdd (LULog.TEXT, 'PathStoreError='+self.Params.PathStoreError)
        # LULog.LoggerAPPSAdd (LULog.TEXT, 'Sheduler='+self.Params.Sheduler)
        # # [Youtube]
        # LULog.LoggerAPPSAdd (LULog.TEXT, 'PathYoutubeLoad='+self.Params.PathYoutubeLoad)
        # LULog.LoggerAPPSAdd (LULog.TEXT, 'CheckBoxCliboard='+str(self.Params.CheckBoxCliboard))
        # LULog.LoggerAPPSAdd (LULog.TEXT, 'CheckBoxAutoDownload='+str(self.Params.CheckBoxAutoDownload))
        # LULog.LoggerAPPSAdd (LULog.TEXT, 'CheckBoxAutoDelete='+str(self.Params.CheckBoxAutoDelete))
        # LULog.LoggerAPPSAdd (LULog.TEXT, 'CheckBoxSkipExists='+str(self.Params.CheckBoxSkipExists))
        # LULog.LoggerAPPSAdd (LULog.TEXT, 'Stop='+str(self.Params.Stop))
        # LULog.LoggerAPPSAdd (LULog.TEXT, 'Chunk=' + str(self.Params.Chunk))
    #endfunction

    #--------------------------------------------------
    # 01.__SetLogs
    #--------------------------------------------------
    def __SetLogs (self):
        """__SetLogs"""
    #beginfunction
        s = '01.__SetLogs...'
        # LULog.LoggerAPPSAdd_info (s)

        # self.APPLog: LULog.TFileMemoLog = LULog.FileMemoLog
        #----------------- Memo_Log --------------------------
        self.ui.Memo_Log.setReadOnly (True)
        self.__SetStylesheetsFor_ALL()
        self.__SetStylesheetsFor_Memo_Log()
        # self.__SetColorFor_Memo_Log()

        # self.ui.Memo_Log.appendPlainText ('mhsdkjhfkjhsakjh'+'\n')

        # LULog.LoggerAPPSAdd (LULog.TEXT, self.Params.FileMemoLog.FileName)
    #endfunction

    #-------------------------------
    # 02.__SetStatusBar_PN
    #-------------------------------
    def __SetStatusBar_PN (self):
        """__SetStatusBar_PN"""
    #beginfunction
        s = '02.__SetStatusBar_PN...'
        # LULog.LoggerAPPSAdd_info (s)

        # self.ui.StatusBar_PN.stasetStyleSheet (
        #     "QStatusBar{padding-left:8px;background:rgba(255,0,0,255);color:black;font-weight:bold;}")
        # display a message in 5 seconds
        # self.ui.StatusBar_PN.showMessage ("Error Cannot determine filepath", 5000)
        # display a message in 5 seconds
        # self.ui.StatusBar_PN.showMessage('Ready', 5000)

        #================================================
        # 01.P_Clock - add a permanent widget to the status bar
        #================================================
        self.P_Clock = QLabel('P_Clock')
        self.ui.StatusBar_PN.addPermanentWidget(self.P_Clock)
        s = f''
        self.P_Clock.setText(s)
        #================================================
        # 02.P_StatSheduler - add a permanent widget to the status bar
        #================================================
        self.P_StatSheduler = QLabel('P_StatEvents')
        self.ui.StatusBar_PN.addPermanentWidget(self.P_StatSheduler)
        s = self.P_StatSheduler.text()
        self.P_StatSheduler.setText('P_StatEvents')
        #================================================
        # 03.P_StatApplication - add a permanent widget to the status bar
        #================================================
        self.P_StatApplication = QLabel('P_StatApplication')
        self.ui.StatusBar_PN.addPermanentWidget(self.P_StatApplication)
        s = self.P_StatApplication.text()
        self.P_StatApplication.setText(LUProc.CStatApplication[self.__FStatApplication])
        #================================================
        #   .P_Main - add a permanent widget to the status bar
        #================================================
        self.P_StatMain = QLabel('P_Main')
        # self.ui.StatusBar_PN.addPermanentWidget(self.P_StatMain)
        s = self.P_StatMain.text()
        self.P_StatMain.setText(LUProc.cProcessStop)
        #================================================
        # 04.P_StatEvents - add a permanent widget to the status bar
        #================================================
        self.P_StatEvents = QLabel('P_StatEvents')
        self.ui.StatusBar_PN.addPermanentWidget(self.P_StatEvents)
        s = self.P_StatEvents.text()
        self.P_StatEvents.setText('P_StatEvents')
        #================================================
        # 05.P_StatCountWidgetObject - add a permanent widget to the status bar
        #================================================
        self.P_StatCountWidgetObject = QLabel('P_StatCountWidgetObject')
        self.ui.StatusBar_PN.addPermanentWidget(self.P_StatCountWidgetObject)
        s = f'{self.__FswNew}:{self.__FswGetInfo}:{self.__FswQueue}:{self.__FswDownload}:{self.__FswDownloaded}'
        self.P_StatCountWidgetObject.setText(s)
        #================================================
        # 06.P_ProgressBar - add a permanent widget to the status bar
        #================================================
        self.P_ProgressBar = QProgressBar(self.ui.StatusBar_PN)
        self.P_ProgressBar.setObjectName(u"P_ProgressBar")
        self.P_ProgressBar.setMinimum(0)
        self.P_ProgressBar.setMaximum(100)
        self.P_ProgressBar.setValue(0)
        self.ui.StatusBar_PN.addPermanentWidget(self.P_ProgressBar)

        #===================================================
        # Splash окно
        #===================================================
        # Splash = TSplash.Create (Self)
        # Splash.Name = 'Splash'
        # Splash.Height = StatusBar_PN.Height
        # Splash.Width = StatusBar_PN.Panels[0].Width
        # StatusBar_PN.InsertControl (Splash)
    #endfunction

    #-------------------------------
    # 03.__SetSheduler
    #-------------------------------
    def __SetSheduler (self):
        """__SetSheduler"""
    #beginfunction
        s = '03.__SetSheduler...'
        # LULog.LoggerAPPSAdd_info (s)

        #-------------------------------
        # Sheduler
        #-------------------------------
        self.__FSheduler = LUSheduler.TSheduler ()
        LEvent = self.__FSheduler.AddEvent ('ShedulerTEST1', self.Params.Sheduler)
        self.__FSheduler.OnSheduler = self.__Action_Sheduler
        # if LEvent is not None:
        #     self.__FSheduler.PrintEvent (LEvent)
        # #endif
    #endfunction

    #--------------------------------------------------
    # 04.__SetClipboard
    #--------------------------------------------------
    def __SetClipboard (self):
        """__SetClipboard"""
    #beginfunction
        s = '04.__SetClipboard...'
        # LULog.LoggerAPPSAdd_info (s)

        self.__FClipboard = QApplication.clipboard ()
        # Slots & Signals
        self.__FClipboard.dataChanged.connect (self.cliboard_changed (QClipboard.Mode))
        self.__FClipboard.dataChanged.connect (self.cliboard_dataChanged)
        self.__FClipboard.dataChanged.connect (self.cliboard_findBufferChanged)
        self.__FClipboard.dataChanged.connect (self.cliboard_selectionChanged)
        self.__FClipboardList = []
        self.Flast_copied = ''
    #endfunction

    #--------------------------------------------------
    # 05.__SetListViewL
    #--------------------------------------------------
    def __SetListViewL (self):
        """__SetListViewL"""
    #beginfunction
        s = '05.__SetListViewL...'
        # LULog.LoggerAPPSAdd_info (s)

        self.__FModel = QStringListModel ()

        # self.__FModel = QStringListModel ([
        #     "An element", "Another element", "Yay! Another one.", '????????????'
        # ])
        self.ui.ListViewL.setModel (self.__FModel)
        # self.__FModel.setStringList(['!!!!!!!!!!!!!!'])

        # self.ui.ListViewL.setViewMode (QListView.IconMode)
        # self.ui.ListViewL.setMovement (QListView.Static)
        # self.ui.ListViewL.setIconSize (QSize (64, 64))

        self.__ClearModel ()
    #endfunction

    #--------------------------------------------------
    # 06.__SetScrollAreaR
    #--------------------------------------------------
    def __SetScrollAreaR (self):
        """__SetScrollAreaR"""
        def LoadFile(AFileName: str) -> str:
        #beginfunction
            if AFileName:
                Lfile = QtCore.QFile (AFileName)

                if Lfile.open (QtCore.QIODevice.ReadOnly):
                    Lstream = QtCore.QTextStream (Lfile)
                    LText = Lstream.readAll ()
                    # info = QtCore.QFileInfo (AFileName)
                    # if info.completeSuffix () == 'html':
                    #     self.editor_text.setHtml (text)
                    # else:
                    #     self.editor_text.setPlainText (text)
                    # #endif
                    Lfile.close ()
                    return LText
                #endif
            #endif
        #endfunction

    #beginfunction
        s = '06.__SetScrollAreaR...'
        # LULog.LoggerAPPSAdd_info (s)

        self.__FListWidgets = list()

        LFileName = os.path.join (LUos.GetCurrentDir(), 'README.md')

        # self.ui.TextEditR.setText ('self.ui.TextEditR.setText')
        self.ui.TextEditR.setText (LoadFile (LFileName))
        # self.ui.TextEditR.insertPlainText(LoadFile (LFileName))
        self.ui.TextEditR.setSizePolicy (QSizePolicy.Expanding, QSizePolicy.Expanding)

        # self.__AQMimeData = QtCore.QMimeData()
        # self.ui.TextEditR.insertFromMimeData ('self.ui.TextEditR.setText')

        self.__ClearWidgets()
    #endfunction

    #--------------------------------------------------
    # 07.__SetListYouTubeObject
    #--------------------------------------------------
    def __SetListYouTubeObject (self):
        """__SetListYouTubeObject"""
    #beginfunction
        s = '07.__SetListYouTubeObject...'
        # LULog.LoggerAPPSAdd_info (s)

        self.__FListYouTubeObject = list()
        self.__ClearListYouTubeObject()
    #endfunction
    def update_str_field (self, Value: str):
        """update_str_field"""
    #beginfunction
        print(Value)
        ...
    #endfunction
    def update_int_field (self, Value: int):
        """update_int_field"""
    #beginfunction
        print(Value)
        ...
    #endfunction

    #--------------------------------------------------
    # 08.__SetTimerApplication
    #--------------------------------------------------
    def __SetTimerApplication (self):
        """__SetTimerApplication"""
    #beginfunction
        s = '08.__SetTimerApplication...'
        # LULog.LoggerAPPSAdd_info (s)

        self.__FQTimerApplication = LUQTimer.TQTimer(parent = self)
        self.__FQTimerApplication.FQTimerName = 'Таймер Application'
        # msec
        self.__FQTimerApplication.setInterval (self.__FQTimerApplicationInterval)
        self.__FAPPSignals.StatApplication_event.connect (self.signalHandler_StatApplication)
    #endfunction
    #--------------------------------------------------
    # 081.__SetTimerParams
    #--------------------------------------------------
    def __SetTimerParams (self):
        """__SetTimerParams"""
    #beginfunction
        s = '081.__SetTimerParams...'
        # LULog.LoggerAPPSAdd_info (s)

        self.__FQTimerParams = LUQTimer.TQTimer(parent = self)
        self.__FQTimerParams.FQTimerName = 'Таймер Params'
        # msec
        self.__FQTimerParams.setInterval (1)
    #endfunction
    #--------------------------------------------------
    # 082.__SetTimerClock
    #--------------------------------------------------
    def __SetTimerClock (self):
        """__SetTimerClock"""
    #beginfunction
        s = '082.__SetTimerClock...'
        # LULog.LoggerAPPSAdd_info (s)

        self.__FQTimerClock = LUQTimer.TQTimer(parent = self)
        self.__FQTimerClock.FQTimerName = 'Таймер Clock'
        # msec
        self.__FQTimerClock.setInterval (self.__FQTimerClockInterval)
    #endfunction
    #--------------------------------------------------
    # 09.__SetActions
    #--------------------------------------------------
    def __SetActions (self):
        """__SetActions"""
    #beginfunction
        s = '09.__SetActions...'
        # LULog.LoggerAPPSAdd_info (s)

        self.ui.action_CreateYoutube.triggered.connect (self.__Action_CreateYoutube)
        self.ui.action_Exit.triggered.connect(self.__Action_Exit)

        self.ui.action_Exit.setProperty("clicked()", False)

        self.ui.action_ExitProgram.triggered.connect(self.__Action_Exit)
        # self.ui.action_Exit.triggered.connect(self.close)
        self.ui.action_Cut.triggered.connect(self.__Action_Cut)
        self.ui.action_Copy.triggered.connect(self.__Action_Copy)
        self.ui.action_Paste.triggered.connect(self.__Action_Paste)
        self.ui.action_Start_Stop.triggered.connect(self.__Action_Start_Stop)
        self.ui.action_Setup.triggered.connect(self.__Action_Setup)
        self.ui.action_About.triggered.connect(self.__Action_About)
        self.ui.action_Help.triggered.connect(self.__Action_Help)
        self.ui.action_DeleteAll.triggered.connect(self.__Action_DeleteAll)
        self.ui.action_TestFunction.triggered.connect(self.__Action_TestFunction)

        self.FiconStart = QIcon()
        self.FiconStart.addFile(u":/ICONS/run.png", QSize(), QIcon.Normal, QIcon.Off)
        self.FiconStop = QIcon()
        self.FiconStop.addFile(u":/ICONS/stop.png", QSize(), QIcon.Normal, QIcon.Off)

        # self.StopApplication_event.connect (self.signalHandler_StopApplication)
        self.__FAPPSignals.StopApplication_event.connect (self.signalHandler_StopApplication)
    #endfunction

    @LUDecotators.TIMING
    def __FormCreate (self):
        """__FormCreate"""
    #beginfunction
        s = '__FormCreate...'
        # LULog.LoggerAPPSAdd_info (s)

        # LULog.PrintHandlers (LULog.LoggerTOOLS)
        LHandler: LULog.TStreamHandler = LULog.GetHandler (LULog.LoggerTOOLS, 'CONSOLE')
        LHandler.FAPPGUI = True
        LHandler.Widget = self.ui.Memo_Log
        # LULog.LoggerTOOLS.info ('LULog.LoggerTOOLS-> '+'TEST...')

        # LULog.PrintHandlers (LULog.LoggerAPPS)
        LHandler: LULog.TStreamHandler = LULog.GetHandler (LULog.LoggerAPPS, 'CONSOLE')
        LHandler.FAPPGUI = True
        LHandler.Widget = self.ui.Memo_Log
        # LULog.LoggerAPPSAdd_info ('LULog.LoggerAPPS-> '+'TEST...')

        self.setWindowTitle(YOUTUBE_Consts.cProjectNAME)

        # 00.__SetParams
        self.__SetParams()
        # 01.__SetLogs
        self.__SetLogs ()
        # 02.__SetStatusBar_PN
        self.__SetStatusBar_PN()
        # 03.__SetSheduler
        self.__SetSheduler()
        # 04.__SetClipboard
        self.__SetClipboard()
        # 05.__SetListViewL
        self.__SetListViewL()
        # 06.__SetScrollAreaR
        self.__SetScrollAreaR()
        # 07.__SetListYouTubeObject
        self.__SetListYouTubeObject()
        # 08.__SetTimerApplication
        self.__SetTimerApplication()
        # 081.__SetTimerParams
        self.__SetTimerParams()
        # 082.__SetTimerClock
        self.__SetTimerClock()
        # 09.__SetActions
        self.__SetActions()
        #----------------- VersionInfo --------------------------
        # VersionInfo = CreateVersion (ParamStr(0))
        # LULog.LoggerAPPSAdd (LULog.TEXT, ParamStr (0) + ' ' + VersionInfo.FileVersion+ ' ' + VersionInfo.FileDate)
        # VersionInfo.Free
        #-----------------------------------------------------------
    #endfunction

    #--------------------------------------------------
    # @property Params
    #--------------------------------------------------
    # getter
    @property
    def Params (self) -> YOUTUBE_Params.TParams:
    #beginfunction
        return self.__FParams
    #endfunction

    def __FormActivate (self):
        """__FormActivate"""
    #beginfunction
        s = '__FormActivate...'
        # LULog.LoggerAPPSAdd_info (s)

        self.ui.TEST_widget.hide()
        self.__StartFQTimerApplication ()
        self.__StartFQTimerParams ()
        self.__StartFQTimerClock ()
    #endfunction

    def __FormClose (self):
        """__FormClose"""
    #beginfunction
        s = '__FormClose...'
        # LULog.LoggerAPPSAdd_info (s)

        self.__StopFQTimerApplication ()
        self.__StopFQTimerParams ()
        self.__StopFQTimerClock ()
    #endfunction

    def __SetStatApplication (self, AStatApplication):
        """__SetStatApplication"""
    #beginfunction
        s = '__SetStatApplication...'
        # LULog.LoggerAPPSAdd_info (s)

        self.__FStatApplication = AStatApplication

        self.ui.action_Start_Stop.setEnabled(True)

        if self.__FStatApplication == LUProc.TStatApplication.saRunning:
            self.ui.action_Start_Stop.setIcon (self.FiconStop)
        #endif

        if self.__FStatApplication == LUProc.TStatApplication.saBreak:
            self.ui.action_Start_Stop.setIcon (self.FiconStart)
        #endif

        bMain = self.__FStatApplication == LUProc.TStatApplication.saMain
        self.ui.action_CreateYoutube.setEnabled (not bMain)
        self.ui.action_Exit.setEnabled (not bMain)
        self.ui.action_ExitProgram.setEnabled (not bMain)
        self.ui.action_Cut.setEnabled (not bMain)
        self.ui.action_Copy.setEnabled (not bMain)
        self.ui.action_Paste.setEnabled (not bMain)
        self.ui.action_Start_Stop.setEnabled (not bMain)
        self.ui.action_Setup.setEnabled (not bMain)
        self.ui.action_About.setEnabled (not bMain)
        self.ui.action_Help.setEnabled (not bMain)
        self.ui.action_DeleteAll.setEnabled (not bMain)

        # self.StatApplication_event.emit (LUProc.CStatApplication [self.__FStatApplication])

        self.__FAPPSignals.StatApplication_event.emit (LUProc.CStatApplication [self.__FStatApplication])
    #endfunction

    def cliboard_changed(self, mode):
    #beginfunction
        s = 'cliboard_changed...'
        # LULog.LoggerAPPSAdd_info (s)
    #endfunction
    def cliboard_findBufferChanged (self):
    #beginfunction
        s = 'cliboard_findBufferChanged...'
        # LULog.LoggerAPPSAdd_info (s)
    #endfunction
    def cliboard_selectionChanged (self):
    #beginfunction
        s = 'cliboard_selectionChanged...'
        # LULog.LoggerAPPSAdd_info (s)
    #endfunction

    def cliboard_dataChanged(self):
    #beginfunction
        s = 'cliboard_dataChanged...'
        # LULog.LoggerAPPSAdd_debug (s)

        mimeData = self.__FClipboard.mimeData()
        if mimeData.hasImage():
            s = ' '*4+'mimeData.hasImage...'
            # LULog.LoggerAPPSAdd_info (s)
            # setPixmap(QPixmap(mimeData.imageData()))
        elif mimeData.hasHtml():
            s = ' '*4+'mimeData.hasHtml...'
            # LULog.LoggerAPPSAdd_info (s)
            # setText(mimeData.html())
            # setTextFormat(Qt.RichText)
        elif mimeData.hasText():
            s = ' '*4+'mimeData.hasText...'
            # LULog.LoggerAPPSAdd_info (s)
            # setText(mimeData.text())
            # setTextFormat(Qt.PlainText)

            # LText = self.__FClipboard.text ()
            LText: str = mimeData.text()
            # self.ui.Memo_Log.insertPlainText (LText + '\n')
            # LULog.LoggerAPPSAdd_debug (LText)
            self.__CreateObjectsURL (LText)
        else:
            s = ' '*4+'Cannot display data...'
            LULog.LoggerAPPSAdd_info (s)
            # QClipboard.Mode.Clipboard - указывает, что данные должны сохраняться и извлекаться из глобального буфера обмена.
            # QClipboard.Selection - ?????
            # QClipboard.FindBuffer - ?????
            # setText("Cannot display data", mode=QClipboard.Mode.Clipboard)
        #endif
    #endfunction

    def __ClearWidgets (self):
    #beginfunction
        s = '__ClearWidgets...'
        # LULog.LoggerAPPSAdd_debug (s)

        for i in reversed (range (self.ui.verticalLayout_3.count ())):
            item = self.ui.verticalLayout_3.itemAt (i).widget ()
            if type(item) is YOUTUBEwidget:
                item.setParent (None)
            #endif
        #endfor
        self.__FListWidgets.clear()
    #endfunction
    #--------------------------------------------------
    # __DelListWidget
    #--------------------------------------------------
    def __DelListWidget (self, AURL: str):
        """__DelListWidget"""
    #beginfunction
        s = '__DelListWidget...'
        # LULog.LoggerAPPSAdd_debug (s)

        for LItem in self.__FListWidgets:
            LWidget_X: YOUTUBEwidget = LItem
            if LWidget_X.YouTubeObject.URL == AURL:
                self.__FListWidgets.remove (LWidget_X)
                #-------------????????????????????----------------------
                # i = self.ui.verticalLayout.indexOf (LWidget_X)
                # self.ui.verticalLayout.takeAt (i)
                #----------------------------------------------------
                LWidget_X.deleteLater ()
                if LWidget_X.isVisible():
                    # ???????????????????????????????????
                    LWidget_X.hide()
                #endif
            #endif
        #endfor
    #endfunction
    #--------------------------------------------------
    # __GetListWidget
    #--------------------------------------------------
    def __GetListWidget (self, AURL: str) -> YOUTUBEwidget:
        """__GetListWidget"""
    #beginfunction
        s = '__GetListWidget...'
        # LULog.LoggerAPPSAdd_debug (s)

        LResult = None
        for LItem in self.__FListWidgets:
            LWidget_X: YOUTUBEwidget = LItem
            if LWidget_X.YouTubeObject.URL == AURL:
                return LWidget_X
            #endif
        #endfor
        return LResult
    #endfunction
    #--------------------------------------------------
    # __GetListWidgetStat
    #--------------------------------------------------
    def __GetListWidgetStat (self, AStatWidget: YOUTUBE_widgetYT.TStatWidgetObject) -> YOUTUBEwidget:
        """__GetListWidget"""
    #beginfunction
        s  = '__GetListWidget...'
        # LULog.LoggerAPPSAdd_debug (s)

        LResult = None
        for LItem in self.__FListWidgets:
            LWidget_X: YOUTUBEwidget = LItem
            if LWidget_X.StatWidgetObject.value == AStatWidget.value:
                return LWidget_X
            #endif
        #endfor
        return LResult
    #endfunction
    def __AddListWidget (self, AYouTubeObject: LUObjectsYT.TYouTubeObject) -> YOUTUBEwidget:
    #beginfunction
        s = '__AddWidget...'
        # LULog.LoggerAPPSAdd_debug (s)

        LMaxRes = LUObjectsYT.cMaxRes480p

        LWidget_X = YOUTUBEwidget(AYouTubeObject, LMaxRes,
                                  self.__FParams.CheckBoxDownload,
                                  self.ui.scrollAreaWidgetContents)
        if self.__FStatApplication == LUProc.TStatApplication.saBreak:
            LWidget_X.StopWidget()
        #endif

        # swNew + 1
        # LWidget_X.StatWidgetObject = YOUTUBE_widgetYT.TStatWidgetObject.swNew
        self.__ChangeCountStatWidgetObject (LWidget_X.StatWidgetObject, 1)

        # сигналы
        LWidget_X.YOUTUBEwidgetSignals.signal_DownloadedURL.connect (self.signalHandler_DownloadedURL)
        LWidget_X.YOUTUBEwidgetSignals.signal_ChangeStatWidgetObject.connect (self.signalHandler_ChangeStatWidgetObject)

        self.ui.verticalLayout_3.insertWidget (0, LWidget_X)
        # self.ui.verticalLayout_3.addWidget(LWidget_X, stretch = 0)

        # self.__FListWidgets.append(LWidget_X)
        self.__FListWidgets.insert(0, LWidget_X)

        # if self.__FStatApplication == LUProc.TStatApplication.saBreak:
        #     LWidget_X.StopWidget()
        # #endif
        # if self.__FStatApplication == LUProc.TStatApplication.saRunning:
        #     LWidget_X.StartWidget()
        # #endif

        LWidget_X.SetStatWidgetObject()

        QCoreApplication.processEvents ()
        return LWidget_X
    #endfunction

    def __ClearListYouTubeObject (self):
    #beginfunction
        s = '__ClearListYouTubeObject...'
        # LULog.LoggerAPPSAdd_debug (s)

        self.__FListYouTubeObject.clear()
    #endfunction
    #--------------------------------------------------
    # __DelListYouTubeObject
    #--------------------------------------------------
    def __DelListYouTubeObject (self, AURL: str):
        """__DelListYouTubeObject"""
    #beginfunction
        s = '__DelListYouTubeObject...'
        # LULog.LoggerAPPSAdd_debug (s)

        for LItem in self.__FListYouTubeObject:
            LYouTubeObject:LUObjectsYT.TYouTubeObject = LItem
            if LYouTubeObject.URL == AURL:
                self.__FListYouTubeObject.remove (LYouTubeObject)
            #endif
        #endfor
    #endfunction
    #--------------------------------------------------
    # __GetListYouTubeObject
    #--------------------------------------------------
    def __GetListYouTubeObject (self, AURL: str) -> LUObjectsYT.TYouTubeObject:
        """__GetListYouTubeObject"""
    #beginfunction
        s = '__GetListYouTubeObject...'
        # LULog.LoggerAPPSAdd_debug (s)

        LResult = None
        for LItem in self.__FListYouTubeObject:
            LYouTubeObject: LUObjectsYT.TYouTubeObject = LItem
            if LYouTubeObject.URL == AURL:
                return LYouTubeObject
            #endif
        #endfor
        return LResult
    #endfunction
    def __AddListYouTubeObject (self, AURL: str, value: dict) -> LUObjectsYT.TYouTubeObject:
    #beginfunction
        s = '__AddListYouTubeObject...'
        # LULog.LoggerAPPSAdd_debug (s)

        # LYouTubeObject
        LObjectID: datetime = LUDateTime.Now ()
        s = LUDateTime.GenerateObjectIDStr (LObjectID)
        # LULog.LoggerTOOLS.log (LULog.PROCESS, s)

        LPATH = self.Params.PathYoutubeLoad
        LYouTubeObject = LUObjectsYT.TYouTubeObject (LPATH)
        LYouTubeObject.ID = LObjectID
        LMaxRes = LUObjectsYT.cMaxRes480p
        LYouTubeObject.SetURL (AURL, LMaxRes, value ['PlayListName'], value ['NN'], value ['N'])
        LYouTubeObject.FChunk = self.__FParams.CheckBoxChunk
        LYouTubeObject.Fskip_existing = self.__FParams.CheckBoxSkipExists
        self.__FListYouTubeObject.append(LYouTubeObject)
        return LYouTubeObject
    #endfunction

    def __ClearModel (self):
    #beginfunction
        s = '__ClearModel...'
        # LULog.LoggerAPPSAdd_debug (s)

        # Вы можете либо использовать model.setStringList( QStringList{} )
        # либо вручную удалить строки с помощью model.removeRows( 0, model.rowCount() ).
        self.__FModel.removeRows (0, self.__FModel.rowCount())
        # self.__FModel.setStringList (())

        # for i in reversed(range(Amodelmodel.rowCount ())):
        #     # self.__FModel.removeRow (i)
        #     self.__FModel.removeRows (self.ui.ListViewL.currentIndex().row(), 1)
        # #enfor
    #endfunction
    def __AddModel (self, AURL: str):
    #beginfunction
        s = '__AddModel...'
        # LULog.LoggerAPPSAdd_debug (s)

        Lindex = self.__FModel.rowCount ()
        self.__FModel.insertRow (Lindex)
        self.__FModel.setData (self.__FModel.index (Lindex), AURL)
    #endfunction
    #--------------------------------------------------
    # __DelModel
    #--------------------------------------------------
    def __DelModel (self, AURL: str):
        """__DelModel"""
    #beginfunction
        s = '__DelModel...'
        # LULog.LoggerAPPSAdd_debug (s)

        for i in reversed (range (self.__FModel.rowCount ())):
            # print (self.__FModel.stringList()[i])
            if self.__FModel.stringList()[i] == AURL:
                self.__FModel.removeRow (i)
                break
            #endif
        #enfor
    #endfunction
    #--------------------------------------------------
    # __GetModel
    #--------------------------------------------------
    def __GetModel (self, AURL: str) -> str:
        """__GetModel"""
    #beginfunction
        s = '__GetModel...'
        # LULog.LoggerAPPSAdd_debug (s)

        LResult = ''
        for i in reversed (range (self.__FModel.rowCount ())):
            # print (self.__FModel.stringList()[i])
            if self.__FModel.stringList()[i] == AURL:
                return self.__FModel.stringList()[i]
            #endif
        #enfor
        return LResult
    #endfunction

    #------------------------------------------
    # __Action_Testfunction
    #------------------------------------------
    def __Action_TestFunction (self):
        """__Action_TestFunction"""
    #beginfunction
        s = '__Action_TestFunction...'
        LULog.LoggerAPPSAdd_info (s)

        # gives a single float value
        Lcpu_percent = psutil.cpu_percent ()
        print(Lcpu_percent)
        # gives an object with many fields
        Lvirtual_memory = psutil.virtual_memory ()
        print(Lvirtual_memory)
        # you can convert that object to a dictionary
        Ldict = dict (psutil.virtual_memory ()._asdict ())
        print(Ldict)
        # you can have the percentage of used RAM
        Lvirtual_memory_percent =  psutil.virtual_memory ().percent
        print(Lvirtual_memory_percent)
        # you can calculate percentage of available memory
        Lvirtual_memory_available =  psutil.virtual_memory ().available * 100 / psutil.virtual_memory ().total
        print (Lvirtual_memory_available)
    #endfunction

    def __Procedure_01(self):
        """__Procedure_01"""
    #beginfunction
        s = '__Procedure_01...'
        LULog.LoggerAPPSAdd_info (s)
    #endfunction

    def Main(self):
        """Main"""
    #beginfunction
        s = 'Main...'
        # LULog.LoggerAPPSAdd_info (s)

        self.StopApplication()
        self.__SetStatApplication (LUProc.TStatApplication.saMain)
        LSaveCurrentDir = LUos.GetCurrentDir()
        LULog.LoggerAPPSAdd (LULog.BEGIN, LUProc.cProcessBegin)
        self.P_StatMain.setText(LUProc.cProcessWork)

        self.__FStopApplicationMain = False
        if self.Params.CheckBoxStop:
            self.__Procedure_01()
        #endif
        i = 0
        iMax = 0
        while not self.__FStopApplicationMain and i < iMax:
            i += 1
            s = 'Main...'
            LULog.LoggerAPPSAdd_info (str(i)+'. '+s)
            # time.sleep(1)
            QCoreApplication.processEvents ()
        #endwhile
        self.__FStopApplicationMain = True

        self.P_StatMain.setText(LUProc.cProcessStop)
        LULog.LoggerAPPSAdd( LULog.END, LUProc.cProcessEnd)
        os.chdir(LSaveCurrentDir)
        self.StartApplication()
    #endfunction

    @LUDecotators.TIMING
    def __CreateObjectsURL (self, AURL: str):
        """__CreateObjectsURL"""
    #beginfunction
        s = '__CreateObjectsURL...'
        # LULog.LoggerAPPSAdd_info (s)

        if self.Flast_copied == AURL:
            s = AURL + ' дубликат cliboard ...'
            LULog.LoggerTOOLS.log (LULog.PROCESS, s)
        #endif
        # self.Flast_copied = ''

        self.Flast_copied = AURL
        if "www.youtube.com" in self.Flast_copied or "youtu.be" in self.Flast_copied:
            self.__FClipboardList.append (self.Flast_copied)
            LURLs = dict ()
            LURL = self.Flast_copied
            LUObjectsYT.CheckURLs (LURL, LURLs)

            for LURL, Lvalue in LURLs.items ():
                s = 'CreateObject...'
                # LULog.LoggerTOOLS.log (LULog.PROCESS, s)
                LULog.LoggerTOOLS.log (LULog.PROCESS, LURL)
                if self.__GetListYouTubeObject (LURL) is None:
                    # Добавить LURL в self.__FListYouTubeObject
                    LYouTubeObject = self.__AddListYouTubeObject (LURL, Lvalue)
                    LYouTubeObject.PathDownload = self.Params.PathYoutubeLoad

                    # Добавить LURL в self.__FModel
                    self.__AddModel (LURL)
                    # Добавить виджет в self.__FWidgets
                    self.__AddListWidget (LYouTubeObject)
                else:
                    s = LURL+' существует ...'
                    LULog.LoggerTOOLS.log (LULog.PROCESS, s)
                #endif
                QCoreApplication.processEvents ()
            #endfor
        #endif
    #endfunction

    @QtCore.Slot (name = '__Action_CreateYoutube')
    def __Action_CreateYoutube (self):
        """__Action_CreateYoutube"""
    #beginfunction
        s = '__Action_CreateYoutube...'
        # LULog.LoggerAPPSAdd_info (s)

        LSaveStatApplication = self.__FStatApplication
        self.__SetStatApplication (LUProc.TStatApplication.saBreak)
        if len (self.Flast_copied) > 0:
            self.cliboard_dataChanged()
        #endif
        self.__SetStatApplication (LSaveStatApplication)
    #endfunction
    @QtCore.Slot (name = '__Action_Exit')
    def __Action_Exit (self):
        """__Action_Exit"""
    #beginfunction
        s = '__Action_Exit...'
        # LULog.LoggerAPPSAdd_info (s)

        self.__FormClose()

        # raise NameError ('HiThere')
    #endfunction
    @QtCore.Slot (name = '__Action_Cut')
    def __Action_Cut (self):
        """__Action_Cut"""
    #beginfunction
        s = '__Action_Cut...'
        LULog.LoggerAPPSAdd_info (s)
    #endfunction
    @QtCore.Slot (name = '__Action_Copy')
    def __Action_Copy (self):
        """__Action_Copy"""
    #beginfunction
        s = '__Action_Copy...'
        LULog.LoggerAPPSAdd_info (s)
    #endfunction
    @QtCore.Slot (name = '__Action_Paste')
    def __Action_Paste (self):
        """__Action_Paste"""
    #beginfunction
        s = '__Action_Paste...'
        LULog.LoggerAPPSAdd_info (s)
    #endfunction
    def __Action_Sheduler (self, A):
        """__Action_Sheduler"""
    #beginfunction
        s = '__Action_Sheduler...'
        # LULog.LoggerAPPSAdd_info (s)

        self.StartApplication ()
        self.Main ()
    #endfunction

    def __StartFQTimerApplication (self):
        """__StartFQTimerApplication"""
    #beginfunction
        s = '__StartFQTimerApplication...'
        # LULog.LoggerAPPSAdd_debug (s)

        # self.__FidleApplication = True
        self.__FQTimerApplication.timeout.connect (self.__run_idleApplication)
        self.__FQTimerApplication.start ()
    #endfunction
    def __StopFQTimerApplication (self):
        """__StopFQTimerApplication"""
    #beginfunction
        s = '__StopFQTimerApplication...'
        # LULog.LoggerAPPSAdd_debug (s)

        # self.__FidleApplication = False
        self.__FQTimerApplication.stop()
        self.__FQTimerApplication.timeout.disconnect(self.__run_idleApplication)
    #endfunction
    def __StartFQTimerParams (self):
        """__StartFQTimerParams"""
    #beginfunction
        s = '__StartFQTimerParams...'
        # LULog.LoggerAPPSAdd_debug (s)

        # self.__FidleParams = True
        self.__FQTimerParams.timeout.connect (self.__run_idleParams)
        self.__FQTimerParams.start ()
    #endfunction
    def __StopFQTimerParams (self):
        """__StopFQTimerParams"""
    #beginfunction
        s = '__StopFQTimerParams...'
        # LULog.LoggerAPPSAdd_debug (s)

        # self.__FidleParams = False
        self.__FQTimerParams.stop()
        self.__FQTimerParams.timeout.disconnect(self.__run_idleParams)
    #endfunction
    def __StartFQTimerClock (self):
        """__StartFQTimerClock"""
    #beginfunction
        s = '__StartFQTimerClock...'
        # LULog.LoggerAPPSAdd_debug (s)

        # self.__FidleParams = True
        self.__FQTimerClock.timeout.connect (self.__run_idleClock)
        self.__FQTimerClock.start ()
    #endfunction
    def __StopFQTimerClock (self):
        """__StopFQTimerClock"""
    #beginfunction
        s = '__StopFQTimerClock...'
        # LULog.LoggerAPPSAdd_debug (s)

        # self.__FidleClock = False
        self.__FQTimerClock.stop()
        self.__FQTimerClock.timeout.disconnect(self.__run_idleClock)
    #endfunction

    def __StartFSheduler (self):
        """__StartFSheduler"""
    #beginfunction
        s = '__StartFSheduler...'
        # LULog.LoggerAPPSAdd_debug (s)

        self.__FSheduler.Enable = True
        s = 'Следующий сеанс: ' + str (self.__FSheduler.DTEvents)
        self.P_StatSheduler.setText (s)
    #endfunction
    def __StopFSheduler (self):
        """__StartFSheduler"""
    #beginfunction
        s = '__StopFSheduler...'
        # LULog.LoggerAPPSAdd_debug (s)

        self.__FSheduler.Enable = False
        s = 'Следующий сеанс:'
        self.P_StatSheduler.setText (s)
    #endfunction

    def StartApplication (self):
        """StartApplication"""
    #beginfunction
        s = 'StartApplication...'
        # LULog.LoggerAPPSAdd_info (s)

        self.__StartFSheduler()
        self.__SetStatApplication (LUProc.TStatApplication.saRunning)
    #endfunction
    def StopApplication (self):
        """StopApplication"""
    #beginfunction
        s = 'StopApplication...'
        # LULog.LoggerAPPSAdd_info (s)

        self.__StopFSheduler()
        self.__SetStatApplication (LUProc.TStatApplication.saBreak)
    #endfunction

    @QtCore.Slot (name = '__Action_Start_Stop')
    def __Action_Start_Stop (self):
        """__Action_Start"""
    #beginfunction
        s = '__Action_Start_Stop...'
        # LULog.LoggerAPPSAdd_info (s)

        if self.__FStatApplication == LUProc.TStatApplication.saBreak:
            self.StartApplication()
            self.Main()
        else:
            self.__FAPPSignals.StopApplication_event.emit (True)
            self.StopApplication()
        #endif
    #endfunction
    @QtCore.Slot (name = '__Action_Setup')
    def __Action_Setup (self):
        """__Action_Setup"""
    #beginfunction
        s = '__Action_Setup...'
        # LULog.LoggerAPPSAdd_info (s)

        LSaveStatApplication = self.__FStatApplication

        self.__SetStatApplication (LUProc.TStatApplication.saBreak)
        self.__FAPPSignals.StatApplication_event.emit(LUProc.cProcessSetup)

        LSaveCurrentDir = LUos.GetCurrentDir()
        LFormSetup = YOUTUBE_FormSetupWindow.FormSetup ()
        LResult = LFormSetup.exec()
        if LResult == LUProc.mrOk:
            # FSheduler.DeleteEvent (ShedulerName)
            # FSheduler.AddEvent (ShedulerName, TEMPLATE_RegIni.ShedulerTEMPLATE)
            LFormSetup.SaveSetup()
        #endif
        os.chdir(LSaveCurrentDir)

        self.__SetStatApplication (LSaveStatApplication)
    #endfunction
    @QtCore.Slot (name = '__Action_About')
    def __Action_About (self):
        """__Action_About"""
    #beginfunction
        s = '__Action_About...'
        # LULog.LoggerAPPSAdd_info (s)

        LSaveStatApplication = self.__FStatApplication
        # Остановить выполнение Application
        self.__SetStatApplication (LUProc.TStatApplication.saBreak)
        self.__FAPPSignals.StatApplication_event.emit(LUProc.cProcessAbout)

        LFormAbout = YOUTUBE_FormAboutWindow.FormAbout ()
        LResult = LFormAbout.exec()

        self.__SetStatApplication (LSaveStatApplication)
    #endfunction
    @QtCore.Slot (name = '__Action_Help')
    def __Action_Help (self):
        """__Action_Help"""
    #beginfunction
        s = '__Action_Help...'
        # LULog.LoggerAPPSAdd_info (s)

        LSaveStatApplication = self.__FStatApplication
        # Остановить выполнение Application
        self.__SetStatApplication (LUProc.TStatApplication.saBreak)
        self.__FAPPSignals.StatApplication_event.emit(LUProc.cProcessHelp)

        # Application.HelpContext (6)

        self.__SetStatApplication (LSaveStatApplication)
    #endfunction

    @QtCore.Slot (name = '__Action_DeleteAll')
    def __Action_DeleteAll (self):
        """__Action_DeleteAll"""
    #beginfunction
        s = '__Action_DeleteAll...'
        # LULog.LoggerAPPSAdd_info (s)
        LSaveStatApplication = self.__FStatApplication

        if LSaveStatApplication == LUProc.TStatApplication.saRunning:
            # Остановить выполнение Application
            self.__SetStatApplication (LUProc.TStatApplication.saBreak)
        #endif
        LCountWidget = len(self.__FListWidgets)
        while LCountWidget > 0:
            # swNew
            LWidget_X = self.__GetListWidgetStat (YOUTUBE_widgetYT.TStatWidgetObject.swNew)
            if not LWidget_X is None:
                LURL = LWidget_X.YouTubeObject.URL
                # swNew - 1
                self.signalHandler_ChangeStatWidgetObject (YOUTUBE_widgetYT.TStatWidgetObject.swNew, -1)
                self.signalHandler_DownloadedURL (LURL)
            else:
                # swQueue
                LWidget_X = self.__GetListWidgetStat (YOUTUBE_widgetYT.TStatWidgetObject.swQueue)
                if not LWidget_X is None:
                    LURL = LWidget_X.YouTubeObject.URL
                    # swQueue - 1
                    self.signalHandler_ChangeStatWidgetObject (YOUTUBE_widgetYT.TStatWidgetObject.swQueue, -1)
                    self.signalHandler_DownloadedURL (LURL)
                else:
                    # swGetInfo
                    LWidget_X = self.__GetListWidgetStat (YOUTUBE_widgetYT.TStatWidgetObject.swGetInfo)
                    if not LWidget_X is None:
                        # Ничего делать не нужно. Ждать завершения потока swGetInfo
                        ...
                    else:
                        # swDownload
                        LWidget_X = self.__GetListWidgetStat (YOUTUBE_widgetYT.TStatWidgetObject.swDownload)
                        if not LWidget_X is None and LWidget_X.YouTubeObject.FChunk:
                            # Завершить поток swDownload
                            LWidget_X.YouTubeObject.Fis_cancelled = True
                        else:
                            # Ничего делать не нужно. Ждать завершения потока swDownload
                            ...
                        #endif
                    #endif
                #endif
            #endif
            LCountWidget = len(self.__FListWidgets)
            QCoreApplication.processEvents ()
        #endwhile

        if LSaveStatApplication == LUProc.TStatApplication.saRunning:
            # Запустить выполнение Application
            self.__SetStatApplication (LUProc.TStatApplication.saRunning)
        #endif
    #endfunction

    #--------------------------------------------------
    # __ChangeCountStatWidgetObject
    #--------------------------------------------------
    def __ChangeCountStatWidgetObject (self, AStatWidget: YOUTUBE_widgetYT.TStatWidgetObject, ACount: int):
        """__GetListWidgetCount"""
    #beginfunction
        s = '__ChangeCountStatWidgetObject...'
        # LULog.LoggerAPPSAdd_debug (s)
        match AStatWidget:
            case YOUTUBE_widgetYT.TStatWidgetObject.swNew:
                self.__FswNew += ACount
            case YOUTUBE_widgetYT.TStatWidgetObject.swQueue:
                self.__FswQueue += ACount
            case YOUTUBE_widgetYT.TStatWidgetObject.swGetInfo:
                self.__FswGetInfo += ACount
            case YOUTUBE_widgetYT.TStatWidgetObject.swDownload:
                self.__FswDownload += ACount
            case YOUTUBE_widgetYT.TStatWidgetObject.swDownloaded:
                self.__FswDownloaded += ACount
            case _:
                ...
        #endmatch
        s = f'{self.__FswNew}:{self.__FswGetInfo}:{self.__FswQueue}:{self.__FswDownload}:{self.__FswDownloaded}'
        self.P_StatCountWidgetObject.setText (s)
    #endfunction

    #--------------------------------------------------
    # __GetListWidgetCount
    #--------------------------------------------------
    def __GetListWidgetCount (self, AStatWidget: YOUTUBE_widgetYT.TStatWidgetObject) -> int:
        """__GetListWidgetCount"""
    #beginfunction
        s = '__GetListWidgetCount...'
        # LULog.LoggerAPPSAdd_debug (s)

        LResult = 0
        for LItem in self.__FListWidgets:
            LWidget_X: YOUTUBEwidget = LItem
            if LWidget_X.StatWidgetObject.value == AStatWidget.value:
                LResult = LResult + 1
            #endif
        #endfor
        return LResult
    #endfunction

    #--------------------------------------------------
    # __runProcess
    #--------------------------------------------------
    def __runProcess(self):
        """__runProcess"""
    #beginfunction
        if self.__FStatApplication == LUProc.TStatApplication.saDeleteAll:
            ...
        else:
            # swNew
            LWidget_X = self.__GetListWidgetStat (YOUTUBE_widgetYT.TStatWidgetObject.swNew)
            if not LWidget_X is None:
                NswGetInfo = self.__GetListWidgetCount (YOUTUBE_widgetYT.TStatWidgetObject.swGetInfo)
                NswDownload = self.__GetListWidgetCount (YOUTUBE_widgetYT.TStatWidgetObject.swDownload)
                if (NswGetInfo + NswDownload) < self.__FParams.NumberThread:
                # if (NswGetInfo+NswDownload) < self.__FMaxThread:
                    LWidget_X.run_GetInfoStream ()
                #endif
            #endif

            # swQueue
            LWidget_X = self.__GetListWidgetStat (YOUTUBE_widgetYT.TStatWidgetObject.swQueue)
            if not LWidget_X is None:
                NswGetInfo = self.__GetListWidgetCount (YOUTUBE_widgetYT.TStatWidgetObject.swGetInfo)
                NswDownload = self.__GetListWidgetCount (YOUTUBE_widgetYT.TStatWidgetObject.swDownload)
                if (NswGetInfo+NswDownload) < self.__FParams.NumberThread:
                    LFileName = LWidget_X.YouTubeObject.FileNameDownload
                    if not LUFile.FileExists (LFileName):
                        LWidget_X.run_Downloader ()
                    else:
                        s = 'Файл ' + LFileName + ' существует...'
                        LULog.LoggerTOOLS.debug (s)
                        if not self.__FParams.CheckBoxSkipExists:
                            s = 'Файл ' + LFileName + ' будет загружен повторно...'
                            LULog.LoggerTOOLS.debug (s)
                            # LUFile.FileDelete (LFileName)
                            LWidget_X.run_Downloader ()
                        else:
                            s = 'Файл ' + LFileName + ' не будет загружен...'
                            LULog.LoggerTOOLS.debug (s)
                            # swQueue - 1
                            self.__ChangeCountStatWidgetObject (LWidget_X.StatWidgetObject, -1)
                            LWidget_X.StopWidget ()
                            # Удаление Widget
                            LURL = LWidget_X.YouTubeObject.URL
                            self.signalHandler_DownloadedURL (LURL)
                        #endif
                    #endif
                #endif
            #endif
        #endif
    #endfunction

    #--------------------------------------------------
    # __run_idleApplication
    #--------------------------------------------------
    @QtCore.Slot (str, name = '__run_idleApplication')
    def __run_idleApplication(self):
        """__run_idleApplication"""
    #beginfunction
        s = '__run_idleApplication'
        # LULog.LoggerAPPSAdd_debug (s)

        # while self.__FidleApplication:

        Lcpu_percent = psutil.cpu_percent ()
        Lvirtual_memory_percent = psutil.virtual_memory ().percent
        if Lcpu_percent > 0:
            self.P_ProgressBar.setValue(Lcpu_percent)
        #endif

        if self.__FStatApplication == LUProc.TStatApplication.saRunning:
            self.__runProcess ()
            self.__FSheduler.run_Function ()
        #endif
        if len (self.__FListWidgets) > 0:
            self.ui.TextEditR.hide ()
        else:
            self.ui.TextEditR.show ()
        #endif
        QCoreApplication.processEvents ()

        #endwhile
    #endfunction

    #--------------------------------------------------
    # __run_idleParams
    #--------------------------------------------------
    @Slot (str, name = '__run_idleParams')
    def __run_idleParams(self):
        """__run_idleParams"""
    #beginfunction
        s = '__run_idleParams'
        # LULog.LoggerAPPSAdd_debug (s)

        self.__FParams.RefreashOption()
        if self.__FStatApplication == LUProc.TStatApplication.saRunning:
            if self.__FParams.CheckBoxStop:
                self.StopApplication()
            #endif
        #endif
        if self.__FStatApplication == LUProc.TStatApplication.saBreak:
            if not self.__FParams.CheckBoxStop:
                self.StartApplication()
            #endif
        #endif
        self.__FQTimerParams.setInterval(self.__FQTimerParamsInterval)
        QCoreApplication.processEvents ()
    #endfunction

    #--------------------------------------------------
    # __run_idleClock
    #--------------------------------------------------
    @QtCore.Slot (str, name = '__run_idleClock')
    def __run_idleClock(self):
        """__run_idleClock"""
    #beginfunction
        s = '__run_idleClock'
        # LULog.LoggerAPPSAdd_debug (s)

        Ltime = QTime.currentTime()
        Ltext = Ltime.toString("hh:mm:ss")
        # # Blinking effect
        # if (Ltime.second() % 2) == 0:
        #     Ltext = Ltext.replace(":", " ")
        # #endif
        self.P_Clock.setText (Ltext)
        QCoreApplication.processEvents ()
    #endfunction
#endclass

#------------------------------------------
#
#------------------------------------------
def main ():
#beginfunction
    LULog.STARTLogging ('LOG', 'LOGGING_FILEINI.log', 'LOGGING_FILEINI_json.log')

    GAPP = QApplication (sys.argv)
    GFormMainWindow = FormMainWindow()
    GFormMainWindow.show()

    GFormMainWindow.StartApplication ()
    GFormMainWindow.Main()

    LResult = GAPP.exec ()
    s = 'ExitProgram...'
    LULog.LoggerAPPSAdd_info (s)
    sys.exit(LResult)
#endfunction

#------------------------------------------
#
#------------------------------------------
#beginmodule
if __name__ == "__main__":
    main()
#endif

#endmodule
