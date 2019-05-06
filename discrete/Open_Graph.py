from math import pi
from random import uniform
from InverseKinematics import inverseKinematics
from Node import Node
from ForwardKinematics import Px,Py,Pz
import pickle
with open('Graph.gph','rb') as Graph1_file:
    Graph1 = pickle.load(Graph1_file)
x = Px(0,0,0,0,0)
y = Py(0,0,0,0,0)
z = Pz(0,0,0,0,0)
print(x,y,z)
q1,q2,q3,q4,q5 = inverseKinematics(-380, -632, 510, -pi / 2)
# print(q1,q2,q3,q4,q5)
q1_f,q2_f,q3_f,q4_f,q5_f = inverseKinematics(436.76, 122.22, 563.33, 0)
Graph1.visualizexyz_path([-1.0308961180703955, 0.0925216937435418, 1.0356925838733066, -1.1282142776168484, 0.27450632311632295],[q1_f,q2_f,q3_f,q4_f,q5_f])
# Graph1.visualizexyz_path([q1,q2,q3,q4,q5],[q1_f,q2_f,q3_f,q4_f,q5_f])
# print(path)

# a = []
#
# Graph1.put_node(Node())
# q1, q2, q3, q4, q5 = inverseKinematics(611.74, 411.22, 776.66, 0)
# # q1, q2, q3, q4, q5 = inverseKinematics(611.74, 500, 100, 0)
# Graph1.visualizexyz_path([1.998590624097611, -1.1340952935402997, 0.4191005098991618, 0.7149947836411379, 1.1429020294925154],[q1,q2,q3,q4,q5])
# path = Graph1.astar([1.998590624097611, -1.1340952935402997, 0.41910050/98991618, 0.7149947836411379, 1.1429020294925154],[0.12283523887789499, -1.6068121493671421, 0.11566883679923867, 1.4911433125679034, -0.12283523887789499])
# path = Graph1.astar([2.0076841941291534, -1.1829360522808943, 0.2995397541333982, 0.8833962981474961, 0.5882534049336479]  ,[q1,q2,q3,q4,q5])
# Graph1.visualizexyz()
# print(path)
# 10 initial_box :  [1.998590624097611, -1.1340952935402997, 0.4191005098991618, 0.7149947836411379, 1.1429020294925154] box_pos :  [0.12283523887789499, -1.6068121493671421, 0.11566883679923867, 1.4911433125679034, -0.12283523887789499]