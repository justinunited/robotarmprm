from Obstacle import Obstacle
from Graph import Graph
from Node import Node
from math import pi
from random import uniform
import matplotlib.pyplot as plt
import numpy as np

Graph1 = Graph()

# point1 = np.array([-507.15,1082,746.39])
# point2 = np.array([545.68,0,502.98])
# R = np.array([[0,0,-1],[-1,0,0],[0,1,0]])
# point1 = np.matmul(R,point1)
# point2 = np.matmul(R,point2)


# point1 = point1.tolist()
# point2 = point2.tolist()
# # print(point1)
obstacle1 = Obstacle([-250,-400,600],[250,-200,800])
# print(obstacle1.vertices[:,0])
Graph1.put_obstacle(obstacle1)
while len(Graph1.nodelist)<52:
    q1 = uniform(-2/3*pi,2/3*pi)
    q2 = uniform(-185/180*pi,20/180*pi)
    q3 = uniform(-19/180*pi,3/2*pi)
    q4 = -q2-q3
    q5 = uniform(-2/3*pi,2/3*pi)
    # print(q1,q2,q3,q4,q5)
    if q4 > (-2/3*pi) and q4 < (2/3*pi):
        Node_i = Node([q1,q2,q3,q4,q5])
        Graph1.put_node(Node_i)
    print(len(Graph1.nodelist))
Graph1.connect_graph()
path = Graph1.astar([0,0,0,0,0],[1,-1,1,0,0])
print(path)
