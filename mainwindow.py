from PyQt4 import QtCore, QtGui
from dlwidget import dlwidget
import sys, os

class Main(QtGui.QMainWindow):
    def __init__(self, parent = None):
        super(Main, self).__init__(parent)
        
        self.dldir = os.path.dirname(os.path.realpath(__file__))
        
        self.resize(550, 403)
        
        #left pane
        self.scrollLayout = QtGui.QFormLayout()
        self.scrollWidget = QtGui.QWidget()
        self.scrollWidget.setLayout(self.scrollLayout)
        self.leftPane = QtGui.QScrollArea()
        self.leftPane.setWidgetResizable(True)
        self.leftPane.setWidget(self.scrollWidget)
        
        #entry box
        self.entryLayout = QtGui.QVBoxLayout()
        #entryfield
        self.entryfield = QtGui.QLineEdit();
        self.entryfield.setPlaceholderText("Artist")
        #download button
        self.dlbutton = QtGui.QPushButton("Download Top 10 Tracks")
        self.dlbutton.clicked.connect(self.adddownload)
        #add widgets to entry box
        self.entryLayout.addWidget(self.entryfield)
        self.entryLayout.addWidget(self.dlbutton)
        self.entryBox = QtGui.QGroupBox("Enter an Artist")
        self.entryBox.setLayout(self.entryLayout)

        #directory box
        self.dirLayout = QtGui.QVBoxLayout()
        #directory button
        self.dirbutton = QtGui.QPushButton("Change")
        self.dirbutton.clicked.connect(self.changedldir)
        #directory field
        self.dirfield = QtGui.QLineEdit();
        self.dirfield.setReadOnly(True)
        self.dirfield.setEnabled(False)
        self.dirfield.setText(self.dldir)
        #add widgets to directory box
        self.dirLayout.addWidget(self.dirfield)
        self.dirLayout.addWidget(self.dirbutton)
        self.dirBox = QtGui.QGroupBox("Download Location")
        self.dirBox.setLayout(self.dirLayout)
        
        #right pane
        self.rightLayout = QtGui.QVBoxLayout()
        #add widgets to right pane
        self.rightLayout.addWidget(self.entryBox)
        self.rightLayout.addWidget(self.dirBox)
        self.rightPane = QtGui.QWidget()
        self.rightPane.setLayout(self.rightLayout)

        self.mainLayout = QtGui.QHBoxLayout()
        #add panes to main layout
        self.mainLayout.addWidget(self.leftPane)
        self.mainLayout.addWidget(self.rightPane)
        self.centralWidget = QtGui.QWidget()
        self.centralWidget.setLayout(self.mainLayout)
        self.setCentralWidget(self.centralWidget)
        
    def adddownload(self):
        if not str(self.entryfield.text()).isspace() and not str(self.entryfield.text())=="":
            self.scrollLayout.addRow(dlwidget(str(self.entryfield.text())))

    def changedldir(self):
        olddldir = self.dldir
        self.dldir = str(QtGui.QFileDialog.getExistingDirectory(self, "Select Output Directory"))
        if(not self.dldir or self.dldir==""):
            self.dldir=olddldir
        self.dirfield.setText(self.dldir)

app = QtGui.QApplication(sys.argv)
myWidget = Main()
myWidget.setWindowTitle("Top 10")
myWidget.show()
myWidget.raise_()
sys.exit(app.exec_())
