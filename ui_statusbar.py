from PyQt4 import QtCore, QtGui

class statusbar(QtGui.QWidget):
  def __init__(self, artist, parent=None):
        super(statusbar, self).__init__(parent)
        
        self.progressBar = QtGui.QProgressBar()
        self.track = QtGui.QLabel("Downloading TRACK (1/10)")
        
        self.boxLayout = QtGui.QVBoxLayout()
        self.boxLayout.addWidget(self.progressBar)
        self.boxLayout.addWidget(self.track)
        self.box = QtGui.QGroupBox(artist)
        self.box.setLayout(self.boxLayout)
        
        layout = QtGui.QHBoxLayout()
        layout.addWidget(self.box)
        self.setLayout(layout)
