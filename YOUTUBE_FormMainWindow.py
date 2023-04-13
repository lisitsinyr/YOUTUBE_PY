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

#------------------------------------------
# БИБЛИОТЕКИ сторонние
#------------------------------------------
from PySide6.QtWidgets import QApplication, QMainWindow
from PySide6.QtUiTools import QUiLoader
from PySide6.QtCore import QFile, QIODevice

#------------------------------------------
# БИБЛИОТЕКИ LU
#------------------------------------------
import LUFile
from LUObjects import *
from LUObjectsYouTube import *
from LULog import *
from LUFile import *
import LUProc
import LUos

#------------------------------------------
# БИБЛИОТЕКИ PROJECT
#------------------------------------------
# from YOUTUBE_Params import *
import YOUTUBE_Proc
import YOUTUBE_Params
import YOUTUBE_Consts

# import YOUTUBE_test
from ui_YOUTUBE_FormMain import Ui_FormMainWindow

#------------------------------------------
#
#------------------------------------------
Lui_file_name1 = "YOUTUBE_FormMain.ui"
Lui_file_name2 = "D:/PROJECTS_LYR/CHECK_LIST/05_DESKTOP/02_Python/PROJECTS_PY/YUOTUBE/YOUTUBE/YOUTUBE_FormMain.ui"

# ------------------------------------
# FormMainWindow(QMainWindow)
# ------------------------------------
class FormMainWindow(QMainWindow):
    """FormMainWindow"""
    __annotations__ = \
    luClassName = 'FormMainWindow'

    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_FormMainWindow()
        self.ui.setupUi(self)

        self.__FormCreate()

        self.__FSaveCurrentDir: str = ''
        self.__FSaveStatApplication: int = 0 #TStatApplication
        self.__FSheduler = None # TSheduler
        self.__FLogDir: str = ''
        self.__FStopYouTube: bool = True

        # Флаг, показывающий - участвует ли наше окно в цепи наблюдателей.
        self.__FInChain: bool = False
        # Хэндл окна, которое в цепи наблюдателей стоит за нами.
        self.__FNextClipboardViewer = None # HWND;

        self.__FFlagIdle: bool = True

        # Журнал
        self.APPLog: TFileMemoLog

    #--------------------------------------------------
    # destructor
    #--------------------------------------------------
    def __del__ (self):
        """destructor"""
    #beginfunction
        self.__FormDestroy()
        LClassName = self.__class__.__name__
        print('{} уничтожен'.format(LClassName))
    #endfunction

    @staticmethod
    def Test ():
        # YOUTUBE_test.print_hi('Test')
        ...

    @staticmethod
    def TestMain ():
        LURL = 'https:#www.youtube.com/watch?v=DCNtylTXgmM'
        # YOUTUBE_test.Main()
        ...

    def __FormCreate (self):
        """__FormCreate"""
    #beginfunction
        # Application.HelpFile 
        # Application.HelpFile = ProjectHELPFileName

        # Состояние программы
        self.__FStatApplication: LUProc.TStatApplication = LUProc.TStatApplication.caTest

        # __FParams
        self.__FParams: YOUTUBE_Params.TParams = YOUTUBE_Params.TParams()
        self.APPLog = self.__FParams.FileMemoLog

        # self.__FYOUTUBE: YOUTUBE_Proc.TYOUTUBE = YOUTUBE_Proc.TYOUTUBE()

        #-------------------------------
        # Panels
        #-------------------------------
        # for i = 0 to StatusBar_P1_P2.Panels.Count - 1 do
        #     StatusBar_P1_P2.Panels[i].Text = ''
    
        #-------------------------------
        # Sheduler
        #-------------------------------
        # FSheduler = TSheduler.Create (Self)
        # with FSheduler do
        # begin
        #     name = 'Sheduler'
        #     Enabled = False
        #     OnSheduler = Action_StartExecute
        #     AddEvent (ShedulerName, TEMPLATE_RegIni.ShedulerTEMPLATE)
        # end

        self.__SetStatApplication (LUProc.TStatApplication.caBreak)

        # Splash = TSplash.Create (Self)
        # Splash.Name = 'Splash'
        # Splash.Height = StatusBar_P1_P2.Height
        # Splash.Width = StatusBar_P1_P2.Panels[0].Width
        # StatusBar_P1_P2.InsertControl (Splash)
    
        # 01.Подключаемся к цепи наблюдателей.
        # FNextClipboardViewer = 0
        # FInChain = False
        # EnableView

        #FFormMainWindow.ui.action_Youtube.triggered.connect (FFormMainWindow.CreateYUOTUBEObject(LUObjectsYoutube.link3))
        #self.ui.action_CreateYoutube.triggered(self.__CreateYUOTUBEObject(LUObjectsYoutube.link3))
        self.__FormActivate()
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

    # TFormMain.FormDestroy

    def __FormDestroy (self):
        """__FormDestroy"""
    #beginfunction
        # del self.__FYOUTUBE
        self.__FormClose(LUProc.TStatApplication.caFree)
        # 04.Отключиться от цепи наблюдателей.
        # DisableView
        ...
    #endfunction

    # TFormMain.FormActivate

    def __FormActivate (self):
        """__FormActivate"""
    #beginfunction
        self.APPLog.AddLog(TTypeLogString.tlsINFO, 'Это информация')

        # ToolButtonAPP.Caption = FormAbout.InternalName
        # Caption = FormAbout.ProductName
    
        # Memo_Log
        # Memo_Log.SetFocus
        # Memo_Log.SelStart = Length (Memo_Log.Lines.Text)
        # Memo_Log.SelLength = 0

        self.APPLog.AddLog (TTypeLogString.tlsINFO, self.__FParams.FileMemoLog.FileName)
        self.APPLog.AddLog (TTypeLogString.tlsINFO, self.__FParams.FileNameINI)

        # VersionInfo
        # VersionInfo = CreateVersion (ParamStr(0))
        # APPLog.LogString[tlsInfo, 1] = ParamStr (0) + ' ' + VersionInfo.FileVersion+ ' ' + VersionInfo.FileDate
        # VersionInfo.Free
        ...
    #endfunction

    # TFormMain.FormClose

    def __FormClose (self, Action):
        """__FormClose"""
    #beginfunction
        # Action = caFree
        ...
    #endfunction

    # 01.Подключение к цепи наблюдателей.

    def __EnableView(self):
    #beginfunction
        """
        # Если мы уже подключены к цепи - выходим.
        if FInChain then
        begin
            APPLog.LogString[tlsInfo, 1] :=
                '01.Окно уже участвует в цепи наблюдателей за буфером обмена.'
            Exit
        end
        FNextClipboardViewer = SetClipboardViewer (Handle)
        APPLog.LogString[tlsInfo, 1] :=
            '01.Выполнено подключение к цепи наблюдателей за буфером обмена.'
        FInChain = True
        """
        ...
    #endfunction

    # 02.Отслеживайте удаленные окна просмотра, обрабатывая сообщение WM_CHANGECBCHAIN
    # и передавая его по цепочке или обновляя запись следующего окна в цепочке
    # по мере необходимости.
    # Вызывается в случае, если из цепи удаляется какой-то наблюдатель.

    def __WMChangeCBChain (self, Msg):
    #beginfunction
        """
        inherited
        # mark message as done
        Msg.Result = 0
        # the chain has changed
        if Msg.Remove = FNextClipboardViewer then
        begin
            # The next window in the clipboard viewer chain had been removed.
            # We recreate it.
            # Если из цепи наблюдателей удаляется некто не равный А4, то мы просто должны
            # переслать сообщение следующему в цепи - т. е. А4.
            APPLog.LogString[tlsInfo, 1] :=
                '02.The next window in the clipboard viewer chain had been removed.'
            FNextClipboardViewer = Msg.Next
        end else begin
            # Inform the next window in the clipboard viewer chain
            # Новые окна добавляются в начало цепи - т. е. перед А1. Поэтому
            # членам цепи не надо обрабатывать ситуации с добавлением.
            APPLog.LogString[tlsInfo, 1] :=
                '02.Inform the next window in the clipboard viewer chain.'
            SendMessage (FNextClipboardViewer, WM_CHANGECBCHAIN, Msg.Remove,
                Msg.Next)
        end
        """
        ...
    #endfunction

    # 03.Отвечайте на изменения буфера обмена, обрабатывая сообщение WM_DRAWCLIPBOARD
    # и передавая сообщение по цепочке.
    # Вызывается в случае, если содержимое буфера обмена изменилось.

    def __WMDrawClipboard (self, Msg):
    #var
        """
        i: Integer
        LIsMod: Boolean
        LURL: string
        LURI: IdURI.TIdURI
        LisYUOTUBE: Boolean
        LisYUOTUBEPlaylist: Boolean
        LisYUOTUBEPlaylists: Boolean
        """
    #beginfunction
        """
        inherited
        # Clipboard content has changed
        APPLog.LogString[tlsInfo, 1] = '03.Clipboard content has changed!'
        # Оповещаем об изменениях следующего за нами наблюдателя.
        # Inform the next window in the clipboard viewer chain
        if FNextClipboardViewer <> 0 then
        begin
            SendMessage (FNextClipboardViewer, WM_DRAWCLIPBOARD, 0, 0)
            Msg.Result = 0
        end
        # ----------------------------------------
        # Далее идёт код работы с буфером обмена.
        # ----------------------------------------
        # Проверяем, есть ли в буфере данные в интересующем нас формате.
        # Интересующий нас формат - текстовые данные.
        LIsMod = False
        for i = 0 to Clipboard.FormatCount - 1 do
            if Clipboard.HasFormat (CF_TEXT) then
            begin
                LIsMod = True
                Break
            end
        # Если данные в требуемом формате есть, то обрабатываем их.
        if LIsMod then
        begin
            APPLog.LogString[tlsInfo, 1] = '03.Данные типа CF_TEXT.'
    
            # LURI.Protocol, LURI.Username, LURI.Password, LURI.Host
            # LURI.Port, LURI.Path, LURI.Params
            LURL = Clipboard.AsText
            LURI = TIdURI.Create ('')
            try
                LURI.URI = LURL
                LisYUOTUBE = (UpperCase(LURI.Host) = cYUOTUBE)
                LisYUOTUBEPlaylists = Pos (cYUOTUBEplaylists,
                    UpperCase(LURI.Document)) > 0
                LisYUOTUBEPlaylist = Pos (cYUOTUBEplaylist,
                    UpperCase(LURI.Document)) > 0
            finally
                LURI.Free
            end
            if LisYUOTUBE then
            begin
                if LisYUOTUBEPlaylist then
                    CreateYUOTUBEPlaylist (LURL)
                else if FYouTubeObjectsCollection.FindYouTubeObjectsItemURL (LURL)
                    <> nil then
                    APPLog.LogString[tlsInfo, 1] = LURL + ' уже существует.'
                else
                    CreateYUOTUBEObject (LURL)
            end
        end else begin
            APPLog.LogString[tlsInfo, 1] :=
                '03.Буфер обмена не содержит данных типа CF_TEXT.'
        end
        """
        ...
    #endfunction

    # ----------------------------------------------------
    # 04.Перед закрытием приложения удалите окно просмотра из цепочки буфера обмена,
    # вызвав API-функцию ChangeClipboardChain.
    # 4. Remove from clipboard chain
    # ----------------------------------------------------
    # Отключение от цепи наблюдателей за буфером обмена.
    # ----------------------------------------------------

    def __DisableViewself(self):
    #beginfunction
        """
        # Если мы уже отключены от цепи - выходим.
        if not FInChain then
            Exit
        ChangeClipboardChain (Handle, FNextClipboardViewer)
        FInChain = False
        FNextClipboardViewer = 0
        APPLog.LogString[tlsInfo, 1] :=
            '04.Выполнено отключение от цепи наблюдателей за буфером обмена.'
        """
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
        ...
    #endfunction

    # TFormMain.CreateYUOTUBEObject
    def __CreateYUOTUBEObject (self, AURL: str):
    #beginfunction
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
        self.APPLog.SetLogString (TTypeLogString.tlsBegin, 0, LUProc.cProcessBegin)
        # --------------------------------------------------
        # FSheduler.DeleteEvent (ShedulerName)
        # FSheduler.AddEvent (ShedulerName, TEMPLATE_RegIni.ShedulerTEMPLATE)

        if self.Params.Stop:
            self.__Procedure_01()
            self.__ProcedureDeleteYUOTUBEObjects()
        #endif
        # --------------------------------------------------
        self.APPLog.SetLogString (TTypeLogString.tlsEnd, 0, LUProc.cProcessEnd)
        os.chdir(LSaveCurrentDir)
    #endfunction

#------------------------------------------
#
#------------------------------------------
Fapp: QApplication
FFormMainWindow: FormMainWindow

#------------------------------------------
# Testfunction ():
#------------------------------------------
def Testfunction ():
#beginfunction
    print ("The 'function' has been called!")
#endfunction

#------------------------------------------
#
#------------------------------------------
#beginmodule
if __name__ == "__main__":
    Fapp = QApplication(sys.argv)

    FFormMainWindow = FormMainWindow()
    #FFormMainWindow.ui.action_Youtube.triggered.connect (Testfunction)
    #FFormMainWindow.ui.action_Youtube.triggered.connect (LFormMainWindow.Test)
    #FFormMainWindow.ui.action_Youtube.triggered.connect (FFormMainWindow.TestMain)

    #FFormMainWindow.ui.action_Youtube.triggered.connect (FFormMainWindow.CreateYUOTUBEObject(LUObjectsYoutube.link3))

    FFormMainWindow.show()

    sys.exit(Fapp.exec())
#endif

#endmodule
