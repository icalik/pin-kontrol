__author__ = 'iscalik'

# !/usr/share/bin/python
# -*- coding: utf-8 -*-
# Author: Ismet Said Calik
# Author Mail : ismetsaid.calik@gmail.com

from PyQt4 import QtCore, QtGui
from pin_kontrol import Ui_Dialog
from pin import switch
from state import *

import sys


class MainWindow(QtGui.QMainWindow, Ui_Dialog):
    def __init__(self):
        QtGui.QMainWindow.__init__(self)
        self.setupUi(self)
        QtCore.QObject.connect(self.btn_uygula, QtCore.SIGNAL("clicked()"), self.apply) #Butona tiklandiginda self.apply yordamini cagir
        self.check_state() # init oldugunda calis

    def check_state(self): #Pin durum kontrol ve pine gore checkbox checked durumu

        if state(2) == '0':
            self.chkbxs_02.setChecked(False)
        elif state(2) == '1':
            self.chkbxs_02.setChecked(True)
        else:
            pass

        if state(3) == '0':
            self.chkbxs_03.setChecked(False)
        elif state(3) == '1':
            self.chkbxs_03.setChecked(True)
        else:
            pass

        if state(4) == '0':
            self.chkbxs_04.setChecked(False)
        elif state(4) == '1':
            self.chkbxs_04.setChecked(True)
        else:
            pass

        if state(17) == '0':
            self.chkbxs_17.setChecked(False)
        elif state(17) == '1':
            self.chkbxs_17.setChecked(True)
        else:
            pass

        if state(27) == '0':
            self.chkbxs_27.setChecked(False)
        elif state(27) == '1':
            self.chkbxs_27.setChecked(True)
        else:
            pass

        if state(22) == '0':
            self.chkbxs_22.setChecked(False)
        elif state(22) == '1':
            self.chkbxs_22.setChecked(True)
        else:
            pass

        if state(10) == '0':
            self.chkbxs_10.setChecked(False)
        elif state(10) == '1':
            self.chkbxs_10.setChecked(True)
        else:
            pass

        if state(9) == '0':
            self.chkbxs_09.setChecked(False)
        elif state(9) == '1':
            self.chkbxs_09.setChecked(True)
        else:
            pass

        if state(11) == '0':
            self.chkbxs_11.setChecked(False)
        elif state(11) == '1':
            self.chkbxs_11.setChecked(True)
        else:
            pass

        if state(5) == '0':
            self.chkbxs_05.setChecked(False)
        elif state(5) == '1':
            self.chkbxs_05.setChecked(True)
        else:
            pass

        if state(6) == '0':
            self.chkbxs_06.setChecked(False)
        elif state(6) == '1':
            self.chkbxs_06.setChecked(True)
        else:
            pass

        if state(13) == '0':
            self.chkbxs_13.setChecked(False)
        elif state(13) == '1':
            self.chkbxs_13.setChecked(True)
        else:
            pass

        if state(19) == '0':
            self.chkbxs_19.setChecked(False)
        elif state(19) == '1':
            self.chkbxs_19.setChecked(True)
        else:
            pass

        if state(26) == '0':
            self.chkbxs_26.setChecked(False)
        elif state(26) == '1':
            self.chkbxs_26.setChecked(True)
        else:
            pass



    def apply(self):
        if self.chkbxs_02.isChecked():
        	switch(2,1)
        elif self.chkbxs_02.isChecked() == False:
        	switch(2,0)

        if self.chkbxs_03.isChecked():
        	switch(3,1)
        elif self.chkbxs_03.isChecked() == False:
        	switch(3,0)

        if self.chkbxs_04.isChecked():
        	switch(4,1)
        elif self.chkbxs_04.isChecked() == False:
        	switch(4,0)

        if self.chkbxs_17.isChecked():
        	switch(17,1)
        elif self.chkbxs_17.isChecked() == False:
        	switch(17,0)

        if self.chkbxs_27.isChecked():
        	switch(27,1)
        elif self.chkbxs_27.isChecked() == False:
        	switch(27,0)

        if self.chkbxs_22.isChecked():
        	switch(22,1)
        elif self.chkbxs_22.isChecked() == False:
        	switch(22,0)

        if self.chkbxs_10.isChecked():
        	switch(10,1)
        elif self.chkbxs_10.isChecked() == False:
        	switch(10,0)

        if self.chkbxs_09.isChecked():
        	switch(9,1)
        elif self.chkbxs_09.isChecked() == False:
        	switch(9,0)

        if self.chkbxs_11.isChecked():
        	switch(11,1)
        elif self.chkbxs_11.isChecked() == False:
        	switch(11,0)

        if self.chkbxs_05.isChecked():
        	switch(5,1)
        elif self.chkbxs_05.isChecked() == False:
        	switch(5,0)

        if self.chkbxs_06.isChecked():
        	switch(6,1)
        elif self.chkbxs_06.isChecked() == False:
        	switch(6,0)

        if self.chkbxs_13.isChecked():
        	switch(13,1)
        elif self.chkbxs_13.isChecked() == False:
        	switch(13,0)

        if self.chkbxs_19.isChecked():
        	switch(19,1)
        elif self.chkbxs_19.isChecked() == False:
        	switch(19,0)

        if self.chkbxs_26.isChecked():
        	switch(26,1)
        elif self.chkbxs_26.isChecked() == False:
        	switch(26,0)



    def app(self):
        screen = QtGui.QDesktopWidget().screenGeometry()
        size = self.geometry()
        self.move((screen.width() - size.width()) / 2, (screen.height() - size.height()) / 2)


def main():
    app = QtGui.QApplication(sys.argv)
    mw = MainWindow()
    mw.app()
    mw.show()
    return app.exec_()


if __name__ == '__main__':
    main()
