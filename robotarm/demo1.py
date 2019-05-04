import cv2
import numpy as np
import easygui
from math import pi
from random import uniform
import pickle
from random import *
import os, shutil
from keras.preprocessing.image import ImageDataGenerator
from math import atan2, cos,sin,sqrt,pi

# cam = cv2.VideoCapture(0)
x_test = []

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
size_box_dic = {}


import matplotlib.pyplot as plt
from keras.models import load_model
from keras.models import Sequential
from InverseKinematics import *
from serial_coms_list import *

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
def shelf(number_shelf,size_box):
    offset = 58.50
    number_shelf -= 1
    if number_shelf != 15:
        x_shelf = 650
    else:
        x_shelf = -400
    yz_position = [[371.22,776.66],[70,808.325],[-145,840],[-335,840],[310,484.995],[70,484.995],[-145,600],[-335,600],[310,161.665],[70,161.665], [-145,360],[-335,360],[-145,120],[-335,120],[-650,300]]
    y_shelf = yz_position[number_shelf][0]
    z_shelf = yz_position[number_shelf][1]
    # if size_box == 1:
    #     z_shelf += 100 + offset
    # else:
    #     z_shelf += 75 + offset
    return x_shelf,y_shelf,z_shelf

def saveandsent(xh,yh,zh,acuteDeg,pos,size_box, ser):
    print(':: function save and sent')
    home_config = [0, 0, 0, 0, 0]

    with open('Graph.gph', 'rb') as Graph1_file:
        Graph1 = pickle.load(Graph1_file)

    q1, q2, q3, q4, q5 = inverseKinematics(xh,yh,zh,acuteDeg*pi/180)            #position detect box
    ini_pos = [q1,q2,q3,q4,q5]
    print(pos,'home_config : ',home_config,'ini_pos : ',ini_pos)
    try:
        path1 = Graph1.astar(home_config,ini_pos)        #path 1
    except Exception as e:
        print(e)
    # Graph1.visualizexyz_path(ini_pos,final_pos)
    print('path 1 [path home config to initial final] :',path1)

    for i in range(len(path1)):
        if i == 0:
            pass
        else:
            sendTarget(i[0], i[1],i[2],i[3], i[4], ser)
            time.sleep(0.01)
    goNow(ser)
    gripSucc(ser)
    size_box_dic[pos] = size_box
    print(pos,size_box)
    x,y,z = shelf(int(pos),int(size_box))
    qs1, qs2, qs3, qs4, qs5 = inverseKinematics(float(x), float(y), float(z),0) #position shelf
    final_pos =  [qs1,qs2,qs3,qs4,qs5]

    with open('Graph.gph', 'rb') as Graph1_file:
        Graph1 = pickle.load(Graph1_file)
    print(pos,'initial_box : ',ini_pos,'box_pos : ',final_pos)

    path2 = Graph1.astar(ini_pos,final_pos)
    # Graph1.visualizexyz_path(ini_pos,final_pos)
    print('path 2[path home initial to final] :',path2)
    # for i in range(len(path2)):
    #     if i == 0:
    #         pass
    #     else:
    #         sendTarget(i[0], i[1],i[2],i[3], i[4], ser)
    #         time.sleep(0.01)
    # goNow(ser)
    # gripOpen(ser)


def savesizebox(pos,sizebox):
    size_box_dic[pos] = sizebox
    print('size box dictionary : ',size_box_dic)




def pushout(pos):
    print(':: running function pushout')
    home_config = [0, 0, 0, 0, 0]
    with open('Graph.gph', 'rb') as Graph1_file:
        Graph1 = pickle.load(Graph1_file)


    for key, value in size_box_dic.items():
        if pos == key:
            size_box = value
    # print('out postion shelf',pos,'sizebox',size_box)
    x, y, z = shelf(int(pos), int(size_box))
    qs1, qs2, qs3, qs4, qs5 = inverseKinematics(float(x), float(y), float(z),0)
    box_pos = [qs1, qs2, qs3, qs4, qs5]
    print(pos,'home_config : ',home_config,'box_pos : ',box_pos)

    path1 = Graph1.astar(home_config, box_pos)  # path 1
    # Graph1.visualizexyz_path(ini_pos,final_pos)
    print('path 1 [path home config to initial final] :', path1)

    x, y, z = shelf(15, int(size_box))      #drop position pos = 15
    qd1, qd2, qd3, qd4, qd5 = inverseKinematics(float(x), float(y), float(z),0)
    drop_pos = [qd1, qd2, qd3, qd4, qd5]

    print('box_pos : ',box_pos,'drop_pos : ',drop_pos)
    with open('Graph.gph', 'rb') as Graph1_file:
        Graph1 = pickle.load(Graph1_file)

    path2 = Graph1.astar(box_pos,drop_pos)          #path 2
    path2 = Graph1.astar(box_pos,drop_pos)          #path 2
    # Graph1.visualizexyz_path(ini_pos,final_pos)
    print('path 2[path home initial to final] :',path2)


def detectchar(input,number):
    img = input
    h, w = img.shape
    imgsave = img.copy()
    im_gray = img
    ret,im_th = cv2.threshold(im_gray,0,255,cv2.THRESH_BINARY+cv2.THRESH_OTSU)
    saveimg = im_th.copy()
    # cv2.imshow('save', saveimg)
    kernel = np.ones((10, 1), np.uint8)
    im_th = cv2.bitwise_not(im_th)
    im_th = cv2.morphologyEx(im_th, cv2.MORPH_CLOSE, kernel)
    # cv2.imshow('im2', im_th)
    cv2.waitKey(0)
    ctrs, hier = cv2.findContours(im_th.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    sorted_ctrs = sorted(ctrs, key=lambda ctr: cv2.boundingRect(ctr)[0])
    arealist =[]
    print(len(sorted_ctrs))
    for i, ctr in enumerate(sorted_ctrs):
        x, y, w, h = cv2.boundingRect(ctr)
        roi = saveimg[y-7:y+h+7, x-3:x + w+3]
        if w > 5 or h > 5:
            roi = cv2.bitwise_not(roi)
            kernel = np.ones((1, 1), np.uint8)
            testchar = cv2.morphologyEx(roi, cv2.MORPH_OPEN, kernel)
            try:
                # cv2.imshow('testchar', testchar)
                char, hierc = cv2.findContours(testchar, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
                char = sorted(char, key=lambda ctr: cv2.boundingRect(ctr)[0])
                hulls = [cv2.convexHull(p.reshape(-1, 1, 2)) for p in char]
                roi = cv2.bitwise_not(roi)
            except:
                try:
                    roi = saveimg[y - 7:y + h + 7, x:x + w]
                    kernel = np.ones((1, 1), np.uint8)
                    testchar = cv2.morphologyEx(roi, cv2.MORPH_OPEN, kernel)
                    # cv2.imshow('testchar', testchar)
                    char, hierc = cv2.findContours(testchar, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
                    char = sorted(char, key=lambda ctr: cv2.boundingRect(ctr)[0])
                    hulls = [cv2.convexHull(p.reshape(-1, 1, 2)) for p in char]
                    roi = cv2.bitwise_not(roi)
                except:
                    print('fail detect char+vowel')
            for i in range(len(hulls)):
                (x, y, w, h) = cv2.boundingRect(hulls[i])
                area = cv2.contourArea(hulls[i])
                # print(area)
                if area > 15:
                    box = roi[y-5:y + h+5, x-1:x + w+1]
                    cv2.imwrite("row/" + 'row(' + str(number) + ')num' + str(i) + '.jpg', box)
                    try:
                        # cv2.imshow('box', box)
                        cv2.imwrite("testdetect/folder/" + 'row(' + str(number) + ')num' + str(i) + '.jpg', box)
                    except:
                        print('fail split char+vowel')
                    # cv2.waitKey(0)
                    add_to_list(number)
                    cleanfolder()
    print('len namepred : ',len(namepred_list),' len addresspred : ',len(addresspred_list))
    name_pred,address_pred = converttext(namepred_list, addresspred_list)
    cv2.destroyAllWindows()
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
                if num_row == 1:
                    namepred_list.append(img)
                else:
                    addresspred_list.append(img)

def converttext(namepred_list,addresspred_list):
    model = load_model('bam_conv3layer3264128_0001.h5')
    name_pred=''
    address_pred=''
    # print('len namepred',len(namepred_list))
    for i in namepred_list:
        pred = model.predict_classes(i)
        n = thisdict[int(pred[0])]
        name_pred += str(n)
    # print('name '+str(name_pred))
    for i in addresspred_list:
        pred = model.predict_classes(i)
        n = thisdict[int(pred[0])]
        address_pred += str(n)
    return name_pred,address_pred


def find_key(inputname,type_add):
    savetext=[]
    for i in name:
        keybox = name[i]
        for key, value in address.items():
            if keybox == value:
                text = 'Name : ' + str(i) + '   Address : ' + str(key) + '  Position : ' + str(name[i])
                savetext.append(text)
    if type_add == 'name':
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
        inputaddress = inputname
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
    return  keybox

def score(type,name_input):
    print(':: running function score')
    nametest =[]
    wtf = []
    splitname=[]
    largesplitname =[]
    for i in name_input:
        nametest.append(i)
    wtf.append(nametest)
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
    name_pred = []
    name_pred_list = []
    name_list=[]
    address_list =[]
    if type =='name':
        for i in name:
            name_list.append(i)
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
    score_list=[]
    score=0
    slide = 0
    print('Input function put_out(split) : ',(largesplitname[0]))
    print('Data in database(split) : ',name_pred_list)
    for counter, value in enumerate(name_pred_list):
        print(value)
        for j ,valuej in enumerate(value):
                if j+slide > len(largesplitname[0])-1:
                    if valuej in largesplitname[0][len(largesplitname[0])-1]:
                        score = score+1
                        print(valuej, largesplitname[0][len(largesplitname[0])-1],'correct')
                    else:
                        score = score-1
                        print(valuej, largesplitname[0][len(largesplitname[0])-1],'uncorrect')
                else:
                    if valuej in largesplitname[0][j+slide]:
                        pos_slide = [i for i, x in enumerate(largesplitname[0][j+slide]) if valuej == largesplitname[0][j+slide][i]]
                        if pos_slide[0] != 0:
                            print('slide position')
                            if j+slide < len(largesplitname[0])-1: #last char don't + slide
                                # print(pos_slide)
                                slide = slide+1
                                # print(j+slide,len(largesplitname[0])-1)
                            score = score+0.5
                            print(valuej, largesplitname[0][j+slide],'50% correct slide position')
                        else:
                            score = score + 1
                            print(valuej, largesplitname[0][j+slide],'correct')
                    else:
                        # print('miss'+str(valuej)+str(largesplitname[0][j+slide]))
                        if valuej in largesplitname[0][j + slide-1]:
                            slide = slide-1
                            score = score+1
                            print(valuej, largesplitname[0][j + slide-1], 'correct')
                        else:
                            score = score-1
                            print(valuej, largesplitname[0][j + slide - 1], 'uncorrect')
        print('score ='+str(score))
        score_list.append(score)
        score = 0
        slide = 0
        print('########################################################################')
    print('score list : ',score_list)
    m = max(score_list)
    out =[i for i, j in enumerate(score_list) if j == m]
    print('position max score in score list : ',out[0])

    # max score in list > 1
    if type == 'address':
        if len(out) <= 1:
            address_result = address[str(address_list[out[0]])]
            return address_result
        else:
            print('pls insert name')
    if type == 'name':
        if len(out) <= 1:
            name_result = name[str(name_list[out[0]])]
            return name_result
        else:
            print('pls insert Address')

def check_available():
    all = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10,11,12,13,14]
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
                text = 'name : ' + str(i) + '\naddress : ' + str(key) + '\nposition : ' + str(name[i])
                savetext.append(text)
    return available_pos_box,box,savetext


def add_input(nameinput,addressinput,action):
    available_pos_box,box,text = check_available()
    name_check = []
    address_check = []
    for i in name:
        name_check.append(i)
    for i in address:
        address_check.append(i)
    # print('*****************************************************')
    # print('name : ',name_check,' address : ',address_check)
    # print('*****************************************************')
    # if nameinput not in name_check and addressinput not in address_check:
    if action == 'random':
        if len(available_pos_box)   >= 1:
            print(available_pos_box)
            pos_box = sample(available_pos_box, 1)
            address[addressinput] = str(pos_box[0])
            name[nameinput] = str(pos_box[0])
            return pos_box[0]
        else:
            print('Full')
    if action != 'random' and int(action) in available_pos_box:
        print(box)
        address[addressinput] = action
        name[nameinput] = action
        print(name, address)
        return action
    else:
        # print(action,available_pos_box,type(action))
        print('position shelf not avaliable')
        return 99
    # else:
    #     print('name or address already exist')
    #     return 0



def nothing(x):
  pass

num =0

pic = []

def nothing(x):
  pass




def testdetect(img):
    small = img
    ret, small = cv2.threshold(small, 86, 255,cv2.THRESH_BINARY)  # *************************************** แก้ threshold
    _, bw = cv2.threshold(small, 0.0, 255.0, cv2.THRESH_BINARY | cv2.THRESH_OTSU)  # Threshold
    bw = cv2.bitwise_not(bw)
    print('o0000000000000000000')


def detectrow(img):
    pic = []
    small = img
    ret, small = cv2.threshold(small, 86, 255, cv2.THRESH_BINARY)  # *************************************** แก้ threshold
    _, bw = cv2.threshold(small, 0.0, 255.0, cv2.THRESH_BINARY | cv2.THRESH_OTSU) #Threshold
    bw = cv2.bitwise_not(bw)
    minArea = cv2.getTrackbarPos('minArea', 'rowdetect')
    minArea = cv2.getTrackbarPos('minArea', 'rowdetect')
    minArea = 2000
    maxArea = 1000000
    kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (60, 8))
    connected = cv2.morphologyEx(bw, cv2.MORPH_CLOSE, kernel)
    # cv2.imshow('image', img)
    # cv2.imshow('gray', bw)
    # cv2.imshow('connect', connected)
    # cv2.waitKey(0)
    print("before countour")
    (cnts, _) = cv2.findContours(connected.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    sorted_ctrs = sorted(cnts, key=lambda ctr: cv2.boundingRect(ctr)[1])
    # print(len(sorted_ctrs))
    for contours in sorted_ctrs:
        if cv2.contourArea(contours)> minArea and cv2.contourArea(contours)<maxArea:
            print('Countour Detect !!')
            (x, y, w, h) = cv2.boundingRect(contours)
            box = [x,y,w,h]
            # print(box)
            if box not in pic:
                pic.append(box)
    return pic