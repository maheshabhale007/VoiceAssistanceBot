from gui import Ui_MainWindow
import siri
from PyQt5 import QtCore, QtWidgets, QtGui
from PyQt5.QtGui import QMovie
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtCore import Qt, QTimer,QTime,  QDate
import sys

class MainThread(QThread):
    def __init__(self):
        super(MainThread,self).__init__()

    def run(self):
        self.Task_Gui()

    def Task_Gui(self):
        siri.Taskexec()

startFunction = MainThread()
#To start GUI
class GuiStart(QMainWindow):
    def __init__(self):
        super().__init__()
        self.BotUi = Ui_MainWindow()
        self.BotUi.setupUi(self)
        self.BotUi.start.clicked.connect(self.startFunc)
        self.BotUi.exit.clicked.connect(self.close)
        
    # For starting the BOT
    def startFunc(self):
        self.BotUi.movies = QtGui.QMovie("1.gif")
        self.BotUi.gif1.setMovie(self.BotUi.movies)
        self.BotUi.movies.start()

        self.BotUi.movies1 = QtGui.QMovie("initial.gif")
        self.BotUi.initial.setMovie(self.BotUi.movies1)
        self.BotUi.movies1.start()

        timer = QTimer()
        timer.timeout.connect(self.showtime)
        timer.start(1000)
        startFunction.start()
    # For displaying Time
    def showtime(self):
        c_t = QTime.currentTime() 
        l_t = c_t.toString("hh:mm:ss")

        labbel = "Time:" + l_t 
        self.BotUi.time.setText(labbel)
        

Gui_App = QApplication(sys.argv)
Gui_Bot = GuiStart()
Gui_Bot.show()
exit(Gui_App.exec_())       




        

        