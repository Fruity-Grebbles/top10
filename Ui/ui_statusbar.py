from PyQt4 import QtCore, QtGui

class statusbar(QtGui.QWidget):
  def __init__( self, parent=None):
        super(statusbar, self).__init__(parent)
        self.progressBar = QtGui.QProgressBar()
        
        layout = QtGui.QHBoxLayout()
        layout.addWidget(self.progressBar)
        self.setLayout(layout)
