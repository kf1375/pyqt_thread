# !/usr/bin/env

# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'qtGUI.ui'

# Created by: PyQt4 UI code generator 4.11.4

# WARNING! All changes made in this file will be lost!


from PyQt4 import QtCore, QtGui
import sys

import time
from PyQt4.QtCore import QThread

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class worker(QtCore.QThread):
    def __init__(self):
        super(worker, self).__init__()
        self.ok_to_send = False
        self.terminated = True
    def run(self):
        while not self.terminated:
            if self.ok_to_send:
                self.send_message()
            time.sleep(1)

    def start_send(self):
        while True: 
            self.ok_to_send = True
            print 'Shahab <3'

    def pause_send():
        self.ok_to_send = False

    def terminated():
        self.terminated = False




class Ui_MainWindow(object):

    worker = worker()
    worker.start()
    worker.start_send()

    # self.obj = worker.Worker()  # no parent!
    # self.thread = QThread()  # no parent!





    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(853, 439)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.gridLayout = QtGui.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.label_15 = QtGui.QLabel(self.centralwidget)
        self.label_15.setObjectName(_fromUtf8("label_15"))
        self.gridLayout.addWidget(self.label_15, 4, 6, 1, 1)
        self.progressBar_2 = QtGui.QProgressBar(self.centralwidget)
        self.progressBar_2.setProperty("value", 24)
        self.progressBar_2.setObjectName(_fromUtf8("progressBar_2"))
        self.gridLayout.addWidget(self.progressBar_2, 3, 8, 1, 1)
        self.label_13 = QtGui.QLabel(self.centralwidget)
        self.label_13.setObjectName(_fromUtf8("label_13"))
        self.gridLayout.addWidget(self.label_13, 0, 6, 1, 1)
        self.label_9 = QtGui.QLabel(self.centralwidget)
        self.label_9.setObjectName(_fromUtf8("label_9"))
        self.gridLayout.addWidget(self.label_9, 0, 4, 1, 1)
        self.progressBar_3 = QtGui.QProgressBar(self.centralwidget)
        self.progressBar_3.setProperty("value", 24)
        self.progressBar_3.setObjectName(_fromUtf8("progressBar_3"))
        self.gridLayout.addWidget(self.progressBar_3, 4, 8, 1, 1)
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem, 0, 5, 1, 1)
        self.label_4 = QtGui.QLabel(self.centralwidget)
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.gridLayout.addWidget(self.label_4, 5, 0, 1, 1)
        self.label_3 = QtGui.QLabel(self.centralwidget)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.gridLayout.addWidget(self.label_3, 4, 0, 1, 1)
        self.progressBar = QtGui.QProgressBar(self.centralwidget)
        self.progressBar.setProperty("value", 24)
        self.progressBar.setObjectName(_fromUtf8("progressBar"))
        self.gridLayout.addWidget(self.progressBar, 0, 8, 1, 1)
        self.label_8 = QtGui.QLabel(self.centralwidget)
        self.label_8.setObjectName(_fromUtf8("label_8"))
        self.gridLayout.addWidget(self.label_8, 5, 2, 1, 1)
        self.label_10 = QtGui.QLabel(self.centralwidget)
        self.label_10.setObjectName(_fromUtf8("label_10"))
        self.gridLayout.addWidget(self.label_10, 3, 4, 1, 1)
        self.label_11 = QtGui.QLabel(self.centralwidget)
        self.label_11.setObjectName(_fromUtf8("label_11"))
        self.gridLayout.addWidget(self.label_11, 4, 4, 1, 1)
        self.label_1 = QtGui.QLabel(self.centralwidget)
        self.label_1.setObjectName(_fromUtf8("label_1"))
        self.gridLayout.addWidget(self.label_1, 0, 0, 1, 1)
        self.label_2 = QtGui.QLabel(self.centralwidget)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.gridLayout.addWidget(self.label_2, 3, 0, 1, 1)
        self.label_5 = QtGui.QLabel(self.centralwidget)
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.gridLayout.addWidget(self.label_5, 0, 2, 1, 1)
        self.label_12 = QtGui.QLabel(self.centralwidget)
        self.label_12.setObjectName(_fromUtf8("label_12"))
        self.gridLayout.addWidget(self.label_12, 5, 4, 1, 1)
        self.label_7 = QtGui.QLabel(self.centralwidget)
        self.label_7.setObjectName(_fromUtf8("label_7"))
        self.gridLayout.addWidget(self.label_7, 4, 2, 1, 1)
        self.Send = QtGui.QPushButton(self.centralwidget)
        self.Send.setObjectName(_fromUtf8("Send"))
        self.gridLayout.addWidget(self.Send, 7, 8, 1, 1)
        self.label_6 = QtGui.QLabel(self.centralwidget)
        self.label_6.setObjectName(_fromUtf8("label_6"))
        self.gridLayout.addWidget(self.label_6, 3, 2, 1, 1)
        self.progressBar_4 = QtGui.QProgressBar(self.centralwidget)
        self.progressBar_4.setProperty("value", 24)
        self.progressBar_4.setObjectName(_fromUtf8("progressBar_4"))
        self.gridLayout.addWidget(self.progressBar_4, 5, 8, 1, 1)
        self.label_16 = QtGui.QLabel(self.centralwidget)
        self.label_16.setObjectName(_fromUtf8("label_16"))
        self.gridLayout.addWidget(self.label_16, 5, 6, 1, 1)
        spacerItem1 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem1, 0, 1, 1, 1)
        spacerItem2 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem2, 0, 3, 1, 1)
        self.label_14 = QtGui.QLabel(self.centralwidget)
        self.label_14.setObjectName(_fromUtf8("label_14"))
        self.gridLayout.addWidget(self.label_14, 3, 6, 1, 1)
        spacerItem3 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem3, 6, 2, 1, 1)
        spacerItem4 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem4, 0, 7, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 853, 26))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)
        


        # self.Send.clicked.connect(self.obj)
        # self.obj.moveToThread(self.thread)
        # self.thread.start()




        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):

        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow", None))
        self.label_1.setText(_translate("MainWindow", "TempBm_1", None))
        self.label_2.setText(_translate("MainWindow", "TempBm_2", None))
        self.label_3.setText(_translate("MainWindow", "TempBm_3", None))
        self.label_4.setText(_translate("MainWindow", "TempBm_4", None))
        self.label_5.setText(_translate("MainWindow", "TextLabel", None))
        self.label_6.setText(_translate("MainWindow", "TextLabel", None))
        self.label_7.setText(_translate("MainWindow", "TextLabel", None))
        self.label_8.setText(_translate("MainWindow", "TextLabel", None))
        self.label_9.setText(_translate("MainWindow", "Voltage BM_1", None))
        self.label_10.setText(_translate("MainWindow", "Voltage BM_2", None))
        self.label_11.setText(_translate("MainWindow", "Voltage BM_3", None))
        self.label_12.setText(_translate("MainWindow", "Voltage BM_4", None))
        self.label_13.setText(_translate("MainWindow", "TextLabel", None))
        self.label_14.setText(_translate("MainWindow", "TextLabel", None))
        self.label_15.setText(_translate("MainWindow", "TextLabel", None))
        self.label_16.setText(_translate("MainWindow", "TextLabel", None))
        self.Send.setText(_translate("MainWindow", "Send", None))

    #     self.Exit.clicked.connect(self.Exitmod)
    # def Exitmod(self):
        

    # def show_message(self):
    
    #         self.label_1.setText("1")
    #     while 1 :
    #         QtGui.QApplication.processEvents()    
    #         print "aa"   
        
                
        

    
# def main():
   # myform=Ui_MainWindow()
    
    # app = QtGui.QApplication(sys.argv)
    # MainWindow = QtGui.QMainWindow()
    # ui = Ui_MainWindow()
    # ui.setupUi(MainWindow)
    # MainWindow.show()
    # sys.exit(app.exec_())
 #   ui.Send.click(ui.show_message())

if __name__ == "__main__":
    # main()
    app = QtGui.QApplication(sys.argv)
    MainWindow = QtGui.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())