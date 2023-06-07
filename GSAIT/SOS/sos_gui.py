import PyQt5
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton,QHBoxLayout, \
QLabel,QComboBox, QLineEdit,QGroupBox,QSpinBox 
import sys

class sos_gui(QWidget):
    def __init__(self):
        super().__init__()
        self.title = "SOS Input File GUI"
        self.main_layout=None
        self.control_variable_count=1
        self.createLayout()
        self.startUI()

    def createLayout(self):
        self.main_layout = QVBoxLayout()
        self.write_input=QPushButton("Write Input File")
        self.make_rows()
        [self.main_layout.addWidget(x) for x in self.rows]

        self.main_layout.addWidget(self.write_input)
        self.setLayout(self.main_layout)
        self.parse_inputs()

    def startUI(self):
        self.setWindowTitle(self.title)
        self.show()

    def make_rows(self):
        self.rows=[]
        self.rows.append(row("Optimization Algorithm", QComboBox() ,
                        dict_repr="optimization_method", 
                        data=["Gradient Descent","Simulated Annealing", "Random Walk"]))
        self.rows.append(row("Gradient Method", QComboBox() ,
                        dict_repr="gradient_method", 
                        data=["Standard","Custom"]))
        # Need a handle on this
        self.control_var_spinner=row("Control Variable Count",QSpinBox(),dict_repr="num_control_vars",data=self.control_variable_count)
        self.rows.append(self.control_var_spinner)
        self.rows.append(control_variable_widget(self.control_variable_count))
        print(self.rows)

    def parse_inputs(self):
        for each in self.rows:
            if isinstance(each, row):
                print(each.dict_repr)
                for each_widget in each.widget:
                    print(each_widget)

class control_variable_widget(QWidget):
    def __init__(self, count):
        super().__init__()
        main=QVBoxLayout()
        self.cvbox = QGroupBox("Control Variables")
        main.addWidget(self.cvbox)
        self.vstack=QVBoxLayout()
        for i in range(count):
            self.vstack.addWidget(row(f"CV{i}:", [QLineEdit(), QLineEdit()]))
        self.cvbox.setLayout(self.vstack)

        self.setLayout(main)

class row(QWidget):
    """
    Abstract class that represents a label + some sort of widget
    """
    def __init__(self, labeltxt, widget, dict_repr=[""], data=None):
        super().__init__()
        self.leftandright = QHBoxLayout()
        self.label = QLabel(self)
        self.label.setText(labeltxt)
        self.widget = widget if isinstance(widget,list) else [widget]
        self.dict_repr = dict_repr if isinstance(dict_repr,list) else [dict_repr]

        self.leftandright.addWidget(self.label)
        for each in self.widget:
            if isinstance(data,list):
                self.set_choices(each,data)
            elif isinstance(data,int):
                each.setMinimum(1)
                each.setMaximum(data)

            self.leftandright.addWidget(each)
        self.setLayout(self.leftandright)

    def set_choices(self, each, items):
        each.addItems(items)



if __name__=='__main__':
    app = QApplication(sys.argv)
    ex = sos_gui()
    sys.exit(app.exec_())