from PyQt4 import QtCore, QtGui
import scraper
import downloader

class dlwidget(QtGui.QWidget):
    def __init__(self, artistname, parent=None):
        super(dlwidget, self).__init__(parent)
        self.artist = scraper.getartist(artistname)
        self.progressBar = QtGui.QProgressBar()
        self.status = QtGui.QLabel("Loading...")
        self.cancelbutton = QtGui.QPushButton("Cancel")
        self.cancelbutton.clicked.connect(self.cancel)
        
        self.boxLayout = QtGui.QVBoxLayout()
        #add widgets to box
        self.boxLayout.addWidget(self.progressBar)
        self.boxLayout.addWidget(self.status)
        self.boxLayout.addWidget(self.cancelbutton)
        self.box = QtGui.QGroupBox(self.artist['name'])
        self.box.setLayout(self.boxLayout)
        
        layout = QtGui.QHBoxLayout()
        layout.addWidget(self.box)
        self.setLayout(layout)
	
    def cancel(self):
		self.deleteLater()
		
    def log(self,msg):
		self.status.setText(msg)
