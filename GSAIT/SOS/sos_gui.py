import PyQt5
from PyQt5 import QtCore
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton,QHBoxLayout, QLabel,QComboBox, QLineEdit,QGroupBox,QSpinBox, QTableView
from PyQt5.QtCore import Qt
import sys

import pandas as pd
from collections import OrderedDict

class sos_gui(QWidget):
    def __init__(self):
        super().__init__()
        self.title = "SOS Input File GUI"
        self.main_layout=None
        self.control_variable_count=3 
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
        self.rows.append(control_variable_widget(self.control_variable_count))
        print(self.rows)

    def parse_inputs(self):

        for each in self.rows:
            if isinstance(each, row):
                print(each.dict_repr)
                print(each.widget)

class control_variable_widget(QWidget):
    def __init__(self, count):
        super().__init__()
        main=QVBoxLayout()
        self.control_var_spinner=row("Control Variable Count",QSpinBox(),dict_repr="num_control_vars",data=count)
        self.INITIAL_COUNT=count
        self.control_var_spinner.widget.valueChanged.connect(self.control_var_spinner_changed)
        main.addWidget(self.control_var_spinner)
        self.cvbox = QGroupBox("Control Variables")
        main.addWidget(self.cvbox)
        cvboxlayout=QVBoxLayout()

        self.table = QTableView()
        self.model = control_variable_table(count)
        self.table.setModel(self.model)
        cvboxlayout.addWidget(self.table)
        self.cvbox.setLayout(cvboxlayout)
        self.setLayout(main)

    def control_var_spinner_changed(self):
        print(self.control_var_spinner.widget.value())
        if self.control_var_spinner.widget.value() < self.INITIAL_COUNT:
            print("DO A WINDOW HERE TO CONFIRM THE CHANGE BECAUSE THEY'LL LOSE DATA")


class row(QWidget):
    """
    Abstract class that represents a label + some sort of widget
    """
    def __init__(self, labeltxt, widget, dict_repr=[""], data=None):
        super().__init__()
        self.leftandright = QHBoxLayout()
        self.label = QLabel(self)
        self.label.setText(labeltxt)
        self.widget = widget
        self.dict_repr = dict_repr if isinstance(dict_repr,list) else [dict_repr]

        self.leftandright.addWidget(self.label)
        if isinstance(data,list):
            self.set_choices(self.widget,data)
        elif isinstance(data,int):
            self.widget.setMinimum(1)
            self.widget.setValue(data)

        self.leftandright.addWidget(self.widget)
        self.setLayout(self.leftandright)

    def set_choices(self, each, items):
        each.addItems(items)

class control_variable_table(QtCore.QAbstractTableModel):
    def __init__(self,count,data=[]):
        super(control_variable_table, self).__init__()
        self.cols=["Name", "Min", "Initial Value", "Max"] # wont change
        self.numcvs=count
        self.INITIAL_NUMCVS=count
        data=self._construct_table(data)
        self._data = data

    def _construct_table(self,data):
        rows=[f"CV{i}:" for i in range(self.numcvs)]
        if data==[]:
            for i in range(self.numcvs):
                data.append([f"CV{i}"]+[0]*3)
        print(data)
        return pd.DataFrame(data, columns=self.cols, index=rows)

    def flags(self, index):
        return Qt.ItemIsSelectable|Qt.ItemIsEnabled|Qt.ItemIsEditable

    def data(self, index, role):
        if role == Qt.DisplayRole:
            value = self._data.iloc[index.row(), index.column()]
            return str(value)
        
    def setData(self, index, value, role):
        if role == Qt.EditRole:
            self._data.iloc[index.row(),index.column()] = value
            return True    
        
    def rowCount(self, index):
        # The length of the outer list.
        return self._data.shape[0]

    def columnCount(self, index):
        # The following takes the first sub-list, and returns
        # the length (only works if all rows are an equal length)
        return self._data.shape[1]
    
    def headerData(self, section, orientation, role):
        # section is the index of the column/row.
        if role == Qt.DisplayRole:
            if orientation == Qt.Horizontal:
                return str(self._data.columns[section])
            if orientation == Qt.Vertical:
                return str(self._data.index[section])     

if __name__=='__main__':
    app = QApplication(sys.argv)
    ex = sos_gui()
    sys.exit(app.exec_())