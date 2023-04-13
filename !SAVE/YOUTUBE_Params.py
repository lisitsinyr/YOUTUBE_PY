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
# import distutils.util

#------------------------------------------
# БИБЛИОТЕКИ сторонние
#------------------------------------------

#------------------------------------------
# БИБЛИОТЕКИ LU
#------------------------------------------
from LUParserINI import *
from LUParserREG import *
from LUParserARG import *
import LUFile
import LULog
import LUDateTime

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
# [Yuoutube]
rkYoutube: str = 'Youtube'
rpStop: str = 'Stop'
rpPathYoutubeLoad: str = 'PathYoutubeLoad'
rpCheckBoxCliboard: str = 'CheckBoxCliboard'
rpCheckBoxAutoDownload: str = 'CheckBoxAutoDownload'
rpCheckBoxAutoDelete: str = 'CheckBoxAutoDelete'
rpCheckBoxSkipExists: str = 'CheckBoxSkipExists'

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
        self.__FIniFile: TINIFile = TINIFile()
        self.__FIniReg: TREGParser = TREGParser()
        self.__FArgParser: TArgParser = TArgParser (description='Параметры', prefix_chars=YOUTUBE_Consts.cPrefixChars)
        self.__FFileMemoLog: LULog.TFileMemoLog  = LULog.TFileMemoLog ()

        YOUTUBE_Consts.APPWorkDir = LUos.APPWorkDir ()
        YOUTUBE_Consts.APPWorkDir = LUos.GetCurrentDir ()
        # print (self, 'sys.argv[0]=', sys.argv[0])
        YOUTUBE_Consts.APPWorkDir = LUFile.ExtractFileDir(sys.argv[0])

        # Параметры
        LFileNameINIArg = self.__FArgParser.add_argument (YOUTUBE_Consts.cParamNameINIFileName, type = str, default='', help = 'DirINI')
        LDirLogArg = self.__FArgParser.add_argument (YOUTUBE_Consts.cParamNameDirLOG, type = str, default = '', help = 'DirLog')
        self.__Fargs = self.__FArgParser.parse_args ()

        # FileINI
        LDirINI = self.__Fargs.ini
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

        # Журнал
        LLogDir = self.__Fargs.log
        if len (LLogDir) == 0:
            LLogDir = LUFile.IncludeTrailingBackslash(YOUTUBE_Consts.APPWorkDir) + 'LOG'
        else:
            LLogDir = LUFile.ExpandFileName (LLogDir)
        #endif
        LLogDir = LUFile.GetDirNameYYMM (LLogDir, LUDateTime.Now())
        self.__FFileMemoLog.FileName = LUFile.IncludeTrailingBackslash (LLogDir) +\
                                       YOUTUBE_Consts.cProjectNAME + '_' + LULog.GetLogFileName ()
    #endfunction

    #--------------------------------------------------
    # destructor
    #--------------------------------------------------
    def __del__ (self):
        """ destructor """
    #beginfunction
        del self.__FIniFile
        del self.__FIniReg
        del self.__FArgParser
        del self.__FFileMemoLog
        LClassName = self.__class__.__name__
        print('{} уничтожен'.format(LClassName))
    #endfunction

    #--------------------------------------------------
    # @property FileMemoLog
    #--------------------------------------------------
    # getter
    @property
    def FileMemoLog (self) -> LULog.TFileMemoLog:
    #beginfunction
        return self.__FFileMemoLog
    #endfunction

    #--------------------------------------------------
    # @property LogDir
    #--------------------------------------------------
    # getter
    @property
    def LogDir (self) -> str:
    #beginfunction
        return self.__Fargs.log
    #endfunction

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
    # @property Stop
    #--------------------------------------------------
    # getter
    @property
    def Stop (self) -> bool:
    #beginfunction
        # return distutils.util.strtobool(self.__FIniFile.GetOption(rkGENERAL, rpStop, False)
        return LUStrUtils.strtobool (self.__FIniFile.GetOption (rkYoutube, rpStop, str(False)))
    #endfunction
    @Stop.setter
    def Stop (self, AValue: bool):
    #beginfunction
        self.__FIniFile.SetOption (rkYoutube, rpStop, str(AValue))
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
        return LUStrUtils.strtobool (self.__FIniFile.GetOption (rkYoutube, rpCheckBoxCliboard, str(False)))
    #endfunction
    @CheckBoxCliboard.setter
    def CheckBoxCliboard (self, AValue: bool):
    #beginfunction
        self.__FIniFile.SetOption (rkYoutube, rpCheckBoxCliboard, str(AValue))
    #endfunction

    #--------------------------------------------------
    # @property CheckBoxAutoDownload
    #--------------------------------------------------
    # getter
    @property
    def CheckBoxAutoDownload (self) -> bool:
    #beginfunction
        return LUStrUtils.strtobool (self.__FIniFile.GetOption (rkYoutube, rpCheckBoxAutoDownload, str(False)))
    #endfunction
    @CheckBoxAutoDownload.setter
    def CheckBoxAutoDownload (self, AValue: bool):
    #beginfunction
        self.__FIniFile.SetOption (rkYoutube, rpCheckBoxAutoDownload, str(AValue))
    #endfunction

    #--------------------------------------------------
    # @property CheckBoxAutoDelete
    #--------------------------------------------------
    # getter
    @property
    def CheckBoxAutoDelete (self) -> bool:
    #beginfunction
        return LUStrUtils.strtobool (self.__FIniFile.GetOption (rkYoutube, rpCheckBoxAutoDelete, str(False)))
    #endfunction
    @CheckBoxAutoDelete.setter
    def CheckBoxAutoDelete (self, AValue: bool):
    #beginfunction
        self.__FIniFile.SetOption (rkYoutube, rpCheckBoxAutoDelete, str(AValue))
    #endfunction

    #--------------------------------------------------
    # @property CheckBoxSkipExists
    #--------------------------------------------------
    # getter
    @property
    def CheckBoxSkipExists (self) -> bool:
    #beginfunction
        return LUStrUtils.strtobool (self.__FIniFile.GetOption (rkYoutube, rpCheckBoxSkipExists, str(False)))
    #endfunction
    @CheckBoxSkipExists.setter
    def CheckBoxSkipExists (self, AValue: bool):
    #beginfunction
        self.__FIniFile.SetOption (rkYoutube, rpCheckBoxSkipExists, str(AValue))
    #endfunction

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

