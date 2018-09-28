# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'z.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QWidget, QInputDialog, QLineEdit, QFileDialog
from PyQt5.QtGui import QIcon
import subprocess
import shlex

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(400, 300)
        self.pushButton_2 = QtWidgets.QPushButton(Form)
        self.pushButton_2.setGeometry(QtCore.QRect(120, 100, 151, 71))
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_2.clicked.connect(self.select1)

        self.pushButton_3 = QtWidgets.QPushButton(Form)
        self.pushButton_3.setGeometry(QtCore.QRect(120, 20, 151, 71))
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_3.clicked.connect(self.openFileNameDialog)

        self.pushButton_4 = QtWidgets.QPushButton(Form)
        self.pushButton_4.setGeometry(QtCore.QRect(120, 180, 151, 71))
        self.pushButton_4.setObjectName("pushButton_4")
        self.pushButton_4.clicked.connect(self.select2)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Detector"))
        self.pushButton_2.setText(_translate("Form", "Detect Mahdi"))
        self.pushButton_3.setText(_translate("Form", "Select Video"))
        self.pushButton_4.setText(_translate("Form", "Detect All"))

    def openFileNameDialog(self):
        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog
        self.direct, _ = QFileDialog.getOpenFileName(None, "QFileDialog.getOpenFileName()", "",
                                                     "All Files (*);;Python Files (*.avi)", options=options)

    def select1(self):


        command2 = "./darknet detector demo obj.data cfg/obj.cfg obj_3000.weights "+self.direct
        args2 = shlex.split(command2)
        subprocess.call(args2)

    def select2(self):


        command3 = "./darknet detector demo cfg/coco.data cfg/yolov3-tiny.cfg yolov3-tiny.weights "+self.direct
        args3 = shlex.split(command3)
        subprocess.call(args3)


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())

