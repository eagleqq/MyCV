from template import ui_threeForm
from PyQt5.QtWidgets import *


class ThreeForm(QWidget, ui_threeForm.Ui_Form):
    def __init__(self):
        super(ThreeForm, self).__init__()
        self.setupUi(self)