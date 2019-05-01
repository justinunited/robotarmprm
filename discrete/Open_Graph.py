from math import pi
from random import uniform
import pickle
with open('Graph.gph','rb') as Graph1_file:
    Graph1 = pickle.load(Graph1_file)
path = Graph1.astar([0,0,0,0,0],[1,-1,1,0,0])
print(path)
# Graph1.visualizexyz_path([0,0,0,0,0],[1,-1,1,0,0])