from os import name
from typing import TextIO
from flask import Flask, request, abort
from PyQt6 import QtWidgets, QtCore

import client2 
#подтягиваем файл, полученный при переводе .ui в .py 
# через командy uic6 Wind_mess.ui -o client2.py

import requests
from datetime import datetime


class MessengerApp(QtWidgets.QMainWindow, client2.Ui_MainWindow):
    def __init__(self, host="http://127.0.0.1:5000"):
        super().__init__()
        self.setupUi(self)

        self.host = host

        # to run botton click:
        # self.some_botton.pressed.connect(self.some_method)
        self.pushButton.pressed.connect(self.send_message)

        # To run by timer:
        self.timer = QtCore.QTimer()
        self.timer.timeout.connect(self.get_messages)
        self.timer.start(1000)
        self.after_val = 0


    def get_messages(self):
        try:
            r=requests.get(
                self.host+"/receive",
                params={"after": self.after_val}
            )
        except requests.exceptions.ConnectionError:
            return
        response = r.json()
        if len(response["messages"]) > 0:
            self.after_val = response["messages"][-1]["date"],
            for item in response["messages"]:
                dt = datetime.fromtimestamp(item["date"]).strftime("%Y.%m.%d %H:%M:%S")
                text = item["msg"]
                name = item["name"]
                self.textBrowser.append(dt + "  " + name)
                self.textBrowser.append(text)
                self.textBrowser.append("  ")

    def send_message(self):
        name = self.textEdit.toPlainText()
        text = self.textEdit_2.toPlainText()
        if len(text)==0 or len(name)==0:
            self.textBrowser.append("Wrong name or text")
            self.textBrowser.append("  ")
            return

        try:
            r=requests.post(
                self.host+"/send",
                json={"text": text, "name": name}
            )
        except requests.exceptions.ConnectionError:
            return

        self.textEdit_2.clear()


    
if __name__ == "__main__": 
    app = QtWidgets.QApplication([])
    window = MessengerApp(
        host="http://ef02-85-236-167-26.ngrok.io"
        #это нестатичная переменная, генерится при запуске ngrok
    )
    window.show()
    app.exec()


# pyuic6 Wind_mess.ui -o client2.py - преобразование файла
