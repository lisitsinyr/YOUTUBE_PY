YOUTUBE_PY
----------

YOUTUBE - Программа загрузки с www.youtube.com, youtu.be

Настройки
-------------------
[GENERAL]
; Каталог store
pathstore = D:\!BACKUP
; Каталог out
pathstoreout = D:\WORK

; Каталог error
pathstoreerror = D:\WORK

; Шедуллер
sheduler = 0,5 4,4,4,4 1,3 1-7 1-12

[Youtube]
; Каталог загрузки видео
pathyoutubeload = D:\WORK

; Использовать Clipboard
checkboxcliboard = 1

; Автоматически запускать загрузку
checkboxautodownload = 1

; Автоматически удалять из списка после загрузки
checkboxautodelete = 1

; Пропускать загруженные видео
checkboxskipexists = 1

; Остановить основной цикл программы при старте
checkboxstop = 0

; Использовать прогресс при загрузке видео
checkboxchunk = 1

; Загружать видео (без эмуляции)
checkboxdownload = 1

; Максимальное разрешение видео
comboboxmaxres = 

; Максимальное количество потоков
numberthread = 4

Средство разработки
-------------------
    python 3.11
    PyCharm 2022.2
    QT Creater 9.0.1

Используемые библиотеки
-------------------
БИБЛИОТЕКИ python
    os
    sys
    time
    datetime
    enum

БИБЛИОТЕКИ сторонние
    PySide6 - QT
    pytube

БИБЛИОТЕКА LU
    TOOLS_PY - бизнес библиотека
    LUConsole
    LUConst
    LUDateTime
    LUDecotators
    LUDict
    LUDoc
    LUErrors
    LUFile
    LUFileUtils
    LULog
    LULog
    LUNetwork
    LUNumUtils
    LUObjects
    LUObjectsYou
    LUObjectsYT
    LUos
    LUParserARG
    LUParserINI
    LUParserREG
    LUProc
    LUQThread
    LUQTimer
    LUSheduler
    LUStrDecode
    LUStrUtils
    LUSupport
    LUsys
    LUThread
    LUTimer
    LUVersion
    LUYouTube
