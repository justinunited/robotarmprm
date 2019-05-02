from math import pi
from random import uniform
import pickle
with open('Graph.gph','rb') as Graph1_file:
    Graph1 = pickle.load(Graph1_file)
# path = Graph1.astar([0,0,0,0,0],[1,-1,1,0,0])
# print(path)
Graph1.visualizexyz_path([2.003087000648988, -1.2055477691605432, 0.3489846690354548, 0.8565631001250884, 0.9341450315936348]  ,[0.507860350961383, -0.8061874860635961, 1.3618140172391935, -0.5556265311755973, -0.507860350961383]        )