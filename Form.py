# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Form.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!
import random
from PyQt5 import QtCore, QtGui, QtWidgets
class ChooseWidget(QtWidgets.QWidget):
    def __init__(self,Form):
        super(ChooseWidget,self).__init__()
        self.text_lis = list()
        self.angle = 0
        self.angle_add = 1
        self.timer = QtCore.QTimer(self)
        self.timer.timeout.connect(self.pointer_update)
    def pointer_update(self):            #更新指针的位置
        if self.angle_add <= self.num:
            self.angle = self.angle+13    #每次转13度
            self.update()
            self.angle_add = self.angle_add+1
        else:
            self.angle = self.angle % 360
            self.angle_add = 1
            self.timer.stop()
    def num_update(self,num):     #更新随机的值，这个值决定了指针的转的位置
        self.num = num
    def window_update(self,lis):  #更新转盘中的内容
        self.text_lis = list()
        self.text_lis = lis
        self.update()
    def paintEvent(self, event):
        painter = QtGui.QPainter(self)
        painter.setRenderHint(QtGui.QPainter.Antialiasing ,True)    #去锯齿
        pm = QtGui.QPixmap("./IMG/ZP2.png")

        pointer = [QtCore.QPointF(-2,0),QtCore.QPointF(2,0),QtCore.QPointF(0,-150)]  #定义指针的多边形的坐标

        side = min(self.width(), self.height())
        painter.setViewport((self.width() - side) / 2, (self.height() - side) / 2,
                            side, side)  #设置绘图区域的位置
        painter.setWindow(0,0,493,493)  #设置绘图区域的坐标系统
        painter.drawPixmap(0 , 0 , pm)   #添加转盘的图片
        trans = QtGui.QTransform()
        if len(self.text_lis) == 8:
            font = QtGui.QFont("宋体",20)
            fm = QtGui.QFontMetrics(font)
            fr = fm.boundingRect("qqqqqqqqqqqqqqqqqq") #得到一个矩形区域的大小，根据字体和字数来定义
            fr.moveCenter(QtCore.QPoint(120, 0))  #将矩形的中心点的坐标移到（120,0）的位置
            trans.translate(246,246)
            trans.rotate(22)
            painter.setTransform(trans)  #旋转坐标系
            painter.setFont(font)
            painter.drawText(QtCore.QRectF(fr), QtCore.Qt.AlignHCenter | QtCore.Qt.AlignTop, self.text_lis[0])  #以点（120,0）处为中心写入内容）
            for i in range(1,8):    #循环旋转坐标写入内容
                trans.rotate(45)
                painter.setTransform(trans)
                painter.setFont(font)
                painter.drawText(QtCore.QRectF(fr), QtCore.Qt.AlignHCenter | QtCore.Qt.AlignTop, self.text_lis[i])
        trans.reset()  #坐标重置，还原成setwindows时的坐标系，也就是说没经过一个转换的时候的坐标系
        trans.translate(246, 246)
        trans.rotate(self.angle)
        painter.setTransform(trans)
        painter.setBrush(QtGui.QBrush(QtCore.Qt.darkBlue))
        painter.drawPolygon(QtGui.QPolygonF(pointer))    #画上指针
        print

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(1305, 719)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(Form)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        # self.widget = QtWidgets.QWidget(Form)
        self.widget = ChooseWidget(Form)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.widget.sizePolicy().hasHeightForWidth())
        self.widget.setSizePolicy(sizePolicy)
        self.widget.setObjectName("widget")
        self.verticalLayout.addWidget(self.widget)
        spacerItem = QtWidgets.QSpacerItem(108, 18, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.verticalLayout.addItem(spacerItem)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem1 = QtWidgets.QSpacerItem(108, 18, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem1)
        self.pushButton_2 = QtWidgets.QPushButton(Form)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_2.sizePolicy().hasHeightForWidth())
        self.pushButton_2.setSizePolicy(sizePolicy)
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_2.setMinimumSize(QtCore.QSize(64, 64))
        self.pushButton_2.setMaximumSize(QtCore.QSize(64, 64))
        self.pushButton_2.setStyleSheet("#pushButton_2{background-image:url(./Img/start.png);}")
        self.horizontalLayout.addWidget(self.pushButton_2)
        spacerItem2 = QtWidgets.QSpacerItem(138, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem2)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.horizontalLayout_2.addLayout(self.verticalLayout)
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.lineEdit = QtWidgets.QLineEdit(Form)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lineEdit.sizePolicy().hasHeightForWidth())
        self.lineEdit.setSizePolicy(sizePolicy)
        self.lineEdit.setObjectName("lineEdit")
        self.gridLayout.addWidget(self.lineEdit, 0, 0, 1, 1)
        self.lineEdit_2 = QtWidgets.QLineEdit(Form)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lineEdit_2.sizePolicy().hasHeightForWidth())
        self.lineEdit_2.setSizePolicy(sizePolicy)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.gridLayout.addWidget(self.lineEdit_2, 1, 0, 1, 1)
        self.lineEdit_3 = QtWidgets.QLineEdit(Form)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lineEdit_3.sizePolicy().hasHeightForWidth())
        self.lineEdit_3.setSizePolicy(sizePolicy)
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.gridLayout.addWidget(self.lineEdit_3, 2, 0, 1, 1)
        self.lineEdit_4 = QtWidgets.QLineEdit(Form)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lineEdit_4.sizePolicy().hasHeightForWidth())
        self.lineEdit_4.setSizePolicy(sizePolicy)
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.gridLayout.addWidget(self.lineEdit_4, 3, 0, 1, 1)
        self.lineEdit_5 = QtWidgets.QLineEdit(Form)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lineEdit_5.sizePolicy().hasHeightForWidth())
        self.lineEdit_5.setSizePolicy(sizePolicy)
        self.lineEdit_5.setObjectName("lineEdit_5")
        self.gridLayout.addWidget(self.lineEdit_5, 4, 0, 1, 1)
        self.lineEdit_7 = QtWidgets.QLineEdit(Form)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lineEdit_7.sizePolicy().hasHeightForWidth())
        self.lineEdit_7.setSizePolicy(sizePolicy)
        self.lineEdit_7.setObjectName("lineEdit_7")
        self.gridLayout.addWidget(self.lineEdit_7, 5, 0, 1, 1)
        self.lineEdit_6 = QtWidgets.QLineEdit(Form)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lineEdit_6.sizePolicy().hasHeightForWidth())
        self.lineEdit_6.setSizePolicy(sizePolicy)
        self.lineEdit_6.setObjectName("lineEdit_6")
        self.gridLayout.addWidget(self.lineEdit_6, 6, 0, 1, 1)
        self.lineEdit_8 = QtWidgets.QLineEdit(Form)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lineEdit_8.sizePolicy().hasHeightForWidth())
        self.lineEdit_8.setSizePolicy(sizePolicy)
        self.lineEdit_8.setObjectName("lineEdit_8")
        self.gridLayout.addWidget(self.lineEdit_8, 7, 0, 1, 1)
        self.pushButton = QtWidgets.QPushButton(Form)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton.sizePolicy().hasHeightForWidth())
        self.pushButton.setSizePolicy(sizePolicy)
        self.pushButton.setMinimumSize(QtCore.QSize(67, 67))
        self.pushButton.setMaximumSize(QtCore.QSize(67, 67))
        self.pushButton.setObjectName("pushButton")
        style = '''
            #pushButton{background-image:url('./IMG/edit1.png');}
            #pushButton:hover{background-image:url('./IMG/edit2.png');}
            #pushButton:pressed{background-image:url('./IMG/edit3.png');}
        '''
        self.pushButton.setStyleSheet(style)
        self.gridLayout.addWidget(self.pushButton, 8, 0, 1, 1)
        self.horizontalLayout_2.addLayout(self.gridLayout)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        # self.pushButton_2.setText(_translate("Form", "PushButton"))
        # self.pushButton.setText(_translate("Form", "PushButton"))

