import sys
from socket import *

from PyQt5 import QtWidgets, QtCore
from PyQt5.QtWidgets import QDialog

import about_mod
import settings_mod
import main_gui

host = '127.0.0.1'
port = 9999


class AboutMod(QDialog, about_mod.Ui_Dialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)


class SettingsMod(QDialog, settings_mod.Ui_Dialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)
        self.pushButton_OK.clicked.connect(self.socket_set)
        self.pushButton_cancel.clicked.connect(self.close)
        self.lineEdit_host.setText(host)
        self.lineEdit_port.setText(str(port))

    def socket_set(self):
        global host, port
        host = self.lineEdit_host.text()
        port = int(self.lineEdit_port.text())
        MainWindow.addr = (host, port)
        MainWindow.udp_socket = socket(AF_INET, SOCK_DGRAM)
        self.close()


class MainWindow(QtWidgets.QMainWindow, main_gui.Ui_MainWindow):
    addr = (host, port)
    udp_socket = socket(AF_INET, SOCK_DGRAM)

    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.pushButton.clicked.connect(self.exit_but1)
        self.pushButton_2.clicked.connect(self.fwd_but2)
        self.pushButton_3.clicked.connect(self.rst_but3)
        self.pushButton_4.clicked.connect(self.left_but4)
        self.pushButton_5.clicked.connect(self.horn_but5)
        self.pushButton_6.clicked.connect(self.right_but6)
        self.pushButton_7.clicked.connect(self.light_on7)
        self.pushButton_8.clicked.connect(self.back_but8)
        self.pushButton_9.clicked.connect(self.light_off9)
        self.Speed.valueChanged.connect(self.speed_dial)
        self.actionAbout.triggered.connect(show_about)
        self.actionSettings.triggered.connect(show_settings)

    def keyPressEvent(self, event):
        if event.key() == QtCore.Qt.Key_Escape:
            self.exit_but1()
        if event.key() == QtCore.Qt.Key_W:
            self.fwd_but2()
        if event.key() == QtCore.Qt.Key_Space:
            self.rst_but3()
        if event.key() == QtCore.Qt.Key_A:
            self.left_but4()
        if event.key() == QtCore.Qt.Key_X:
            self.horn_but5()
        if event.key() == QtCore.Qt.Key_D:
            self.right_but6()
        if event.key() == QtCore.Qt.Key_Q:
            self.light_on7()
        if event.key() == QtCore.Qt.Key_S:
            self.back_but8()
        if event.key() == QtCore.Qt.Key_E:
            self.light_off9()
        if event.key() == QtCore.Qt.Key_C:
            print('Increase')
        if event.key() == QtCore.Qt.Key_Z:
            print('Decrease')

    def exit_but1(self):
        self.udp_socket.close()
        print('Exit')
        exit(0)

    def fwd_but2(self):
        self.send_data('Forward')

    def rst_but3(self):
        self.send_data('Rst')
        self.send_data('Rst')
        self.send_data('Rst')

    def left_but4(self):
        self.send_data('Left')

    def horn_but5(self):
        self.send_data('Hornon')

    def right_but6(self):
        self.send_data('Right')

    def light_on7(self):
        self.send_data('Lighton')

    def back_but8(self):
        self.send_data('Back')

    def light_off9(self):
        self.send_data('Lightoff')

    def speed_dial(self):
        speed_inp = self.Speed.value()
        self.send_data(str(speed_inp))

    def send_data(self, inp_str):
        data = inp_str
        data = str.encode(data)
        print(data)
        try:
            self.udp_socket.sendto(data, self.addr)
        except:
            pass


def show_about():
    cam_ = AboutMod()
    cam_.exec()


def show_settings():
    cam_ = SettingsMod()
    cam_.exec()


def main():
    app = QtWidgets.QApplication(sys.argv)
    main_window = MainWindow()
    main_window.show()
    app.exec_()


if __name__ == '__main__':
    main()
