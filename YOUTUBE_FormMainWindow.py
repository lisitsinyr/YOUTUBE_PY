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
    QListView, QMainWindow, QMenu, QMenuBar,
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

GAPP = QApplication (sys.argv)

class CustomButton_01 (QPushButton):
    def mousePressEvent (self, event):
        event.accept ()
class CustomButton_02 (QPushButton):
    def event (self, event):
        event.ignore ()

# ------------------------------------
# FormMainWindow(QMainWindow)
# ------------------------------------
class FormMainWindow(QMainWindow):
    """FormMainWindow"""
    luClassName = 'FormMainWindow'

    #----------------------------------------------
    # СИГНАЛ
    #----------------------------------------------
    StatApplication_event = QtCore.Signal(str)

    closed = QtCore.Signal ()

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
    def signalHandler_DownloadURL(self, text):
        """signalHandler_DownloadURL"""
    #beginfunction
        s = 'signalHandler_DownloadURL...'
        LULog.LoggerAPPS.debug (s)
        LURL = text
        self.__DelModel (LURL)
        self.__DelListWidget (LURL)
        self.__DelListYouTubeObject (LURL)
    #endfunction

    def __init__(self, parent=None):
    #beginfunction
        super().__init__()
        self.ui = Ui_FormMainWindow()
        self.ui.setupUi(self)

        self.__FLogDir: str = ''
        self.__FStopYouTube: bool = True

        self.idle = False

        # Состояние программы
        self.__FStatApplication: LUProc.TStatApplication = LUProc.TStatApplication.saRunning
        # __FParams
        self.__FParams: YOUTUBE_Params.TParams = YOUTUBE_Params.TParams ()
        # self.APPLog = self.__FParams.FileMemoLog

        self.__FSheduler = None

        self.__FormCreate ()
        self.__FormActivate ()

        self.__FMaxThread: int = 5

        self.ui.TEST_widget.hide()
    #endfunction

    #--------------------------------------------------
    # destructor
    #--------------------------------------------------
    def __del__ (self):
        """__del__"""
    #beginfunction
        # self.__FormDestroy()
        LClassName = self.__class__.__name__
        s = '{} уничтожен'.format(LClassName)
        #print (s)
    #endfunction

    def closeEvent(self, event):
        """closeEvent"""
    #beginfunction
        self.closed.emit()
        super().closeEvent(event)
        # QCoreApplication.instance ().quit()
        QApplication.quit()
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
        LULog.LoggerAPPS.debug (s)
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
        LULog.LoggerAPPS.debug (s)
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
        LULog.LoggerAPPS.debug (s)
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
        LULog.LoggerAPPS.debug (s)
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
    # 01.__SetLogs
    #--------------------------------------------------
    def __SetLogs (self):
        """__SetLogs"""
    #beginfunction
        s = '01.__SetLogs...'
        LULog.LoggerAPPS.info (s)
        # self.APPLog: LULog.TFileMemoLog = LULog.FileMemoLog
        #----------------- Memo_Log --------------------------
        self.ui.Memo_Log.setReadOnly (True)
        self.__SetStylesheetsFor_ALL()
        self.__SetStylesheetsFor_Memo_Log()
        # self.__SetColorFor_Memo_Log()

        LULog.PrintHandlers (LULog.LoggerAPPS)
        LHandler: LULog.TStreamHandler = LULog.GetHandler (LULog.LoggerAPPS, 'CONSOLE')
        LHandler.widget = self.ui.Memo_Log
        # LULog.LoggerAPPS.info ('LULog.LoggerAPPS-> '+'TEST...')
        # self.ui.Memo_Log.appendPlainText ('mhsdkjhfkjhsakjh'+'\n')

        LULog.PrintHandlers (LULog.LoggerTOOLS)
        LHandler: LULog.TStreamHandler = LULog.GetHandler (LULog.LoggerAPPS, 'CONSOLE')
        LHandler.widget = self.ui.Memo_Log
        # LULog.LoggerAPPS.info ('LULog.LoggerTOOLS-> '+'TEST...')
    #endfunction

    #-------------------------------
    # 02.__SetStatusBar_PN
    #-------------------------------
    def __SetStatusBar_PN (self):
        """__SetStatusBar_PN"""
    #beginfunction
        s = '02.__SetStatusBar_PN...'
        LULog.LoggerAPPS.info (s)

        # self.ui.StatusBar_PN.stasetStyleSheet (
        #     "QStatusBar{padding-left:8px;background:rgba(255,0,0,255);color:black;font-weight:bold;}")
        # display a message in 5 seconds
        # self.ui.StatusBar_PN.showMessage ("Error Cannot determine filepath", 5000)
        # display a message in 5 seconds
        # self.ui.StatusBar_PN.showMessage('Ready', 5000)

        #================================================
        # P_Main - add a permanent widget to the status bar
        #================================================
        self.P_StatMain = QLabel('P_Main')
        self.ui.StatusBar_PN.addPermanentWidget(self.P_StatMain)
        s = self.P_StatMain.text()
        self.P_StatMain.setText(LUProc.cProcessStop)

        #================================================
        # P_StatApplication - add a permanent widget to the status bar
        #================================================
        self.P_StatApplication = QLabel('P_StatApplication')
        self.ui.StatusBar_PN.addPermanentWidget(self.P_StatApplication)
        s = self.P_StatApplication.text()
        self.P_StatApplication.setText(LUProc.CStatApplication[self.__FStatApplication])

        #================================================
        # P_StatEvents - add a permanent widget to the status bar
        #================================================
        self.P_StatEvents = QLabel('P_StatEvents')
        self.ui.StatusBar_PN.addPermanentWidget(self.P_StatEvents)
        s = self.P_StatEvents.text()
        self.P_StatEvents.setText('P_StatEvents')

        #================================================
        # P_StatSheduler - add a permanent widget to the status bar
        #================================================
        self.P_StatSheduler = QLabel('P_StatEvents')
        self.ui.StatusBar_PN.addPermanentWidget(self.P_StatSheduler)
        s = self.P_StatSheduler.text()
        self.P_StatSheduler.setText('P_StatEvents')

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
        LULog.LoggerAPPS.info (s)
        #-------------------------------
        # Sheduler
        #-------------------------------
        self.__FSheduler = LUSheduler.TSheduler ()
        LEvent = self.__FSheduler.AddEvent ('ShedulerTEST1', '* * * * *')
        self.__FSheduler.OnSheduler = self.__Action_Sheduler
        if LEvent is not None:
            self.__FSheduler.PrintEvent (LEvent)
        #endif
        self.__FSheduler.Enable = True
        self.__FSheduler.start()

        # FSheduler = TSheduler.Create (Self)
        # with FSheduler do begin
        #     Enabled = False
        #     OnSheduler = Action_Start
        #     AddEvent (ShedulerName, TEMPLATE_RegIni.ShedulerTEMPLATE)
        # end
    #endfunction

    #--------------------------------------------------
    # 04.__SetClipboard
    #--------------------------------------------------
    def __SetClipboard (self):
        """__SetClipboard"""
    #beginfunction
        s = '04.__SetClipboard...'
        LULog.LoggerAPPS.info (s)
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
        LULog.LoggerAPPS.info (s)

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
        LULog.LoggerAPPS.info (s)

        self.__FListWidgets = list()

        LFileName = os.path.join (LUos.GetCurrentDir(), 'YOUTUBE.txt')

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
        LULog.LoggerAPPS.info (s)
        self.__FListYouTubeObject = list()
        self.__ClearListYouTubeObject()
    #endfunction
    #--------------------------------------------------
    # 08.__SetTimer
    #--------------------------------------------------
    def __SetTimer (self):
        """__SetTimer"""
    #beginfunction
        s = '08.__SetTimer...'
        LULog.LoggerAPPS.info (s)
        self.__FTimer = QtCore.QTimer ()
        self.__FTimer.setInterval (1)
        # self.__FTimer.timeout.connect (self.recurring_timer)
        self.__FTimer.timeout.connect (self.__run_idle)
        self.__FTimer.start ()
        self.StatApplication_event.connect (self.signalHandler_StatApplication)
    #endfunction
    #--------------------------------------------------
    # 09.__SetActions
    #--------------------------------------------------
    def __SetActions (self):
        """__SetActions"""
    #beginfunction
        s = '09.__SetActions...'
        LULog.LoggerAPPS.info (s)

        self.ui.action_CreateYoutube.triggered.connect (self.__Action_CreateYoutube)
        self.ui.action_Exit.triggered.connect(self.__Action_Exit)
        self.ui.action_Cut.triggered.connect(self.__Action_Cut)
        self.ui.action_Copy.triggered.connect(self.__Action_Copy)
        self.ui.action_Paste.triggered.connect(self.__Action_Paste)
        self.ui.action_Start_Stop.triggered.connect(self.__Action_Start_Stop)
        self.ui.action_Setup.triggered.connect(self.__Action_Setup)
        self.ui.action_About.triggered.connect(self.__Action_About)
        self.ui.action_Help.triggered.connect(self.__Action_Help)
        self.ui.action_DeleteAll.triggered.connect(self.__Action_DeleteAll)

        self.FiconStart = QIcon()
        self.FiconStart.addFile(u":/ICONS/run.png", QSize(), QIcon.Normal, QIcon.Off)
        self.FiconStop = QIcon()
        self.FiconStop.addFile(u":/ICONS/stop.png", QSize(), QIcon.Normal, QIcon.Off)
    #endfunction

    @LUDecotators.TIMING
    def __FormCreate (self):
        """__FormCreate"""
    #beginfunction
        s = '__FormCreate...'
        LULog.LoggerAPPS.info (s)
        self.setWindowTitle(YOUTUBE_Consts.cProjectNAME)
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
        # 08.__SetTimer
        self.__SetTimer()
        # 09.__SetActions
        self.__SetActions()
        #----------------- VersionInfo --------------------------
        # VersionInfo = CreateVersion (ParamStr(0))
        # LULog.LoggerAPPS.log (LULog.TEXT, ParamStr (0) + ' ' + VersionInfo.FileVersion+ ' ' + VersionInfo.FileDate)
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

    # def __FormDestroy (self):
    #     """__FormDestroy"""
    # #beginfunction
    #     s = '__FormDestroy...'
    #     LULog.LoggerAPPS.info (s)
    #     self.__FormClose ()
    # #endfunction

    def __FormActivate (self):
        """__FormActivate"""
    #beginfunction
        s = '__FormActivate...'
        LULog.LoggerAPPS.info (s)
        LULog.LoggerAPPS.log (LULog.TEXT, self.__FParams.FileMemoLog.FileName)
        LULog.LoggerAPPS.log (LULog.TEXT, self.__FParams.FileNameINI)
        self.__SetStatApplication (LUProc.TStatApplication.saRunning)
        self.__Main ()
    #endfunction

    def __FormClose (self):
        """__FormClose"""
    #beginfunction
        s = '__FormClose...'
        LULog.LoggerAPPS.info (s)

        self.__FTimer.timeout.disconnect()
        self.__FTimer.stop()

        self.close()
    #endfunction

    # TFormMain.SetStatApplication
    def __SetStatApplication (self, AStatApplication):
    #beginfunction
        self.__FStatApplication = AStatApplication

        self.ui.action_Start_Stop.setEnabled(True)

        if self.__FStatApplication == LUProc.TStatApplication.saRunning:
            self.ui.action_Start_Stop.setIcon (self.FiconStop)
            # Sheduler
            self.__FSheduler.Enable = True
        #endif

        if self.__FStatApplication == LUProc.TStatApplication.saBreak:
            self.ui.action_Start_Stop.setIcon (self.FiconStart)
            # Sheduler
            self.__FSheduler.Enable = False
        #endif

        if self.__FSheduler.Enable:
            s = 'Следующий сеанс: ' + str (self.__FSheduler.DTEvents)
            self.P_StatSheduler.setText (s)
        else:
            s = 'Следующий сеанс: '
            self.P_StatSheduler.setText (s)
        #endif
        self.StatApplication_event.emit (LUProc.CStatApplication [self.__FStatApplication])
    #endfunction

    def cliboard_changed(self, mode):
    #beginfunction
        s = 'cliboard_changed...'
        # LULog.LoggerAPPS.info (s)
    #endfunction
    def cliboard_findBufferChanged (self):
    #beginfunction
        s = 'cliboard_findBufferChanged...'
        # LULog.LoggerAPPS.info (s)
    #endfunction
    def cliboard_selectionChanged (self):
    #beginfunction
        s = 'cliboard_selectionChanged...'
        # LULog.LoggerAPPS.info (s)
    #endfunction

    def cliboard_dataChanged(self):
    #beginfunction
        s = 'cliboard_dataChanged...'
        # LULog.LoggerAPPS.debug (s)
        mimeData = self.__FClipboard.mimeData()
        if mimeData.hasImage():
            s = ' '*4+'mimeData.hasImage...'
            # LULog.LoggerAPPS.info (s)
            # setPixmap(QPixmap(mimeData.imageData()))
        elif mimeData.hasHtml():
            s = ' '*4+'mimeData.hasHtml...'
            # LULog.LoggerAPPS.info (s)
            # setText(mimeData.html())
            # setTextFormat(Qt.RichText)
        elif mimeData.hasText():
            s = ' '*4+'mimeData.hasText...'
            # LULog.LoggerAPPS.info (s)
            # setText(mimeData.text())
            # setTextFormat(Qt.PlainText)

            # LText = self.__FClipboard.text ()
            LText: str = mimeData.text()
            # self.ui.Memo_Log.insertPlainText (LText + '\n')
            # LULog.LoggerAPPS.debug (LText)
            self.__CreateObjectsURL (LText)
        else:
            s = ' '*4+'Cannot display data...'
            LULog.LoggerAPPS.info (s)
            # QClipboard.Mode.Clipboard - указывает, что данные должны сохраняться и извлекаться из глобального буфера обмена.
            # QClipboard.Selection - ?????
            # QClipboard.FindBuffer - ?????
            # setText("Cannot display data", mode=QClipboard.Mode.Clipboard)
        #endif
    #endfunction

    def __ClearWidgets (self):
    #beginfunction
        s = '__ClearWidgets...'
        # LULog.LoggerAPPS.debug (s)
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
        # LULog.LoggerAPPS.debug (s)
        for LItem in self.__FListWidgets:
            Lwidget_X: YOUTUBEwidget = LItem
            if Lwidget_X.FYouTubeObject.URL == AURL:
                self.__FListWidgets.remove (Lwidget_X)
                #-------------????????????????????----------------------
                # i = self.ui.verticalLayout.indexOf (Lwidget_X)
                # self.ui.verticalLayout.takeAt (i)
                #----------------------------------------------------
                Lwidget_X.deleteLater ()
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
        # LULog.LoggerAPPS.debug (s)
        LResult = None
        for LItem in self.__FListWidgets:
            Lwidget_X: YOUTUBEwidget = LItem
            if Lwidget_X.FYouTubeObject.URL == AURL:
                return Lwidget_X
            #endif
        #endfor
        return LResult
    #endfunction
    #--------------------------------------------------
    # __GetListWidgetStat
    #--------------------------------------------------
    def __GetListWidgetStat (self, AStatWidget: YOUTUBE_widgetYT.TStatWidget) -> YOUTUBEwidget:
        """__GetListWidget"""
    #beginfunction
        s  = '__GetListWidget...'
        # LULog.LoggerAPPS.debug (s)
        LResult = None
        for LItem in self.__FListWidgets:
            Lwidget_X: YOUTUBEwidget = LItem
            if Lwidget_X.FStatWidget.value == AStatWidget.value:
                return Lwidget_X
            #endif
        #endfor
        return LResult
    #endfunction
    #--------------------------------------------------
    # __GetListWidgetCount
    #--------------------------------------------------
    def __GetListWidgetCount (self, AStatWidget: YOUTUBE_widgetYT.TStatWidget) -> int:
        """__GetListWidgetCount"""
    #beginfunction
        s = '__GetListWidgetCount...'
        # LULog.LoggerAPPS.debug (s)
        LResult = 0
        for LItem in self.__FListWidgets:
            Lwidget_X: YOUTUBEwidget = LItem
            if Lwidget_X.FStatWidget.value == AStatWidget.value:
                LResult = LResult + 1
            #endif
        #endfor
        return LResult
    #endfunction
    def __AddListWidget (self, AYouTubeObject: LUObjectsYT.TYouTubeObject) -> YOUTUBE_widgetYT.YOUTUBEwidget:
    #beginfunction
        s = '__AddWidget...'
        # LULog.LoggerAPPS.debug (s)
        LMaxRes = LUObjectsYT.cMaxRes480p
        Lwidget_X = YOUTUBEwidget(AYouTubeObject, LMaxRes, self.ui.scrollAreaWidgetContents)
        Lwidget_X.FStatWidget = YOUTUBE_widgetYT.TStatWidget.swNew
        # сигналы
        Lwidget_X.SDownloadURL.connect (self.signalHandler_DownloadURL)
        self.ui.verticalLayout_3.insertWidget (0, Lwidget_X)
        # self.ui.verticalLayout_3.addWidget(Lwidget_X, stretch = 0)

        # self.__FListWidgets.append(Lwidget_X)
        self.__FListWidgets.insert(0, Lwidget_X)
        return Lwidget_X
    #endfunction

    def __ClearListYouTubeObject (self):
    #beginfunction
        s = '__ClearListYouTubeObject...'
        # LULog.LoggerAPPS.debug (s)
        self.__FListYouTubeObject.clear()
    #endfunction
    #--------------------------------------------------
    # __DelListYouTubeObject
    #--------------------------------------------------
    def __DelListYouTubeObject (self, AURL: str):
        """__DelListYouTubeObject"""
    #beginfunction
        s = '__DelListYouTubeObject...'
        # LULog.LoggerAPPS.debug (s)
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
        # LULog.LoggerAPPS.debug (s)
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
        # LULog.LoggerAPPS.debug (s)
        # LYouTubeObject
        LObjectID: datetime = LUDateTime.Now ()
        s = LUDateTime.GenerateObjectIDStr (LObjectID)
        # LULog.LoggerTOOLS.log (LULog.PROCESS, s)
        LYouTubeObject = LUObjectsYT.TYouTubeObject ()
        LYouTubeObject.ID = LObjectID
        LMaxRes = LUObjectsYT.cMaxRes480p
        LYouTubeObject.SetURL (AURL, LMaxRes, value ['PlayListName'], value ['NN'], value ['N'])
        self.__FListYouTubeObject.append(LYouTubeObject)
        return LYouTubeObject
    #endfunction

    def __ClearModel (self):
    #beginfunction
        s = '__ClearModel...'
        # LULog.LoggerAPPS.debug (s)
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
        # LULog.LoggerAPPS.debug (s)
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
        # LULog.LoggerAPPS.debug (s)
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
        # LULog.LoggerAPPS.debug (s)
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
    # Testfunction ():
    #------------------------------------------
    def Testfunction (self):
        """Testfunction"""
    #beginfunction
        s = 'Testfunction...'
        LULog.LoggerAPPS.info (s)
    #endfunction

    def __Procedure_01(self):
        """__Procedure_01"""
    #beginfunction
        s = '__Procedure_01...'
        LULog.LoggerAPPS.info (s)
    #endfunction

    def __Main(self):
        """__Main"""
    #beginfunction
        s = '__Main...'
        LULog.LoggerAPPS.info (s)
        LSaveCurrentDir = LUos.GetCurrentDir()
        LULog.LoggerAPPS.log (LULog.BEGIN, LUProc.cProcessBegin)
        self.P_StatMain.setText(LUProc.cProcessWork)

        self.__FSheduler.Enable = False

        if self.Params.Stop:
            self.__Procedure_01()
        #endif

        self.__FSheduler.Enable = True
        self.P_StatMain.setText(LUProc.cProcessStop)
        LULog.LoggerAPPS.log( LULog.END, LUProc.cProcessEnd)
        os.chdir(LSaveCurrentDir)
    #endfunction

    @LUDecotators.TIMING
    def __CreateObjectsURL (self, AURL: str):
        """__CreateObjectsURL"""
    #beginfunction
        s = '__CreateObjectsURL...'
        LULog.LoggerAPPS.info (s)
        if self.Flast_copied != AURL:
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
        else:
            s = AURL + ' дубликат cliboard ...'
            LULog.LoggerTOOLS.log (LULog.PROCESS, s)
        #endif

        # self.Flast_copied = ''

    #endfunction

    @QtCore.Slot (name = '__Action_CreateYoutube')
    def __Action_CreateYoutube (self):
        """__Action_CreateYoutube"""
    #beginfunction
        s = '__Action_CreateYoutube...'
        LULog.LoggerAPPS.info (s)
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
        LULog.LoggerAPPS.info (s)
        self.__SetStatApplication (LUProc.TStatApplication.saBreak)
        self.__FormClose()

        QCoreApplication.instance().exit()



        GAPP.exit()
        GAPP.quit()



    #endfunction
    @QtCore.Slot (name = '__Action_Cut')
    def __Action_Cut (self):
        """__Action_Cut"""
    #beginfunction
        s = '__Action_Cut...'
        LULog.LoggerAPPS.info (s)
    #endfunction
    @QtCore.Slot (name = '__Action_Copy')
    def __Action_Copy (self):
        """__Action_Copy"""
    #beginfunction
        s = '__Action_Copy...'
        LULog.LoggerAPPS.info (s)
    #endfunction
    @QtCore.Slot (name = '__Action_Paste')
    def __Action_Paste (self):
        """__Action_Paste"""
    #beginfunction
        s = '__Action_Paste...'
        LULog.LoggerAPPS.info (s)
    #endfunction
    def __Action_Sheduler (self, A):
        """__Action_Sheduler"""
    #beginfunction
        s = '__Action_Sheduler...'
        LULog.LoggerAPPS.info (s)
        # self.__SetStatApplication (LUProc.TStatApplication.saRunning)
        self.__Main ()
    #endfunction
    @QtCore.Slot (name = '__Action_Start_Stop')
    def __Action_Start_Stop (self):
        """__Action_Start"""
    #beginfunction
        s = '__Action_Start_Stop...'
        LULog.LoggerAPPS.info (s)
        if self.__FStatApplication == LUProc.TStatApplication.saBreak:
            self.__SetStatApplication (LUProc.TStatApplication.saRunning)
            self.__Main ()
        else:
            self.__SetStatApplication (LUProc.TStatApplication.saBreak)
    #endfunction
    @QtCore.Slot (name = '__Action_Setup')
    def __Action_Setup (self):
        """__Action_Setup"""
    #beginfunction
        s = '__Action_Setup...'
        LULog.LoggerAPPS.info (s)
        LSaveStatApplication = self.__FStatApplication
        LSaveCurrentDir = LUos.GetCurrentDir()

        self.__SetStatApplication (LUProc.TStatApplication.saBreak)
        self.StatApplication_event.emit(LUProc.cProcessSetup)
        # if ExecSetup = mrOk then
        #    FSheduler.DeleteEvent (ShedulerName)
        #    FSheduler.AddEvent (ShedulerName, TEMPLATE_RegIni.ShedulerTEMPLATE)
        # end

        os.chdir(LSaveCurrentDir)
        self.__SetStatApplication (LSaveStatApplication)
    #endfunction
    @QtCore.Slot (name = '__Action_About')
    def __Action_About (self):
        """__Action_About"""
    #beginfunction
        s = '__Action_About...'
        LULog.LoggerAPPS.info (s)
        LSaveStatApplication = self.__FStatApplication

        self.__SetStatApplication (LUProc.TStatApplication.saBreak)
        self.StatApplication_event.emit(LUProc.cProcessAbout)
        # ExecAbout

        self.__SetStatApplication (LSaveStatApplication)
    #endfunction
    @QtCore.Slot (name = '__Action_Help')
    def __Action_Help (self):
        """__Action_Help"""
    #beginfunction
        s = '__Action_Help...'
        LULog.LoggerAPPS.info (s)
        LSaveStatApplication = self.__FStatApplication

        self.__SetStatApplication (LUProc.TStatApplication.saBreak)
        self.StatApplication_event.emit(LUProc.cProcessHelp)
        # Application.HelpContext (6)

        self.__SetStatApplication (LSaveStatApplication)
    #endfunction

    @QtCore.Slot (name = '__Action_DeleteAll')
    def __Action_DeleteAll (self):
        """__Action_DeleteAll"""
    #beginfunction
        s = '__Action_DeleteAll...'
        LULog.LoggerAPPS.info (s)
        LSaveStatApplication = self.__FStatApplication

        self.__SetStatApplication (LUProc.TStatApplication.saBreak)

        self.StatApplication_event.emit(LUProc.cProcessDeleteAll)
        # Удалить не запущенные потоки
        # Остановить запущенные потоки
        # Удалить остановленные потоки
        for LItem in self.__FListYouTubeObject:
            LYouTubeObject:LUObjectsYT.TYouTubeObject = LItem
            LURL = LYouTubeObject.URL
            self.__DelModel (LURL)
            self.__DelListWidget (LURL)
        #endfor
        self.__ClearListYouTubeObject()

        self.__SetStatApplication (LSaveStatApplication)
    #endfunction

    def __runProcess(self):
        """__runProcess"""
    #beginfunction
        NswNew = self.__GetListWidgetCount (YOUTUBE_widgetYT.TStatWidget.swNew)
        NswGetInfo = self.__GetListWidgetCount (YOUTUBE_widgetYT.TStatWidget.swGetInfo)
        if NswNew > 0 and NswGetInfo < self.__FMaxThread:
            LWidget_X = self.__GetListWidgetStat (YOUTUBE_widgetYT.TStatWidget.swNew)
            if not LWidget_X is None:
                if not LWidget_X.FGetInfoStream_YOUTUBE.FStartThread:
                    s = YOUTUBE_widgetYT.CStatWidget [LWidget_X.FStatWidget]
                    s = 'Получение информации о потоке ...'
                    LWidget_X.S1_YT_StatWidget.emit (s)
                    LWidget_X.run_GetInfoStream ()
                #endif
            #endif
        #endif

        NswGetInfo = self.__GetListWidgetCount (YOUTUBE_widgetYT.TStatWidget.swGetInfo)
        NswDownload = self.__GetListWidgetCount (YOUTUBE_widgetYT.TStatWidget.swDownload)
        if NswGetInfo > 0 and NswDownload < self.__FMaxThread:
            LWidget_X = self.__GetListWidgetStat (YOUTUBE_widgetYT.TStatWidget.swGetInfo)
            if not LWidget_X is None:
                LWidget_X.FStatWidget = YOUTUBE_widgetYT.TStatWidget.swDownload

                if not LWidget_X.FDownloader_YOUTUBE.FStartThread:

                    s = YOUTUBE_widgetYT.CStatWidget [LWidget_X.FStatWidget]
                    s = 'Загрузка потока ...'
                    LWidget_X.S1_YT_StatWidget.emit (s)
                    LWidget_X.run_Downloader ()
                #endif
            #endif
        else:
            LWidget_X = self.__GetListWidgetStat (YOUTUBE_widgetYT.TStatWidget.swGetInfo)
            if not LWidget_X is None:
                LWidget_X.FStatWidget = YOUTUBE_widgetYT.TStatWidget.swQueue
                s = YOUTUBE_widgetYT.CStatWidget [LWidget_X.FStatWidget]
                s = 'Поток в очереди ...'
                LWidget_X.S1_YT_StatWidget.emit (s)
            #endif
        #endif

        NswQueue = self.__GetListWidgetCount (YOUTUBE_widgetYT.TStatWidget.swQueue)
        NswDownload = self.__GetListWidgetCount (YOUTUBE_widgetYT.TStatWidget.swDownload)
        if NswQueue > 0 and NswDownload < self.__FMaxThread:
            LWidget_X = self.__GetListWidgetStat (YOUTUBE_widgetYT.TStatWidget.swQueue)
            if not LWidget_X is None:
                LWidget_X.FStatWidget = YOUTUBE_widgetYT.TStatWidget.swDownload

                if not LWidget_X.FDownloader_YOUTUBE.FStartThread:

                    s = YOUTUBE_widgetYT.CStatWidget [LWidget_X.FStatWidget]
                    LWidget_X.S1_YT_StatWidget.emit (s)
                    s = 'Загрузка потока ...'
                    LWidget_X.run_Downloader ()
                #endif
            #endif
        #endif
    #endfunction

    #--------------------------------------------------
    # __run_idle
    #--------------------------------------------------
    @QtCore.Slot (str, name = '__run_idle')
    def __run_idle(self):
        """__run_idle"""
    #beginfunction
        self.idle = True
        # self.StatApplication_event.emit(LUProc.CStatApplication[self.__FStatApplication])
        while self.idle:
            if self.__FStatApplication == LUProc.TStatApplication.saRunning:
                self.__runProcess()
                ...
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
    # __process_single
    #--------------------------------------------------
    @QtCore.Slot (str, name = '__process_single')
    def __process_single(self):
        """__process_single"""
    #beginfunction
        self.StatApplication_event.emit('Processing item...')
        self.__run_idle()
    #endfunction
#endclass

#------------------------------------------
#
#------------------------------------------
def main ():
#beginfunction
    try:
        GFormMainWindow = FormMainWindow()
        GFormMainWindow.show()
        LResult = GAPP.exec ()
        GAPP.quit()
        sys.exit(LResult)

        #   clean up and exit code
        # for model in main_view.models:
        #     model.submitAll ()  # commit all pending changes to all models
        # app.quit ()
        # sys.exit (0)

        s = 'Exit...'
        LULog.LoggerAPPS.info (s)

    except SystemExit:
        print ("Closing Window...")
    except Exception as e:
        print (str (e))
#endfunction

#------------------------------------------
#
#------------------------------------------
#beginmodule
if __name__ == "__main__":
    main()
#endif

#endmodule
