from Obstacle import Obstacle
from Graph import Graph
from Node import Node
from math import pi
from random import uniform
import pickle
import matplotlib.pyplot as plt
import numpy as np
from math import sin, cos, atan2, pi,sqrt
from ForwardKinematics import Px, Py, Pz,Pz2
from InverseKinematics import inverseKinematics
# print(Pz(0,-0.5,0.5,0,0))
# print(Pz2(0,-0.5,0.5,0,0))
# from mpl_toolkits.mplot3d import Axes3D
# fig = plt.figure()
# ax = fig.gca(projection='3d')


#
# ### simulation code
Graph1 = Graph()
# obstacle1 = Obstacle([536.5,513,0],[712.88,-552.32,40])
# obstacle2 = Obstacle([536.5,513.79,1052],[712.88,-552.32,1082])
# obstacle3 = Obstacle([535.87,493.8,40],[713.51,439.18,1052])
# obstacle4 = Obstacle([535.13,-477.71,40],[713.51,-532.33,1052])
# obstacle5 = Obstacle([536.5,435.83,361.47],[728.82,-48.33,387.34])
# obstacle6 = Obstacle([536.5,435.83,722.8],[728.82,-48.33,748.67])
# obstacle7 = Obstacle([536.5,225.94,40],[728.82,171.32,1052])
# obstacle8 = Obstacle([536.5,-41.93,40],[728.82,-96.55,1052])
# obstacle9 = Obstacle([536.5,-96.55,238],[728.82,-477.71,286])
# obstacle10 = Obstacle([536.5,-96.55,516],[728.82,-477.71,564])
# obstacle11 = Obstacle([536.5,-96.55,784],[728.82,-477.71,832])
# obstacle12 = Obstacle([536.5,-259.82,40],[728.82,-314.44,1052])
# base1 = Obstacle([-220,-470,0],[-300,-830,310])
# Graph1.put_obstacle(base1)
# obstacle1 = Obstacle([200,570,0],[820,440,1069.99])
# obstacle2 = Obstacle([200,-440,0],[820,-570,1069.99])
# obstacle3 = Obstacle([490,-350,0],[810,-560,1069.99])
# obstacle4 = Obstacle([490,560,969.99],[810,-470,1069.99])
# obstacle5 = Obstacle([490,560,0],[820,-570,40])
# obstacle6 = Obstacle([490,310,10],[820,180,1059.99])
# obstacle7 = Obstacle([490,60,10],[820,-70,1059.99])
# obstacle8 = Obstacle([490,-130,10],[820,-270,1059.99])
# obstacle9 = Obstacle([490,550,606.66],[820,-60,736.66])
# obstacle10 = Obstacle([490,550,273.33],[820,-60,403.33])
# obstacle11 = Obstacle([490,10,720],[820,-470,790])
# obstacle12 = Obstacle([490,10,470],[820,-470,540])
# obstacle13 = Obstacle([490,10,220],[820,-470,290])
# Graph1.put_obstacle(obstacle1)
# Graph1.put_obstacle(obstacle2)
# Graph1.put_obstacle(obstacle3)
# Graph1.put_obstacle(obstacle4)
# Graph1.put_obstacle(obstacle5)
# Graph1.put_obstacle(obstacle6)
# Graph1.put_obstacle(obstacle7)
# Graph1.put_obstacle(obstacle8)
# Graph1.put_obstacle(obstacle9)
# Graph1.put_obstacle(obstacle10)
# Graph1.put_obstacle(obstacle11)
# Graph1.put_obstacle(obstacle12)
# Graph1.put_obstacle(obstacle13)
# while len(Graph1.nodelist)<300:
#     q1 = uniform(-2/3*pi,2/3*pi)
#     q2 = uniform(-185/180*pi,20/180*pi)
#     q3 = uniform(-19/180*pi,3/2*pi)
#     q4 = -q2-q3
#     q5 = uniform(-80*pi/180,80*pi/180)
#     # print(q1,q2,q3,q4,q5)
#     x5 = Px(q1,q2,q3,q4,q5)-83*cos(q1+q5)
#     y5 = Py(q1,q2,q3,q4,q5)-83*sin(q1+q5)
#     z = Pz(q1,q2,q3,q4,q5)
#     r = sqrt(x5**2+y5**2)
#     if q2+2*pi/3 < atan2(z,r):
#         continue
#     if q4 > (-2/3*pi) and q4 < (2/3*pi):
#         Node_i = Node([q1,q2,q3,q4,q5])
#         Graph1.put_node(Node_i)
#     print(len(Graph1.nodelist))
# while len(Graph1.nodelist)<330:
#     x = uniform(400,550)
#     y = uniform(-500,500)
#     z = uniform(40,300)
#     q1,q2,q3,q4,q5 = inverseKinematics(x,y,z,0)
#     Node_i = Node([q1, q2, q3, q4, q5])
#     Graph1.put_node(Node_i)
#     print(len(Graph1.nodelist))
# Graph1.connect_graph()
# filename = 'Graph.gph'
# with open(filename,'wb') as Graphfile:
#     pickle.dump(Graph1,Graphfile)

# path = Graph1.astar([0,0,0,0,0],[1,-1,1,0,0])
# print(path)
# print('done')
# Graph1.visualizexyz()
# Graph1.visualizexyz_path([0,0,0,0,0],[1,-1,1,0,0])
# Graph1.visualize15zpath([0,0,0,0,0],[1,-1,1,0,0])
# from ForwardKinematics import Px,Py,Pz
# from InverseKinematics import inverseKinematics
#
print(Px(0,0,0,0,0),Py(0,0,0,0,0),Pz(0,0,0,0,0))
print(inverseKinematics(479.09000000000015,0.0,718.1101615137754,0))
# print(Px(0.0, -0.24541250634982736, 0.21370438653764268, 0.03170811981218469, 0q.0),Py(0.0, -0.24541250634982736, 0.21370438653764268, 0.03170811981218469, 0.0),Pz(0.0, -0.24541250634982736, 0.21370438653764268, 0.03170811981218469, 0.0))
