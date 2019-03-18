from PyQt5 import QtCore, QtGui, QtWidgets
from getMovie import pick_movie
from picked_movie_window import Ui_movieDetailWin
from watchlist_window import Ui_watchListWindow
from notification_window import Ui_uyariWin
import sqlite3

class Ui_mainWin(object):
    def setupUi(self, mainWin):
        mainWin.setObjectName("mainWin")
        mainWin.resize(400, 240)
        mainWin.setMinimumSize(QtCore.QSize(400, 240))
        mainWin.setMaximumSize(QtCore.QSize(400, 240))
        mainWin.setFocusPolicy(QtCore.Qt.TabFocus)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("icons/movie.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        mainWin.setWindowIcon(icon)
        mainWin.setTabShape(QtWidgets.QTabWidget.Rounded)
        self.centralwidget = QtWidgets.QWidget(mainWin)
        self.centralwidget.setObjectName("centralwidget")
        self.genreInput = QtWidgets.QComboBox(self.centralwidget)
        self.genreInput.setGeometry(QtCore.QRect(125, 40, 150, 30))
        font = QtGui.QFont()
        font.setFamily("Ebrima")
        font.setPointSize(11)
        font.setBold(False)
        font.setWeight(50)
        self.genreInput.setFont(font)
        self.genreInput.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.genreInput.setFocusPolicy(QtCore.Qt.WheelFocus)
        self.genreInput.setObjectName("genreInput")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("icons/family-room.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.genreInput.addItem(icon1, "")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("icons/explosion.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.genreInput.addItem(icon2, "")
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap("icons/television.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.genreInput.addItem(icon3, "")
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap("icons/alien.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.genreInput.addItem(icon4, "")
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap("icons/notebook.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.genreInput.addItem(icon5, "")
        icon6 = QtGui.QIcon()
        icon6.addPixmap(QtGui.QPixmap("icons/emotion.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.genreInput.addItem(icon6, "")
        icon7 = QtGui.QIcon()
        icon7.addPixmap(QtGui.QPixmap("icons/unicorn.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.genreInput.addItem(icon7, "")
        icon8 = QtGui.QIcon()
        icon8.addPixmap(QtGui.QPixmap("icons/film.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.genreInput.addItem(icon8, "")
        icon9 = QtGui.QIcon()
        icon9.addPixmap(QtGui.QPixmap("icons/block.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.genreInput.addItem(icon9, "")
        icon10 = QtGui.QIcon()
        icon10.addPixmap(QtGui.QPixmap("icons/laugh.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.genreInput.addItem(icon10, "")
        icon11 = QtGui.QIcon()
        icon11.addPixmap(QtGui.QPixmap("icons/ghost.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.genreInput.addItem(icon11, "")
        icon12 = QtGui.QIcon()
        icon12.addPixmap(QtGui.QPixmap("icons/apollo.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.genreInput.addItem(icon12, "")
        icon13 = QtGui.QIcon()
        icon13.addPixmap(QtGui.QPixmap("icons/hearts.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.genreInput.addItem(icon13, "")
        icon14 = QtGui.QIcon()
        icon14.addPixmap(QtGui.QPixmap("icons/guns.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.genreInput.addItem(icon14, "")
        self.genreLabel = QtWidgets.QLabel(self.centralwidget)
        self.genreLabel.setGeometry(QtCore.QRect(185, 0, 30, 40))
        font = QtGui.QFont()
        font.setFamily("Mangal")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.genreLabel.setFont(font)
        self.genreLabel.setObjectName("genreLabel")
        self.ratingLabel = QtWidgets.QLabel(self.centralwidget)
        self.ratingLabel.setGeometry(QtCore.QRect(125, 80, 150, 40))
        font = QtGui.QFont()
        font.setFamily("Mangal")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.ratingLabel.setFont(font)
        self.ratingLabel.setObjectName("ratingLabel")
        self.chooseMovieButton = QtWidgets.QPushButton(self.centralwidget)
        self.chooseMovieButton.setGeometry(QtCore.QRect(70, 180, 120, 23))
        font = QtGui.QFont()
        font.setFamily("Ebrima")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.chooseMovieButton.setFont(font)
        self.chooseMovieButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.chooseMovieButton.setObjectName("chooseMovieButton")
        self.showWatchlistButton = QtWidgets.QPushButton(self.centralwidget)
        self.showWatchlistButton.setGeometry(QtCore.QRect(210, 180, 120, 23))
        font = QtGui.QFont()
        font.setFamily("Ebrima")
        font.setPointSize(10)
        self.showWatchlistButton.setFont(font)
        self.showWatchlistButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.showWatchlistButton.setObjectName("showWatchlistButton")
        icon15 = QtGui.QIcon()
        icon15.addPixmap(QtGui.QPixmap("icons/down-arrow.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.ratingInput = QtWidgets.QLineEdit(self.centralwidget)
        self.onlyFloat = QtGui.QDoubleValidator()
        self.ratingInput.setValidator(self.onlyFloat)
        self.ratingInput.setGeometry(QtCore.QRect(150, 130, 100, 24))
        self.ratingInput.setObjectName("ratingInput")
        mainWin.setCentralWidget(self.centralwidget)

        self.retranslateUi(mainWin)
        QtCore.QMetaObject.connectSlotsByName(mainWin)

        self.chooseMovieButton.clicked.connect(self.recommend_movie)
        self.showWatchlistButton.clicked.connect(self.showWatchListWindow)

    def retranslateUi(self, mainWin):
        _translate = QtCore.QCoreApplication.translate
        mainWin.setWindowTitle(_translate("mainWin", "movieNight"))
        self.genreInput.setWhatsThis(_translate("mainWin", "<html><head/><body><p>This</p></body></html>"))
        self.genreInput.setItemText(0, _translate("mainWin", "Aile"))
        self.genreInput.setItemText(1, _translate("mainWin", "Aksiyon"))
        self.genreInput.setItemText(2, _translate("mainWin", "Animasyon"))
        self.genreInput.setItemText(3, _translate("mainWin", "Bilim-Kurgu"))
        self.genreInput.setItemText(4, _translate("mainWin", "Biyografi"))
        self.genreInput.setItemText(5, _translate("mainWin", "Dram"))
        self.genreInput.setItemText(6, _translate("mainWin", "Fantastik"))
        self.genreInput.setItemText(7, _translate("mainWin", "Gerilim"))
        self.genreInput.setItemText(8, _translate("mainWin", "Gizem"))
        self.genreInput.setItemText(9, _translate("mainWin", "Komedi"))
        self.genreInput.setItemText(10, _translate("mainWin", "Korku"))
        self.genreInput.setItemText(11, _translate("mainWin", "Müzikal"))
        self.genreInput.setItemText(12, _translate("mainWin", "Romantik"))
        self.genreInput.setItemText(13, _translate("mainWin", "Suç"))
        self.genreLabel.setText(_translate("mainWin", "<html><head/><body><p>Tür</p></body></html>"))
        self.ratingLabel.setText(_translate("mainWin", "Minimum IMDb Puanı"))
        self.chooseMovieButton.setText(_translate("mainWin", "Bana bi film seç!"))
        self.showWatchlistButton.setText(_translate("mainWin", "İzleme Listem"))

    def recommend_movie(self):
        genre = self.genreInput.currentText()

        rating = self.check_rating_input(self.ratingInput.text())
        if rating == -1:
            self.showNotificationWindow(60,10,180,20,"icons/warning.png","Puan 10'dan büyük olamaz!")

        else:
            title,rating,year = pick_movie(genre,float(rating))
            if title == -1:
                self.showNotificationWindow(35,10,230,20,"icons/warning.png","Kriterlerinize uygun film bulunamadı")
            else:
                self.showMovieWindow(title,rating,year)

    def check_rating_input(self,rating):
        # float olarak okunabilmesi için bu işlem yapılıyor
        rating = rating.replace(",",".")

        # eğer bir değer girilmemişse default olarak 0 puan atanacak
        if len(rating) == 0:
            rating = 0

        elif float(rating)>10:
            return -1

        return rating

    def showWatchListWindow(self):
        self.watchListWindow = QtWidgets.QMainWindow()
        self.ui = Ui_watchListWindow()
        self.ui.setupUi(self.watchListWindow)
        self.watchListWindow.show()

    def showMovieWindow(self,title,rating,year):
        self.movieWindow = QtWidgets.QWidget()
        self.ui = Ui_movieDetailWin()
        self.ui.setupUi(self.movieWindow,title,rating,year)
        self.movieWindow.show()

    def showNotificationWindow(self,x,y,w,h,icon_dir,msg):
        self.notificationWindow = QtWidgets.QWidget()
        self.ui = Ui_uyariWin()
        self.ui.setupUi(self.notificationWindow,x,y,w,h,icon_dir,msg)
        self.notificationWindow.show()


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    mainWin = QtWidgets.QMainWindow()
    ui = Ui_mainWin()
    ui.setupUi(mainWin)
    mainWin.show()
    sys.exit(app.exec_())
