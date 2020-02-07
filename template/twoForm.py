from template import ui_twoForm
from PyQt5.QtWidgets import *


class TwoForm(QWidget, ui_twoForm.Ui_Form):
    def __init__(self):
        super(TwoForm, self).__init__()
        self.setupUi(self)