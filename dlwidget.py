from PyQt4 import QtCore, QtGui
import scraper

class dlwidget(QtGui.QWidget):
  def __init__(self, artist, parent=None):
        super(dlwidget, self).__init__(parent)
        
        self.progressBar = QtGui.QProgressBar()
        self.status = QtGui.QLabel("Searching...")
        self.cancelbutton = QtGui.QPushButton("Cancel")
        self.cancelbutton.clicked.connect(self.deleteLater)
        
        
        self.boxLayout = QtGui.QVBoxLayout()
        #add widgets to box
        self.boxLayout.addWidget(self.progressBar)
        self.boxLayout.addWidget(self.status)
        self.boxLayout.addWidget(self.cancelbutton)
        self.box = QtGui.QGroupBox(artist)
        self.box.setLayout(self.boxLayout)
        
        layout = QtGui.QHBoxLayout()
        layout.addWidget(self.box)
        self.setLayout(layout)
