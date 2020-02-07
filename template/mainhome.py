from template import ui_mainhome
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
import sys

from template import oneForm, twoForm, threeForm

class MainHome(QMainWindow, ui_mainhome.Ui_MainWindow):
    def __init__(self):
        super(MainHome, self).__init__()
        self.setupUi(self)
        self.setWindowModality(Qt.ApplicationModal)
        self.setFixedSize(self.width(), self.height())
        self.menubar.setNativeMenuBar(False)  # 不同平台
        self.qsl = QStackedLayout(self.frame_right)
        oneform = oneForm.OneForm()
        towform = twoForm.TwoForm()
        threeform = threeForm.ThreeForm()
        self.qsl.addWidget(oneform)
        self.qsl.addWidget(towform)
        self.qsl.addWidget(threeform)

        self.pushButton_one.clicked.connect(self.show_form)
        self.pushButton_two.clicked.connect(self.show_form)
        self.pushButton_three.clicked.connect(self.show_form)

    def show_form(self):
        dic = {
            "pushButton_one": 0,
            "pushButton_two": 1,
            "pushButton_three": 2,
        }
        index = dic[self.sender().objectName()]
        self.qsl.setCurrentIndex(index)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    mainwin = MainHome()
    mainwin.show()
    sys.exit(app.exec_())