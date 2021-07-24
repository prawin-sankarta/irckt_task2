#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'test3.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from geometry_msgs.msg import Twist
import rospy  
from std_msgs.msg import Float64

move_cmd = Twist()

class Ui_Form(object):
    def setupUi(self, Form):


        

        def value_changed():
            angle = self.verticalSlider.value() #angular vel = theta/180
            rad = (angle*3.14)/180
            print(rad)
            slidepub.publish(rad)

      


        Form.setObjectName("Form")
        Form.resize(456, 345)
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(160, 10, 111, 17))
        self.label.setAutoFillBackground(False)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.pushButton = QtWidgets.QPushButton(Form)
        self.pushButton.setGeometry(QtCore.QRect(40, 60, 81, 51))
        self.pushButton.setObjectName("pushButton")
        self.pushButton_3 = QtWidgets.QPushButton(Form)
        self.pushButton_3.setGeometry(QtCore.QRect(130, 120, 81, 51))
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_4 = QtWidgets.QPushButton(Form)
        self.pushButton_4.setGeometry(QtCore.QRect(40, 180, 81, 51))
        self.pushButton_4.setObjectName("pushButton_4")
        self.pushButton_5 = QtWidgets.QPushButton(Form)
        self.pushButton_5.setGeometry(QtCore.QRect(220, 180, 81, 51))
        self.pushButton_5.setObjectName("pushButton_5")
        self.pushButton_6 = QtWidgets.QPushButton(Form)
        self.pushButton_6.setGeometry(QtCore.QRect(220, 60, 81, 51))
        self.pushButton_6.setObjectName("pushButton_6")
        self.frame = QtWidgets.QFrame(Form)
        self.frame.setGeometry(QtCore.QRect(330, 40, 120, 301))
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.verticalSlider = QtWidgets.QSlider(self.frame)
        self.verticalSlider.setGeometry(QtCore.QRect(10, 30, 41, 221))
        self.verticalSlider.setOrientation(QtCore.Qt.Vertical)
        self.verticalSlider.setObjectName("verticalSlider")
        self.verticalSlider_2 = QtWidgets.QSlider(self.frame)
        self.verticalSlider_2.setGeometry(QtCore.QRect(60, 30, 41, 221))
        self.verticalSlider_2.setOrientation(QtCore.Qt.Vertical)
        self.verticalSlider_2.setObjectName("verticalSlider_2")
        self.label_2 = QtWidgets.QLabel(self.frame)
        self.label_2.setGeometry(QtCore.QRect(0, 250, 61, 17))
        self.label_2.setAutoFillBackground(False)
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.frame)
        self.label_3.setGeometry(QtCore.QRect(60, 250, 61, 17))
        self.label_3.setAutoFillBackground(False)
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setObjectName("label_3")
        self.frame_2 = QtWidgets.QFrame(Form)
        self.frame_2.setGeometry(QtCore.QRect(30, 270, 281, 51))
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.pushButton_7 = QtWidgets.QPushButton(self.frame_2)
        self.pushButton_7.setGeometry(QtCore.QRect(10, 10, 121, 25))
        self.pushButton_7.setObjectName("pushButton_7")
        self.pushButton_2 = QtWidgets.QPushButton(self.frame_2)
        self.pushButton_2.setGeometry(QtCore.QRect(180, 10, 89, 31))
        self.pushButton_2.setObjectName("pushButton_2")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)


        self.verticalSlider.valueChanged.connect(value_changed)
        self.verticalSlider_2.valueChanged.connect(value_changed)


    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label.setText(_translate("Form", "Cafe waiter Bot"))
        self.pushButton.setText(_translate("Form", "TABLE 1"))
        self.pushButton_3.setText(_translate("Form", "TABLE 3"))
        self.pushButton_4.setText(_translate("Form", "TABLE 4"))
        self.pushButton_5.setText(_translate("Form", "TABLE 5"))
        self.pushButton_6.setText(_translate("Form", "TABLE 2"))
        self.label_2.setText(_translate("Form", "Angular"))
        self.label_3.setText(_translate("Form", "Linear"))
        self.pushButton_7.setText(_translate("Form", "RETURN HOME"))
        self.pushButton_2.setText(_translate("Form", "STOP"))


if __name__ == "__main__":
    import sys

    rospy.init_node('UI_003')
    pub = rospy.Publisher('cmd_vel', Twist, queue_size=1)
    slidepub = rospy.Publisher('/irckt/motor_finger_right_position_controller/command', Float64, queue_size=1)
    

    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())

