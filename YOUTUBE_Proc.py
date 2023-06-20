"""
 =======================================================
 Copyright (c) 2023
 Author:
     Lisitsin Y.R.
 Project:
     YouTube_PY
     Python (PROJECTS)
 Module:
     YouTube_Proc.py

 =======================================================
"""

#------------------------------------------
# БИБЛИОТЕКИ python
#------------------------------------------
from pathlib import Path, WindowsPath
from pathlib import WindowsPath

#------------------------------------------
# БИБЛИОТЕКИ сторонние
#------------------------------------------
# from ManageHD import ProcessMovies, Progress, FileManip

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
    QFileDialog, QMessageBox, QInputDialog,
    QListView, QMainWindow, QMenu, QMenuBar, QDialog,
    QPlainTextEdit, QScrollArea, QSizePolicy, QSplitter,
    QStatusBar, QTextEdit, QToolBar, QVBoxLayout,
    QSizePolicy, QPushButton,
    QLineEdit,
    QWidget, QLabel
    )

#------------------------------------------
# БИБЛИОТЕКИ LU
#------------------------------------------
import LUos

#------------------------------------------
# БИБЛИОТЕКИ PROJECT
#------------------------------------------

#------------------------------------------
# CONST
#------------------------------------------
StyleColor_Error = 'color: black; background-color: red'
StyleColor_Ok = 'color: black; background-color: white'

"""
Диалог выбора файлов QFileDialog
-------------------------------------
QFileDialog это диалог, который позволяет пользователям выбирать/сохранять
файлы или папки. Метод getOpenFileName отвечает за открытие файлов/папок.
Методом QFileDialog.getOpenFileName() открываем диалоговое окно выбора файлов/папок.
У метода есть список необязательных параметров 
title - название диалогового окна, directory указывает на показываемую директорию, 
filter_file - фильтрация файлов по расширению. 
Метод возвращает два параметра. 
Первый путь к выбранному файлу, 
а второй логическое значение, зависящее от того, был выбран файл или нет.
"""
def OpenFileDialog (Aparent = None) -> str:
    """OpenFileDialog"""
#beginfunction
    Ltitle = 'Открыть файл'
    Ldirectory = LUos.GetCurrentDir()
    # filter_file = "Word File *doc; *docx"
    Lfilter_file = "INI файл *ini"
    LResult = QFileDialog.getOpenFileName (Aparent, Ltitle, Ldirectory, Lfilter_file)
    Lfile_path = str(WindowsPath (LResult[0]))
    return Lfile_path
#endfunction

"""
Диалог выбора файлов QFileDialog.getExistingDirectory
-------------------------------------
QFileDialog это диалог, который позволяет пользователям выбирать/сохранять
файлы или папки. 
Метод getExistingDirectory отвечает за открытие файлов/папок.
Методом QFileDialog.getOpenFileName() открываем диалоговое окно выбора файлов/папок.
У метода есть список необязательных параметров 
title - название диалогового окна, directory указывает на показываемую директорию, 
Метод возвращает два параметра. 
Первый путь к выбранному файлу, 
а второй логическое значение, зависящее от того, был выбран файл или нет.
"""
def OpenDirectoryDialog (Aparent = None, dir = '') -> str:
    """OpenDirectory"""
#beginfunction
    Lcaption = 'Выбор папки'
    if len(dir) == 0:
        Ldirectory = LUos.GetCurrentDir()
    else:
        Ldirectory = dir
    #endif
    LResult = QFileDialog.getExistingDirectory (parent=Aparent, caption=Lcaption, dir=Ldirectory, options=QFileDialog.Option.ShowDirsOnly)
    # s0 = LResult.replace('/','\\')
    # s1 = Path(LResult)
    # s2 = WindowsPath (LResult)
    Ldirectory_path = str(WindowsPath (LResult))
    return Ldirectory_path
#endfunction

"""
Диалог сохранения файла QFileDialog
-------------------------------------
QFileDialog это диалог, который позволяет пользователям выбирать/сохранять файлы или папки. 
Метод getSaveFileName отвечает за сохранение файлов/папок.
Методом QFileDialog.getSaveFileName() открываем диалоговое окно выбора файлов/папок. 
У метода есть список необязательных параметров 
title - название диалогового окна, directory указывает на показываемую директорию, 
filter_file - фильтрация/сохранение файлов по расширению. 
Метод возвращает два параметра. 
Первый путь к сохраняемому файлу, 
а второй логическое значение, зависящее от того, был сохранен файл или нет.
"""
def SaveFileDialog (Aparent = None) -> str:
    """SaveFileDialog"""
#beginfunction
    Ltitle = 'Открыть файл'
    Ldirectory = LUos.GetCurrentDir()
    # filter_file = "Word File *doc; *docx"
    Lfilter_file = "INI файл *ini"
    LResult = QFileDialog.getSaveFileName (Aparent, Ltitle, Ldirectory, Lfilter_file)
    Lfile_path = str(WindowsPath (LResult[0]))
    return Lfile_path
#endfunction

"""
Диалоги сообщений QMessageBox
-------------------------------------
Окна сообщений обычно используются для объявления небольшой информации пользователю. 
QMessageBox представляет собой диалоговое окно сообщений. 
Окно сообщений можно создать с множеством различных параметров. 
Для удобства работы мы создали функцию в которую передаются необходимые параметры. 
Методом setWindowTitle() задается заголовок окна сообщений, 
setText() - задает основной текст сообщения, 
setIcon - задает тип окна сообщений возможен один из следующих параметров: 
QMessageBox.Information информационное окно, 
QMessageBox.Question сообщение с вопросом, 
QMessageBox.Warning, 
QMessageBox.Critical окно предупреждения, критическое сообщение, 
text_detalic() - дополнительное сообщение пользователю, появляется при нажатии кнопки show detalis.
"""
def MessageBoxDialog(Atext_title: str, Atext_msg: str, Atext_Detailed: str, Aico, Aico_msg):
    """MessageBoxDialog"""
#beginfunction
    msg = QMessageBox ()
    msg.setWindowTitle (Atext_title)
    msg.setText (Atext_msg)
    if not Aico is None:
        msg.setIcon (Aico_msg)
        icon = QIcon ()
        icon.addPixmap (QPixmap (Aico), QIcon.Normal, QIcon.Off)
        msg.setWindowIcon (icon)
    #endif
    if Atext_Detailed != "":
        msg.setDetailedText (Atext_Detailed)
    msg.exec ()
#endfunction
"""
QMessageBox.about
-------------------------------------
"""
def MessageBoxAbout(Aparent = None):
    """MessageBoxAbout"""
#beginfunction
    QMessageBox.about (Aparent, "About ManageHD",
                       "Program written in Python v3.4 \n\n"
                       "ManageHD allows you to select an entire "
                       "directory of HD video files and lower their "
                       "resolution from 1080 HD to 720 HD, in batch. "
                       "It calls the HandBrake Command Line Interface "
                       "(CLI) in order to re-encode each video. \n\nYou must "
                       "have the Handbrake CLI installed to use this "
                       "software. "
                       "The CLI (command line interface) can be downloaded at:\n\n "
                       "     http://handbrake.fr/downloads2.php \n\n"
                       "The average video file at 720 HD "
                       "is generally one fourth to one sixth the size "
                       "of its 1080 HD source file. \n\n"
                       "Coding was done by InfanteLabz. \n\n"
                       "This sofware is released under GPL v3 "
                       "licensing. \n\n Developed on Wing IDE")
#endfunction

"""
Диалоги ввода информации QInputDialog.getText
-------------------------------------
QInputDialog простой удобный диалог для получения информации отт пользователя. 
Введённое значение может быть строкой, числом или пунктом из списка. 
метод QInputDialog.getText() имеет следующие параметры: 
заголовок окна, сообщение внутри окна. 
Диалог возвращает введённый текст и логическое значение. 
Если мы нажимаем кнопку ОК, то логическое значение является правдой.
"""
def InputDialog(Aparent=None, Atitle='', Atext='', Alabel=''):
    """MessageDialog"""
#beginfunction
    Ltext, Lok = QInputDialog.getText (parent = Aparent, title = Atitle, label = Alabel,
                                       echo = None, text = Atext, flags = None,
                                       inputMethodHints = None)

    return Ltext
#endfunction

"""
Диалог выбора цвета QColorDialog
QColorDialog представляет собой диалоговое окно для выбора цвета. 
Методом getColor() вызываем диалоговое окно выбора цвета. Метод возвращает параметры цвета в формате RGBF.
"""

"""
Диалог выбора шрифта QFontDialog
QFontDialog представляет собой диалоговое окно для выбора шрифта. 
Методом getFont() вызываем диалоговое окно выбора шрифта. Метод возвращает два параметра. 
Первый True/False в зависимости от того был ли выбран шрифт или нет, 
второй параметры и название выбранного шрифта.
"""

class QLineEditNoPeriodsOrCommas(QLineEdit):
    """ Subclassing PySide.QtGui.QLineEdit to add field validation ability """
    def __init__(self):
        super(QLineEditNoPeriodsOrCommas, self).__init__()

    def keyPressEvent(self, event): #Override
        keyLeft = 16777234
        keyRight = 16777236
        keyUp = 16777235
        keyDown = 16777237
        keyReturn = 16777220
        if event.key() == Qt.Key_Period:
            pass
        else:
            QLineEdit.keyPressEvent(self, event)
#endclass

class QLineEditIntsOnly(QLineEdit):
    """ Subclassing PySide.QtGui.QLineEdit to add field validation ability """
    def __init__(self):
        super(QLineEditIntsOnly, self).__init__()

    def keyPressEvent(self, event): #Override
        keyLeft = 16777234
        keyRight = 16777236
        keyUp = 16777235
        keyDown = 16777237
        keyReturn = 16777220
        if event.key() == Qt.Key_0 or \
           event.key() == Qt.Key_1 or \
           event.key() == Qt.Key_2 or \
           event.key() == Qt.Key_3 or \
           event.key() == Qt.Key_4 or \
           event.key() == Qt.Key_5 or \
           event.key() == Qt.Key_6 or \
           event.key() == Qt.Key_7 or \
           event.key() == Qt.Key_8 or \
           event.key() == Qt.Key_9 or \
           event.key() == Qt.Key_Backspace or \
           event.key() == Qt.LeftArrow or \
           event.key() == Qt.RightArrow or \
           event.key() == Qt.UpArrow or \
           event.key() == Qt.DownArrow or \
           event.key() == Qt.ArrowCursor or \
           event.key() == keyLeft or \
           event.key() == keyRight or \
           event.key() == keyUp or \
           event.key() == keyDown or \
           event.key() == keyReturn or \
           event.key() == Qt.Key_Delete:
            QLineEdit.keyPressEvent(self, event)
        else:
            pass
#endclass

class QLineEditDirectoriesOnly(QLineEdit):
    """ Subclassing PySide.QtGui.QLineEdit to add field validation ability """
    def __init__(self):
        super(QLineEditDirectoriesOnly, self).__init__()

    def focusOutEvent(self, event): #Override
        if self.text() == '':
            # Progress.statuses['DirectoryChanged'] = True
            QLineEdit.focusOutEvent(self, event)
            return
        # fm = FileManip()
        # if fm.VerifyExists(self.text()) != True:
        #     QMessageBox.warning(self, 'Error',
        #                         "The path you specified cannot be located.\n\n Could not find: \"{}\"".format(self.text()),
        #                         QMessageBox.Ok)
        #     self.setFocus()
        #     return
        # Progress.statuses['DirectoryChanged'] = True
        QLineEdit.focusOutEvent(self, event)
#endclass

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
