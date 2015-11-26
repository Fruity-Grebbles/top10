import sys
import os
from PyQt4.QtGui import QApplication, QDialog
from PyQt4 import QtGui, QtCore
from ui_top10 import Ui_widget
from functions import top

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

if __name__ == '__main__':

    app = QApplication(sys.argv)
    window = QDialog()
    window.setWindowTitle(_translate("widget", "Top Ten Tracks", None))
    ui = Ui_widget(window)
    window.show()
    window.raise_()
    sys.exit(app.exec_())


