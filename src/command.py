#!/usr/bin/env python3
# -*-coding:utf-8-*-
import time
import robomaster
from robomaster import conn
from MyQR import myqr
from PIL import Image


QRCODE_NAME = "qrcode.png"

if __name__ == '__main__':

    helper = conn.ConnectionHelper()
    info = helper.build_qrcode_string(ssid="Center for Robotics", password="1234567890")
    myqr.run(words=info)
    time.sleep(1)
    img = Image.open(QRCODE_NAME)
    img.show()
    if helper.wait_for_connection():
        print("Connected!")
    else:
        print("Connect failed!")

