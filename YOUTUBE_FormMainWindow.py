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
import LUYouTube
from LUObjectsYT import *
# import LUThreadQ

#------------------------------------------
# БИБЛИОТЕКИ PROJECT
#------------------------------------------
import YOUTUBE_Proc
import YOUTUBE_Params
import YOUTUBE_Consts

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

    def __init__(self, parent=None):
    #beginfunction
        super().__init__(parent)
        self.ui = Ui_FormMainWindow()
        self.ui.setupUi(self)

        self.__FSaveCurrentDir: str = ''
        self.__FSaveStatApplication: int = 0    # TStatApplication
        self.__FSheduler = None                 # TSheduler
        self.__FLogDir: str = ''
        self.__FStopYouTube: bool = True

        self.__FFlagIdle: bool = True

        # self.ui.action_Youtube.triggered.connect (Testfunction)
        # self.ui.action_Youtube.triggered.connect (LFormMainWindow.Test)
        # self.ui.action_Youtube.triggered.connect (FFormMainWindow.TestMain)
        # self.ui.action_Youtube.triggered.connect (FFormMainWindow.CreateYUOTUBEObject(LUObjectsYoutube.link3))

        # Состояние программы
        self.__FStatApplication: LUProc.TStatApplication = LUProc.TStatApplication.caTest

        # __FParams
        self.__FParams: YOUTUBE_Params.TParams = YOUTUBE_Params.TParams ()
        # self.APPLog = self.__FParams.FileMemoLog


        # self.__FYOUTUBE: YOUTUBE_Proc.TYOUTUBE = YOUTUBE_Proc.TYOUTUBE()
        #FFormMainWindow.ui.action_Youtube.triggered.connect (FFormMainWindow.CreateYUOTUBEObject(LUObjectsYoutube.link3))
        #self.ui.action_CreateYoutube.triggered(self.__CreateYUOTUBEObject(LUObjectsYoutube.link3))

        self.__FormCreate ()
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

    def __ClearWidget (self, AWidget: list):
    #beginfunction
        self.ui.TextEditR.hide ()
        LULog.LoggerAPPS.info ('__ClearWidget...')
        for i in reversed (range (self.ui.verticalLayout_3.count ())):
            item = self.ui.verticalLayout_3.itemAt (i).widget ()
            if type(item) is YOUTUBEwidget:
                item.setParent (None)
            #endif
        #endfor
        AWidget.clear()
    #endfunction
    def __AddWidget (self, AWidget: list, AYouTubeObject: TYouTubeObject):
    #beginfunction
        LULog.LoggerAPPS.info ('__AddWidget...')
        self.widget_X = YOUTUBEwidget(self.ui.scrollAreaWidgetContents)
        self.widget_X.setObjectName(u"widget_X")
        self.widget_X.setMinimumSize(QSize(400, 40))
        self.widget_X.setMaximumSize(QSize(400, 40))
        # self.widget_X.setSizePolicy(QSizePolicy.Maximum, QSizePolicy.Maximum)

        self.widget_X.ui.YT_Caption.setText (AYouTubeObject.URLInfo['title'])
        s = AYouTubeObject.URLInfo ['thumbnail_url']
        s = AYouTubeObject.URLInfo ['author']

        self.widget_X.ui.YT_ProgressBar.setMinimum (0)
        self.widget_X.ui.YT_ProgressBar.setMaximum (100)
        self.widget_X.ui.YT_ProgressBar.setRange(0, 100)
        self.widget_X.ui.YT_ProgressBar.setValue(0)

        self.ui.verticalLayout_3.insertWidget(0,self.widget_X)

        # self.ui.verticalLayout_3.addWidget(self.widget_X, 0)

        self.__FWidget.mo

        self.__FWidget.append(self.widget_X)
    #endfunction

    def __ClearModel (self, Amodel: QStringListModel):
    #beginfunction
        LULog.LoggerAPPS.info ('__ClearModel...')
        # Вы можете либо использовать model.setStringList( QStringList{} )
        # либо вручную удалить строки с помощью model.removeRows( 0, model.rowCount() ).
        Amodel.removeRows (0, Amodel.rowCount())
        # Amodel.setStringList (())

        # for i in reversed(range(Amodelmodel.rowCount ())):
        #     # Amodelmodel.removeRow (i)
        #     Amodelmodel.removeRows (self.ui.ListViewL.currentIndex().row(), 1)
        # #enfor
    #endfunction
    def __AddModel (self, Amodel: QStringListModel, s: str):
    #beginfunction
        LULog.LoggerAPPS.info ('__AddModel...')
        Lindex = Amodel.rowCount ()
        Amodel.insertRow (Lindex)
        Amodel.setData (Amodel.index (Lindex), s)
    #endfunction

    #--------------------------------------------------
    # __SetListViewL
    #--------------------------------------------------
    def __SetListViewL (self):
        """__SetListViewL"""
    #beginfunction
        LULog.LoggerAPPS.info ('__SetListViewL...')
        self.__Fmodel = QStringListModel ()
        # self.__Fmodel = QStringListModel ([
        #     "An element", "Another element", "Yay! Another one.", '????????????'
        # ])
        self.ui.ListViewL.setModel (self.__Fmodel)
        # self.__Fmodel.setStringList(['!!!!!!!!!!!!!!'])

        # self.ui.ListViewL.setViewMode (QListView.IconMode)
        # self.ui.ListViewL.setMovement (QListView.Static)
        # self.ui.ListViewL.setIconSize (QSize (64, 64))

        ...
    #endfunction

    #--------------------------------------------------
    # __SetScrollAreaR
    #--------------------------------------------------
    def __SetScrollAreaR (self):
        """__SetScrollAreaR"""
    #beginfunction
        LULog.LoggerAPPS.info ('__SetScrollAreaR...')
        self.__FWidget = list()
        self.ui.TextEditR.setText ('self.ui.TextEditR.setText')

        # self.ui.textEdit1 = QTextEdit(self.ui.scrollAreaWidgetContents)
        # self.ui.textEdit1.setObjectName(u"textEdit1")
        # self.ui.textEdit1.hide()
        # self.ui.textEdit1.setEnabled(False)
        # self.ui.textEdit1.setText('self.ui.textEdit1')
        # self.ui.verticalLayout_3.addWidget (self.ui.textEdit1)
        # self.ui.verticalLayout_3.addStretch()
        ...
    #endfunction

    # # Instantiate and start a new thread
    # def start_thread (self):
    #     instanced_thread = LUThreadQ.TQThread (self)
    #     instanced_thread.start ()
    #
    # # Create the Slots that will receive signals
    # @Slot (str)
    # def update_str_field (self, message):
    #     print (message)
    #
    # @Slot (int)
    # def update_int_field (self, value):
    #     print (value)

    def __job (self):
    #beginfunction
        LULog.LoggerAPPS.info ('__job...')
        self.__ClearModel(self.__Fmodel)
        self.__ClearWidget(self.__FWidget)

        last_copied = self.__FClipboard.text ()
        if "www.youtube.com" in last_copied or "youtu.be" in last_copied:
            LULog.LoggerAPPS.info (last_copied)
            self.__FClipboardList.append (last_copied)
            # YOUTUBE
            LYOUTUBE = LUYouTube.TYouTube ()
            Llist = LYOUTUBE.CreateURLs (last_copied)
            for item in Llist:
                LYouTubeObject: TYouTubeObject = item
                s = LYouTubeObject.URL
                LULog.LoggerAPPS.info (s)

                # Добавить self.__Fmodel
                self.__AddModel (self.__Fmodel, s)

                # Добавить self.__FWiget
                self.__AddWidget (self.__FWidget, LYouTubeObject)

                # for i in range(101):
                #     self.widget_X.ui.YT_ProgressBar.setValue (i)
                # #endfor

                # self.start_thread()

                try:
                    LYouTubeObject.StartYouTubeQThread ('d:\\work',
                                                       cMaxRes480p, type = 'video', file_extension = 'mp4')
                    #,skip_existing = True
                except BaseException as ERROR:
                    s = 'Ошибка загрузки!'
                    LULog.LoggerAPPS.exception (s, exc_info = True, stack_info = True)
                #endtry

            #endfor
        #endif
    #endfunction

    def cliboard_changed(self, mode):
    #beginfunction
        # LULog.LoggerAPPS.info ('cliboard_changed...')
        ...
    #endfunction

    def cliboard_findBufferChanged (self):
    #beginfunction
        # LULog.LoggerAPPS.info ('cliboard_findBufferChanged...')
        ...
    #endfunction

    def cliboard_selectionChanged (self):
    #beginfunction
        # LULog.LoggerAPPS.info ('cliboard_selectionChanged...')
        ...
    #endfunction

    def cliboard_dataChanged(self):
    #beginfunction
        LULog.LoggerAPPS.info ('cliboard_dataChanged...')
        mimeData = self.__FClipboard.mimeData()
        if mimeData.hasImage():
            LULog.LoggerAPPS.info (' '*4+'mimeData.hasImage...')
            # setPixmap(QPixmap(mimeData.imageData()))
            ...
        elif mimeData.hasHtml():
            LULog.LoggerAPPS.info (' '*4+'mimeData.hasHtml...')
            # setText(mimeData.html())
            # setTextFormat(Qt.RichText)
            ...
        elif mimeData.hasText():
            LULog.LoggerAPPS.info (' '*4+'mimeData.hasText...')
            # setText(mimeData.text())
            # setTextFormat(Qt.PlainText)
            Ltext = self.__FClipboard.text ()
            # self.ui.Memo_Log.insertPlainText (Ltext + '\n')
            LULog.LoggerAPPS.info (Ltext)
            self.__job()
            ...
        else:
            LULog.LoggerAPPS.info (' '*4+'Cannot display data...')
            # setText(tr("Cannot display data"))
            ...
        #endif
    #endfunction

    #------------------------------------------
    # Testfunction ():
    #------------------------------------------
    @staticmethod
    def Testfunction ():
    #beginfunction
        LULog.LoggerAPPS.info ('Testfunction...')
    #endfunction

    #--------------------------------------------------
    # Clipboard
    #--------------------------------------------------
    def __SetClipboard (self):
        """__SetClipboard"""
    #beginfunction
        LULog.LoggerAPPS.info ('__SetClipboard...')
        self.__FClipboard = QApplication.clipboard ()
        # Signals
        self.__FClipboard.dataChanged.connect (self.cliboard_changed (QClipboard.Mode))
        self.__FClipboard.dataChanged.connect (self.cliboard_dataChanged)
        self.__FClipboard.dataChanged.connect (self.cliboard_findBufferChanged)
        self.__FClipboard.dataChanged.connect (self.cliboard_selectionChanged)
        # clipboard = QGuiApplication.clipboard ()
        # originalText = self.clipboard.text ()
        self.__FClipboardList = []

    #endfunction

    def __SetStylesheetsFor_ALL (self):
        """__SetStylesheetsFor_ALL"""
    #beginfunction
        # LULog.LoggerAPPS.info ('__SetStylesheetsFor_ALL...')

        # Create Stylesheets
        self.style_light = """
            * {font-family: 'Noto Sans';}  /* REMOVING THIS LINE AVOIDS THE ISSUE, BUT THEN FONTS ARE WRONG INITIALLY */
            QMainWindow {background-color: white;}
            """
        # print (self.style_light)
        self.style_dark = """
            * {font-family: 'Noto Sans';} 
            QMainWindow {background-color: gray;}
            """
        # print (self.style_dark)

        # Create Stylesheets
        self.style_light = """
            * QPlainTextEdit {color: rgba(0, 0, 0, .5); background-color: rgb(157, 157, 157); font-weight: bold; font-size: 10px; font: 20pt "Courier New"}
            QPlainTextEdit {color: blue; background-color: rgb(157, 157, 157); font-weight: bold; font-size: 10px; font: 10pt "Courier New"}
            """
        self.setStyleSheet (self.style_light)
    #endfunction

    def __SetColorFor_Memo_Log (self):
        """__SetupColorFor_Memo_Log"""
    #beginfunction
        # LULog.LoggerAPPS.info ('__SetColorFor_Memo_Log...')

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

    def __SetStylesheetsFor_Memo_Log (self):
        """__SetupStylesheetsFor_Memo_Log"""
    #beginfunction
        # LULog.LoggerAPPS.info ('__SetStylesheetsFor_Memo_Log...')

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

    def __SetColorGroup (self):
        """__SetColorGroup"""
    #beginfunction
        # LULog.LoggerAPPS.info ('__SetColorGroup...')

        palette = self.ui.Memo_Log.palette ()
        palette.setCurrentColorGroup (QPalette.Normal)
        palette.setColorGroup (QPalette.Disabled,
                               palette.windowText (), palette.button (),
                               palette.light (), palette.dark (), palette.mid (),
                               palette.text (), palette.brightText (),
                               palette.base (), palette.window (),
                               )
        self.ui.Memo_Log.setPalette (palette)
    #endfunction

    #-------------------------------
    # StatusBar_P1_P2
    #-------------------------------
    def __SetStatusBar_P1_P2 (self):
        """__SetStatusBar_P1_P2"""
    #beginfunction
        LULog.LoggerAPPS.info ('__SetStatusBar_P1_P2...')
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
    # __SetSheduler
    #-------------------------------
    def __SetSheduler (self):
        """__SetSheduler"""
    #beginfunction
        LULog.LoggerAPPS.info ('__SetSheduler...')
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
    # __SetLogs
    #--------------------------------------------------
    def __SetLogs (self):
        """__FormCreate"""
    #beginfunction
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

        LULog.LoggerAPPS.info ('__SetLogs...')
    #endfunction

    def __FormCreate (self):
        """__FormCreate"""
    #beginfunction
        self.setWindowTitle(YOUTUBE_Consts.cProjectNAME)
        self.__SetLogs ()
        self.__SetStatusBar_P1_P2()
        self.__SetSheduler()
        self.__SetStatApplication (LUProc.TStatApplication.caBreak)
        self.__SetClipboard()

        self.__SetListViewL()

        self.__SetScrollAreaR()
        #----------------- VersionInfo --------------------------
        # VersionInfo = CreateVersion (ParamStr(0))
        # LULog.LoggerAPPS.log (LULog.TEXT, ParamStr (0) + ' ' + VersionInfo.FileVersion+ ' ' + VersionInfo.FileDate)
        # VersionInfo.Free
        #-----------------------------------------------------------
        self.__FormActivate()
        ...
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
        self.__FormClose (LUProc.TStatApplication.caFree)
        ...
    #endfunction

    # TFormMain.FormActivate
    def __FormActivate (self):
        """__FormActivate"""
    #beginfunction
        LULog.LoggerAPPS.info ('__FormActivate...')
        LULog.LoggerAPPS.log (LULog.TEXT, self.__FParams.FileMemoLog.FileName)
        LULog.LoggerAPPS.log (LULog.TEXT, self.__FParams.FileNameINI)
    #endfunction

    def __FormClose (self, Action):
        """__FormClose"""
    #beginfunction
        # Action = caFree
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

    # TFormMain.ActionStartExecute

    def __Action_StartExecute (self, Sender):
    #beginfunction
        LSaveCurrentDir = LUos.GetCurrentDir()
        self.__SetStatApplication (LUProc.TStatApplication.caMain)
        self.__Main()
        self.__SetStatApplication (LUProc.TStatApplication.caSheduler)
        os.chdir(LSaveCurrentDir)
    #endfunction

    # TFormMain.ActionExitExecute
    def __Action_ExitExecute (self, Sender):
    #beginfunction
        """
        Close
        """
        ...
    #endfunction

    # TFormMain.ActionSetupExecute
    def __Action_SetupExecute (self, Sender):
    #beginfunction
        LSaveCurrentDir = LUos.GetCurrentDir()
        LSaveStatApplication = self.__FStatApplication
        self.__SetStatApplication (LUProc.TStatApplication.caSetup)
        # if ExecSetup = mrOk then
        #    FSheduler.DeleteEvent (ShedulerName)
        #    FSheduler.AddEvent (ShedulerName, TEMPLATE_RegIni.ShedulerTEMPLATE)
        # end
        self.__SetStatApplication (LSaveStatApplication)
        os.chdir(LSaveCurrentDir)
    #endfunction

    # TFormMain.ActionStopExecute
    def __Action_StopExecute (self, Sender):
    #beginfunction
        self.__SetStatApplication (LUProc.TStatApplication.caBreak)
    #endfunction

    # TFormMain.ActionAboutExecute
    def __Action_AboutExecute (self, Sender):
    #beginfunction
        LSaveStatApplication = self.__FStatApplication
        self.__SetStatApplication (LUProc.TStatApplication.caAbout)
        # ExecAbout
        self.__SetStatApplication (LSaveStatApplication)
    #endfunction

    # TFormMain.DeleteYUOTUBEObject
    def __DeleteYUOTUBEObject (self, AObjectIDStr: str):
        """
        #var
        i: Integer
        """
    #beginfunction
        """
        # ListBox_Objects.Items.Delete тестирование
        i = ListBox_Objects.Items.IndexOf (AObjectIDStr)
        if i >= 0 then
            ListBox_Objects.Items.Delete (i)
    
        # FYouTubeObjectsCollection.DeleteObjectItem
        FYouTubeObjectsCollection.DeleteObjectsItem (AObjectIDStr)
        """
        ...
    #endfunction

    # TFormMain.DeleteYouTubeThread
    def __DeleteYouTubeThread (self, Sender):
    #beginfunction
        """
        LYoutubeThread: TYoutubeThread = TYoutubeThread (Sender)
        LYoutubeThreadNew: TYoutubeThreadNew = TYoutubeThreadNew (Sender)
        if not LYoutubeThreadNew.FStopYouTubeBooleanThread then
        begin
            LObjectIDStr: str = LYoutubeThreadNew.FObjectIDStr
            DeleteYUOTUBEObject (LObjectIDStr)
            DeleteLUPanel (LObjectIDStr)
        end
        """
        ...
    #endfunction

    # TFormMain.ButtonDeleteYouTubeClick

    def __ButtonDeleteYouTubeClick (self, Sender):
    #beginfunction
        """
        LYouTubeObject: TYouTubeObject = TYouTubeObject (TLUPanel(TButton(Sender).Parent).Objects)
        LObjectIDStr: str = GenerateObjectIDStr (LYouTubeObject.ID)
        DeleteYUOTUBEObject (LObjectIDStr)
        # TPanel
        TLUPanel (TButton(Sender).Parent).Free
        """
        ...
    #endfunction

    # TFormMain.ButtonStartYouTubeClick
    def __ButtonStartYouTubeClick (self, Sender):
    #beginfunction
        """
        LThread: bool = True
        LObjectIDStr: str = TLUPanel (TButton(Sender).Parent).Caption
        LYouTubeObject: TYouTubeObject = FYouTubeObjectsCollection.YouTubeObjectsItem[LObjectIDStr].YouTubeObject
        if LThread then
        begin
            LYouTubeObject.StartYouTubeThread (DeleteYouTubeThread)
        end else begin
            LYouTubeObject.StartYouTube
            if not LYouTubeObject.StopYouTubeBoolean then
            begin
                ButtonDeleteYouTubeClick (Sender)
            end
        end
        """
        ...
    #endfunction

    # TFormMain.ButtonStopYouTubeClick
    def __ButtonStopYouTubeClick (self, Sender):
    #beginfunction
        """
        LThread: bool = True
        LObjectIDStr: str = TLUPanel (TButton(Sender).Parent).Caption
        LYouTubeObject: TYouTubeObject = FYouTubeObjectsCollection.YouTubeObjectsItem[LObjectIDStr].YouTubeObject
        if LThread then
        begin
            LYouTubeObject.StopYouTubeThread
        end else begin
            LYouTubeObject.StopYouTube
        end
        """
        ...
    #endfunction

    # TFormMain.CreateYUOTUBEPlaylist
    def __CreateYUOTUBEPlaylist (self, AURL: str):
    #beginfunction
        LULog.LoggerAPPS.info ('__CreateYUOTUBEPlaylist...')
        ...
    #endfunction

    # TFormMain.CreateYUOTUBEObject
    def __CreateYUOTUBEObject (self, AURL: str):
    #beginfunction
        LULog.LoggerAPPS.info ('__CreateYUOTUBEObject...')
        """
        # LLUPanel
        LLUPanel = TLUPanel.Create (Self)
        with LLUPanel do
        begin
            Objects = LYouTubeObject
            Caption = LObjectIDStr
            Parent = Panel_ProgressBarRx
            AutoSize = False
            Align = alTop
            Height = LHeight
        end
    
        # LButtonDeleteYouTube
        LButtonDeleteYouTube = TButton.Create (Self)
        with LButtonDeleteYouTube do
        begin
            Parent = LLUPanel
            Caption = 'Удалить'
            Align = alLeft
            OnClick = ButtonDeleteYouTubeClick
            Height = LHeight
        end
    
        # LButtonStartYouTube
        LButtonStartYouTube = TButton.Create (Self)
        with LButtonStartYouTube do
        begin
            Parent = LLUPanel
            Caption = 'Старт'
            Align = alLeft
            OnClick = ButtonStartYouTubeClick
            Height = LHeight
        end
    
        # LButtonStoptYouTube
        LButtonStopYouTube = TButton.Create (Self)
        with LButtonStopYouTube do
        begin
            Parent = LLUPanel
            Caption = 'Стоп'
            Align = alLeft
            OnClick = ButtonStopYouTubeClick
            Height = LHeight
        end
    
        # LRxProgress
        LRxProgress = TRxProgress.Create (Self)
        with LRxProgress do
        begin
            Parent = LLUPanel
            Align = alClient
            Text = LObjectIDStr
            Height = LHeight
            Min = 0
            Max = cProgressBarMax
            Position = 0
        end
   
        # LLUPanel
        LLUPanel.RxProgress = LRxProgress
        """
    #endfunction

    def __Action_CreateObjectExecute (self, Sender):
    #beginfunction
        """
        # CreateObject
        CreateYUOTUBEObject (LURL)
        """
        ...
    #endfunction

    # TFormMain.ActionHelpExecute
    def __Action_HelpExecute (self, Sender):
    #beginfunction
        # Application.HelpContext (6)
        ...
    #endfunction

    def __Action_PasteExecute (self, Sender):
    #beginfunction
        """
        LTS = TStringList.Create
        LTS.Add (Clipboard.AsText)
        if LTS.Count > 0 then
        begin
            s = LTS.Strings[0]
            APPLog.LogString[tlsInfo, 0] = s
        end
        LTS.Free
        """
        ...
    #endfunction

    # TFormMain.ActionViewLogsExecute
    def __ActionViewLogsExecute (self, Sender):
    #beginfunction
        """
        APPLog.LogString[tlsInfo, 0] = 'Action: ViewLogs ' + TMenuItem (Sender).Caption
        FSaveStatApplication = StatApplication
        SetStatApplication (saViewLog)
        ExecViewLog (TMenuItem(Sender).Caption, APPLog)
        SetStatApplication (FSaveStatApplication)
        """
        ...
    #endfunction

    # TFormMain.ActionViewLogFileExecute
    def __Action_ViewLogFileExecute (self, Sender):
    #beginfunction
        """
        APPLog.LogString[tlsInfo, 0] = 'Action: ViewLog'
        FSaveStatApplication = StatApplication
        SetStatApplication (saViewLog)
        ViewFile (APPLog, IncludeTrailingBackslash(FLogDir) + ProjectName + '*.log')
        SetStatApplication (FSaveStatApplication)
        """
        ...
    #endfunction

    # TFormMain.ProcedureDeleteYUOTUBEObjects
    def __ProcedureDeleteYUOTUBEObjects(self):
        """
        #var
        i: Integer
        j: Integer
        LObjectIDStr: string
        LYouTubeObjectsItem: TYouTubeObjectsItem
        LYouTubeObject: TYouTubeObject
        LLUPanel: TLUPanel
        LComponent: TComponent
        """
    #beginfunction
        """
        for i = 0 to FYouTubeObjectsCollection.Count - 1 do
        begin
            # FYouTubeObjectsCollection
            LYouTubeObjectsItem = FYouTubeObjectsCollection.Items[i]
            LObjectIDStr = GenerateObjectIDStr
                (LYouTubeObjectsItem.YouTubeObject.ID)
            APPLog.LogString[tlsInfo, 1] = LObjectIDStr
            DeleteYUOTUBEObject (LObjectIDStr)
    
            # TPanel
            for j = 0 to FormMain.ComponentCount - 1 do
            begin
                LComponent = FormMain.Components[j]
                if LComponent is TLUPanel then
                begin
                    LLUPanel = TLUPanel (FormMain.Components[j])
                    LYouTubeObject = TYouTubeObject (LLUPanel.Objects)
                    LObjectIDStr = GenerateObjectIDStr (LYouTubeObject.ID)
                    APPLog.LogString[tlsInfo, 1] = LObjectIDStr
                    LLUPanel.Free
                    Break
                end
            end
        end
        """
        ...
    #endfunction

    # TFormMain.ProcedureDeleteYUOTUBEObjects
    def __DeleteLUPanel (self, AObjectIDStr: str):
    #beginfunction
        """
        # TPanel
        for j = 0 to FormMain.ComponentCount - 1 do
        begin
            LComponent = FormMain.Components[j]
            if LComponent is TLUPanel then
            begin
                LLUPanel = TLUPanel (FormMain.Components[j])
                if LLUPanel.Caption = AObjectIDStr then
                begin
                    LLUPanel.Free
                    Break
                end
            end
        end
        """
        ...
    #endfunction

    # TFormMain.Procedure_01
    def __Procedure_01(self):
        """
        #var
        LTEMPLATE_Procedure: TTEMPLATE_Procedure
        LFileName: string
        """
    #beginfunction
        """
        LFileName = 'https://www.youtube.com/embed/DCNtylTXgmM'
        LTEMPLATE_Procedure = TTEMPLATE_Procedure.Create (nil)
        LTEMPLATE_Procedure.Free
        """
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

        if self.Params.Stop:
            self.__Procedure_01()
            self.__ProcedureDeleteYUOTUBEObjects()
        #endif
        # --------------------------------------------------
        LULog.LoggerAPPS.log( LULog.BEGIN, LUProc.cProcessEnd)
        os.chdir(LSaveCurrentDir)
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
