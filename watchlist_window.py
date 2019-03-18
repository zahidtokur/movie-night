from PyQt5 import QtCore, QtGui, QtWidgets
import sqlite3

class Ui_watchListWindow(object):
    def setupUi(self, watchListWindow):
        watchListWindow.setObjectName("watchListWindow")
        watchListWindow.resize(600, 285)
        watchListWindow.setMinimumSize(QtCore.QSize(600, 285))
        watchListWindow.setMaximumSize(QtCore.QSize(600, 285))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("icons/movie.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        watchListWindow.setWindowIcon(icon)
        self.centralwidget = QtWidgets.QWidget(watchListWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.table = QtWidgets.QTableWidget(self.centralwidget)
        self.table.setGeometry(QtCore.QRect(0, 0, 600, 200))
        self.table.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.table.setRowCount(1)
        self.table.setColumnCount(3)
        self.table.setObjectName("table")
        item = QtWidgets.QTableWidgetItem()
        self.table.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.table.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.table.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.table.setItem(0, 0, item)
        self.deleteButton = QtWidgets.QPushButton(self.centralwidget)
        self.deleteButton.setGeometry(QtCore.QRect(200, 230, 80, 25))
        font = QtGui.QFont()
        font.setFamily("Ebrima")
        font.setPointSize(10)
        self.deleteButton.setFont(font)
        self.deleteButton.setObjectName("deleteButton")
        self.closeButton = QtWidgets.QPushButton(self.centralwidget)
        self.closeButton.setGeometry(QtCore.QRect(320, 230, 80, 25))
        font = QtGui.QFont()
        font.setFamily("Ebrima")
        font.setPointSize(10)
        self.closeButton.setFont(font)
        self.closeButton.setObjectName("closeButton")
        watchListWindow.setCentralWidget(self.centralwidget)

        self.load_data_to_table()

        self.retranslateUi(watchListWindow)
        QtCore.QMetaObject.connectSlotsByName(watchListWindow)

        self.closeButton.clicked.connect(watchListWindow.close)
        self.deleteButton.clicked.connect(self.delete_from_table)

    def retranslateUi(self, watchListWindow):
        _translate = QtCore.QCoreApplication.translate
        watchListWindow.setWindowTitle(_translate("watchListWindow", "İzleme Listem"))
        self.deleteButton.setText(_translate("watchListWindow", "Sil"))
        self.closeButton.setText(_translate("watchListWindow", "Kapat"))
        item = self.table.horizontalHeaderItem(0)
        item.setText(_translate("watchListWindow", "Film Adı"))
        item = self.table.horizontalHeaderItem(1)
        item.setText(_translate("watchListWindow", "IMDb Puanı"))
        item = self.table.horizontalHeaderItem(2)
        item.setText(_translate("watchListWindow", "Yapım Yılı"))

    def delete_from_table(self):
        con = sqlite3.connect('watchlist.db')
        cursor = con.cursor()

        # tabloda seçilen satırların indexlerini al
        rows = sorted(set(index.row() for index in self.table.selectedIndexes()))
        moviesToDelete = []

        for row in rows:
            movie = self.table.item(row,0)
            movie = movie.text()
            moviesToDelete.append(movie)

        for movie in moviesToDelete:
            cursor.execute("DELETE FROM Movies WHERE Film = ?",(movie,))

        con.commit()
        con.close()
        self.load_data_to_table()

    def load_data_to_table(self):
        con = sqlite3.connect('watchlist.db')
        cursor = con.cursor()
        cursor.execute("CREATE TABLE IF NOT EXISTS Movies (Film Adı TEXT, Puan REAL, Yapım Yılı INT)")
        query = "SELECT * FROM Movies"

        result = cursor.execute(query)
        self.table.setRowCount(0)
        for row_number,row_data in enumerate(result):
            self.table.insertRow(row_number)
            for column_number,data in enumerate(row_data):
                self.table.setItem(row_number,column_number,QtWidgets.QTableWidgetItem(str(data)))

        con.close()


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    watchListWindow = QtWidgets.QMainWindow()
    ui = Ui_watchListWindow()
    ui.setupUi(watchListWindow)
    watchListWindow.show()
    sys.exit(app.exec_())
