from PyQt5 import QtCore
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton,QHBoxLayout, QLabel,QComboBox, \
    QLineEdit,QGroupBox,QSpinBox, QTableView, QLayout
from PyQt5.QtCore import Qt
from serialize_class import serialize_class

class sos_input():
    def __init__(self):
        from sos_gui import serialize_class
        sos_input.sos_dict = {}
        sos_input.EPSILON = 1e-8
        sos_input.ITERMAX = 100_000 # Confession: I learned how to do this on tiktok
        sos_input.STEPSIZE = 0.001
        sos_input.METHOD="gradient-descent"
        sos_input.CONSTRAINED=True
    
    def read(self, filename):
        pass

    
    def convert_to_dict(self,gui):
        ret_dict={}
        for each in gui.findChildren(QWidget):
            if isinstance(each, serialize_class) and each.serialize: 
                print(each)
                print("yesy",each.layout())
                ret_dict[gui.layout().objectName()]=self.convert_to_dict(each)
            elif isinstance(each, QComboBox) or isinstance(each, QSpinBox) or isinstance(each,QTableView):
                print(f"{str(each.objectName())}: {sos_input.get_value(each)}")
                ret_dict[each.objectName()]=sos_input.get_value(each)
        return ret_dict

    def get_value(gui_element):
        """
        Use multiple dispatch to retrieve the value of the gui element
        """
        if isinstance(gui_element,QComboBox):
            return gui_element.currentText()
        elif isinstance(gui_element, QSpinBox):
            return gui_element.value()