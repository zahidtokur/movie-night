from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_uyariWin(object):
    def setupUi(self, uyariWin,x,y,w,h,icon_dir,msg):
        uyariWin.setObjectName("uyariWin")
        uyariWin.resize(300, 90)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(icon_dir), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        uyariWin.setWindowIcon(icon)
        self.okayButton = QtWidgets.QPushButton(uyariWin)
        self.okayButton.setGeometry(QtCore.QRect(110, 50, 80, 23))
        self.okayButton.setObjectName("okayButton")
        self.message = QtWidgets.QLabel(uyariWin)
        self.message.setGeometry(QtCore.QRect(x, y, w, h))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.message.setFont(font)
        self.message.setObjectName("message")
        
        self.okayButton.clicked.connect(uyariWin.close)

        self.retranslateUi(uyariWin,msg)
        QtCore.QMetaObject.connectSlotsByName(uyariWin)

    def retranslateUi(self, uyariWin,msg):
        _translate = QtCore.QCoreApplication.translate
        uyariWin.setWindowTitle(_translate("uyariWin", "Bildirim"))
        self.okayButton.setText(_translate("uyariWin", "Tamam"))
        self.message.setText(_translate("uyariWin", msg))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    uyariWin = QtWidgets.QWidget()
    ui = Ui_uyariWin()
    ui.setupUi(uyariWin)
    uyariWin.show()
    sys.exit(app.exec_())
