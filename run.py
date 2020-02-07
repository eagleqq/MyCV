from ui import ui_camera
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
import sys
import cv2
import threading
import os
import time


from src.mythreads import CaptureFrameThread

class Camera(QMainWindow, ui_camera.Ui_MainWindow):
    def __init__(self):
        super(Camera, self).__init__()
        self.setupUi(self)
        self.setWindowModality(Qt.ApplicationModal)
        self.setFixedSize(self.width(), self.height())
        self.menubar.setNativeMenuBar(False)  # 不同平台

        # 变量
        self.isClose = False    # 关闭
        self.isTake = False     # 拍照
        self.canny_max = 0
        self.canny_min = 0

        # 信号槽函
        self.pushButton_open.clicked.connect(self.btnOpenCamera)
        self.pushButton_close.clicked.connect(self.btnCloseCamera)
        self.pushButton_takephoto.clicked.connect(self.btnTakePhoto)
        self.pushButton_savePic.clicked.connect(self.btnSavePic)

        self.checkBox_canny_use.stateChanged.connect(self.activateCanny)
        self.horizontalSlider_canny_max.valueChanged.connect(self.setCannyMaxValue)
        self.horizontalSlider_canny_min.valueChanged.connect(self.setCannyMinValue)

        # 初始化
        self.ui_init()

    def ui_init(self):
        self.horizontalSlider_canny_max.setEnabled(False)
        self.horizontalSlider_canny_min.setEnabled(False)

    ################################################################################################
    # 边缘检测相关函数
    def activateCanny(self):
        if self.checkBox_canny_use.isChecked():
            print("激活")
            self.horizontalSlider_canny_max.setEnabled(True)
            self.horizontalSlider_canny_min.setEnabled(True)
            self.horizontalSlider_canny_max.setValue(100)
            self.horizontalSlider_canny_min.setValue(100)
        else:
            print("不激活")
            self.horizontalSlider_canny_max.setEnabled(False)
            self.horizontalSlider_canny_min.setEnabled(False)
            self.horizontalSlider_canny_max.setValue(0)
            self.horizontalSlider_canny_min.setValue(0)

    def setCannyMaxValue(self):
        self.canny_max = self.horizontalSlider_canny_max.value()
        print(self.canny_min, self.canny_max)
        self.refreshCanny()

    def setCannyMinValue(self):
        self.canny_min = self.horizontalSlider_canny_min.value()
        print(self.canny_min, self.canny_max)
        self.refreshCanny()

    def refreshCanny(self):
        image = cv2.cvtColor(self.tempLabelFrame, cv2.COLOR_BGR2GRAY)   # bug修复：一定要先灰度处理
        edges = cv2.Canny(image, self.canny_min, self.canny_max)
        edges = cv2.cvtColor(edges, cv2.COLOR_BGR2RGB)  # bug修复：再转为RGB
        Img = QImage(edges.data, edges.shape[1],edges.shape[0], QImage.Format_RGB888)
        self.label_image.setPixmap(QPixmap.fromImage(Img))

    ################################################################################################
    # 打开摄像头
    def btnOpenCamera(self):
        self.captureFrameThread = CaptureFrameThread()
        self.captureFrameThread.signal_capture_a_frame.connect(self.slot_capture_a_frame)
        self.captureFrameThread.start()

    # 关闭摄像头呀
    def btnCloseCamera(self):
        if self.captureFrameThread.isRunning():
            self.captureFrameThread.work = False

    # captureFrameThread槽函数：显示图片
    def slot_capture_a_frame(self, result_frame):
        self.recv_current_frame = result_frame
        result_frame = cv2.cvtColor(result_frame, cv2.COLOR_BGR2RGB)
        img = QImage(result_frame.data, result_frame.shape[1],
                     result_frame.shape[0], QImage.Format_RGB888)
        self.label_camera.setPixmap(QPixmap.fromImage(img))

    # 拍照
    def btnTakePhoto(self):
        self.tempLabelFrame = self.recv_current_frame
        RGBframe = cv2.cvtColor(self.tempLabelFrame, cv2.COLOR_BGR2RGB)
        self.tempLabelImg = QImage(RGBframe.data, RGBframe.shape[1],
                     RGBframe.shape[0], QImage.Format_RGB888)
        self.label_image.setPixmap(QPixmap.fromImage(self.tempLabelImg))
        self.label_imageSize.setText("W:" + str(self.recv_current_frame.shape[1]) +
                                     "\t H:" + str(self.recv_current_frame.shape[0]))


    ################################################################################################
    # 保存图片
    def btnSavePic(self):
        ctime = time.strftime('Taking pictures %Y-%m-%d %H:%M:%S', time.localtime(time.time()))
        self.cwd = os.getcwd()
        fileName_choose, filetype = QFileDialog.getSaveFileName(self,"图片保存", self.cwd,  # 起始路径
                                                                "Files (*.jpg)")
        if fileName_choose == "":
            print("取消选择")
            return
        print("你选择要保存的文件为:",fileName_choose)
        print("文件筛选器类型: ", filetype)
        self.tempLabelImg.save(fileName_choose)


    # else:
    #     reply = QMessageBox.information(self, '提示', '', QMessageBox.Ok | QMessageBox.Close,
    #                                     QMessageBox.Close)
    #     if reply == QMessageBox.Ok:
    #         pass

    def closeEvent(self, QCloseEvent):
        try:
            if self.captureFrameThread.isRunning():
                self.captureFrameThread.work = False
        except Exception as e:
            pass
        self.close()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    mainwin = Camera()
    mainwin.show()
    sys.exit(app.exec_())
