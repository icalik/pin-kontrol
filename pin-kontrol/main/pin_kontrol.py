# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '../ui/tasarim.ui'
#
# Created: Wed Jul 22 21:02:46 2015
#      by: PyQt4 UI code generator 4.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName(_fromUtf8("Dialog"))
        Dialog.setEnabled(True)
        Dialog.resize(611, 513)
        Dialog.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.verticalLayoutWidget_2 = QtGui.QWidget(Dialog)
        self.verticalLayoutWidget_2.setGeometry(QtCore.QRect(80, 70, 91, 124))
        self.verticalLayoutWidget_2.setObjectName(_fromUtf8("verticalLayoutWidget_2"))
        self.verticalLayout_3 = QtGui.QVBoxLayout(self.verticalLayoutWidget_2)
        self.verticalLayout_3.setMargin(0)
        self.verticalLayout_3.setObjectName(_fromUtf8("verticalLayout_3"))
        self.chkbx_13 = QtGui.QCheckBox(self.verticalLayoutWidget_2)
        self.chkbx_13.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.chkbx_13.setObjectName(_fromUtf8("chkbx_13"))
        self.verticalLayout_3.addWidget(self.chkbx_13)
        self.chkbx_19 = QtGui.QCheckBox(self.verticalLayoutWidget_2)
        self.chkbx_19.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.chkbx_19.setObjectName(_fromUtf8("chkbx_19"))
        self.verticalLayout_3.addWidget(self.chkbx_19)
        self.chkbx_06 = QtGui.QCheckBox(self.verticalLayoutWidget_2)
        self.chkbx_06.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.chkbx_06.setObjectName(_fromUtf8("chkbx_06"))
        self.verticalLayout_3.addWidget(self.chkbx_06)
        self.chkbx_26 = QtGui.QCheckBox(self.verticalLayoutWidget_2)
        self.chkbx_26.setEnabled(True)
        self.chkbx_26.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.chkbx_26.setChecked(False)
        self.chkbx_26.setObjectName(_fromUtf8("chkbx_26"))
        self.verticalLayout_3.addWidget(self.chkbx_26)
        self.btn_ac = QtGui.QPushButton(Dialog)
        self.btn_ac.setGeometry(QtCore.QRect(310, 60, 179, 127))
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Ignored, QtGui.QSizePolicy.Ignored)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_ac.sizePolicy().hasHeightForWidth())
        self.btn_ac.setSizePolicy(sizePolicy)
        self.btn_ac.setObjectName(_fromUtf8("btn_ac"))

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(_translate("Dialog", "Dialog", None))
        self.chkbx_13.setText(_translate("Dialog", "GPIO 13", None))
        self.chkbx_19.setText(_translate("Dialog", "GPIO 19", None))
        self.chkbx_06.setText(_translate("Dialog", "GPIO 6", None))
        self.chkbx_26.setText(_translate("Dialog", "GPIO 26", None))
        self.btn_ac.setText(_translate("Dialog", "UYGULA", None))

