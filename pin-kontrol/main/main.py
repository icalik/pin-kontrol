__author__ = 'iscalik'

#!/usr/share/bin/python
# -*- coding: utf-8 -*-
# Author: Ismet Said Calik
# Author Mail : ismetsaid.calik@gmail.com

from PyQt4 import QtCore, QtGui
from pin_kontrol import Ui_Dialog
from pin import switch
from state import state



import sys
class MainWindow(QtGui.QMainWindow, Ui_Dialog):
    def __init__(self):
        QtGui.QMainWindow.__init__(self)
        self.setupUi(self)
        QtCore.QObject.connect(self.pushButton, QtCore.SIGNAL("clicked()"), self.stateOn)
        QtCore.QObject.connect(self.pushButton_2, QtCore.SIGNAL("clicked()"), self.stateOff)
    def stateOn(self):
        switch(13,1)
    def stateOff(self):
        switch(13,0)
    def app(self):
        screen = QtGui.QDesktopWidget().screenGeometry()
        size = self.geometry()
        self.move((screen.width()-size.width())/2, (screen.height()-size.height())/2)

def main():
    app = QtGui.QApplication(sys.argv)
    mw = MainWindow()
    mw.app()
    mw.show()
    return app.exec_()
if __name__ == '__main__':
    main()