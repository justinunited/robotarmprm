import cv2
import numpy as np
import easygui
from random import *
import os, shutil
from keras.preprocessing.image import ImageDataGenerator
from math import atan2, cos,sin,sqrt,pi

cam = cv2.VideoCapture(0)
x_test = []

# thisdict = { 1:'\u0E01', 2:'\u0E02', 3:'\u0E03', 4:'\
#
#
# u0E04', 5:'\u0E05', 6:'\u0E06', 7:'\u0E07', 8:'\u0E08',9:'\u0E09',
#              10:'\u0E0A', 11:'\u0E0B',12:'\u0E0C',13:'\u0E0D',14:'\u0E0E',15:'\u0E0F',16:'\u0E10',
#             17:'\u0E11',18:'\u0E12',19:'\u0E13',20:'\u0E14',21:'\u0E15',22:'\u0E16',23:'\u0E17',24:'\u0E18',
#             25:'\u0E19',26:'\u0E1A',27:'\u0E1B',28:'\u0E1C',29:'\u0E1D',30:'\u0E1E',31:'\u0E1F',32:'\u0E20',
#             33:'\u0E21',34:'\u0E22',35:'\u0E23',36:'\u0E24',37:'\u0E25',38:'\u0E26',39:'\u0E27',40:'\u0E28',
#             41:'\u0E29',42:'\u0E2A',43:'\u0E2B',44:'\u0E2C',45:'\u0E2D',46:'\u0E2E',47:'\u0E2F',48:'\u0E30',
#             49:'\u0E31',50:'\u0E32',51:'\u0E33',52:'\u0E34',53:'\u0E35',54:'\u0E36',55:'\u0E37',56:'\u0E38',
#             57:'\u0E39',58:'\u0E40',59:'\u0E41',60:'\u0E42',61:'\u0E43',62:'\u0E44',63:'\u0E45',64:'\u0E46',
#             65:'\u0E47',66:'\u0E48',67:'\u0E49',68:'\u0E4A',69:'\u0E4B',70:'\u0E4C',71:'\u0E4D',72:'2',}

thisdict = { 0:'0',1:'\u0E01', 2:'\u0E02', 3:'\u0E03', 4:'\u0E04', 5:'\u0E05', 6:'\u0E06', 7:'\u0E07', 8:'\u0E08',9:'\u0E09',
             10:'\u0E0A', 11:'\u0E0B',12:'\u0E0C',13:'\u0E0D',14:'\u0E0E',15:'\u0E0F',16:'\u0E10',
            17:'\u0E11',18:'\u0E12',19:'\u0E13',20:'\u0E14',21:'\u0E15',22:'\u0E16',23:'\u0E17',24:'\u0E18',
            25:'\u0E19',26:'\u0E1A',27:'\u0E1B',28:'\u0E1C',29:'\u0E1D',30:'\u0E1E',31:'\u0E1F',32:'\u0E20',
            33:'\u0E21',34:'\u0E22',35:'\u0E23',36:'\u0E24',37:'\u0E25',38:'\u0E26',39:'\u0E27',40:'\u0E28',
            41:'\u0E29',42:'\u0E2A',43:'\u0E2B',44:'\u0E2C',45:'\u0E2D',46:'\u0E2E',47:'\u0E2F',48:'\u0E30',
            49:'\u0E31',50:'\u0E32',51:'\u0E34',52:'\u0E35',53:'\u0E36',54:'\u0E37',55:'\u0E38',56:'\u0E39',
            57:'\u0E40',58:'\u0E41',59:'\u0E42',60:'\u0E43',61:'\u0E44',62:'\u0E45',63:'\u0E46',64:'\u0E47',
            65:'\u0E48',66:'\u0E49',67:'\u0E4A',68:'\u0E4B',69:'\u0E4C',70:'\u0E4D',71:'1',72:'2',73:'3',74:'4',75:'5',76:'6',77:'7',78:'8',79:'9',80:'slash'}

name = {}
address = {}
namepred_list = []
addresspred_list = []
import matplotlib.pyplot as plt
from keras.models import load_model
from keras.models import Sequential

def inverseKinematics(x,y,z,facing_angle):
    l1 = 340
    l2 = 96.12
    l3 = 400
    l4 = 400
    l5 = 89.97
    l6 = 83
    x5 = x - l6 * cos(facing_angle)
    y5 = y - l6 * sin(facing_angle)
    r = sqrt(x5**2 + y5**2)
    q1 = atan2(y5, x5)
    q5 = facing_angle - q1
    A = z - l1
    B = r - l2 - l5
    cos_q3m3pi = (A ** 2 + B ** 2 - l3 ** 2 - l4 ** 2) / (2 * l3 * l4)
    print(cos_q3m3pi)
    sin_q3m3pi = sqrt(1 - cos_q3m3pi ** 2)
    print(sin_q3m3pi)
    print(atan2(sin_q3m3pi, cos_q3m3pi))
    q3 = atan2(sin_q3m3pi, cos_q3m3pi) + 3 * pi / 4
    print(q3)
    sin_q2 = -(A * l3 ** 2 + B * l3 ** 2 + 2 * A * l4 ** 2 * cos(q3) ** 2 - 2 * B * l4 ** 2 * cos(q3) * sin(q3) - 2 * 2 ** (
                1 / 2) * A * l3 * l4 * cos(q3) - 2 ** (1 / 2) * B * l3 * l4 * cos(q3) + 2 ** (1 / 2) * B * l3 * l4 * sin(
                q3)) / ((2 ** (1 / 2) * l3 - 2 * l4 * cos(q3)) * (
                l3 ** 2 + l4 ** 2 - 2 ** (1 / 2) * l3 * l4 * cos(q3) + 2 ** (1 / 2) * l3 * l4 * sin(q3)))
    cos_q2 = (2 ** (1 / 2) * A * l3 - 2 ** (1 / 2) * B * l3 + 2 * B * l4 * cos(q3) + 2 * A * l4 * sin(q3)) / (
                2 * (l3 ** 2 + l4 ** 2 - 2 ** (1 / 2) * l3 * l4 * cos(q3) + 2 ** (1 / 2) * l3 * l4 * sin(q3)))
    q2 = atan2(sin_q2, cos_q2)
    print('q2',q2)
    if q2 < atan2(z,r):
        q2+=135*pi/180
        q3 = q3 - 270 * pi / 180
    q4 = - q2 - q3

    # rad to degree
    q1 = (q1*180)/pi
    q2 = (q2*180)/pi
    q3 = (q3*180)/pi
    q4 = (q4*180)/pi
    q5 = (q5*180)/pi
    return(q1,q2,q3,q4,q5)


def cleanfolder():
    folder = 'testdetect/folder/'
    for the_file in os.listdir(folder):
        file_path = os.path.join(folder, the_file)
        try:
            if os.path.isfile(file_path):
                os.unlink(file_path)
            elif os.path.isdir(file_path): shutil.rmtree(file_path)
        except Exception as e:
            print(e)

def detectchar(input,number):
    img = input
    h, w = img.shape
    imgsave = img.copy()
    im_gray = img

    # Threshold the image
    # ret, im_th = cv2.threshold(im_gray, 190, 255, cv2.THRESH_BINARY_INV)
    ret,im_th = cv2.threshold(im_gray,0,255,cv2.THRESH_BINARY+cv2.THRESH_OTSU)
    saveimg = im_th.copy()
    # saveimg = cv2.bitwise_not(saveimg)
    cv2.imshow('save', saveimg)
    kernel = np.ones((10, 1), np.uint8)
    im_th = cv2.bitwise_not(im_th)
    im_th = cv2.morphologyEx(im_th, cv2.MORPH_CLOSE, kernel)
    cv2.imshow('im2', im_th)
    # cv2.waitKey(0)

    image, ctrs, hier = cv2.findContours(im_th.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    # # Sort the bounding boxes
    sorted_ctrs = sorted(ctrs, key=lambda ctr: cv2.boundingRect(ctr)[0])
    #
    arealist =[]
    for i, ctr in enumerate(sorted_ctrs):
        x, y, w, h = cv2.boundingRect(ctr)
        roi = saveimg[y-7:y+h+7, x-3:x + w+3]
        if w > 5 or h > 5: #ไม่เอา noise
            roi = cv2.bitwise_not(roi)
            kernel = np.ones((1, 1), np.uint8)
            testchar = cv2.morphologyEx(roi, cv2.MORPH_OPEN, kernel)
            try:
                cv2.imshow('testchar', testchar)
                imag, char, hierc = cv2.findContours(testchar, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
                hulls = [cv2.convexHull(p.reshape(-1, 1, 2)) for p in char]
                roi = cv2.bitwise_not(roi)
            except:
                print('fail')
            for i in range(len(hulls)-1, -1, -1):
                (x, y, w, h) = cv2.boundingRect(hulls[i])
                area = cv2.contourArea(hulls[i])
                # print(area)
                if area > 15:
                    box = roi[y-5:y + h+5, x-1:x + w+1]
                    cv2.imwrite("row/" + 'row(' + str(number) + ')num' + str(i) + '.jpg', box)
                    try:
                        cv2.imshow('box', box)
                        cv2.imwrite("testdetect/folder/" + 'row(' + str(number) + ')num' + str(i) + '.jpg', box)
                    except:
                        print('fail')
                    # cv2.waitKey(0)
                    add_to_list(number)
                    cleanfolder()
    name_pred,address_pred = converttext(namepred_list, addresspred_list)
    return name_pred,address_pred



def add_to_list(num_row):
    filelist = os.listdir('testdetect/folder/')
    for i in filelist:
        if i.endswith(".jpg"):
            img = cv2.imread('testdetect/folder/' + i, 0)
            h, w = img.shape
            if h>10 and w>10:
                img = cv2.resize(img, (24, 20))
                img = img / 255
                img = np.reshape(img, (1, 20, 24, 1))
                # print(i)
                if num_row == 1:
                    namepred_list.append(img)
                else:
                    addresspred_list.append(img)

def converttext(namepred_list,addresspred_list):
    model = load_model('bam_conv3layer3264128_0001.h5')
    name_pred=''
    address_pred=''
    print(len(namepred_list))
    for i in namepred_list:
        pred = model.predict_classes(i)
        n = thisdict[int(pred[0])]
        # print('pred' + str(n))
        name_pred += str(n)
    # print('name'+str(name_pred))
    for i in addresspred_list:
        pred = model.predict_classes(i)
        n = thisdict[int(pred[0])]
        # print('pred' + str(n))
        address_pred += str(n)
    # print('address'+str(address_pred))
    return name_pred,address_pred


def find_key():
    savetext=[]
    for i in name:
        keybox = name[i]
        for key, value in address.items():
            if keybox == value:
                # print(key)
                text = 'Name : ' + str(i) + '   Address : ' + str(key) + '  Position : ' + str(name[i])
                savetext.append(text)
    type_add = easygui.buttonbox("Input?"+'\n\n******************* Information *******************\n'
                               +str('\n'.join(str(i) for i in savetext)),title='Find key', choices=['name', 'address', 'name+address'])
    if type_add == 'name':
        inputname = easygui.enterbox('******************* Information *******************\n'+str('\n'.join(str(i) for i in savetext)),title = 'Find name')
        namescore = score('name',inputname)
        keybox = namescore
        for key, value in address.items():
            if keybox == value:
                delkey = key
        del address[delkey]
        for key, value in name.items():
            if keybox == value:
                delkey = key
        del name[delkey]

    if type_add == 'address':
        inputname = easygui.enterbox('******************* Information *******************\n'+str('\n'.join(str(i) for i in savetext)),title = 'Find address')
        inputaddress = easygui.enterbox("address")
        addressscore = score('address', inputaddress)
        keybox = addressscore
        for key, value in address.items():
            if keybox == value:
                delkey = key
        del address[delkey]
        for key, value in name.items():
            if keybox == value:
                delkey = key
        del name[delkey]

    if type_add == 'name+address':

        fieldNames = ['Name', 'Address']
        fieldValues = []  # we start with blanks for the values
        fieldValues = easygui.multenterbox('******************* Information *******************\n'+str('\n'.join(str(i) for i in savetext)), 'Name,address', fieldNames)
        namescore = score('name',fieldValues[0])
        keybox = namescore
        for key, value in address.items():
            if keybox == value:
                delkey = key
        del address[delkey]
        for key, value in name.items():
            if keybox == value:
                delkey = key
        del name[delkey]

def score(type,name_input):
    nametest =[]
    wtf = []
    splitname=[]
    largesplitname =[]
    for i in name_input:
        # print(i)
        nametest.append(i)
    wtf.append(nametest)
    # print(wtf)
    for i in wtf:
        for j in range(len(i)):
            if j == len(i)-3:
                splitname.append([i[j], i[j + 1],i[j+2],0])
                splitname.append([i[j+1], i[j+2],0,0])
                break
            else:
                splitname.append([i[j],i[j+1],i[j+2],i[j+3]])
        largesplitname.append(splitname)
        splitname=[]
    # print(largesplitname)
    name_pred = []
    name_pred_list = []
    name_list=[]
    address_list =[]
    if type =='name':
        for i in name:
            print(i)
            name_list.append(i)
            print(name_list)
            for j in i:
                name_pred.append(j)
            name_pred_list.append(name_pred)
            name_pred =[]
    if type == 'address':
        for i in address:
            address_list.append(i)
            for j in i:
                name_pred.append(j)
            name_pred_list.append(name_pred)
            name_pred =[]
    # print(name_pred_list)
    score_list=[]
    score=0
    slide = 0
    print((largesplitname[0]))
    print(name_pred_list)
    for counter, value in enumerate(name_pred_list):
        print(value)
        for j ,valuej in enumerate(value):
            # if len(value) <= len(largesplitname[0]):
                if j+slide > len(largesplitname[0])-1:
                    # print(print(j+slide,len(largesplitname[0][len(largesplitname[0])-1])))
                    if valuej in largesplitname[0][len(largesplitname[0])-1]:
                        score = score+1
                else:
                    if valuej in largesplitname[0][j+slide]:
                        pos_slide = [i for i, x in enumerate(largesplitname[0][j+slide]) if valuej == largesplitname[0][j+slide][i]]
                        if pos_slide[0] != 0:
                            print('slide')
                            if j+slide < len(largesplitname[0])-1: #last char don't + slide
                                print(pos_slide)
                                slide = slide+1
                                print(j+slide,len(largesplitname[0])-1)
                            score = score+0.5
                            print(valuej, largesplitname[0][j+slide])
                        else:
                            score = score + 1
                            print(valuej, largesplitname[0][j+slide])
                    else:
                        print('miss'+str(valuej)+str(largesplitname[0][j+slide]))
                        if valuej in largesplitname[0][j + slide-1]:
                            slide = slide-1
                            score = score+1
                # else:
                #     print(valuej, largesplitname[0][len(largesplitname[0])])
            # else:
            #     if j + slide > len(largesplitname[0]) - 1:
            #         print(print(j + slide, len(largesplitname[0][len(largesplitname[0]) - 1])))
            #     else:
            #         if valuej in largesplitname[0][j + slide]:
            #             pos_slide = [i for i, x in enumerate(largesplitname[0][j + slide]) if
            #                          valuej == largesplitname[0][j + slide][i]]
            #             if pos_slide[0] != 0:
            #                 print('slide')
            #                 if j + slide < len(largesplitname[0]) - 1:  # last char don't + slide
            #                     slide = slide + 1
            #                     print(j + slide, len(largesplitname[0]) - 1)
            #                 score = score + 0.5
            #                 print(valuej, largesplitname[0][j + slide])
            #             else:
            #                 score = score + 1
            #                 print(valuej, largesplitname[0][j + slide])
            #         else:
            #             print('miss' + str(valuej) + str(largesplitname[0][j + slide]))
            #             if valuej in largesplitname[0][j + slide - 1]:
            #                 slide = slide - 1
            #                 score = score + 1

        print('score'+str(score))
        score_list.append(score)
        score = 0
        slide = 0
        print('########################################################################')
    print(score_list)
    m = max(score_list)
    out =[i for i, j in enumerate(score_list) if j == m]
    print(out[0])
    print('kkkkkkkkkkkkkkkkkkkkkkkkkkk')
    if type == 'address':
        address_result = address[str(address_list[out[0]])]
        return address_result
    if type == 'name':
        # print(name_list[2],out[0])
        name_result = name[str(name_list[out[0]])]
        return name_result


def check_available():
    all = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    box = []
    for key, value in name.items():
        box.append(value)
    boxint = list(map(int, box))
    available_pos_box = list(set(all) - set(boxint))
    savetext = []
    for i in name:
        keybox = name[i]
        for key, value in address.items():
            if keybox == value:
                # print(key)
                text = 'name : ' + str(i) + '\naddress : ' + str(key) + '\nposition : ' + str(name[i])
                savetext.append(text)
    return available_pos_box,box,savetext


def add_input(nameinput,addressinput,action):
    available_pos_box,box,text = check_available()
    # print(available_pos_box)
    # choice = ['random']
    # for i in available_pos_box:
    #     choice.append(str(i))
    # savetext =[]
    # for i in name:
    #     keybox = name[i]
    #     for key, value in address.items():
    #         if keybox == value:
    #             # print(key)
    #             text = 'Name : ' + str(i) + '   Address : ' + str(key) + '  Position : ' + str(name[i])
    #             savetext.append(text)
    # action = easygui.buttonbox("Do you want add name : \" "+str(nameinput) + ' \"\n'
    #                            +'At position '+str(available_pos_box)
    #                            +'\n\n'+'******************* Information *******************\n'
    #                            +str('\n'.join(str(i) for i in savetext)),title = 'Add input', choices=choice)
    if action == 'random':
        if len(available_pos_box)   >= 1:
            print(available_pos_box)
            pos_box = sample(available_pos_box, 1)
            address[addressinput] = str(pos_box[0])
            name[nameinput] = str(pos_box[0])
        else:
            print('Full')
    elif action != 'random' and action not in box:
        print('self')
        address[addressinput] = action
        name[nameinput] = action



def nothing(x):
  pass

cv2.namedWindow('Colorbars')
cv2.createTrackbar("Max", "Colorbars",0,255,nothing)
cv2.createTrackbar("Min", "Colorbars",0,255,nothing)
cv2.createTrackbar('minArea','Colorbars',0,8000,nothing)
cv2.createTrackbar('maxArea','Colorbars',0,500000,nothing)

num =0

# img = cv2.imread('1.png')
# img = cv2.imread('3.jpg')
# img = cv2.imread('New/New folder/capturetext4.jpg') # edit file name
# h,w, channels = img.shape
# img = img[10:h-10, 10:w-10] #crop image
# imgsave = img.copy()
pic = []

def nothing(x):
  pass







def detectrow():
    # cv2.namedWindow('rowdetect')
    # hh='Max'
    # hl='Min'
    # wnd = 'rowdetect'
    # cv2.createTrackbar('minArea','rowdetect',0,8000,nothing)
    # cv2.createTrackbar('maxArea','rowdetect',0,50000,nothing)
    # small = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)       # grayscale
    small = img
    ret, small = cv2.threshold(small, 86, 255, cv2.THRESH_BINARY)  # *************************************** แก้ threshold
    _, bw = cv2.threshold(small, 0.0, 255.0, cv2.THRESH_BINARY | cv2.THRESH_OTSU) #Threshold
    bw = cv2.bitwise_not(bw)
    minArea = cv2.getTrackbarPos('minArea', 'rowdetect')
    # maxArea = cv2.getTrackbarPos('maxArea', 'rowdetect')
    minArea = 2000
    maxArea = 1000000
    kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (60, 5))
    connected = cv2.morphologyEx(bw, cv2.MORPH_CLOSE, kernel)
    (_, cnts, _) = cv2.findContours(connected.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    sorted_ctrs = sorted(cnts, key=lambda ctr: cv2.boundingRect(ctr)[1])
    cv2.imshow('gray', bw)
    cv2.imshow('connect', connected)
    for contours in sorted_ctrs:
        if cv2.contourArea(contours)> minArea and cv2.contourArea(contours)<maxArea:
            (x, y, w, h) = cv2.boundingRect(contours)
            row = imgsave[y - 7:y + h + 7, x-5:x + w+5]
            cv2.imwrite("row/" + str(h) + '.jpg', row);
            box = [x,y,w,h]
            if box not in pic:
                pic.append(box)
                # print('wtf')

            cv2.rectangle(img, (x, y), (x + w, y + h), (255, 255, 0), 2)
            cv2.imshow('IMG', img)

while(1):
    ret, img = cam.read()
    paper = img.copy()
    kernel_sharpening = np.array([[-1, -1, -1],
                                  [-1, 9, -1],
                                  [-1, -1, -1]])
    # applying the sharpening kernel to the input image & displaying it.
    img = cv2.filter2D(img, -1, kernel_sharpening)
    # minArea = cv2.getTrackbarPos('minArea', 'Colorbars')
    # maxArea = cv2.getTrackbarPos('maxArea', 'Colorbars')
    # maxthres = cv2.getTrackbarPos("Max", "Colorbars")
    # minthres = cv2.getTrackbarPos("Min", "Colorbars")
    minArea = 5000
    maxArea = 500000
    maxthres = 255
    minthres = 90
    img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    ret, th1 = cv2.threshold(img, minthres, maxthres, cv2.THRESH_BINARY)  # *************************************** แก้ threshold
    ret, thres1 = cv2.threshold(th1, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)
    (cnts, _) = cv2.findContours(thres1, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    for contour in cnts:
        if cv2.contourArea(contour) > minArea and cv2.contourArea(contour) < maxArea:
            (x, y, w, h) = cv2.boundingRect(contour)
            box = paper[y:y + h, x:x + w]
            # cv2.drawContours(img, contour, 0, (255, 0, 0), 2)
            cv2.rectangle(img, (x, y), (x + w, y + h), (255, 255, 0), 2)
            area = cv2.contourArea(contour)
            shift = 0
    cv2.imshow('th',thres1)
    cv2.imshow('img', img)
    k = cv2.waitKey(1) & 0xFF
    if k == ord('m'):
        num=0
        # img = cv2.imread('testdetect/capturetext4.jpg',0)  # edit file name
        cv2.imshow('img', img)
        h, w= img.shape
        # img = img[10:h - 10, 10:w -]  # crop image
        imgsave = img.copy()
        detectrow()
        for i in pic:
            x,y,w   ,h = i[0],i[1],i[2],i[3]
            row = imgsave[y-10:y+h+10,x-5:x+w+5]
            # cv2.imwrite("rowdetection/" + str(num) + '.jpg', saveimg);
            num = num+1
            cv2.imshow('saveimg',row)
            # cv2.waitKey(0)
            name_pred,address_pred = detectchar(row,num)
        print('namepred_list : ' + str(name_pred) + '\naddresspred_list : ' + str(address_pred))
        namepred_list.clear()
        addresspred_list.clear()

        # converttext()
        # cleanfolder()
        print('savess')
        pic =[]
    elif k == ord('t'):
        pos_available,box,text = check_available()
        action = easygui.buttonbox("Action?       pos_available : "+str(pos_available)+'\n              not_available : '+str(box) , choices=[' put in(auto)','put in(manual)', 'put out','test mode'])
        if action == 'put in(manual)':
            while(1):
                available_pos_box, box, text = check_available()
                print(available_pos_box)
                choice = ['random']
                for i in available_pos_box:
                    choice.append(str(i))
                savetext = []
                for i in name:
                    keybox = name[i]
                    for key, value in address.items():
                        if keybox == value:
                            # print(key)
                            text = 'Name : ' + str(i) + '   Address : ' + str(key) + '  Position : ' + str(name[i])
                            savetext.append(text)
                print(savetext)
                fieldNames = ['Name', 'Address','position_storage']
                fieldValues = []  # we start with blanks for the values
                fieldValues = easygui.multenterbox('******************* Information *******************\n' + str('\n'.join(str(i) for i in savetext)), 'Put in(manual)', fieldNames)
                print(fieldValues)
                if int(fieldValues[2]) in pos_available and int(fieldValues[2]) < 15:
                    add_input(fieldValues[0],fieldValues[1],fieldValues[2])
                    break
                else:
                    print('try again')
        if action == ' put in(auto)':
            num = 0
            cv2.imshow('img', img)
            h, w = img.shape
            imgsave = img.copy()
            detectrow()
            for i in pic:
                try:
                    x, y, w, h = i[0], i[1], i[2], i[3]
                    row = imgsave[y - 7:y + h + 7, x - 5:x + w + 5]
                    num = num + 1
                    cv2.imshow('saveimg', row)
                    name_pred, address_pred = detectchar(row, num)
                except:
                    print('error save row')
            print('namepred_list : ' + str(name_pred) + '\naddresspred_list : ' + str(address_pred))
            add_input(str(name_pred),str(address_pred),'random')
            print(name,address)
            pic = []
            namepred_list.clear()
            addresspred_list.clear()
        if action == 'put out':
            print('name : '+str(name),'  address :' + str(address))
            find_key()
            print('name : '+str(name),'  address :' + str(address))
            ################################################################################### test mode
        if action == 'test mode':
            testmode = easygui.buttonbox("Kanut test mode",choices=['joint space','task space'])
            if testmode == 'joint space':
                q1, q2, q3, q4, q5 = 0,0,0,0,0
                joint = ['q1','q2', 'q3','q4','q5']
                jointValues = []  # we start with blanks for the values
                jointValues = easygui.multenterbox('Hello','joint space', joint)
                q1, q2, q3, q4, q5 = jointValues[0],jointValues[1],jointValues[2],jointValues[3],jointValues[4]
            if testmode == 'task space':
                q1, q2, q3, q4, q5 = 0, 0, 0, 0, 0
                joint = ['x','y','z', 'q']
                jointValues = []  # we start with blanks for the values
                jointValues = easygui.multenterbox('Hello', 'task space', joint)
                q1,q2,q3,q4,q5 = inverseKinematics(float(jointValues[0]), float(jointValues[1]), float(jointValues[2]),float(jointValues[3]))
            print(q1,q2,q3,q4,q5)
            # Serial here

        cv2.destroyAllWindows()
    elif k == 27:
        break
cv2.waitKey(0)