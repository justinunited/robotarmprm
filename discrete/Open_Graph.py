from math import pi
from random import uniform
from InverseKinematics import inverseKinematics
import pickle
with open('Graph.gph','rb') as Graph1_file:
    Graph1 = pickle.load(Graph1_file)
# path = Graph1.astar([0,0,0,0,0],[1,-1,1,0,0])
# print(path)
q1,q2,q3,q4,q5 = inverseKinematics(651.74,371.22,776.66,0)
Graph1.visualizexyz_path([2.0076841941291534, -1.1829360522808943, 0.2995397541333982, 0.8833962981474961, 0.5882534049336479]  ,[q1,q2,q3,q4,q5]      )
# print(path)