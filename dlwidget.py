from PyQt4 import QtCore, QtGui
import scraper
import downloader

class dlwidget(QtGui.QWidget):
    
    def __init__(self, artist, dldir,parent=None):
        super(dlwidget, self).__init__(parent)
        self.progressBar = QtGui.QProgressBar()
        self.status = QtGui.QLabel("Loading...")
        self.cancelbutton = QtGui.QPushButton("Cancel")
        self.cancelbutton.setEnabled(False)
        self.boxLayout = QtGui.QVBoxLayout()
        self.boxLayout.addWidget(self.progressBar)
        self.boxLayout.addWidget(self.status)
        self.boxLayout.addWidget(self.cancelbutton)
        self.box = QtGui.QGroupBox("\""+artist+"\"")
        self.box.setLayout(self.boxLayout)
        
        layout = QtGui.QHBoxLayout()
        layout.addWidget(self.box)
        self.setLayout(layout)
        
        self.thread = Thread(artist,dldir)
        self.connect(self.thread, QtCore.SIGNAL('log(QString)'),self.log)
        self.connect(self.thread, QtCore.SIGNAL('bar(int)'),self.bar)
        self.connect(self.thread, QtCore.SIGNAL('setbox(QString)'),self.setbox)
        self.connect(self.thread, QtCore.SIGNAL('setcancelbutton(bool)'),self.setcancelbutton)
        self.connect(self.thread, QtCore.SIGNAL("finished()"), self.deleteLater)
        self.connect(self.thread, QtCore.SIGNAL("terminated()"), self.deleteLater)
        
        self.cancelbutton.clicked.connect(self.thread.terminate)
        
        self.thread.start()
		
    def log(self,msg):
        self.status.setText(msg)
    def bar(self,val):
        self.progressBar.setValue(val)
    def setbox(self,title):
        self.box.setTitle(title)
    def setcancelbutton(self,val):
        self.cancelbutton.setEnabled(val)
        

class Thread(QtCore.QThread):
    
    def __init__(self,artist,dldir):
        QtCore.QThread.__init__(self)
        self.artist = artist
        self.dldir = dldir
    def __del__(self):
        self.wait()
    
    def run(self):
        self.artist = scraper.getartist(self.artist)
        self.setbox(self.artist['name'])
        tracks = scraper.toptracks(self.artist['id'])
        self.setcancelbutton(True)
        for track in tracks:
            self.log("Downloading "+track['name'])
            urls = downloader.search(track['name']+" "+self.artist['name'])
            for url in urls:
                try:
                    downloader.download(url,self.bar,self.dldir+"/"+self.artist['name']+" - "+track['name']+".mp3")
                except Exception:
                    pass
                break
                
                    
    def log(self,msg):
        self.emit(QtCore.SIGNAL('log(QString)'), msg)
    def bar(self,val):
        self.emit(QtCore.SIGNAL('bar(int)'), val)
    def setbox(self,title):
        self.emit(QtCore.SIGNAL('setbox(QString)'), title)
    def setcancelbutton(self,val):
        self.emit(QtCore.SIGNAL('setcancelbutton(bool)'), val)
