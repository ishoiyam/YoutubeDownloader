from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.uic import loadUiType
import sys
from urllib.request import urlretrieve


MainUI,_ = loadUiType("main.ui")



class Main(QMainWindow, MainUI):
    def __init__(self, parent=None):
        super(Main, self).__init__(parent)
        QMainWindow.__init__(self)
        self.setupUi(self)
        self.manage_buttons()
        
    def manage_buttons(self):
        self.download_button.clicked.connect(self.download)
        self.browse_button.clicked.connect(self.browse)

    def browse(self):
        save_location = QFileDialog.getSaveFileName(self, caption="Save As", directory=".", filter="All Files(*.*)")
        self.location_line.setText(str(save_location[0]))

    def progress_status(self, block_num, block_size, total_size):
        wanted_data = block_num * block_size

        if total_size > 0:
            download_percent = wanted_data * 100 / total_size
            self.progress_bar.setValue(int(download_percent))
            QApplication.processEvents()
        

    def download(self):
        url = self.url_line.text()
        location = self.location_line.text()
        
        if not url == "" or location == "":
            try:
                urlretrieve(url, location, self.progress_status)
            except Exception:
                return QMessageBox.warning(self, "Error", "Invalide URL or Location!")
        else:
            return QMessageBox.warning(self, "Error", "Invalide URL or Location!!")

        QMessageBox.information(self, "Process Completed", "The Download Completed Successfully!")

        self.url_line.setText("")
        self.location_line.setText("")
        self.progress_bar.setValue(0)




def main():
    app = QApplication(sys.argv)
    window = Main()
    window.show()
    app.exec_()


if __name__ == "__main__":
    main()
