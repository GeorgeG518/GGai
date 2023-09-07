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

    @staticmethod
    def convert_to_dict(gui):
        ret_dict={}
        items={}
        for widget in gui.findChildren(QWidget):
            if isinstance(widget, serialize_class) and widget.serialize:
                for each in widget.children():
                    if isinstance(each, QLabel) :
                        continue
                    if isinstance(each, QComboBox) or isinstance(each, QSpinBox) :
                        items[each.objectName()]=sos_input.get_value(each)
                    elif isinstance(each, QGroupBox) :
                        items[each.objectName()]=sos_input.convert_group_box(each)
                    else:
                        print("yes", each)

        ret_dict[gui.layout().objectName()]=items
        return ret_dict

    @staticmethod
    def convert_group_box(box):
        #for widget in box.findChildren(QWidget):
        ret_dict={}
        print(box.children())
        for widget in box.children():
            if isinstance(widget, QTableView) :
                ret_dict[widget.objectName()]=widget.model()._data
        return ret_dict


    def get_value(gui_element):
        """
        Use multiple dispatch to retrieve the value of the gui element
        """
        if isinstance(gui_element,QComboBox):
            return gui_element.currentText()
        elif isinstance(gui_element, QSpinBox):
            return gui_element.value()