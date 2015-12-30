# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'statusbar.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

class Ui_Statusbar(QtGui.QWidget):
  def __init__( self, parent=None):
        super(Test, self).__init__(parent)
        self.verticalLayout = QtGui.QVBoxLayout()
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.groupBox_4 = QtGui.QGroupBox()
        self.groupBox_4.setMaximumSize(QtCore.QSize(16777215, 60))
        self.groupBox_4.setObjectName(_fromUtf8("groupBox_4"))
        self.groupBox_4.setTitle("Artist: Track (#)")
        self.horizontalLayout_7 = QtGui.QHBoxLayout(self.groupBox_4)
        self.horizontalLayout_7.setObjectName(_fromUtf8("horizontalLayout_7"))
        self.toolButton_7 = QtGui.QToolButton(self.groupBox_4)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8(":/Images/cancel.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.toolButton_7.setIcon(icon)
        self.toolButton_7.setObjectName(_fromUtf8("toolButton_7"))
        self.toolButton_7.setText("...")
        self.horizontalLayout_7.addWidget(self.toolButton_7)
        self.progressBar_6 = QtGui.QProgressBar(self.groupBox_4)
        self.progressBar_6.setProperty("value", 24)
        self.progressBar_6.setObjectName(_fromUtf8("progressBar_6"))
        self.horizontalLayout_7.addWidget(self.progressBar_6)
        self.verticalLayout.addWidget(self.groupBox_4)

        QtCore.QMetaObject.connectSlotsByName(self)
        

import resources_rc
