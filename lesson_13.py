import os
import sys
import pandas as pd
import YOUR_UI_FILE
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import *


class MainApplication(QtWidgets.QMainWindow, YOUR_UI_FILE.YOUR_UI_CLASS):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.directory = os.getcwd()
        self.data = None
        self.save_btn.clicked.connect(self.save_file)
        self.exit_btn.clicked.connect(self.exit)
    def save(self):
       self.mytext=self.vidget.ToPlaintext()
       qpl..getSaveFiledone()
        self.vidget.clear()
    def exit(self):
       exit()


def main():
  app = QtWidgets.QApplication(sys.argv)
  window = MainApplication()
  window.show()
  app.exec_()


if __name__ == '__main__':
  main()






#2 виджет текст, высота 90, форма
#3 виджет кнопки(все без отступов). минимум 0,0
#у главного окна написать размеры 450*800
#перенести 2 кнопки в 3 виджет,они будут снизу, сейв и выход, минимальный размер по высоте 40 и ширине 100
#добавить пружину справа внизу
#стайлшип qpushbutton hover(background-color )
#text edit = эдит виджет. РАСТянуть по площади
#виндоу тайтл = название



