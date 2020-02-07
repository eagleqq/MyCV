from template import ui_oneForm
from PyQt5.QtWidgets import *


class OneForm(QWidget, ui_oneForm.Ui_Form):
    def __init__(self):
        super(OneForm, self).__init__()
        self.setupUi(self)
