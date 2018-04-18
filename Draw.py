# -*- coding: utf-8 -*-
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from Form import Ui_Form
import sys
import random
class Choose(QWidget,Ui_Form):
    Single_text = pyqtSignal([list])   #自定义信号
    Single_num = pyqtSignal(int)   #自定义信号
    def __init__(self):
        super(Choose,self).__init__()
        self.setWindowTitle("Choose")
        self.lis_word = list()
        self.setupUi(self)
        self.pushButton.clicked.connect(self.get_text)
        self.pushButton_2.clicked.connect(self.timer_start)
        self.Single_text[list].connect(self.widget.window_update)  #信号绑定
        self.Single_num[int].connect(self.widget.num_update)  #信号绑定
    def get_text(self):
        self.lis_word = list()
        self.lis_word.append(self.lineEdit.text().encode('utf-8'))
        self.lis_word.append(self.lineEdit_2.text().encode('utf-8'))
        self.lis_word.append(self.lineEdit_3.text().encode('utf-8'))
        self.lis_word.append(self.lineEdit_4.text().encode('utf-8'))
        self.lis_word.append(self.lineEdit_5.text().encode('utf-8'))
        self.lis_word.append(self.lineEdit_6.text().encode('utf-8'))
        self.lis_word.append(self.lineEdit_7.text().encode('utf-8'))
        self.lis_word.append(self.lineEdit_8.text().encode('utf-8'))
        print len(self.lis_word)
        print self.lis_word
        self.Single_text[list].emit(self.lis_word)
    def timer_start(self):
        self.widget.timer.start(10)
        num = random.randint(100,200)
        self.Single_num[int].emit(num)
if __name__ == "__main__":
    app = QApplication(sys.argv)
    win = Choose()
    win.show()
    app.exec_()
