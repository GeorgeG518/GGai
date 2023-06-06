import PyQt5
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton,QHBoxLayout, \
QLabel,QComboBox, QLineEdit
import sys

class sos_gui(QWidget):
    def __init__(self):
        super().__init__()
        self.title = "SOS Input File GUI"
        self.main_layout=None
        self.createLayout()
        self.startUI()

    def createLayout(self):
        self.main_layout = QVBoxLayout()
        self.write_input=QPushButton("Write Input File")
        self.rowtest=row("Testing", QLineEdit())
        self.main_layout.addWidget(self.rowtest)
        self.main_layout.addWidget(self.write_input)
        self.setLayout(self.main_layout)

    def startUI(self):
        self.setWindowTitle(self.title)
        self.show()

class row(QWidget):
    def __init__(self, labeltxt, widget, dict_repr=""):
        super().__init__()
        self.leftandright = QHBoxLayout()
        self.label = QLabel(self)
        self.label.setText(labeltxt)
        self.widget = widget
        self.leftandright.addWidget(self.label)
        self.leftandright.addWidget(self.widget)
        self.setLayout(self.leftandright)

    def set_choices(self, list):
        self.widget.addChoices(list)



if __name__=='__main__':
    app = QApplication(sys.argv)
    ex = sos_gui()
    sys.exit(app.exec_())