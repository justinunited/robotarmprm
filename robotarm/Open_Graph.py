from math import pi
from random import uniform
from InverseKinematics import inverseKinematics
import pickle
with open('Graph.gph','rb') as Graph1_file:
    Graph1 = pickle.load(Graph1_file)
# path = Graph1.astar([0,0,0,0,0],[1,-1,1,0,0])
# print(path)
q1,q2,q3,q4,q5 = inverseKinematics(651.74,371.22,776.66,0)
Graph1.visualizexyz_path([1.9994831898801764, -1.1668857339038468, 0.2732125089443369, 0.8936732249595098, 0.5964544091826249]   ,[q1,q2,q3,q4,q5]      )
# print(path)