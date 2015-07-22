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
        QtCore.QObject.connect(self.btn_ac, QtCore.SIGNAL("clicked()"), self.check_state())
        self.check_state()


    def check_state(self):
        if state(26) == '0':
            self.chkbx_26.setChecked(False)
        elif state(26) == '1':
            self.chkbx_26.setChecked(True)
        else:
            pass

        if state(19) == '0':
            self.chkbx_19.setChecked(False)
        elif state(19) == '1':
            self.chkbx_19.setChecked(True)
        else:
            pass

        if state(13) == '0':
            self.chkbx_13.setChecked(False)
        elif state(13) == '1':
            self.chkbx_13.setChecked(True)
        else:
            pass

        if state(6) == '0':
            self.chkbx_06.setChecked(False)
        elif state(6) == '1':
            self.chkbx_06.setChecked(True)
        else:
            pass


    

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
