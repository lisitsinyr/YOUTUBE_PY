"""
 =======================================================
 Copyright (c) 2023
 Author:
     Lisitsin Y.R.
 Project:
     YOUTUBE_PY
     Python (PROJECTS)
 Module:
     YOUTUBE_Params.py
     Параметры проекта
 =======================================================
"""

#------------------------------------------
# БИБЛИОТЕКИ python
#------------------------------------------
import sys

#------------------------------------------
# БИБЛИОТЕКИ сторонние
#------------------------------------------

#------------------------------------------
# БИБЛИОТЕКИ LU
#------------------------------------------
import LULog
import LUParserINI
import LUParserARG
import LUFile
import LUDateTime
import LUStrUtils
import LUos

#------------------------------------------
# БИБЛИОТЕКИ PROJECT
#------------------------------------------
import YOUTUBE_Consts

# ---------------------------------------------------------- 
# Ini
# ---------------------------------------------------------- 
pPATHIN: str = 'PATHIN'
pPATHOUT1: str = 'PATHOUT1'
pPATHOUT2: str = 'PATHOUT2'
pWILDCARDS: str = 'WILDCARDS'
pOPERATIONS: str = 'OPERATIONS'
pActive: str = 'ACTIVE'
# ---------------------------------------------------------- 
pSYSTEM: str = 'SYSTEM'
pMASK: str = 'MASK'
pADDRESSFrom: str = 'ADDRESSFROM'
pIBEGINFrom: str = 'IBEGINFROM'
pICOUNTFrom: str = 'ICOUNTFROM'
pADDRESSTo: str = 'ADDRESSTO'
pIBEGINTo: str = 'IBEGINTO'
pICOUNTTo: str = 'ICOUNTTO'

# ---------------------------------------------------------- 
# Registry 
# ---------------------------------------------------------- 
#RootKeyHKLM = HKEY_LOCAL_MACHINE
#RootKeyHKCU = HKEY_CURRENT_USER
sSoftware: str = 'SOFTWARE'
rkSoftware: str = sSoftware + '\\' + YOUTUBE_Consts.cProjectNAME
# ---------------------------------------------------------- 

# ---------------------------------------------------------- 
# IniFile
# ---------------------------------------------------------- 
rkROOT: str = YOUTUBE_Consts.cProjectNAME
# [GENERAL]
rkGENERAL: str = 'GENERAL'
rpPathStore: str = 'PathStore'
rpPathStoreOut: str = 'PathStoreOut'
rpPathStoreError: str = 'PathStoreError'
rpSheduler: str = 'Sheduler'
# [Youtube]
rkYoutube: str = 'Youtube'
rpPathYoutubeLoad: str = 'PathYoutubeLoad'
rpCheckBoxCliboard: str = 'CheckBoxCliboard'
rpCheckBoxAutoDownload: str = 'CheckBoxAutoDownload'
rpCheckBoxAutoDelete: str = 'CheckBoxAutoDelete'
rpCheckBoxSkipExists: str = 'CheckBoxSkipExists'
rpCheckBoxStop: str = 'CheckBoxStop'
rpCheckBoxChunk: str = 'CheckBoxChunk'
rpCheckBoxDownload: str = 'CheckBoxDownload'
rpComboboxMaxRes: str = 'ComboboxMaxRes'
rpNumberThread: str = 'NumberThread'
class TParams(object):
    """TParams"""
    __annotations__ = \
        """
        TPParams - Параметры проекта
        """
    luClassName = 'TParams'

    #--------------------------------------------------
    # constructor
    #--------------------------------------------------
    def __init__ (self, **kwargs):
        """ Constructor """
    #beginfunction
        super ().__init__ (**kwargs)
        self.__FFileNameINI: str = ''
        self.__FIniFile = LUParserINI.TINIFile()
        # self.__FFileMemoLog: LULog.TFileMemoLog  = LULog.TFileMemoLog ()

        # YOUTUBE_Consts.APPWorkDir = LUos.APPWorkDir ()
        # YOUTUBE_Consts.APPWorkDir = LUos.GetCurrentDir ()
        YOUTUBE_Consts.APPWorkDir = LUFile.ExtractFileDir(sys.argv[0])

        # Параметры
        self.__GetARGS ()

        # FileINI
        LDirINI = LUParserARG.GArgParser.Args.ini
        if len (LDirINI) == 0:
            LDirINI = YOUTUBE_Consts.APPWorkDir
        else:
            LDirINI = LUFile.ExpandFileName (LDirINI)
            if not LUFile.DirectoryExists(LDirINI):
                LDirINI = YOUTUBE_Consts.APPWorkDir
            #endif
        #endif
        LFileNameINI = LUFile.IncludeTrailingBackslash(LDirINI)+YOUTUBE_Consts.cProjectINIFileName
        self.FileNameINI = LFileNameINI

        # # Журнал
        # LLogDir = LUParserARG.GArgParser.Args.log
        # if len (LLogDir) == 0:
        #     LLogDir = LUFile.IncludeTrailingBackslash(YOUTUBE_Consts.APPWorkDir) + 'LOG'
        # else:
        #     LLogDir = LUFile.ExpandFileName (LLogDir)
        # #endif
        # LLogDir = LUFile.GetDirNameYYMM (LLogDir, LUDateTime.Now())
        # self.__FFileMemoLog.FileName = LUFile.IncludeTrailingBackslash (LLogDir) +\
        #                                YOUTUBE_Consts.cProjectNAME + '_' + LULog.GetLogFileName ()
        self.__FPathStore: str = ''
        self.__FPathStoreOut: str = ''
        self.__FPathStoreError: str = ''
        self.__FPathYoutubeLoad: str = ''
        self.__FSheduler: str = ''

        self.__FCheckBoxCliboard: bool = False
        self.__FCheckBoxAutoDownload: bool = False
        self.__FCheckBoxAutoDelete: bool = False
        self.__FCheckBoxSkipExists: bool = False
        self.__FCheckBoxStop: bool = False
        self.__FCheckBoxChunk: bool = False
        self.__FCheckBoxDownload: bool = False

        self.__FComboboxMaxRes: str = ''
        self.__FNumberTread: int = 5

        self.GetParams ()
    #endfunction

    #--------------------------------------------------
    # destructor
    #--------------------------------------------------
    def __del__ (self):
        """ destructor """
    #beginfunction
        del self.__FIniFile
        # del self.__FFileMemoLog
        LClassName = self.__class__.__name__
        s = '{} уничтожен'.format(LClassName)
        #print (s)
    #endfunction

    @staticmethod
    def __GetARGS ():
        """__GetARGS"""
    #beginfunction
        if not LUParserARG.GArgParser is None:
            LUParserARG.GArgParser.Clear ()
            if LUParserARG.GArgParser.Args is None:
                LArg = LUParserARG.GArgParser.add_argument ('-log', type = str, default = '', help = 'log dir')
                LArg = LUParserARG.GArgParser.add_argument ('-ini', type = str, default = '', help = 'INI')
                LUParserARG.GArgParser.Args = LUParserARG.GArgParser.ArgParser.parse_args ()
                #print (LUParserARG.GArgParser.Args)
                #print (f'log = {LUParserARG.GArgParser.Args.log}')
                #print (f'ini = {LUParserARG.GArgParser.Args.ini}')
            else:
                #print (LUParserARG.GArgParser.Args)
                ...
            #endif
        #endif
    #endfunction

    def RefreashOption (self):
        """RefreashOption"""
    #beginfunction
        self.__FIniFile.RefreashOption()
    #endfunction
    def GetParams (self):
        """GetParams"""
    #beginfunction
        self.RefreashOption()
        self.__FPathStore = self.__FIniFile.GetOption (rkGENERAL, rpPathStore, '')
        self.__FPathStoreOut = self.__FIniFile.GetOption(rkGENERAL, rpPathStoreOut, '')
        self.__FPathStoreError = self.__FIniFile.GetOption(rkGENERAL, rpPathStoreError, '')
        self.__FPathYoutubeLoad = self.__FIniFile.GetOption(rkYoutube, rpPathYoutubeLoad, '')
        self.__FSheduler = self.__FIniFile.GetOption(rkGENERAL, rpSheduler, '')

        self.__FCheckBoxCliboard = LUStrUtils.strtobool (self.__FIniFile.GetOption (rkYoutube, rpCheckBoxCliboard, str(False)))
        self.__FCheckBoxAutoDownload = LUStrUtils.strtobool (self.__FIniFile.GetOption (rkYoutube, rpCheckBoxAutoDownload, str(False)))
        self.__FCheckBoxAutoDelete = LUStrUtils.strtobool (self.__FIniFile.GetOption (rkYoutube, rpCheckBoxAutoDelete, str(False)))
        self.__FCheckBoxSkipExists = LUStrUtils.strtobool (self.__FIniFile.GetOption (rkYoutube, rpCheckBoxSkipExists, str(False)))
        self.__FCheckBoxStop = LUStrUtils.strtobool (self.__FIniFile.GetOption (rkYoutube, rpCheckBoxStop, str (False)))
        self.__FCheckBoxChunk = LUStrUtils.strtobool (self.__FIniFile.GetOption (rkYoutube, rpCheckBoxChunk, str (False)))
        self.__FCheckBoxDownload = LUStrUtils.strtobool (self.__FIniFile.GetOption (rkYoutube, rpCheckBoxDownload, str(False)))

        self.__FComboboxMaxRes = self.__FIniFile.GetOption (rkYoutube, rpComboboxMaxRes, '')
        self.__FNumberThread = self.__FIniFile.GetOption (rkYoutube, rpNumberThread, 5)
    #endfunction
    def SetParams (self):
        """SetParams"""
    #beginfunction
        self.__FIniFile.SetOption (rkGENERAL, rpPathStore, self.__FPathStore)
        self.__FIniFile.SetOption (rkGENERAL, rpPathStoreOut, self.__FPathStoreOut)
        self.__FIniFile.SetOption (rkGENERAL, rpPathStoreError, self.__FPathStoreError)
        self.__FIniFile.SetOption (rkYoutube, rpPathYoutubeLoad, self.__FPathYoutubeLoad)
        self.__FIniFile.SetOption (rkGENERAL, rpSheduler, self.__FSheduler)

        self.__FIniFile.SetOption (rkYoutube, rpCheckBoxCliboard, str(self.__FCheckBoxCliboard))
        self.__FIniFile.SetOption (rkYoutube, rpCheckBoxAutoDownload, str(self.__FCheckBoxAutoDownload))
        self.__FIniFile.SetOption (rkYoutube, rpCheckBoxAutoDelete, str(self.__FCheckBoxAutoDelete))
        self.__FIniFile.SetOption (rkYoutube, rpCheckBoxSkipExists, str(self.__FCheckBoxSkipExists))
        self.__FIniFile.SetOption (rkYoutube, rpCheckBoxStop, str (self.__FCheckBoxStop))
        self.__FIniFile.SetOption (rkYoutube, rpCheckBoxChunk, str (self.__FCheckBoxChunk))
        self.__FIniFile.SetOption (rkYoutube, rpCheckBoxDownload, str (self.__FCheckBoxDownload))

        self.__FIniFile.SetOption (rkYoutube, rpComboboxMaxRes, self.__FComboboxMaxRes)
        self.__FIniFile.SetOption (rkYoutube, rpNumberThread, self.__FNumberThread)

    #endfunction

    # #--------------------------------------------------
    # # @property FileMemoLog
    # #--------------------------------------------------
    # # getter
    # @property
    # def FileMemoLog (self) -> LULog.TFileMemoLog:
    # #beginfunction
    #     return self.__FFileMemoLog
    # #endfunction

    #--------------------------------------------------
    # @property FileNameINI
    #--------------------------------------------------
    # getter
    @property
    def FileNameINI (self):
    #beginfunction
        return self.__FFileNameINI
    #endfunction
    # setter
    @FileNameINI.setter
    def FileNameINI (self, AValue: str):
    #beginfunction
        self.__FFileNameINI = AValue
        self.__FIniFile.FileNameINI = self.FileNameINI
    #endfunction

    #--------------------------------------------------
    # @property PathStore
    #--------------------------------------------------
    # getter
    @property
    def PathStore (self) -> str:
    #beginfunction
        return self.__FIniFile.GetOption(rkGENERAL, rpPathStore, '')
    #endfunction
    # setter
    @PathStore.setter
    def PathStore (self, AValue: str):
    #beginfunction
        self.__FIniFile.SetOption (rkGENERAL, rpPathStore, AValue)
    #endfunction
    #--------------------------------------------------
    # @property PathStoreOut
    #--------------------------------------------------
    # getter
    @property
    def PathStoreOut (self) -> str:
    #beginfunction
        return self.__FIniFile.GetOption(rkGENERAL, rpPathStoreOut, '')
    #endfunction
    # setter
    @PathStoreOut.setter
    def PathStoreOut (self, AValue: str):
    #beginfunction
        self.__FIniFile.SetOption (rkGENERAL, rpPathStoreOut, AValue)
    #endfunction

    #--------------------------------------------------
    # @property PathStoreError
    #--------------------------------------------------
    # getter
    @property
    def PathStoreError (self) -> str:
    #beginfunction
        return self.__FIniFile.GetOption(rkGENERAL, rpPathStoreError, '')
    #endfunction
    # setter
    @PathStoreError.setter
    def PathStoreError (self, AValue: str):
    #beginfunction
        self.__FIniFile.SetOption (rkGENERAL, rpPathStoreError, AValue)
    #endfunction

    #--------------------------------------------------
    # @property Sheduler
    #--------------------------------------------------
    # getter
    @property
    def Sheduler (self) -> str:
    #beginfunction
        return self.__FIniFile.GetOption(rkGENERAL, rpSheduler, '')
    #endfunction
    # setter
    @Sheduler.setter
    def Sheduler (self, AValue: str):
    #beginfunction
        self.__FIniFile.SetOption (rkGENERAL, rpSheduler, AValue)
    #endfunction

    #--------------------------------------------------
    # @property PathYoutubeLoad
    #--------------------------------------------------
    # getter
    @property
    def PathYoutubeLoad (self) -> str:
    #beginfunction
        return self.__FIniFile.GetOption(rkYoutube, rpPathYoutubeLoad, '')
    #endfunction
    # setter
    @PathYoutubeLoad.setter
    def PathYoutubeLoad (self, AValue: str):
    #beginfunction
        self.__FIniFile.SetOption (rkYoutube, rpPathYoutubeLoad, AValue)
    #endfunction

    #--------------------------------------------------
    # @property CheckBoxCliboard
    #--------------------------------------------------
    # getter
    @property
    def CheckBoxCliboard (self) -> bool:
    #beginfunction
        b = self.__FIniFile.GetOption (rkYoutube, rpCheckBoxCliboard, False)
        return b
    #endfunction
    @CheckBoxCliboard.setter
    def CheckBoxCliboard (self, AValue: bool):
    #beginfunction
        self.__FIniFile.SetOption (rkYoutube, rpCheckBoxCliboard, AValue)
    #endfunction

    #--------------------------------------------------
    # @property CheckBoxAutoDownload
    #--------------------------------------------------
    # getter
    @property
    def CheckBoxAutoDownload (self) -> bool:
    #beginfunction
        b = self.__FIniFile.GetOption (rkYoutube, rpCheckBoxAutoDownload, False)
        return b
    #endfunction
    @CheckBoxAutoDownload.setter
    def CheckBoxAutoDownload (self, AValue: bool):
    #beginfunction
        self.__FIniFile.SetOption (rkYoutube, rpCheckBoxAutoDownload, AValue)
    #endfunction

    #--------------------------------------------------
    # @property CheckBoxAutoDelete
    #--------------------------------------------------
    # getter
    @property
    def CheckBoxAutoDelete (self) -> bool:
    #beginfunction
        b = self.__FIniFile.GetOption (rkYoutube, rpCheckBoxAutoDelete, False)
        return b
    #endfunction
    @CheckBoxAutoDelete.setter
    def CheckBoxAutoDelete (self, AValue: bool):
    #beginfunction
        self.__FIniFile.SetOption (rkYoutube, rpCheckBoxAutoDelete, bool(AValue))
    #endfunction

    #--------------------------------------------------
    # @property CheckBoxSkipExists
    #--------------------------------------------------
    # getter
    @property
    def CheckBoxSkipExists (self) -> bool:
    #beginfunction
        b = self.__FIniFile.GetOption (rkYoutube, rpCheckBoxSkipExists, False)
        return b
    #endfunction
    @CheckBoxSkipExists.setter
    def CheckBoxSkipExists (self, AValue: bool):
    #beginfunction
        self.__FIniFile.SetOption (rkYoutube, rpCheckBoxSkipExists, AValue)
    #endfunction

    #--------------------------------------------------
    # @property CheckBoxStop
    #--------------------------------------------------
    # getter
    @property
    def CheckBoxStop (self) -> bool:
    #beginfunction
        b = self.__FIniFile.GetOption (rkYoutube, rpCheckBoxStop, False)
        return b
    #endfunction
    @CheckBoxStop.setter
    def CheckBoxStop (self, AValue: bool):
    #beginfunction
        self.__FIniFile.SetOption (rkYoutube, rpCheckBoxStop, AValue)
    #endfunction

    #--------------------------------------------------
    # @property CheckBoxChunk
    #--------------------------------------------------
    # getter
    @property
    def CheckBoxChunk (self) -> bool:
    #beginfunction
        b = self.__FIniFile.GetOption (rkYoutube, rpCheckBoxChunk, False)
        return b
    #endfunction
    @CheckBoxChunk.setter
    def CheckBoxChunk (self, AValue: bool):
    #beginfunction
        self.__FIniFile.SetOption (rkYoutube, rpCheckBoxChunk, AValue)
    #endfunction

    #--------------------------------------------------
    # @property CheckBoxDownload
    #--------------------------------------------------
    # getter
    @property
    def CheckBoxDownload (self) -> bool:
    #beginfunction
        b = self.__FIniFile.GetOption (rkYoutube, rpCheckBoxDownload, False)
        return b
    #endfunction
    @CheckBoxDownload.setter
    def CheckBoxDownload (self, AValue: bool):
    #beginfunction
        self.__FIniFile.SetOption (rkYoutube, rpCheckBoxDownload, AValue)
    #endfunction

    #--------------------------------------------------
    # @property ComboboxMaxRes
    #--------------------------------------------------
    # getter
    @property
    def ComboboxMaxRes (self) -> str:
    #beginfunction
        return self.__FIniFile.GetOption(rkYoutube, rpComboboxMaxRes, '')
    #endfunction
    # setter
    @ComboboxMaxRes.setter
    def ComboboxMaxRes (self, AValue: str):
    #beginfunction
        self.__FIniFile.SetOption (rkYoutube, rpComboboxMaxRes, AValue)
    #endfunction

    #--------------------------------------------------
    # @property NumberThread
    #--------------------------------------------------
    # getter
    @property
    def NumberThread (self) -> int:
    #beginfunction
        return self.__FIniFile.GetOption(rkYoutube, rpNumberThread, 5)
    #endfunction
    # setter
    @NumberThread.setter
    def NumberThread (self, AValue: int):
    #beginfunction
        self.__FIniFile.SetOption (rkYoutube, rpNumberThread, AValue)
    #endfunction



#endclass

# ------------------------------------------
#
#------------------------------------------
def main ():
#beginfunction
    ...
#endfunction

# ------------------------------------------
#
# ------------------------------------------
#beginmodule
if __name__ == "__main__":
    main ()
#endif

#endmodule

