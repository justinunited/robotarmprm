from PyQt5 import QtCore, QtGui, uic,QtWidgets
import sys
import cv2
import numpy as np
import threading
import time
import queue
from serial_coms_list import *

running = False
capture_thread = None
form_class = uic.loadUiType("new_ui.ui")[0]
q = queue.Queue()

from demo1 import *
from top_camera import *
def grab(cam, queue, width, height, fps):
    global running
    capture = cv2.VideoCapture(2)
    capture.set(cv2.CAP_PROP_FRAME_WIDTH, width)
    capture.set(cv2.CAP_PROP_FRAME_HEIGHT, height)
    capture.set(cv2.CAP_PROP_FPS, fps)

    while (running):
        frame = {}
        capture.grab()
        retval, img = capture.retrieve(2)
        frame["img"] = img

        if queue.qsize() < 10:
            queue.put(frame)
        else:
            print
            queue.qsize()


class OwnImageWidget(QtWidgets.QWidget):
    def __init__(self, parent=None):
        super(OwnImageWidget, self).__init__(parent)
        self.image = None

    def setImage(self, image):
        self.image = image
        sz = image.size()
        self.setMinimumSize(sz)
        self.update()

    def paintEvent(self, event):
        qp = QtGui.QPainter()
        qp.begin(self)
        if self.image:
            qp.drawImage(QtCore.QPoint(0, 0), self.image)
        qp.end()


class MyWindowClass(QtWidgets.QMainWindow, form_class):
    def __init__(self, parent=None):
        QtWidgets.QMainWindow.__init__(self, parent)
        self.setupUi(self)
        self.inManual.clicked.connect(self.put_in_manual)
        self.out.clicked.connect(self.put_out)
        self.inAuto.clicked.connect(self.start_clicked)
        global running
        running = True
        capture_thread.start()
        self.window_width = self.ImgWidget.frameSize().width()
        self.window_height = self.ImgWidget.frameSize().height()
        self.ImgWidget = OwnImageWidget(self.ImgWidget)
        self.timer = QtCore.QTimer(self)
        self.timer.timeout.connect(self.update_frame)
        self.timer.start(1)

    def put_in_manual(self):
        print(":: running function put_in_manual")
        # ser = autoConnect(9600, "COM5")
        # setHome(ser)
        if w.posIn.text() == "" or w.nameIn.text() == "" or w.addIn.text() == "" :
            print('error no input')
            self.porlor.setText('Please input again !!!!')
        else:
            nameinput = w.nameIn.text()
            nameinput = nameinput.replace(" ", "")
            addressinput = w.addIn.text()
            addressinput = addressinput.replace(" ", "")
            sizebox = w.sizeIn.text()
            if int(sizebox) not in [0,1]:
                print(sizebox)
                print('size box must be 0 or 1')
                pos = 88
            else:
                pos = add_input(nameinput, addressinput, w.posIn.text())
                print('position shelf : ', pos, 'size box : ', sizebox)
            if pos != 0 and pos!= 99 and pos!= 88:
                # xh, yh, zh, acuteDeg, size_box = camera2()      #test only
                # saveandsent(xh, yh, zh, acuteDeg, pos, size_box, ser)    #test only
                # savesizebox(pos,sizebox)
                if int(pos) == 1:
                    self.label1.setText(w.nameIn.text())
                elif int(pos) == 2:
                    self.label2.setText(w.nameIn.text())
                elif int(pos) == 3:
                    self.label3.setText(w.nameIn.text())
                elif int(pos) == 4:
                    self.label4.setText(w.nameIn.text())
                elif int(pos) == 5:
                    self.label5.setText(w.nameIn.text())
                elif int(pos) == 6:
                    self.label6.setText(w.nameIn.text())
                elif int(pos) == 7:
                    self.label7.setText(w.nameIn.text())
                elif int(pos) == 8:
                    self.label8.setText(w.nameIn.text())
                elif int(pos) == 9:
                    self.label9.setText(w.nameIn.text())
                elif int(pos) == 10:
                    self.label10.setText(w.nameIn.text())
                elif int(pos) == 11:
                    self.label11.setText(w.nameIn.text())
                elif int(pos) == 12:
                    self.label12.setText(w.nameIn.text())
                elif int(pos) == 13:
                    self.label13.setText(w.nameIn.text())
                elif int(pos) == 14:
                    self.label14.setText(w.nameIn.text())
            elif int(pos) == 99:
                print('box not avaliable')
                self.porlor.setText('box not avaliable!!!!')
            elif int(pos) == 0:
                print('same input')
                self.porlor.setText('same input!!!!')
            elif int(pos) == 88:
                self.porlor.setText('size box must be 0 or 1!!!!')


    def put_out(self):
        print(":: running function put_out")
        print(w.nameOut.text())
        if w.nameOut.text() == '' and w.addOut.text() == "":
            print('pls insert name or address')
            self.porlor.setText('pls insert name or address')
        else:
            if w.nameOut.text() == '':
                print('address')
                text = w.addOut.text()
                text.replace(" ", "")
                print(text)
                key = find_key(text, 'address')
            elif w.addOut.text() == "":
                print('name')
                text =w.nameOut.text()
                text.replace(" ", "")
                key = find_key(text,'name')
            else:
                print('name+address')
                print('name')
                text =w.nameOut.text()
                text.replace(" ", "")
                key = find_key(text,'name')
            print(key)
            # pushout(key)
            if int(key) == 1:
                self.label1.setText("")
            elif int(key) == 2:
                self.label2.setText("")
            elif int(key) == 3:
                self.label3.setText("")
            elif int(key) == 4:
                self.label4.setText("")
            elif int(key) == 5:
                self.label5.setText("")
            elif int(key) == 6:
                self.label6.setText("")
            elif int(key) == 7:
                self.label7.setText("")
            elif int(key) == 8:
                self.label8.setText("")
            elif int(key) == 9:
                self.label9.setText("")
            elif int(key) == 10:
                self.label10.setText("")
            elif int(key) == 11:
                self.label11.setText("")
            elif int(key) == 12:
                self.label12.setText("")
            elif int(key) == 13:
                self.label13.setText("")
            elif int(key) == 14:
                self.label14.setText("")


    def replace_text(self,text):
        text = text.replace("ๅ", "า")
        text = text.replace("ฦ", "ภ")
        # print('replace')
        return text


    def start_clicked(self):
        name_pred = []
        address_pred = []
        print(':: running function input auto')
        # frame = q.get()
        frame = q.get()
        num = 1
        img = frame["img"]
        kernel_sharpening = np.array([[-1, -1, -1],[-1, 9, -1],[-1, -1, -1]])
        img = cv2.filter2D(img, -1, kernel_sharpening)
        imgsave = img.copy()
        img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        cv2.imwrite("row" + '.jpg', img)
        h, w = img.shape
        img = img[100:h, 15:w - 50]
        # cv2.imshow('wtfimg', img)
        # cv2.waitKey(0)
        pic = detectrow(img)
        for i in pic:
            try:
                x, y, w, h = i[0], i[1], i[2], i[3]
                row = img[y-7:y+h+7,x-7:x+5+w]
                # cv2.imshow('row',row)
                # cv2.waitKey(0)
                name_pred, address_pred = detectchar(row, num)
                name_pred = self.replace_text(name_pred)
                address_pred = self.replace_text(address_pred)
                num = num+1
            except Exception as e:
                print("type error: " + str(e))
                try:
                    x, y, w, h = i[0], i[1], i[2], i[3]
                    print(x, y, w, h)
                    row = img[y-7:y + h+7, x:x + w]
                    # cv2.imshow('row', row)
                    # cv2.waitKey(0)
                    name_pred, address_pred = detectchar(row, num)
                    num = num + 1
                except:
                    print('error save row')
        print('namepred_list : ' + str(name_pred) + '\naddresspred_list : ' + str(address_pred))
        pos = add_input(name_pred, address_pred, 'random')
        print(" Box will keep in position : ",pos)
        # xh, yh, zh, acuteDeg,size_box = camera2()
        # print(xh, yh, zh, acuteDeg,pos)
        # saveandsent(xh, yh, zh, acuteDeg,str(pos),size_box)
        namepred_list.clear()
        addresspred_list.clear()
        if int(pos) == 1:
            self.label1.setText(name_pred)
        elif int(pos) == 2:
            self.label2.setText(name_pred)
        elif int(pos) == 3:
            self.label3.setText(name_pred)
        elif int(pos) == 4:
            self.label4.setText(name_pred)
        elif int(pos) == 5:
            self.label5.setText(name_pred)
        elif int(pos) == 6:
            self.label6.setText(name_pred)
        elif int(pos) == 7:
            self.label7.setText(name_pred)
        elif int(pos) == 8:
            self.label8.setText(name_pred)
        elif int(pos) == 9:
            self.label9.setText(name_pred)
        elif int(pos) == 10:
            self.label10.setText(name_pred)
        elif int(pos) == 11:
            self.label11.setText(name_pred)
        elif int(pos) == 12:
            self.label12.setText(name_pred)
        elif int(pos) == 13:
            self.label13.setText(name_pred)
        elif int(pos) == 14:
            self.label14.setText(name_pred)


    def update_frame(self):
        if not q.empty():
            frame = q.get()
            img = frame["img"]
            img_height, img_width, img_colors = img.shape
            scale_w = float(self.window_width) / float(img_width)
            scale_h = float(self.window_height) / float(img_height)
            scale = min([scale_w, scale_h])
            if scale == 0:
                scale = 1
            img = cv2.resize(img, None, fx=scale, fy=scale, interpolation=cv2.INTER_CUBIC)
            img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
            height, width, bpc = img.shape
            bpl = bpc * width
            image = QtGui.QImage(img.data, width, height, bpl, QtGui.QImage.Format_RGB888)
            self.ImgWidget.setImage(image)

    def closeEvent(self, event):
        global running
        running = False


capture_thread = threading.Thread(target=grab, args=(0, q, 640, 480, 30))

app = QtWidgets.QApplication(sys.argv)
w = MyWindowClass(None)
w.setWindowTitle('Sukimoo_ui')
w.show()
app.exec_()