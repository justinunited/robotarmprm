# from scipy.spatial import distance as dist
# from imutils import perspective
# from imutils import contours
# import numpy as np
# import argparse
# import imutils
# import cv2
import serial
import time
import struct
from serial_coms_list import *
from InverseKinematics import *

# Connect to mcu

BAUDRATE = int(input("input baud rate: "))
portName = "COM" + str(input("Port: COM"))

serialDevice = autoConnect(BAUDRATE, portName)

while(1):
    if serialDevice.inWaiting() > 0:
        # data = serialDevice.read(1)
        # print("data =", ord(data))
        try:
            print(serialDevice.readline().decode('utf-8'))
        except:
            pass
    else:
        print("1: set Home\n2: get enc data \n")
        keyinput = input(": ")
        if keyinput != '':
            if keyinput == '0':
                break
            elif keyinput == '1':
                setHome(serialDevice)
            elif keyinput == '2':
                getEncData(serialDevice)
            elif keyinput == '3':
                sendSPI(serialDevice)
            elif keyinput == '10':
                getRawEncData(serialDevice)
            elif keyinput == '4':
                sendSPItest(serialDevice)
            elif keyinput == '7':
                Kp1 = float(input("Kp1 = "))
                Ki1 = float(input("Ki1 = "))
                Kd1 = float(input("Kd1 = "))
                Kp2 = float(input("Kp2 = "))
                Ki2 = float(input("Ki2 = "))
                Kd2 = float(input("Kd2 = "))
                setGains(Kp1, Ki1, Kd1, Kp2, Ki2, Kd2, serialDevice)
            elif keyinput == '8':
                tol_1 = float(input("set tolerance for q1:"))
                tol_2 = float(input("set tolerance for q2:"))
                setTolerances(tol_1, tol_2, serialDevice)
            elif keyinput == '5':
                q1 = float(input("input q1 from -120 to 120:"))
                q2 = float(input("input q2 from -170 to 35:"))
                q3 = float(input("input q3 from -34 to 255:"))
                q4 = float(input("input q4 from -120 to 120:"))
                q5 = float(input("input q5 from -80 to 80:"))
                sendTarget(q1, q2, q3, q4, q5, serialDevice)
            elif keyinput == '6':
                # dimensions in mm
                x = float(input("input x:"))
                y = float(input("input y:"))
                z = float(input("input z:"))
                facing_angle = float(input("input facing_angle:"))
                sendInverse(x, y, z, facing_angle, serialDevice)
            elif keyinput == 'go':
                goNow(serialDevice)
            elif keyinput == 'open':
                gripRelease(serialDevice)
            elif keyinput == 'succ':
                gripSucc(serialDevice)
            elif keyinput == 'pre':
                ind = int(input("input index:"))
                sendPreset(ind, serialDevice)
            elif keyinput == 'path':
                initial = input('input starting point: ')
                final = input('input goal point: ')
                pathTraversal(initial, final, 0, 0, serialDevice)

serialDevice.close()
print("end")
