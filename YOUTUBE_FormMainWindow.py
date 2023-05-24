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


#------------------------------------------
#
#------------------------------------------
# Lui_file_name1 = "YOUTUBE_FormMain.ui"
# Lui_file_name2 = "D:/PROJECTS_LYR/CHECK_LIST/05_DESKTOP/02_Python/PROJECTS_PY/YUOTUBE/YOUTUBE/YOUTUBE_FormMain.ui"

# ------------------------------------
# FormMainWindow(QMainWindow)
# ------------------------------------
class FormMainWindow(QMainWindow):
    """FormMainWindow"""
    luClassName = 'FormMainWindow'

    #----------------------------------------------
    # СИГНАЛ
    #----------------------------------------------
    log_event = QtCore.Signal(str)

    #----------------------------------------------
    # Коннектор - сюда приходит СИГНАЛ log_event
    #----------------------------------------------
    def signalHandler_log_event(self, text):
        """signalHandler_log_event"""
    #beginfunction
        s = 'signalHandler_log_event...'
        # print(text)
        self.P1.setText (text)
    #endfunction

    #----------------------------------------------
    # Коннектор - сюда приходит СИГНАЛ
    #----------------------------------------------
    def signalHandler_DownloadURL(self, text):
        """signalHandler_DownloadURL"""
    #beginfunction
        s = 'signalHandler_DownloadURL...'
        # LULog.LoggerAPPS.debug (s)
        LURL = text
        # print(LURL)
        # LULog.LoggerAPPS.info (LURL)

        # s = self.__GetModel(LURL)
        # print(s)
        self.__DelModel (LURL)

        # Lwidget_X: YOUTUBEwidget = self.__GetListWidget(LURL)
        # s = Lwidget_X.FYouTubeObject.URL
        # print(s)
        self.__DelListWidget (LURL)

        self.__DelListYouTubeObject (LURL)
    #endfunction

    def __init__(self, parent=None):
    #beginfunction
        super().__init__(parent)
        self.ui = Ui_FormMainWindow()
        self.ui.setupUi(self)
        self.__FLogDir: str = ''
        self.__FStopYouTube: bool = True

        self.idle = True
        # Состояние программы
        self.__FStatApplication: LUProc.TStatApplication = LUProc.TStatApplication.caTest
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
        """destructor"""
    #beginfunction
        self.__FormDestroy()
        LClassName = self.__class__.__name__
        s = '{} уничтожен'.format(LClassName)
        #print (s)
    #endfunction

    def __SetColorGroup (self):
        """__SetColorGroup"""
    #beginfunction
        LULog.LoggerAPPS.debug ('__SetColorGroup...')
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
        LULog.LoggerAPPS.debug ('__SetStylesheetsFor_ALL...')
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
        LULog.LoggerAPPS.debug ('__SetColorFor_Memo_Log...')
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
        LULog.LoggerAPPS.debug ('__SetStylesheetsFor_Memo_Log...')
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
        LULog.LoggerAPPS.info ('01.__SetLogs...')
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
    # 02.__SetStatusBar_P1_P2
    #-------------------------------
    def __SetStatusBar_P1_P2 (self):
        """__SetStatusBar_P1_P2"""
    #beginfunction
        LULog.LoggerAPPS.info ('02.__SetStatusBar_P1_P2...')
        # self.ui.StatusBar_P1_P2.stasetStyleSheet (
        #     "QStatusBar{padding-left:8px;background:rgba(255,0,0,255);color:black;font-weight:bold;}")

        # display a message in 5 seconds
        self.ui.StatusBar_P1_P2.showMessage ("Error Cannot determine filepath", 5000)

        # display a message in 5 seconds
        self.ui.StatusBar_P1_P2.showMessage('Ready', 5000)

        # for i = 0 to StatusBar_P1_P2.Panels.Count - 1 do
        #     StatusBar_P1_P2.Panels[i].Text = ''

        # add a permanent widget to the status bar
        self.P1 = QLabel('Length: 0')
        s = self.P1.text()
        self.P1.setText('!!!!!!!!!!!!!!!')
        self.ui.StatusBar_P1_P2.addPermanentWidget(self.P1)

        self.P2 = QLabel('Length: 0')
        s = self.P2.text()
        self.P2.setText('???????????')
        self.ui.StatusBar_P1_P2.addPermanentWidget(self.P2)

        # Splash = TSplash.Create (Self)
        # Splash.Name = 'Splash'
        # Splash.Height = StatusBar_P1_P2.Height
        # Splash.Width = StatusBar_P1_P2.Panels[0].Width
        # StatusBar_P1_P2.InsertControl (Splash)
    #endfunction

    #-------------------------------
    # 03.__SetSheduler
    #-------------------------------
    def __SetSheduler (self):
        """__SetSheduler"""
    #beginfunction
        LULog.LoggerAPPS.info ('03.__SetSheduler...')
        # FSheduler = TSheduler.Create (Self)
        # with FSheduler do
        # begin
        #     name = 'Sheduler'
        #     Enabled = False
        #     OnSheduler = Action_StartExecute
        #     AddEvent (ShedulerName, TEMPLATE_RegIni.ShedulerTEMPLATE)
        # end
    #endfunction

    #--------------------------------------------------
    # 04.__SetClipboard
    #--------------------------------------------------
    def __SetClipboard (self):
        """__SetClipboard"""
    #beginfunction
        LULog.LoggerAPPS.info ('04.__SetClipboard...')
        self.__FClipboard = QApplication.clipboard ()
        # Signals
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
        LULog.LoggerAPPS.info ('05.__SetListViewL...')

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
        LULog.LoggerAPPS.info ('06.__SetScrollAreaR...')
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
        LULog.LoggerAPPS.info ('07.__SetListYouTubeObject...')
        self.__FListYouTubeObject = list()
        self.__ClearListYouTubeObject()
    #endfunction
    #--------------------------------------------------
    # 08.__SetTimer
    #--------------------------------------------------
    def __SetTimer (self):
        """__SetTimer"""
    #beginfunction
        LULog.LoggerAPPS.info ('08.__SetTimer...')
        self.timer = QtCore.QTimer ()
        self.timer.setInterval (1)
        # self.timer.timeout.connect (self.recurring_timer)
        self.timer.timeout.connect (self.__run_idle)
        self.timer.start ()
        self.log_event.connect (self.signalHandler_log_event)
    #endfunction

    def __FormCreate (self):
        """__FormCreate"""
    #beginfunction
        LULog.LoggerAPPS.info ('__FormCreate...')
        self.setWindowTitle(YOUTUBE_Consts.cProjectNAME)
        # 01.__SetLogs
        self.__SetLogs ()
        # 02.__SetStatusBar_P1_P2
        self.__SetStatusBar_P1_P2()
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
        #----------------- VersionInfo --------------------------
        # VersionInfo = CreateVersion (ParamStr(0))
        # LULog.LoggerAPPS.log (LULog.TEXT, ParamStr (0) + ' ' + VersionInfo.FileVersion+ ' ' + VersionInfo.FileDate)
        # VersionInfo.Free
        #-----------------------------------------------------------
        self.__SetStatApplication (LUProc.TStatApplication.caBreak)
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

    def __FormDestroy (self):
        """__FormDestroy"""
    #beginfunction
        self.__FormClose ()
    #endfunction

    def __FormActivate (self):
        """__FormActivate"""
    #beginfunction
        LULog.LoggerAPPS.info ('__FormActivate...')
        LULog.LoggerAPPS.log (LULog.TEXT, self.__FParams.FileMemoLog.FileName)
        LULog.LoggerAPPS.log (LULog.TEXT, self.__FParams.FileNameINI)
    #endfunction

    def __FormClose (self):
        """__FormClose"""
    #beginfunction
        # RuntimeError: Internal C++ object (FormMainWindow) already deleted.
        # self.close()
        ...
    #endfunction

    # TFormMain.SetStatApplication
    def __SetStatApplication (self, AStatApplication):
    #beginfunction
        self.__FStatApplication = AStatApplication
        # Sheduler
        # FSheduler.Enabled = (self.__FStatApplication == LUProc.TStatApplication.saSheduler)
        # Start
        # Action_Start.Enabled = (self.FStatApplication == LUProc.TStatApplication.saBreak)
        # Action_Start.Checked = (self.FStatApplication == LUProc.TStatApplication.saMain)
        # Stop
        # Action_Stop.Enabled = (self.FStatApplication == LUProc.TStatApplication.saMain) or\
        #                         (self.FStatApplication == LUProc.TStatApplication.saSheduler)
        # Action_Stop.Checked = (self.FStatApplication == LUProc.TStatApplication.saBreak)
        # Setup
        # Action_Setup.Enabled = (self.FStatApplication == LUProc.TStatApplication.saBreak) or\
        #                         (self.FStatApplication == LUProc.TStatApplication.saSheduler)
        # ViewLogFile
        # Action_ViewLogFile.Enabled = (self.FStatApplication == LUProc.TStatApplication.saBreak) or\
        #                              (self.FStatApplication == LUProc.TStatApplication.saSheduler)
        # Exit
        # Action_Exit.Enabled = (self.FStatApplication == LUProc.TStatApplication.saBreak) or\
        #                       (self.FStatApplication == LUProc.TStatApplication.saSheduler)

        if (self.__FStatApplication == LUProc.TStatApplication.caMain):
            # StatusBar_P1_P2.Panels[0].Text = SProcessWork
            # Screen.Cursor = crAppStart
            ...
        else:
            # StatusBar_P1_P2.Panels[0].Text = SProcessStop
            # Screen.Cursor = crDefault
            ...
        #endif

        # TS = FSheduler.NameEvents
        # if (TS.Count > 0) and (self.FStatApplication = saSheduler):
        #     StatusBar_P1_P2.Panels[0].Text = 'Следующий сеанс: ' + DateTimeToStr (FSheduler.DTEvents)
        #endif

        # StatusBar_P1_P2.Panels[1].Text = ''
    #endfunction

    def cliboard_changed(self, mode):
    #beginfunction
        s = 'cliboard_changed...'
        # LULog.LoggerAPPS.info (s)
        ...
    #endfunction
    def cliboard_findBufferChanged (self):
    #beginfunction
        s = 'cliboard_findBufferChanged...'
        # LULog.LoggerAPPS.info (s)
        ...
    #endfunction
    def cliboard_selectionChanged (self):
    #beginfunction
        s = 'cliboard_selectionChanged...'
        # LULog.LoggerAPPS.info (s)
        ...
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
            self.__Action_CreateObjectExecute (LText)
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
        LResult = None
        s = '__GetListYouTubeObject...'
        # LULog.LoggerAPPS.debug (s)
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
    @staticmethod
    def Testfunction ():
        """Testfunction"""
    #beginfunction
        s = 'Testfunction...'
        LULog.LoggerAPPS.info (s)
    #endfunction

    def __Procedure_01(self):
    #beginfunction
        ...
    #endfunction

    # TFormMain.Main
    def __Main(self):
    #beginfunction
        LSaveCurrentDir = LUos.GetCurrentDir()
        LULog.LoggerAPPS.log( LULog.BEGIN, LUProc.cProcessBegin)
        # --------------------------------------------------
        # FSheduler.DeleteEvent (ShedulerName)
        # FSheduler.AddEvent (ShedulerName, TEMPLATE_RegIni.ShedulerTEMPLATE)
        # --------------------------------------------------
        if self.Params.Stop:
            self.__Procedure_01()
        #endif
        # --------------------------------------------------
        LULog.LoggerAPPS.log( LULog.BEGIN, LUProc.cProcessEnd)
        os.chdir(LSaveCurrentDir)
    #endfunction

    def __Action_StartExecute (self):
    #beginfunction
        LSaveStatApplication = self.__FStatApplication
        LSaveCurrentDir = LUos.GetCurrentDir()
        self.__SetStatApplication (LUProc.TStatApplication.caMain)
        self.__Main()
        os.chdir(LSaveCurrentDir)
        self.__SetStatApplication (LSaveStatApplication)
    #endfunction

    def __Action_ExitExecute (self):
    #beginfunction
        ...
    #endfunction

    def __Action_SetupExecute (self):
    #beginfunction
        LSaveStatApplication = self.__FStatApplication
        LSaveCurrentDir = LUos.GetCurrentDir()
        self.__SetStatApplication (LUProc.TStatApplication.caSetup)
        # if ExecSetup = mrOk then
        #    FSheduler.DeleteEvent (ShedulerName)
        #    FSheduler.AddEvent (ShedulerName, TEMPLATE_RegIni.ShedulerTEMPLATE)
        # end
        os.chdir(LSaveCurrentDir)
        self.__SetStatApplication (LSaveStatApplication)
    #endfunction

    def __Action_StopExecute (self, Sender):
    #beginfunction
        self.__SetStatApplication (LUProc.TStatApplication.caBreak)
    #endfunction

    def __Action_AboutExecute (self, Sender):
    #beginfunction
        LSaveStatApplication = self.__FStatApplication
        self.__SetStatApplication (LUProc.TStatApplication.caAbout)
        # ExecAbout
        self.__SetStatApplication (LSaveStatApplication)
    #endfunction

    def __Action_CreateObjectExecute (self, AText: str):
    #beginfunction
        LSaveStatApplication = self.__FStatApplication
        self.__SetStatApplication (LUProc.TStatApplication.caAddWidget)
        if self.Flast_copied != AText:
            self.Flast_copied = AText
            if "www.youtube.com" in self.Flast_copied or "youtu.be" in self.Flast_copied:
                # LULog.LoggerAPPS.info (self.Flast_copied)
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

                        # # s = self.__GetModel(LURL)
                        # self.__DelModel (LURL)
                        # # s = self.__GetListWidget(LURL)
                        # self.__DelListWidget (LURL)
                        # self.__DelListYouTubeObject (LURL)
                        ...
                    #endif
                    QCoreApplication.processEvents ()
                #endfor
            #endif
        else:
            s = AText + ' дубликат cliboard ...'
            LULog.LoggerTOOLS.log (LULog.PROCESS, s)
        #endif

        self.Flast_copied = ''

        self.__SetStatApplication (LSaveStatApplication)
    #endfunction

    def __Action_HelpExecute (self, Sender):
    #beginfunction
        LSaveStatApplication = self.__FStatApplication
        self.__SetStatApplication (LUProc.TStatApplication.caHelp)
        # Application.HelpContext (6)
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
        self.log_event.emit('running idle... ')
        while self.idle:
            if self.__FStatApplication != LUProc.TStatApplication.caAddWidget:
                self.__runProcess()
            #endif
            if len (self.__FListWidgets) > 0:
                self.ui.TextEditR.hide ()
            else:
                self.ui.TextEditR.show ()
            #endif

            # time.sleep(0.00001)
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
        self.log_event.emit('Processing item...')
        self.__run_idle()
    #endfunction

#endclass

#------------------------------------------
#
#------------------------------------------
def main ():
#beginfunction
    GAPP = QApplication(sys.argv)
    GFormMainWindow = FormMainWindow()
    GFormMainWindow.show()
    sys.exit(GAPP.exec())
#endfunction

#------------------------------------------
#
#------------------------------------------
#beginmodule
if __name__ == "__main__":
    main()
#endif

#endmodule
