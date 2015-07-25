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
        QtCore.QObject.connect(self.btn_bilgi, QtCore.SIGNAL("clicked()"), self.about)
        QtCore.QObject.connect(self.btn_kapat, QtCore.SIGNAL("clicked()"), self.close)
        self.check_state() # init oldugunda calis
        self.set_disable()
        self.setFixedSize(462, 396) #Boyut

    def about(self):
        QtGui.QMessageBox.information(self, u"Hakkinda", u"Ismet Said Calik <ismetsaid.calik@pardus.net.tr>\nErdogan Bilgici <destek@linuxcozumleri.com>")

    def set_disable(self):
        self.chkbxs_3v3_1.setEnabled(False)
        self.chkbxs_3v3_2.setEnabled(False)
        self.chkbxs_G1.setEnabled(False)
        self.chkbxs_G2.setEnabled(False)
        self.chkbxs_G3.setEnabled(False)
        self.chkbxs_SD.setEnabled(False)

        self.chkbxa_5v_1.setEnabled(False)
        self.chkbxa_5v_2.setEnabled(False)
        self.chkbxa_G1.setEnabled(False)
        self.chkbxa_G2.setEnabled(False)
        self.chkbxa_G3.setEnabled(False)
        self.chkbxa_G4.setEnabled(False)
        self.chkbxa_G5.setEnabled(False)
        self.chkbxa_SC.setEnabled(False)

        #GPIO 16 ACT LED

        self.chkbxa_16.setEnabled(False)

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

        if state(14) == '0':
            self.chkbxa_14.setChecked(False)
        elif state(14) == '1':
            self.chkbxa_14.setChecked(True)
        else:
            pass

        if state(15) == '0':
            self.chkbxa_15.setChecked(False)
        elif state(15) == '1':
            self.chkbxa_15.setChecked(True)
        else:
            pass

        if state(18) == '0':
            self.chkbxa_18.setChecked(False)
        elif state(18) == '1':
            self.chkbxa_18.setChecked(True)
        else:
            pass

        if state(23) == '0':
            self.chkbxa_23.setChecked(False)
        elif state(23) == '1':
            self.chkbxa_23.setChecked(True)
        else:
            pass

        if state(24) == '0':
            self.chkbxa_24.setChecked(False)
        elif state(24) == '1':
            self.chkbxa_24.setChecked(True)
        else:
            pass

        if state(25) == '0':
            self.chkbxa_25.setChecked(False)
        elif state(25) == '1':
            self.chkbxa_25.setChecked(True)
        else:
            pass

        if state(8) == '0':
            self.chkbxa_08.setChecked(False)
        elif state(8) == '1':
            self.chkbxa_08.setChecked(True)
        else:
            pass

        if state(7) == '0':
            self.chkbxa_07.setChecked(False)
        elif state(7) == '1':
            self.chkbxa_07.setChecked(True)
        else:
            pass

        if state(12) == '0':
            self.chkbxa_12.setChecked(False)
        elif state(12) == '1':
            self.chkbxa_12.setChecked(True)
        else:
            pass
        """
        if state(16) == '0':
            self.chkbxa_16.setChecked(False)
        elif state(16) == '1':
            self.chkbxa_16.setChecked(True)
        else:
            pass
        """
        if state(20) == '0':
            self.chkbxa_20.setChecked(False)
        elif state(20) == '1':
            self.chkbxa_20.setChecked(True)
        else:
            pass

        if state(21) == '0':
            self.chkbxa_21.setChecked(False)
        elif state(21) == '1':
            self.chkbxa_21.setChecked(True)
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

        #SAG

        if self.chkbxa_14.isChecked():
        	switch(14,1)
        elif self.chkbxa_14.isChecked() == False:
        	switch(14,0)

        if self.chkbxa_15.isChecked():
        	switch(15,1)
        elif self.chkbxa_15.isChecked() == False:
        	switch(15,0)

        if self.chkbxa_18.isChecked():
        	switch(18,1)
        elif self.chkbxa_18.isChecked() == False:
        	switch(18,0)

        if self.chkbxa_23.isChecked():
        	switch(23,1)
        elif self.chkbxa_23.isChecked() == False:
        	switch(23,0)

        if self.chkbxa_24.isChecked():
        	switch(24,1)
        elif self.chkbxa_24.isChecked() == False:
        	switch(24,0)

        if self.chkbxa_25.isChecked():
        	switch(25,1)
        elif self.chkbxa_25.isChecked() == False:
        	switch(25,0)

        if self.chkbxa_08.isChecked():
        	switch(8,1)
        elif self.chkbxa_08.isChecked() == False:
        	switch(8,0)

        if self.chkbxa_07.isChecked():
        	switch(7,1)
        elif self.chkbxa_07.isChecked() == False:
        	switch(7,0)

        if self.chkbxa_12.isChecked():
        	switch(12,1)
        elif self.chkbxa_12.isChecked() == False:
        	switch(12,0)

        if self.chkbxa_16.isChecked():
        	switch(16,1)
        elif self.chkbxa_16.isChecked() == False:
        	switch(16,0)

        if self.chkbxa_20.isChecked():
        	switch(20,1)
        elif self.chkbxa_20.isChecked() == False:
        	switch(20,0)

        if self.chkbxa_21.isChecked():
        	switch(21,1)
        elif self.chkbxa_21.isChecked() == False:
        	switch(21,0)

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
