from PyQt5 import QtCore, QtGui, QtWidgets
import sqlite3
from notification_window import Ui_uyariWin

class Ui_movieDetailWin(object):
    def setupUi(self, movieDetailWin,title,rating,year):
        movieDetailWin.setObjectName("movieDetailWin")
        movieDetailWin.resize(435, 287)
        movieDetailWin.setMinimumSize(QtCore.QSize(435, 287))
        movieDetailWin.setMaximumSize(QtCore.QSize(435, 287))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("icons/movie.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        movieDetailWin.setWindowIcon(icon)
        self.titleLabel = QtWidgets.QLabel(movieDetailWin)
        self.titleLabel.setGeometry(QtCore.QRect(30, 15, 161, 16))
        font = QtGui.QFont()
        font.setFamily("Mangal")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.titleLabel.setFont(font)
        self.titleLabel.setObjectName("titleLabel")
        self.ratingLabel = QtWidgets.QLabel(movieDetailWin)
        self.ratingLabel.setGeometry(QtCore.QRect(30, 88, 81, 16))
        font = QtGui.QFont()
        font.setFamily("Mangal")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.ratingLabel.setFont(font)
        self.ratingLabel.setObjectName("ratingLabel")
        self.yearLabel = QtWidgets.QLabel(movieDetailWin)
        self.yearLabel.setGeometry(QtCore.QRect(30, 160, 71, 16))
        font = QtGui.QFont()
        font.setFamily("Mangal")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.yearLabel.setFont(font)
        self.yearLabel.setObjectName("yearLabel")
        self.addToWatchlistBtn = QtWidgets.QCommandLinkButton(movieDetailWin)
        self.addToWatchlistBtn.setGeometry(QtCore.QRect(30, 232, 180, 40))
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("icons/plus.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.addToWatchlistBtn.setIcon(icon1)
        self.addToWatchlistBtn.setObjectName("addToWatchlistBtn")
        self.closeButton = QtWidgets.QCommandLinkButton(movieDetailWin)
        self.closeButton.setGeometry(QtCore.QRect(225, 232, 180, 40))
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("icons/error.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.closeButton.setIcon(icon2)
        self.closeButton.setObjectName("closeButton")
        self.titleOutput = QtWidgets.QTextBrowser(movieDetailWin)
        self.titleOutput.setGeometry(QtCore.QRect(30, 47, 250, 26))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.titleOutput.setFont(font)
        self.titleOutput.setObjectName("titleOutput")
        self.titleOutput.setText(title)
        self.ratingOutput = QtWidgets.QTextBrowser(movieDetailWin)
        self.ratingOutput.setGeometry(QtCore.QRect(30, 119, 100, 26))
        self.ratingOutput.setObjectName("ratingOutput")
        self.ratingOutput.setText(rating)
        self.yearOutput = QtWidgets.QTextBrowser(movieDetailWin)
        self.yearOutput.setGeometry(QtCore.QRect(30, 191, 100, 26))
        self.yearOutput.setObjectName("yearOutput")
        self.yearOutput.setText(year)

        self.addToWatchlistBtn.clicked.connect(lambda: self.save_to_db(title,rating,year))
        self.closeButton.clicked.connect(movieDetailWin.close)

        self.retranslateUi(movieDetailWin)
        QtCore.QMetaObject.connectSlotsByName(movieDetailWin)

    def retranslateUi(self, movieDetailWin):
        _translate = QtCore.QCoreApplication.translate
        movieDetailWin.setWindowTitle(_translate("movieDetailWin", "İşte Filmin!"))
        self.titleLabel.setText(_translate("movieDetailWin", "Filmin Adı"))
        self.ratingLabel.setText(_translate("movieDetailWin", "IMDb Puanı"))
        self.yearLabel.setText(_translate("movieDetailWin", "Yapım Yılı"))
        self.addToWatchlistBtn.setText(_translate("movieDetailWin", "İzleme Listeme Ekle"))
        self.closeButton.setText(_translate("movieDetailWin", "Kapat"))

    def save_to_db(self,title,rating,year):
        con = sqlite3.connect("watchlist.db")
        cursor = con.cursor()

        # eklenmeye çalışılan film zaten veritabanında var mı diye kontrol ediyor
        cursor.execute("SELECT * FROM Movies WHERE Film = ?",(title,))
        data = cursor.fetchall()
        if len(data) == 0:
            cursor.execute("CREATE TABLE IF NOT EXISTS Movies (Film TEXT, Puan REAL, Yapım INT)")
            cursor.execute("INSERT INTO Movies VALUES(?,?,?)",(title,rating,year))
            con.commit()
            con.close()
            self.showNotificationWindow(70,10,160,20,"icons/checked.png","İzleme Listene Eklendi!")

        else:
            self.showNotificationWindow(70,10,160,20,"icons/warning.png","Bu Zaten Listende Var!")


    def showNotificationWindow(self,x,y,w,h,icon,msg):
        self.notificationWindow = QtWidgets.QWidget()
        self.ui = Ui_uyariWin()
        self.ui.setupUi(self.notificationWindow,x,y,w,h,icon,msg)
        self.notificationWindow.show()

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    movieDetailWin = QtWidgets.QWidget()
    ui = Ui_movieDetailWin()
    ui.setupUi(movieDetailWin)
    movieDetailWin.show()
    sys.exit(app.exec_())
