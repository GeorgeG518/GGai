import PyQt5
from PyQt5 import QtCore
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton,QHBoxLayout, QLabel,QComboBox, QLineEdit,QGroupBox,QSpinBox, QTableView
from PyQt5.QtCore import Qt
import sys

import pandas as pd
from collections import OrderedDict
from sos_input import sos_input
from serialize_class import serialize_class

class sos_gui(serialize_class):
    def __init__(self):
        super().__init__(objectName="SOS_input")
        self.title = "SOS Input File GUI"
        self.optimization_methods=["Gradient-Ascent","Simulated Annealing", "Random Walk"]
        self.main_layout=None
        self.control_variable_count=3 
        self.createLayout()
        self.startUI()

    def createLayout(self):
        self.main_layout = QVBoxLayout(objectName="solver_settings")
        self.write_input=QPushButton("Write Input File")
        self.write_input.clicked.connect(self.serialize_gui)
        self.make_rows()
        [self.main_layout.addWidget(x) for x in self.rows]

        self.main_layout.addWidget(self.write_input)
        self.setLayout(self.main_layout)

    def startUI(self):
        self.setWindowTitle(self.title)
        self.show()

    def make_rows(self):
        self.rows=[]
        self.rows.append(row("Optimization Algorithm", QComboBox(objectName="optimization_method"), 
                        data=self.optimization_methods))
        self.rows.append(row("Gradient Method", QComboBox(objectName="gradient_method") ,
                        data=["Standard","Custom"]))     
        # Need a handle on this
        self.rows.append(control_variable_widget(self.control_variable_count))

    def serialize_gui(self):
        dickt=sos_input.convert_to_dict(self)
        print(dickt)
class control_variable_widget(serialize_class):
    def __init__(self, count):
        super().__init__(objectName="control_variables")
        main=QVBoxLayout()
        self.control_var_spinner=row("Control Variable Count",QSpinBox(objectName="num_control_vars"),data=count)
        self.control_var_spinner.widget.valueChanged.connect(self.control_var_spinner_changed)
        main.addWidget(self.control_var_spinner)
        self.cvbox = QGroupBox("Control Variables", objectName="controls")
        main.addWidget(self.cvbox)
        cvboxlayout=QVBoxLayout()

        self.table = QTableView(objectName="control_vars")
        self.model = control_variable_table(count)

        self.table.setModel(self.model)
        cvboxlayout.addWidget(self.table)
        self.cvbox.setLayout(cvboxlayout)
        self.setLayout(main)

    def control_var_spinner_changed(self):
        print(self.control_var_spinner.widget.value())
        self.table.setModel(control_variable_table(self.control_var_spinner.widget.value()))

class row(serialize_class):
    """
    Abstract class that represents a label + some sort of widget
    """
    def __init__(self, labeltxt, widget, dict_repr=[""], data=None):
        super().__init__(objectName=widget.objectName())
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
class control_variable_table(QtCore.QAbstractTableModel, serialize_class):
    def __init__(self,count,data=[]):
        super(control_variable_table, self).__init__(objectName="table")
        self.rows=["Name", "Min", "Initial Value", "Max"] # wont change

        self.INITIAL_NUMCVS=count

        if not hasattr(self,'df'):
            control_variable_table.numcvs=count
            cols=[f"CV{i}" for i in range(self.numcvs)]
            control_variable_table.df=pd.DataFrame(0, columns=cols, index=self.rows)
            for each in cols:
                control_variable_table.df.loc['Name',each]=each
            self._data = control_variable_table.df # this is the allocated pandas df, not necessarily the one being shown
        else:
            showdf=self._update_table(count)
            self._data=showdf 

    def _update_table(self,count):
        retdf=control_variable_table.df
        if count > control_variable_table.numcvs:
            newcols=[f"CV{control_variable_table.numcvs+i}" for i in range(count-control_variable_table.numcvs)]
            print(newcols)
            for i,each in enumerate(newcols):
                retdf[each]=[f"CV{control_variable_table.numcvs+i}",0,0,0]
            control_variable_table.numcvs=count
        elif count < control_variable_table.numcvs:
            # lose data here

            colstoret=[f"CV{i}" for i in range(count)]

            retdf=retdf[colstoret]    
  
        return retdf

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