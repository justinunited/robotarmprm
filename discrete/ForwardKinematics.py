import numpy as np
from math import sin, cos, sqrt, pi

def Px(q1,q2,q3,q4,q5):

    off = 120 / 180 * pi
    l1 = 371.7
    l2 = 96.12
    l3 = 400
    l4 = 400
    l5 = 89.97
    l6 = 93
    x = l2*cos(q1) - l6*sin(q1)*sin(q5) + l3*cos(off)*cos(q1)*cos(q2) + l4*cos(q1)*cos(q2)*cos(q3) - l3*cos(q1)*sin(off)*sin(q2) - l4*cos(q1)*sin(q2)*sin(q3) + l5*cos(q1)*cos(q2)*cos(q3)*cos(q4) - l5*cos(q1)*cos(q2)*sin(q3)*sin(q4) - l5*cos(q1)*cos(q3)*sin(q2)*sin(q4) - l5*cos(q1)*cos(q4)*sin(q2)*sin(q3) - l6*cos(q1)*cos(q2)*cos(q5)*sin(q3)*sin(q4) - l6*cos(q1)*cos(q3)*cos(q5)*sin(q2)*sin(q4) - l6*cos(q1)*cos(q4)*cos(q5)*sin(q2)*sin(q3) + l6*cos(q1)*cos(q2)*cos(q3)*cos(q4)*cos(q5)
    return x

def Py(q1,q2,q3,q4,q5):
    off = 120 / 180 * pi
    l1 = 371.7
    l2 = 96.12
    l3 = 400
    l4 = 400
    l5 = 89.97
    l6 = 93
    y = l2*sin(q1) + l6*cos(q1)*sin(q5) + l3*cos(off)*cos(q2)*sin(q1) + l4*cos(q2)*cos(q3)*sin(q1) - l3*sin(off)*sin(q1)*sin(q2) - l4*sin(q1)*sin(q2)*sin(q3) + l5*cos(q2)*cos(q3)*cos(q4)*sin(q1) - l5*cos(q2)*sin(q1)*sin(q3)*sin(q4) - l5*cos(q3)*sin(q1)*sin(q2)*sin(q4) - l5*cos(q4)*sin(q1)*sin(q2)*sin(q3) + l6*cos(q2)*cos(q3)*cos(q4)*cos(q5)*sin(q1) - l6*cos(q2)*cos(q5)*sin(q1)*sin(q3)*sin(q4) - l6*cos(q3)*cos(q5)*sin(q1)*sin(q2)*sin(q4) - l6*cos(q4)*cos(q5)*sin(q1)*sin(q2)*sin(q3)
    return y

def Pz(q1,q2,q3,q4,q5):
    off = 120/180*pi
    l1 = 371.7
    l2 = 96.12
    l3 = 400
    l4 = 400
    l5 = 89.97
    l6 = 93
    z = l1 + (l6*sin(q2 + q3 + q4 + q5))/2 + l3*sin(off + q2) + l4*sin(q2 + q3) + (l6*sin(q2 + q3 + q4 - q5))/2 + l5*sin(q2 + q3 + q4)
    # z = l1 + (l6*sin(q2 + q3 + q4 + q5))/2 + l3*sin(off + q2) + l4*sin(q2 + q3) + (l6*sin(q2 + q3 + q4 - q5))/2 + l5*sin(q2 + q3 + q4)

    # z = l1+l4*sin(q2+q3) + (l6*sin(q2+q3+q4-q5))/2 +l5*sin(q2+q3+q4) +(l6*sin(q2+q3+q4+q5)/2 + (sqrt(2)*l3*cos(q2))/2 - (sqrt(2)*l3*sin(q2))/2)
    return z

def Pz2(q1,q2,q3,q4,q5):
    off = 120 / 180 * pi
    l1 = 371.7
    l2 = 96.12
    l3 = 400
    l4 = 400
    l5 = 89.97
    l6 = 93
    z = l1+l3*sin(q2+off)+l4*sin(q2+q3)
    return z

def forward(x):
    for i in x.shape[0]:
        out = np.array([Px(x[i][0],x[i][1],x[i][2],x[i][3],x[i][4]),Py(x[i][0],x[i][1],x[i][2],x[i][3],x[i][4]),Px(x[i][0],x[i][1],x[i][2],x[i][3],x[i][4])])
        if i == 0:
            y = out
        else:
            y = np.concatenate(y,out, axis = 0)
    return y
