from PyQt4 import QtCore, QtGui
from ui_statusbar import statusbar
import sys

class Main(QtGui.QMainWindow):
    def __init__(self, parent = None):
        super(Main, self).__init__(parent)
        self.resize(500, 403)
        self.setMinimumSize(QtCore.QSize(500, 403))
        
        #left pane
        self.scrollLayout = QtGui.QFormLayout()
        self.scrollWidget = QtGui.QWidget()
        self.scrollWidget.setLayout(self.scrollLayout)
        self.leftPane = QtGui.QScrollArea()
        self.leftPane.setWidgetResizable(True)
        self.leftPane.setWidget(self.scrollWidget)
        
        #right pane
        self.rightLayout = QtGui.QVBoxLayout()
        self.rightPane = QtGui.QWidget()
        self.rightPane.setLayout(self.rightLayout)

        self.mainLayout = QtGui.QHBoxLayout()
        #Add panes to main layout
        self.mainLayout.addWidget(self.leftPane)
        self.mainLayout.addWidget(self.rightPane)
        
        self.centralWidget = QtGui.QWidget()
        self.centralWidget.setLayout(self.mainLayout)
        self.setCentralWidget(self.centralWidget)
        self.adddownload()
        
    def adddownload(self):
        self.scrollLayout.addRow(statusbar())

app = QtGui.QApplication(sys.argv)
myWidget = Main()
myWidget.setWindowTitle("top10")
myWidget.show()
myWidget.raise_()
sys.exit(app.exec_())
