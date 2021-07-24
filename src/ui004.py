# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'test4.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
import rospy
from geometry_msgs.msg import Twist
from std_msgs.msg import Float64
 
move_cmd = Twist()

class Ui_Form(object):
    def setupUi(self, Form):

        def value_changed():
            angle = self.horizontalSlider.value()
            rad = (angle*3.14)/180
            print(rad)
            slidepub.publish(rad)




        Form.setObjectName("Form")
        Form.resize(271, 322)
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(80, 10, 111, 17))
        self.label.setAutoFillBackground(False)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.pushButton = QtWidgets.QPushButton(Form)
        self.pushButton.setGeometry(QtCore.QRect(10, 40, 71, 41))
        self.pushButton.setStyleSheet("background-color: rgb(19, 174, 27);")
        self.pushButton.setObjectName("pushButton")
        self.pushButton_6 = QtWidgets.QPushButton(Form)
        self.pushButton_6.setGeometry(QtCore.QRect(100, 40, 71, 41))
        self.pushButton_6.setStyleSheet("background-color: rgb(252, 175, 62);")
        self.pushButton_6.setObjectName("pushButton_6")
        self.pushButton_3 = QtWidgets.QPushButton(Form)
        self.pushButton_3.setGeometry(QtCore.QRect(190, 40, 71, 41))
        self.pushButton_3.setStyleSheet("background-color: rgb(114, 159, 207);")
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_4 = QtWidgets.QPushButton(Form)
        self.pushButton_4.setGeometry(QtCore.QRect(50, 100, 71, 41))
        self.pushButton_4.setStyleSheet("background-color: rgb(117, 80, 123);")
        self.pushButton_4.setObjectName("pushButton_4")
        self.pushButton_5 = QtWidgets.QPushButton(Form)
        self.pushButton_5.setGeometry(QtCore.QRect(150, 100, 71, 41))
        self.pushButton_5.setStyleSheet("background-color: rgb(245, 121, 0);")
        self.pushButton_5.setObjectName("pushButton_5")
        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setGeometry(QtCore.QRect(100, 210, 61, 17))
        self.label_2.setAutoFillBackground(False)
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(Form)
        self.label_3.setGeometry(QtCore.QRect(100, 170, 61, 17))
        self.label_3.setAutoFillBackground(False)
        self.label_3.setTextFormat(QtCore.Qt.PlainText)
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setObjectName("label_3")
        


        self.horizontalSlider = QtWidgets.QSlider(Form)
        self.horizontalSlider.setGeometry(QtCore.QRect(30, 180, 191, 21))
        self.horizontalSlider.setSliderPosition(0)
        self.horizontalSlider.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalSlider.setTickPosition(QtWidgets.QSlider.NoTicks)
        self.horizontalSlider.setObjectName("horizontalSlider")



        self.horizontalSlider_2 = QtWidgets.QSlider(Form)
        self.horizontalSlider_2.setGeometry(QtCore.QRect(30, 220, 191, 21))
        self.horizontalSlider_2.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalSlider_2.setObjectName("horizontalSlider_2")
        

        self.pushButton_7 = QtWidgets.QPushButton(Form)
        self.pushButton_7.setGeometry(QtCore.QRect(20, 260, 121, 51))
        self.pushButton_7.setStyleSheet("background-color: rgb(237, 212, 0);")
        self.pushButton_7.setObjectName("pushButton_7")
        self.pushButton_2 = QtWidgets.QPushButton(Form)
        self.pushButton_2.setGeometry(QtCore.QRect(160, 260, 81, 51))
        self.pushButton_2.setStyleSheet("background-color: rgb(204, 0, 0);")
        self.pushButton_2.setObjectName("pushButton_2")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)


        self.horizontalSlider.valueChanged.connect(value_changed)
        self.horizontalSlider_2.valueChanged.connect(value_changed)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label.setText(_translate("Form", "Cafe waiter Bot"))
        self.pushButton.setText(_translate("Form", "TABLE1"))
        self.pushButton_6.setText(_translate("Form", "TABLE2"))
        self.pushButton_3.setText(_translate("Form", "TABLE3"))
        self.pushButton_4.setText(_translate("Form", "TABLE4"))
        self.pushButton_5.setText(_translate("Form", "TABLE5"))
        self.label_2.setText(_translate("Form", "Linear"))
        self.label_3.setText(_translate("Form", "Angular"))
        self.pushButton_7.setText(_translate("Form", "RETURN HOME"))
        self.pushButton_2.setText(_translate("Form", "STOP"))


if __name__ == "__main__":

    import sys

    rospy.init_node('UI_002')
    pub = rospy.Publisher('cmd_vel', Twist, queue_size=1)
    slidepub = rospy.Publisher('/irckt/motor_finger_right_position_controller/command', Float64, queue_size=1)

    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())

