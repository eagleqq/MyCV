# -*- coding:utf-8 -*-
__author__ = 'shenjun'
__version__ = 1.0
__date__ = '2020-02-06'

from PyQt5.QtCore import *
import cv2

# 摄像头捕获图片
class CaptureFrameThread(QThread):
    signal_capture_a_frame = pyqtSignal(object)
    signal_failed = pyqtSignal(str)

    def __init__(self, parent=None):
        super(CaptureFrameThread, self).__init__(parent)
        self.work = True
        self.isCanny = False


    def __del__(self):
        self.work = False
        # self.wait()

    def run(self):
        try:
            self.capture = cv2.VideoCapture(0)
            while True:
                if not self.work:
                    if self.capture.isOpened():
                        self.capture.release()
                    break
                success, result_frame = self.capture.read()
                if success:
                    if self.isCanny:
                        image = cv2.cvtColor(result_frame, cv2.COLOR_BGR2GRAY)
                        image1 = cv2.Canny(image, 50, 120)
                        result_frame = cv2.cvtColor(image1, cv2.COLOR_BGR2RGB)
                    self.signal_capture_a_frame.emit(result_frame)
        except Exception as e:
            self.signal_failed.emit(str(e))
            return

