import cv2
import numpy as np
import math

def findCM(box):
    p1 = box[0]
    p2 = box[2]
    x1 = p1[0]
    y1 = p1[1]
    x2 = p2[0]
    y2 = p2[1]
    xcm_2 = (x1+x2)*0.5
    ycm_2 = (y1+y2)*0.5
    return xcm_2,ycm_2

def distanceBetweenPoint(x1,y1,x2,y2):
    dx = x1-x2
    dy = y1-y2
    dist_2 = math.sqrt(dx**2 + dy**2)
    return dist_2

def findEquation(x1,y1,x2,y2):
    dx = x1-x2
    dy = y1-y2
    if dx != 0:
        m_2 = dy/dx
    else:
        m_2 = 0.0001
        print("denominator error, dx=0")
    c_2 = y1-m_2*x1
    return m_2,c_2

def findDegree(box):
    p1 = box[0]
    p2 = box[1]
    p3 = box[2]
    x1 = p1[0]
    y1 = p1[1]
    x2 = p2[0]
    y2 = p2[1]
    x3 = p3[0]
    y3 = p3[1]
    dist1 = distanceBetweenPoint(x1,y1,x2,y2)
    dist2 = distanceBetweenPoint(x2,y2,x3,y3)
    if dist1>dist2:
        side= dist2
        xf1 = x1
        yf1 = y1
        xf2 = x2
        yf2 = y2
    else:
        side = dist1
        xf1 = x2
        yf1 = y2
        xf2 = x3
        yf2 = y3
    m1_2,c1 = findEquation(xf1,yf1,xf2,yf2)
    dmx = abs(m1_2)
    acuteRad = math.atan2(dmx,1)
    acuteDeg_2 = acuteRad * (180/math.pi)
    if m1_2 > 0:
        acuteDeg_2 = 180 - acuteDeg_2
    # Change to World Coordinate
    acuteDeg_2+=90
    if acuteDeg_2 >= 180:
        acuteDeg_2-=180
    return m1_2,acuteDeg_2,side

def findBoxSize(box):
    p1 = box[0]
    p2 = box[1]
    p3 = box[2]
    x1 = p1[0]
    y1 = p1[1]
    x2 = p2[0]
    y2 = p2[1]
    x3 = p3[0]
    y3 = p3[1]
    dist1 = distanceBetweenPoint(x1,y1,x2,y2)
    dist2 = distanceBetweenPoint(x2,y2,x3,y3)
    if dist1 + dist2 > 200 :
        return 1 # BIG
    else:
        return 0

def findBoxRef(xcm,ycm,size,ratio):
    xcm = xcm*ratio
    ycm = ycm*ratio
    y_2 = 800-xcm
    x_2 = -250-ycm
    if size == 1:
        z_2 = 280+100
    else:
        z_2 = 280+75
    return x_2,y_2,z_2

def nothing(x):
    # any operation
    pass

def camera2():
    offset = 58.50
    print('calling camera')
    cap = cv2.VideoCapture(0)
    whileLoop = True
    while whileLoop :
        ratio = 284 / 300
        _, frame = cap.read()
        frame2 = frame[130:400,170:470]
        ret, thresh = cv2.threshold(frame2, 127, 255, cv2.THRESH_BINARY)
        ##### Check Box Colour @ (x,y) = (150,135)
        white_box = 0
        if np.all(thresh[150][135] == np.array([255,255,255])):
            white_box = 1

        if white_box == 0:
            hsv = cv2.cvtColor(frame2, cv2.COLOR_BGR2HSV)
            maxArea = 100000
            minArea = 1000
            low = np.array([0, 42, 0])
            high = np.array([179, 255, 255])
            mask = cv2.inRange(hsv, low, high)
            contours, _ = cv2.findContours(mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
            for i in range(len(contours)):
                    if cv2.contourArea(contours[i])> minArea and cv2.contourArea(contours[i])< maxArea:
                        rect = cv2.minAreaRect(contours[i])
                        box = cv2.boxPoints(rect)
                        box = np.int0(box)
                        xcm,ycm = findCM(box)
                        m1,acuteDeg,side = findDegree(box)
                        DEG = "Degree = " + str(acuteDeg)
                        size = findBoxSize(box)
                        xh,yh,zh = findBoxRef(xcm,ycm,size,ratio)
                        zh += offset
                        print(' NON-WHITE BOX DETECT!')
                        print(DEG)
                        print("HomeConfig = " + "("+str(xh)+","+str(yh)+","+str(zh)+")")
                        print(":: Box side length = " + str(side*ratio))
                        whileLoop = False
        else:
            gray = cv2.cvtColor(frame2, cv2.COLOR_BGR2GRAY)
            maxArea = 100000
            minArea = 2000
            mask = cv2.Canny(gray, 50, 50)
            kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (15, 15))
            mask = cv2.morphologyEx(mask, cv2.MORPH_CLOSE, kernel)
            contours, hierarchy = cv2.findContours(mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
            for i in range(len(contours)):
                if cv2.contourArea(contours[i]) > minArea and cv2.contourArea(contours[i]) < maxArea:
                    rect = cv2.minAreaRect(contours[i])
                    box = cv2.boxPoints(rect)
                    box = np.int0(box)
                    xcm, ycm = findCM(box)
                    m1,acuteDeg,side = findDegree(box)
                    if side*ratio <= 120 and side*ratio >= 75:
                        DEG = "Degree = " + str(acuteDeg)
                        size = findBoxSize(box)
                        xh, yh, zh = findBoxRef(xcm, ycm, size,ratio)
                        zh += offset
                        print(' WHITE BOX DETECT!')
                        print(DEG)
                        print("HomeConfig = " + "(" + str(xh) + "," + str(yh) + "," + str(zh) + ")")
                        print(":: Box side length = " + str(side * ratio))
                        # whileLoop = False
                    cv2.imshow('frame2', frame2)
                    cv2.imshow("Mask", mask)
                    key = cv2.waitKey(1)
                    if key == 27:
                        break
    cap.release()
    return xh,yh,zh,acuteDeg,size