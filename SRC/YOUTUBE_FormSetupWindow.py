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

from PySide6.QtCore import (
    QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt, QObject, QThread, Signal, Slot,
    QRegularExpression,
    QStringListModel, QModelIndex
    )

from PySide6.QtGui import (
    QAction, QBrush, QColor, QConicalGradient,
    QCursor, QFont, QFontDatabase, QGradient,
    QIcon, QImage, QKeySequence, QLinearGradient,
    QPainter, QPalette, QPixmap, QRadialGradient,
    QRegularExpressionValidator, QValidator,
    QTransform,
    QClipboard
    )

from PySide6.QtWidgets import (
    QAbstractScrollArea, QApplication, QFrame, QHBoxLayout, QVBoxLayout,
    QListView, QMainWindow, QMenu, QMenuBar, QDialog,
    QPlainTextEdit, QScrollArea, QSizePolicy, QSplitter,
    QStatusBar, QTextEdit, QToolBar, QVBoxLayout,
    QSizePolicy, QPushButton,
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

import YOUTUBE_Params

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

        # __FParams
        self.__FParams: YOUTUBE_Params.TParams = YOUTUBE_Params.TParams ()

        self.__FPathStore: str = ''
        self.__FPathStoreOut: str = ''
        self.__FPathStoreError: str = ''
        self.__FPathYoutubeLoad: str = ''
        self.__FSheduler: str = ''
        self.__FMIN: str = ''
        self.__FHH: str = ''
        self.__FDD: str = ''
        self.__FDN: str = ''
        self.__FMM: str = ''

        self.__FCheckBoxCliboard: bool = False
        self.__FCheckBoxAutoDownload: bool = False
        self.__FCheckBoxAutoDelete: bool = False
        self.__FCheckBoxSkipExists: bool = False
        self.__FCheckBoxChunck: bool = False
        self.__FCheckBoxStop: bool = False
        self.__FCheckBoxDownload: bool = False

        self.__FMaxRes: str = ''
        self.__FNumberThread: int = 0

        self.ui.toolButton_PathStore.clicked.connect(self.__toolButton_PathStore)
        self.ui.toolButton_PathStoreOut.clicked.connect (self.__toolButton_PathStoreOut)
        self.ui.toolButton_PathStoreError.clicked.connect (self.__toolButton_PathStoreError)
        self.ui.toolButton_PathYoutubeLoad.clicked.connect (self.__toolButton_PathYoutubeLoad)

        # self.ui.comboBox_MaxRes.addItems(['1','2','3'])
        self.ui.comboBox_MaxRes.addItems (LUObjectsYT.cMaxRes1080p)
        # Set initial selected item
        self.ui.comboBox_MaxRes.setCurrentIndex (0)
        # Connect ComboBox to method that will handle the user's selection
        self.ui.comboBox_MaxRes.activated.connect (self.__comboBox_MaxRes_selection)
        # self.ui.comboBox_MaxRes.connect (self.__comboBox_MaxRes)

        # Сигнал, который активируется при любом изменении текста в виджете QLineEdit.
        # self.ui.lineEdit_PathStore.textChanged[str].connect(self.__lineEdit_PathStore)

        # Почти такой же, как textChanged(), однако этот сигнал не выдается, когда текст изменяется программно, например, вызовом setText().
        # self.ui.lineEdit_PathStore.textEdited[str].connect(self.__lineEdit_PathStore)

        # This signal is emitted when the Return or Enter key is pressed or the line edit loses focus (when it’s no longer highlighted)
        # Этот сигнал излучается, когда нажимается клавиша «Ввод» или «Ввод», или при редактировании строки теряется фокус (когда она больше не выделена).
        # self.ui.lineEdit_PathStore.editingFinished [str].connect (self.__lineEdit_PathStore)

        # Emits a signal when the user inputs a character that’s considered “invalid”. This signal is used together with the Validator functions.
        # Выдает сигнал, когда пользователь вводит символ, который считается «недопустимым».
        # Этот сигнал используется вместе с функциями валидатора.
        # self.ui.lineEdit_PathStore.inputRejected [str].connect (self.__lineEdit_PathStore)

        # Emitted when either the return key or enter key is pressed by the user.
        # Генерируется, когда пользователь нажимает либо клавишу возврата, либо клавишу ввода.
        # self.ui.lineEdit_PathStore.returnPressed [str].connect (self.__lineEdit_PathStore)

        self.ui.lineEdit_PathStore.textChanged.connect(self.__lineEdit_PathStore)
        self.ui.lineEdit_PathStoreOut.textChanged.connect (self.__lineEdit_PathStoreOut)
        self.ui.lineEdit_PathStoreError.textChanged.connect (self.__lineEdit_PathStoreError)
        self.ui.lineEdit_PathYoutubeLoad.textChanged.connect (self.__lineEdit_PathYoutubeLoad)

        # MIN - //0-59
        self.__FMIN_re = QRegularExpression (
            '^(((([0-5]?[0-9]|60)(-([0-5]?[0-9]|60)){0,1}?)|\*)(,([0-5]?[0-9]|60)((-([0-5]?[0-9]|60)){0,1}?))*?)$')
        self.__FMIN_validator = QRegularExpressionValidator(self.__FMIN_re, self.ui.lineEdit_MIN)
        self.ui.lineEdit_MIN.setValidator(self.__FMIN_validator)
        self.ui.lineEdit_MIN.textChanged.connect (self.__lineEdit_MIN)
        # HH - //0-23
        self.__FHH_re = QRegularExpression (
            '^(((([0-1]?[0-9]|2[0-4])(-([0-1]?[0-9]|2[0-4])){0,1}?)|\*)(,([0-1]?[0-9]|2[0-4])((-([0-1]?[0-9]|2[0-4])){0,1}?))*?)$')
        self.__FHH_validator = QRegularExpressionValidator (self.__FHH_re, self.ui.lineEdit_HH)
        self.ui.lineEdit_HH.setValidator (self.__FHH_validator)
        self.ui.lineEdit_HH.textChanged.connect (self.__lineEdit_HH)
        # DD - //1-31
        self.__FDD_re = QRegularExpression (
            '^(((([0-2]?[0-9]|3[0-1])(-([0-2]?[0-9]|3[0-1])){0,1}?)|\*)(,([0-2]?[0-9]|3[0-1])((-([0-2]?[0-9]|3[0-1])){0,1}?))*?)$')
        self.__FDD_validator = QRegularExpressionValidator (self.__FDD_re, self.ui.lineEdit_DD)
        self.ui.lineEdit_DD.setValidator (self.__FDD_validator)
        self.ui.lineEdit_DD.textChanged.connect (self.__lineEdit_DD)
        # DN //1-7
        self.__FDN_re = QRegularExpression (
            '^(((([1]?[1-7])(-([1]?[1-7])){0,1}?)|\*)(,([1]?[1-7])((-([1]?[1-7])){0,1}?))*?)$')
        self.__FDN_validator = QRegularExpressionValidator (self.__FDN_re, self.ui.lineEdit_DN)
        self.ui.lineEdit_DN.setValidator (self.__FDN_validator)
        self.ui.lineEdit_DN.textChanged.connect (self.__lineEdit_DN)
        # MM - //1-12
        self.__FMM_re = QRegularExpression (
            '^(((([1]?[1-9]|1[0-2])(-([0]?[0-9]|1[0-2])){0,1}?)|\*)(,([0]?[0-9]|1[0-2])((-([0]?[0-9]|1[0-2])){0,1}?))*?)$')
        self.__FMM_validator = QRegularExpressionValidator (self.__FMM_re, self.ui.lineEdit_MM)
        self.ui.lineEdit_MM.setValidator (self.__FMM_validator)
        self.ui.lineEdit_MM.textChanged.connect (self.__lineEdit_MM)

        self.__LoadSetup()

        """
        QLineEdit Methods
        setAlignment()  Decides the Alignment of the text. Takes 4 possible values, Qt.AlignLeft, Qt.AlignRight, Qt.AlignCenter and Qt.AlignJustify.
        clear()         Deletes the contents within the QLineEdit widget.
        setEchoMode()   Controls the mode for text appearance in the widget. Values are QLineEdit.Normal, QLineEdit.NoEcho, QLineEdit.Password, QLineEdit.PasswordEchoOnEdit.
        setMaxLength()  Defines the maximum number of characters that can be typed into the widget.
        setReadOnly()   Makes the widget non-editable
        setText()       The text passed to this method will appear in the widget.
        text()          Returns the text currently in the widget.
        setValidator()  Defines the validation rules.
        setInputMask()  Applies mask of combination of characters for input
        setFont()       Sets the font for the widget.
        setFixedWidth(width)    Sets the maximum width for the Widget in pixels.
        """
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

    def __comboBox_MaxRes_selection (self, index):
        """__comboBox_MaxRes_selection"""
    #beginfunction
        # Get the selected item from the ComboBox and display it in the console
        LMaxRes = self.ui.comboBox_MaxRes.currentText()
        # print(f'Selected item: {selected_item}')
        self.__FMaxRes = LMaxRes
    #endfunction

    def __toolButton_PathStore (self, text):
        """__toolButton_PathStore"""
    #beginfunction
        Ldirectory_path = YOUTUBE_Proc.OpenDirectoryDialog(Aparent = self, dir = self.ui.lineEdit_PathStore.text())
        if Ldirectory_path != '':
            self.ui.lineEdit_PathStore.setText (Ldirectory_path)
        #endif
    #endfunction
    def __toolButton_PathStoreOut (self, text):
        """__toolButton_PathStoreOut"""
    #beginfunction
        Ldirectory_path = YOUTUBE_Proc.OpenDirectoryDialog(Aparent = self, dir = self.ui.lineEdit_PathStoreOut.text())
        if Ldirectory_path != '':
            self.ui.lineEdit_PathStoreOut.setText (Ldirectory_path)
        #endif
    #endfunction
    def __toolButton_PathStoreError (self, text):
        """__toolButton_PathStoreError"""
    #beginfunction
        Ldirectory_path = YOUTUBE_Proc.OpenDirectoryDialog(Aparent = self, dir = self.ui.lineEdit_PathStoreError.text())
        if Ldirectory_path != '':
            self.ui.lineEdit_PathStoreError.setText (Ldirectory_path)
        #endif
    #endfunction
    def __toolButton_PathYoutubeLoad (self, text):
        """__toolButton_PathYoutubeLoad"""
    #beginfunction
        Ldirectory_path = YOUTUBE_Proc.OpenDirectoryDialog(Aparent = self, dir = self.ui.lineEdit_PathYoutubeLoad.text())
        if Ldirectory_path != '':
            self.ui.lineEdit_PathYoutubeLoad.setText (Ldirectory_path)
        #endif
    #endfunction

    def __lineEdit_PathStore (self, text):
        """__lineEdit_PathStore"""
    #beginfunction
        self.__FPathStore = text
        if not LUFile.DirectoryExists(self.__FPathStore):
            self.ui.lineEdit_PathStore.setStyleSheet (YOUTUBE_Proc.StyleColor_Error)
        else:
            self.ui.lineEdit_PathStore.setStyleSheet (YOUTUBE_Proc.StyleColor_Ok)
        #endif
    #endfunction
    def __lineEdit_PathStoreOut (self, text):
        """__lineEdit_PathStoreOut"""
    #beginfunction
        self.__FPathStoreOut = text
        if not LUFile.DirectoryExists(self.__FPathStoreOut):
            self.ui.lineEdit_PathStoreOut.setStyleSheet (YOUTUBE_Proc.StyleColor_Error)
        else:
            self.ui.lineEdit_PathStoreOut.setStyleSheet (YOUTUBE_Proc.StyleColor_Ok)
        #endif
    #endfunction
    def __lineEdit_PathStoreError (self, text):
        """__lineEdit_PathStoreError"""
    #beginfunction
        self.__FPathStoreError = text
        if not LUFile.DirectoryExists(self.__FPathStoreError):
            self.ui.lineEdit_PathStoreError.setStyleSheet (YOUTUBE_Proc.StyleColor_Error)
        else:
            self.ui.lineEdit_PathStoreError.setStyleSheet (YOUTUBE_Proc.StyleColor_Ok)
        #endif
    #endfunction
    def __lineEdit_PathYoutubeLoad (self, text):
        """__lineEdit_PathYoutubeLoad"""
    #beginfunction
        self.__FPathYoutubeLoad = text
        if not LUFile.DirectoryExists(self.__FPathYoutubeLoad):
            self.ui.lineEdit_PathYoutubeLoad.setStyleSheet (YOUTUBE_Proc.StyleColor_Error)
        else:
            self.ui.lineEdit_PathYoutubeLoad.setStyleSheet (YOUTUBE_Proc.StyleColor_Ok)
        #endif
    #endfunction

    def __lineEdit_MIN (self, text):
        """__lineEdit_MIN"""
    #beginfunction
        self.__FMIN = text
        LResult: tuple = self.__FMIN_validator.validate(text,0)
        """
        LResult [0]
            QValidator.State.Invalid
            QValidator.State.Intermediate
            QValidator.State.Acceptable
        LResult [1]
            text
        LResult [2]
            количество символов
        """
        if LResult [0] == QValidator.State.Invalid:
            self.ui.lineEdit_MIN.setStyleSheet (YOUTUBE_Proc.StyleColor_Error)
        else:
            self.ui.lineEdit_MIN.setStyleSheet (YOUTUBE_Proc.StyleColor_Ok)
        #endif
    #endfunction
    def __lineEdit_HH (self, text):
        """__lineEdit_HH"""
    #beginfunction
        self.__FHH = text
        LResult: tuple = self.__FHH_validator.validate (text, 0)
        if LResult [0] == QValidator.State.Invalid:
            self.ui.lineEdit_HH.setStyleSheet (YOUTUBE_Proc.StyleColor_Error)
        else:
            self.ui.lineEdit_HH.setStyleSheet (YOUTUBE_Proc.StyleColor_Ok)
    #endfunction
    def __lineEdit_DD (self, text):
        """__lineEdit_DD"""
    #beginfunction
        self.__FDD = text
        LResult: tuple = self.__FDD_validator.validate (text, 0)
        if LResult [0] == QValidator.State.Invalid:
            self.ui.lineEdit_DD.setStyleSheet (YOUTUBE_Proc.StyleColor_Error)
        else:
            self.ui.lineEdit_DD.setStyleSheet (YOUTUBE_Proc.StyleColor_Ok)
    #endfunction
    def __lineEdit_DN (self, text):
        """__lineEdit_DN"""
    #beginfunction
        self.__FDN = text
        LResult: tuple = self.__FDN_validator.validate (text, 0)
        if LResult [0] == QValidator.State.Invalid:
            self.ui.lineEdit_DN.setStyleSheet (YOUTUBE_Proc.StyleColor_Error)
        else:
            self.ui.lineEdit_DN.setStyleSheet (YOUTUBE_Proc.StyleColor_Ok)
    #endfunction
    def __lineEdit_MM (self, text):
        """__lineEdit_MM"""
    #beginfunction
        self.__FMM = text
        LResult: tuple = self.__FMM_validator.validate (text, 0)
        if LResult [0] == QValidator.State.Invalid:
            self.ui.lineEdit_MM.setStyleSheet (YOUTUBE_Proc.StyleColor_Error)
        else:
            self.ui.lineEdit_MM.setStyleSheet (YOUTUBE_Proc.StyleColor_Ok)
    #endfunction

    def __LoadSetup (self):
        """LoadSetup"""
    #beginfunction
        self.ui.lineEdit_PathStore.setText (self.__FParams.PathStore)
        self.ui.lineEdit_PathStoreOut.setText (self.__FParams.PathStoreOut)
        self.ui.lineEdit_PathStoreError.setText (self.__FParams.PathStoreError)
        self.ui.lineEdit_PathYoutubeLoad.setText (self.__FParams.PathYoutubeLoad)
        LMIN, LHH, LDD, LDN, LMM = self.__FParams.Sheduler.split(' ')
        self.ui.lineEdit_MIN.setText (LMIN)
        self.ui.lineEdit_HH.setText (LHH)
        self.ui.lineEdit_DD.setText (LDD)
        self.ui.lineEdit_DN.setText (LDN)
        self.ui.lineEdit_MM.setText (LMM)
        self.ui.checkBox_CheckBoxCliboard.setChecked(self.__FParams.CheckBoxCliboard)
        self.ui.checkBox_CheckBoxAutoDownload.setChecked (self.__FParams.CheckBoxAutoDownload)
        self.ui.checkBox_CheckBoxAutoDelete.setChecked (self.__FParams.CheckBoxAutoDelete)
        self.ui.checkBox_CheckBoxSkipExists.setChecked (self.__FParams.CheckBoxSkipExists)
        self.ui.checkBox_CheckBoxChunk.setChecked (self.__FParams.CheckBoxChunk)
        self.ui.checkBox_CheckBoxStop.setChecked (self.__FParams.CheckBoxStop)
        self.ui.checkBox_CheckBoxDownload.setChecked (self.__FParams.CheckBoxDownload)

        i = self.ui.comboBox_MaxRes.findText(self.__FParams.ComboboxMaxRes)
        self.ui.comboBox_MaxRes.setCurrentIndex(i)

        self.ui.spinBox_NumberThread.setValue(self.__FParams.NumberThread)


    #endfunction
    def CheckSetup (self) -> bool:
        """CheckSetup"""
    #beginfunction
        bPathStore = LUFile.DirectoryExists(self.__FPathStore)
        bPathStoreOut = LUFile.DirectoryExists(self.__FPathStoreOut)
        bPathStoreError = LUFile.DirectoryExists(self.__FPathStoreError)
        bPathYoutubeLoad = LUFile.DirectoryExists(self.__FPathYoutubeLoad)
        LResult: tuple = self.__FMIN_validator.validate(self.__FMIN,0)
        bMIN = LResult [0] == QValidator.State.Acceptable
        LResult: tuple = self.__FHH_validator.validate(self.__FHH,0)
        bHH = LResult [0] == QValidator.State.Acceptable
        LResult: tuple = self.__FDD_validator.validate(self.__FDD,0)
        bDD = LResult [0] == QValidator.State.Acceptable
        LResult: tuple = self.__FDN_validator.validate(self.__FDN,0)
        bDN = LResult [0] == QValidator.State.Acceptable
        LResult: tuple = self.__FMM_validator.validate(self.__FMM,0)
        bMM = LResult [0] == QValidator.State.Acceptable
        bSheduler = bMIN and bHH and bDD and bDN and bMM

        # Проверить self.__FParams.ComboboxMaxRes
        bComboboxMaxRes = True

        # Проверить self.__FParams.NumberThread
        if self.__FParams.NumberThread > 0 and self.__FParams.NumberThread < 6:
            bNumberThread = True
        else:
            bNumberThread = False
        return bPathStore and bPathStoreOut and bPathStoreError and bPathYoutubeLoad and \
               bSheduler and bComboboxMaxRes and bNumberThread
    #endfunction

    def SaveSetup (self):
        """SaveSetup"""
    #beginfunction
        if self.CheckSetup:
            self.__FParams.PathStore = self.ui.lineEdit_PathStore.text()
            self.__FParams.PathStoreOut = self.ui.lineEdit_PathStoreOut.text()
            self.__FParams.PathStoreError = self.ui.lineEdit_PathStoreError.text()
            self.__FParams.PathYoutubeLoad = self.ui.lineEdit_PathYoutubeLoad.text()

            LMIN = self.ui.lineEdit_MIN.text ()
            LHH = self.ui.lineEdit_HH.text ()
            LDD = self.ui.lineEdit_DD.text ()
            LDN = self.ui.lineEdit_DN.text ()
            LMM = self.ui.lineEdit_MM.text ()
            s = LMIN+' '+LHH+' '+LDD+' '+LDN+' '+LMM
            self.__FParams.Sheduler = s

            self.__FParams.CheckBoxCliboard = self.ui.checkBox_CheckBoxCliboard.isChecked()
            self.__FParams.CheckBoxAutoDownload = self.ui.checkBox_CheckBoxAutoDownload.isChecked()
            self.__FParams.CheckBoxAutoDelete = self.ui.checkBox_CheckBoxAutoDelete.isChecked()
            self.__FParams.CheckBoxSkipExists = self.ui.checkBox_CheckBoxSkipExists.isChecked()
            self.__FParams.CheckBoxChunk = self.ui.checkBox_CheckBoxChunk.isChecked ()
            self.__FParams.CheckBoxStop = self.ui.checkBox_CheckBoxStop.isChecked ()
            self.__FParams.CheckBoxDownload = self.ui.checkBox_CheckBoxDownload.isChecked ()

            self.__FParams.ComboboxMaxRes = self.__FMaxRes
            self.__FParams.NumberThread = int(self.ui.spinBox_NumberThread.text())
        #endif
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
