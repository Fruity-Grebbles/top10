from PyQt4 import QtCore, QtGui
import scraper
import downloader
from threading import Thread

class dlwidget(QtGui.QWidget):
    
    def __init__(self, artistname, dldir,parent=None):
        super(dlwidget, self).__init__(parent)
        self.artist = artistname
        self.terminated = False
        self.dldir = dldir
        self.progressBar = QtGui.QProgressBar()
        self.status = QtGui.QLabel("Loading...")
        self.cancelbutton = QtGui.QPushButton("Cancel")
        self.cancelbutton.clicked.connect(self.halt)
        self.cancelbutton.setEnabled(False)
        self.boxLayout = QtGui.QVBoxLayout()
        self.boxLayout.addWidget(self.progressBar)
        self.boxLayout.addWidget(self.status)
        self.boxLayout.addWidget(self.cancelbutton)
        self.box = QtGui.QGroupBox("\""+self.artist+"\"")
        self.box.setLayout(self.boxLayout)
        
        layout = QtGui.QHBoxLayout()
        layout.addWidget(self.box)
        self.setLayout(layout)
        
        self.thread = Thread(target=self.gettracks)
        self.thread.start()
		
    def log(self,msg):
        self.status.setText(msg)
        
    def bar(self,val):
        self.progressBar.setValue(val)
    
    def halt(self):
        self.log("Stopping...")
        self.terminated = True
        
    
    def gettracks(self):
        self.artist = scraper.getartist(self.artist)
        self.box.setTitle(self.artist['name'])
        tracks = scraper.toptracks(self.artist['id'])
        self.cancelbutton.setEnabled(True)
        for track in tracks:
            if(self.terminated):
                break
            self.log("Downloading "+track['name'])
            urls = downloader.search(track['name']+" "+self.artist['name'])
            for url in urls:
                if(self.terminated):
                    break
                try:
                    downloader.download(url,self.bar,self.dldir+"/"+self.artist['name']+" - "+track['name']+".mp3")
                    break
                except Exception:
                    raise Exception
        self.deleteLater()
