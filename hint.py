from PyQt6 import QtWidgets
import client2

class MessengerApp(QtWidgets.QMainWindow, client2.Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        # to run botton click:
        # self.some_botton.pressed.connect(self.some_method)

        # To run by timer:
        # self.timer = QtQore.QTimer()
        

if __name__ == "__main__":
    app = QtWidgets.QApplication([])
    window = MessengerApp()
    window.show()
    app.exec()


# pyuic6 Wind_mess.ui -o client2.py
