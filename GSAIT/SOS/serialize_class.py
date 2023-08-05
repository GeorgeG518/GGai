from PyQt5.QtWidgets import QWidget
class serialize_class(QWidget):
    def __init__(self, objectName=""):
        super().__init__(objectName=objectName)
        self.serialize=True