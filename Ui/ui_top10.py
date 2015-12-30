# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'top10.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui
from ui_statusbar import Ui_Statusbar

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

class Ui_MainWindow(object):	
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(500, 403)
        MainWindow.setMinimumSize(QtCore.QSize(500, 403))
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.gridLayout = QtGui.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.scrollLayout = QtGui.QFormLayout()
        self.scrollWidget = QtGui.QWidget()
        self.scrollWidget.setLayout(self.scrollLayout)
        self.scrollArea = QtGui.QScrollArea(self.centralwidget)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName(_fromUtf8("scrollArea"))
        self.scrollArea.setWidget(self.scrollWidget)
        self.scrollAreaWidgetContents = QtGui.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 232, 379))
        self.scrollAreaWidgetContents.setObjectName(_fromUtf8("scrollAreaWidgetContents"))
        self.verticalLayout_7 = QtGui.QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout_7.setObjectName(_fromUtf8("verticalLayout_7"))
        spacerItem = QtGui.QSpacerItem(20, 358, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout_7.addItem(spacerItem)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.horizontalLayout.addWidget(self.scrollArea)
        self.gridLayout.addLayout(self.horizontalLayout, 0, 0, 1, 1)
        self.verticalLayout = QtGui.QVBoxLayout()
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.groupBox = QtGui.QGroupBox(self.centralwidget)
        self.groupBox.setObjectName(_fromUtf8("groupBox"))
        self.verticalLayout_2 = QtGui.QVBoxLayout(self.groupBox)
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.artistentry = QtGui.QLineEdit(self.groupBox)
        self.artistentry.setObjectName(_fromUtf8("artistentry"))
        self.verticalLayout_2.addWidget(self.artistentry)
        self.verifybox = QtGui.QCheckBox(self.groupBox)
        self.verifybox.setObjectName(_fromUtf8("verifybox"))
        self.verticalLayout_2.addWidget(self.verifybox)
        self.dlbutton = QtGui.QPushButton(self.groupBox)
        self.dlbutton.setObjectName(_fromUtf8("dlbutton"))
        self.dlbutton.clicked.connect(self.adddownload)
        self.verticalLayout_2.addWidget(self.dlbutton)
        self.verticalLayout.addWidget(self.groupBox)
        self.groupBox_2 = QtGui.QGroupBox(self.centralwidget)
        self.groupBox_2.setObjectName(_fromUtf8("groupBox_2"))
        self.verticalLayout_3 = QtGui.QVBoxLayout(self.groupBox_2)
        self.verticalLayout_3.setObjectName(_fromUtf8("verticalLayout_3"))
        self.dllocation = QtGui.QLineEdit(self.groupBox_2)
        self.dllocation.setEnabled(False)
        self.dllocation.setFocusPolicy(QtCore.Qt.NoFocus)
        self.dllocation.setAutoFillBackground(False)
        self.dllocation.setFrame(True)
        self.dllocation.setEchoMode(QtGui.QLineEdit.Normal)
        self.dllocation.setReadOnly(True)
        self.dllocation.setObjectName(_fromUtf8("dllocation"))
        self.verticalLayout_3.addWidget(self.dllocation)
        self.dirbutton = QtGui.QToolButton(self.groupBox_2)
        self.dirbutton.setObjectName(_fromUtf8("dirbutton"))
        self.verticalLayout_3.addWidget(self.dirbutton)
        self.verticalLayout.addWidget(self.groupBox_2)
        self.groupBox_3 = QtGui.QGroupBox(self.centralwidget)
        self.groupBox_3.setObjectName(_fromUtf8("groupBox_3"))
        self.gridLayout_2 = QtGui.QGridLayout(self.groupBox_3)
        self.gridLayout_2.setObjectName(_fromUtf8("gridLayout_2"))
        self.label = QtGui.QLabel(self.groupBox_3)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        self.label.setTextFormat(QtCore.Qt.RichText)
        self.label.setScaledContents(False)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setWordWrap(True)
        self.label.setObjectName(_fromUtf8("label"))
        self.gridLayout_2.addWidget(self.label, 0, 0, 1, 2)
        self.verticalLayout.addWidget(self.groupBox_3)
        self.gridLayout.addLayout(self.verticalLayout, 0, 3, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow", None))
        self.groupBox.setTitle(_translate("MainWindow", "Enter an artist", None))
        self.artistentry.setPlaceholderText(_translate("MainWindow", "Artist", None))
        self.verifybox.setText(_translate("MainWindow", "Verify downloaded tracks", None))
        self.dlbutton.setText(_translate("MainWindow", "Start Download", None))
        self.groupBox_2.setTitle(_translate("MainWindow", "Download location", None))
        self.dirbutton.setText(_translate("MainWindow", "Change", None))
        self.groupBox_3.setTitle(_translate("MainWindow", "NOTICE:", None))
        self.label.setText(_translate("MainWindow", "This software is intended to be used for obtaining media in the public domain. Should you intentionally or inadvertantly download any file to which you are not legally entitled, delete it immediately.", None))
		
    	
    def adddownload(self):
        self.scrollLayout.addRow(Ui_Statusbar())
        
import resources_rc
