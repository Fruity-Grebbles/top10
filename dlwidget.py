from PyQt4 import QtCore, QtGui
import scraper
import downloader
from threading import Thread

class dlwidget(QtGui.QWidget):
    def __init__(self, artistname, parent=None):
        super(dlwidget, self).__init__(parent)
        self.artist = scraper.getartist(artistname)
        self.progressBar = QtGui.QProgressBar()
        self.status = QtGui.QLabel("Loading...")
        self.cancelbutton = QtGui.QPushButton("Cancel")
        self.cancelbutton.clicked.connect(self.cease)
        
        self.boxLayout = QtGui.QVBoxLayout()
        self.boxLayout.addWidget(self.progressBar)
        self.boxLayout.addWidget(self.status)
        self.boxLayout.addWidget(self.cancelbutton)
        self.box = QtGui.QGroupBox(self.artist['name'])
        self.box.setLayout(self.boxLayout)
        
        layout = QtGui.QHBoxLayout()
        layout.addWidget(self.box)
        self.setLayout(layout)
        
        self.thread = Thread(target=self.gettracks)
        self.thread.start()
        
    def cease(self):
		self.deleteLater()
		
    def log(self,msg):
        self.status.setText(msg)
        print msg
        
    def bar(self,val):
        self.progressBar.setValue(val)
    
    def gettracks(self):
        tracks = scraper.toptracks(self.artist['id'])
        for track in tracks:
            self.log("Downloading "+track['name'])
            urls = downloader.search(track['name'])
            for url in urls:
                try:
                    downloader.download(url,self.bar)
                    break
                except Exception:
                    pass
        self.cease()
