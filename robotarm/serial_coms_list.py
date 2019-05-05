# from scipy.spatial import distance as dist
# from imutils import perspective
# from imutils import contours
import numpy as np
# import argparse
# import imutils
# import cv2
import serial
import time
import struct
from InverseKinematics import *
from Graph import astar
import pickle
from math import pi

countsPerMillimeter = (321 / 300 * 400) / (np.pi * 10)
countsPerMillimeter_z = (12 * 66) / (np.pi * 12)

# Connect to mcu


def autoConnect(baud, portName):
    while(1):
        try:
            serialDevice = serial.Serial()
            serialDevice.baudrate = baud
            # serialDevice.parity = 'E'
            serialDevice.port = portName
            serialDevice.timeout = 1
            serialDevice.rts = 0
            serialDevice.dtr = 0
            serialDevice.open()
            print('connected to mcu')
            return serialDevice
        except:
            print('connection failed')
            pass


def sendCommand(command, ser):
    ser.write(bytes(command))
    while(1):
        if ser.inWaiting() > 0:
            # data = ser.read(1)
            # print("data =", ord(data))
            response = ser.readline().decode('utf-8')
            print(response)
            # if response != 'received' or 'starting':
            #     pass
            if response == 'resend':
                ser.write(bytes(command))
            elif response == 'done':
                return 1
            elif response == 'starting':
                break
            else:
                pass
            #     return 0
            #     break
        # else:
        #     ser.write(bytes(command))


def setHome(ser):
    buffer = [255, 255, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    checksum = 0
    for i in buffer:
        checksum += i
    checksum = checksum % 256
    buffer.append(checksum)
    print('sending ')
    print(buffer)
    sendCommand(buffer, ser)


def getEncData(ser):
    buffer = [255, 255, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    checksum = 0
    for i in buffer:
        checksum += i
    checksum = checksum % 256
    buffer.append(checksum)
    print('sending ')
    print(buffer)
    sendCommand(buffer, ser)


def getRawEncData(ser):
    buffer = [255, 255, 10, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    checksum = 0
    for i in buffer:
        checksum += i
    checksum = checksum % 256
    buffer.append(checksum)
    print('sending ')
    print(buffer)
    sendCommand(buffer, ser)


def sendSPI(ser):
    buffer = [255, 255, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    checksum = 0
    for i in buffer:
        checksum += i
    checksum = checksum % 256
    buffer.append(checksum)
    print('sending ')
    print(buffer)
    sendCommand(buffer, ser)


def sendSPItest(ser):
    buffer = [255, 255, 4, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    checksum = 0
    for i in buffer:
        checksum += i
    checksum = checksum % 256
    buffer.append(checksum)
    print('sending ')
    print(buffer)
    sendCommand(buffer, ser)


def sendTarget(q1, q2, q3, q4, q5, ser):
    buffer = [255, 255, 5]
    checksum = 0
    q1_sign = 0 if q1 >= 0 else 1
    q2_sign = 0 if q2 >= 0 else 1
    q3_sign = 0 if q3 >= 0 else 1
    q4_sign = 0 if q4 >= 0 else 1
    q5_sign = 0 if q5 >= 0 else 1
    buffer.append(q1_sign)
    buffer.extend(split_floats(abs(q1)))
    buffer.append(q2_sign)
    buffer.extend(split_floats(abs(q2)))
    buffer.append(q3_sign)
    buffer.extend(split_floats(abs(q3)))
    buffer.append(q4_sign)
    buffer.extend(split_floats(abs(q4)))
    buffer.append(q5_sign)
    buffer.extend(split_floats(abs(q5)))

    for i in buffer:
        checksum += i
    checksum = checksum % 256
    buffer.append(checksum)
    print('sending ')
    print(buffer)
    sendCommand(buffer, ser)
    return 1


def sendPreset(index, ser):
    arr = [[115.03183091872435, -67.77724322956213, 17.16236370823007, 50.61487952133207, 33.70443738689822], [88.93694791509603, -23.802426449115767, 7.15227539696151, 16.650151052154254, 55.89542196233564],
           [41.77250722897626, -15.721380473387095, 38.183703192384655, -22.462322718997566, -44.71842850676669], [38.404866441001076, -40.9614505836742, 42.717535179301954, -1.7560845956277524, -38.404866441001076]]
    sendTarget(arr[index][0], arr[index][1], arr[index]
               [2], arr[index][3], arr[index][4], ser)


def goNow(ser):
    buffer = [255, 255, 9, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    checksum = 0
    for i in buffer:
        checksum += i
    checksum = checksum % 256
    buffer.append(checksum)
    print('sending ')
    print(buffer)
    sendCommand(buffer, ser)


def gripRelease(ser):
    buffer = [255, 255, 11, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    checksum = 0
    for i in buffer:
        checksum += i
    checksum = checksum % 256
    buffer.append(checksum)
    print('sending ')
    print(buffer)
    sendCommand(buffer, ser)


def gripSucc(ser):
    buffer = [255, 255, 12, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    checksum = 0
    for i in buffer:
        checksum += i
    checksum = checksum % 256
    buffer.append(checksum)
    print('sending ')
    print(buffer)
    sendCommand(buffer, ser)


def softReset(ser):
    buffer = [255, 255, 13, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    checksum = 0
    for i in buffer:
        checksum += i
    checksum = checksum % 256
    buffer.append(checksum)
    print('sending ')
    print(buffer)
    sendCommand(buffer, ser)


def sendInverse(x, y, z, facing_angle, ser):
    q1, q2, q3, q4, q5 = inverseKinematics(x, y, z, facing_angle)
    a = sendTarget(q1, q2, q3, q4, q5, ser)
    if a == 1:
        return 1
    else:
        return 0


def pathTraversal(initial, final, type, mode, ser):
    with open('Graph.gph', 'rb') as Graph1_file:
        Graph1 = pickle.load(Graph1_file)
    setpointDict = {
        '0': [-380, -632, 510, -pi / 2],
        '1': [636.76, 371.22, 901.66, 0],
        '2': [636.76, 122.22, 891.66, 0],
        '3': [636.76, -103.78, 946.66],
        '4': [636.76, -303.78, 958.66, 0],
        '5': [636.76, 371.22, 568.33, 0],
        '6': [636.76, 122.22, 563.33, 0],
        '7': [636.76, -103.78, 701.66, 0],
        '8': [636.76, -303.78, 706.66, 0],
        '9': [636.76, 371.22, 240, 0],
        '10': [636.76, 122.22, 235, 0],
        '11': [676.76, -103.78, 451.66, 0],
        '12': [636.76, -303.78, 461.66, 0],
        '13': [636.76, -103.78, 206.66, 0],
        '14': [636.76, -303.78, 211.66, 0],
        '15': [-380, 632, 510, pi / 2]
    }
    if initial == 'home':
        q1_i, q2_i, q3_i, q4_i, q5_i = 0, 0, 0, 0, 0
    else:
        task_init = setpointDict[str(initial)]
        q1_i, q2_i, q3_i, q4_i, q5_i = inverseKinematics(
            task_init[0], task_init[1], task_init[2], task_init[3])
    if final == 'home':
        q1_f, q2_f, q3_f, q4_f, q5_f = 0, 0, 0, 0, 0
    else:
        task_final = setpointDict[str(final)]
        q1_f, q2_f, q3_f, q4_f, q5_f = inverseKinematics(
            task_final[0], task_final[1], task_final[2], task_final[3])
    path = Graph1.astar([q1_i, q2_i, q3_i, q4_i, q5_i],
                        [q1_f, q2_f, q3_f, q4_f, q5_f])
    # if type == "small":
    #     q1, q2, q3, q4, q5 = inverseKinematics(
    #         task_final[0], task_final[1], task_final[2] - 75, task_final[3])
    # elif type == "big":
    #     q1, q2, q3, q4, q5 = inverseKinematics(
    #         task_final[0], task_final[1], task_final[2] - 50, task_final[3])
    # path.append([q1, q2, q3, q4, q5])
    print(path)
    for i in path:
        sendTarget(i[0], i[1], i[2], i[3], i[4], ser)


def setGains(K_P1, K_I1, K_D1, K_P2, K_I2, K_D2, ser):
    buffer = [255, 255, 7, 0, 0, 0]
    buffer.extend(split_floats(K_P1))
    buffer.extend(split_floats(K_I1))
    buffer.extend(split_floats(K_D1))
    buffer.extend(split_floats(K_P2))
    buffer.extend(split_floats(K_I2))
    buffer.extend(split_floats(K_D2))
    checksum = 0
    for i in buffer:
        checksum += i
    checksum = checksum % 256
    buffer.append(checksum)
    print('sending ')
    print(buffer)
    sendCommand(buffer, ser)


def setTolerances(t_1, t_2, ser):
    buffer = [255, 255, 8, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    buffer.extend(split_floats(t_1))
    buffer.extend(split_floats(t_2))
    checksum = 0
    for i in buffer:
        checksum += i
    checksum = checksum % 256
    buffer.append(checksum)
    print('sending ')
    print(buffer)
    sendCommand(buffer, ser)


# def setPosXY(x, y, ser):
#     buffer = [255, 255, 1]
#     a = int(np.sqrt(2) / 2 * (y - x))
#     b = int(np.sqrt(2) / 2 * (y + x))
#     print("x = " + str(x / countsPerMillimeter))
#     print("y = " + str(y / countsPerMillimeter))
#     print("a = " + str(a))
#     print("b = " + str(b))
#     a_sign = 0 if a >= 0 else 1
#     b_sign = 0 if b >= 0 else 1
#     buffer.extend(split_large_ints(abs(a)))
#     buffer.extend(split_large_ints(abs(b)))
#     buffer.extend([a_sign, b_sign])
#     checksum = 0
#     for i in buffer:
#         checksum += i
#     checksum = checksum % 256
#     buffer.append(checksum)
#     print('sending ')
#     print(buffer)
#     sendCommand(buffer, ser)
#
#
# def setPosXY_mm(x, y, ser, x_pix, y_pix, countsPerMillimeter=countsPerMillimeter):
#     buffer = [255, 255, 1]
#     x = x * countsPerMillimeter
#     y = y * countsPerMillimeter
#
#     a = int(np.sqrt(2) / 2 * (y - x))
#     b = int(np.sqrt(2) / 2 * (y + x))
#     print("x = " + str(x / countsPerMillimeter))
#     print("y = " + str(y / countsPerMillimeter))
#     print("a = " + str(a))
#     print("b = " + str(b))
#     a_sign = 0 if a >= 0 else 1
#     b_sign = 0 if b >= 0 else 1
#     buffer.extend(split_large_ints(abs(a)))
#     buffer.extend(split_large_ints(abs(b)))
#     buffer.extend([a_sign, b_sign])
#     checksum = 0
#     for i in buffer:
#         checksum += i
#     checksum = checksum % 256
#     buffer.append(checksum)
#     print('sending ')
#     print(buffer)
#     sendCommand(buffer, ser)
#
#
# def setPosZ(z, ser):
#     buffer = [255, 255, 2]
#     buffer.extend(split_large_ints(z))
#     buffer.extend([0, 0, 0, 0])
#     checksum = 0
#     for i in buffer:
#         checksum += i
#     checksum = checksum % 256
#     buffer.append(checksum)
#     print('sending ')
#     print(buffer)
#     sendCommand(buffer, ser)
#
#
# def setPosZ_mm(z, ser, countsPerMillimeter_z):
#     buffer = [255, 255, 2]
#     z = int(z * countsPerMillimeter_z)
#     buffer.extend(split_large_ints(z))
#     buffer.extend([0, 0, 0, 0])
#     checksum = 0
#     for i in buffer:
#         checksum += i
#     checksum = checksum % 256
#     buffer.append(checksum)
#     print('sending ')
#     print(buffer)
#     sendCommand(buffer, ser)
#
#
# def gripClose(ser):
#     buffer = [255, 255, 3, 0, 0, 0, 0, 0, 0]
#     checksum = 0
#     for i in buffer:
#         checksum += i
#     checksum = checksum % 256
#     buffer.append(checksum)
#     print('sending ')
#     print(buffer)
#     sendCommand(buffer, ser)
#
#
# def gripOpen(ser):
#     buffer = [255, 255, 4, 0, 0, 0, 0, 0, 0]
#     checksum = 0
#     for i in buffer:
#         checksum += i
#     checksum = checksum % 256
#     buffer.append(checksum)
#     print('sending ')
#     print(buffer)
#     sendCommand(buffer, ser)
#
#
# def gripHalf(duty, ser):
#     buffer = [255, 255, 10, ]
#     buffer.extend(split_large_ints(duty))
#     buffer.extend([0, 0, 0, 0])
#     checksum = 0
#     for i in buffer:
#         checksum += i
#     checksum = checksum % 256
#     buffer.append(checksum)
#     print('sending ')
#     print(buffer)
#     sendCommand(buffer, ser)
#
#
# def gripRotate(angle, ser):
#     buffer = [255, 255, 5]
#     buffer.extend(split_large_ints(angle))
#     buffer.extend([0, 0, 0, 0])
#     checksum = 0
#     for i in buffer:
#         checksum += i
#     checksum = checksum % 256
#     buffer.append(checksum)
#     print('sending ')
#     print(buffer)
#     sendCommand(buffer, ser)
#
#
# def setAGains(K_P, K_I, K_D, ser):
#     buffer = [255, 255, 6]
#     buffer.extend(split_floats(K_P))
#     buffer.extend(split_floats(K_I))
#     buffer.extend(split_floats(K_D))
#     checksum = 0
#     for i in buffer:
#         checksum += i
#     checksum = checksum % 256
#     buffer.append(checksum)
#     print('sending ')
#     print(buffer)
#     sendCommand(buffer, ser)
#
#
# def setBGains(K_P, K_I, K_D, ser):
#     buffer = [255, 255, 7]
#     buffer.extend(split_floats(K_P))
#     buffer.extend(split_floats(K_I))
#     buffer.extend(split_floats(K_D))
#     checksum = 0
#     for i in buffer:
#         checksum += i
#     checksum = checksum % 256
#     buffer.append(checksum)
#     print('sending ')
#     print(buffer)
#     sendCommand(buffer, ser)
#
#
# def setZGains(K_P, K_I, K_D, ser):
#     buffer = [255, 255, 8]
#     buffer.extend(split_floats(K_P))
#     buffer.extend(split_floats(K_I))
#     buffer.extend(split_floats(K_D))
#     checksum = 0
#     for i in buffer:
#         checksum += i
#     checksum = checksum % 256
#     buffer.append(checksum)
#     print('sending ')
#     print(buffer)
#     sendCommand(buffer, ser)
#
#
# def setTolerances(ser):
#     buffer = [255, 255, 9]
#     tolerances = []
#     for al in ['a', 'b', 'z']:
#         while(1):
#             try:
#                 tolerance = (int(input("set tolerance_" + al + ": ")))
#                 buffer.extend(split_large_ints(tolerance))
#                 break
#             except:
#                 print("try again")
#     checksum = 0
#     for i in buffer:
#         checksum += i
#     checksum = checksum % 256
#     buffer.append(checksum)
#     print('sending ')
#     print(buffer)
#     sendCommand(buffer, ser)

# splits large ints into msb and lsb. Doesn't support ints larger than 16 bits


def split_large_ints(num):
    # numstring = str(hex(num))
    # lsB = '0x'
    # msB = '0x'
    # if len(numstring) < 5:
    #     msB = '0x00'
    # else:
    #     if len(numstring) == 5:
    #         msB += numstring[2]
    #     else:
    #         msB = msB + numstring[len(numstring) - 4] + \
    #             numstring[len(numstring) - 3]
    # if len(numstring) < 4:
    #     lsB += numstring[len(numstring) - 1]
    # else:
    #     lsB = lsB + numstring[len(numstring) - 2] + \
    #         numstring[len(numstring) - 1]
    msB = (num // 256) % 256
    lsB = num % 256

    return [msB, lsB]


# splits floats from their decimals and turns them into ints
def split_floats(num):
    a, b = divmod(num, 1.0)
    a = int(a) % 256
    b = int(b * 256)
    return [a, b]
