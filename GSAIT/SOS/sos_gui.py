import PyQt5
from PyQt5.QtWidgets import QApplication, QWidget
import sys

class sos_gui(QWidget):
    def __init__(self):
        super().__init__(self)




if __name__=='__main__':
    app = QApplication(sys.argv)
    ex = sos_gui()
    sys.exit(app.exec_())