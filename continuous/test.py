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
while len(Graph1.nodelist)<7:
    q1 = uniform(-2/3*pi,2/3*pi)
    q2 = uniform(-185/180*pi,20/180*pi)
    q3 = uniform(3/2*pi,-19/180*pi)
    q4 = -q2-q3
    q5 = uniform(-2/3*pi,2/3*pi)
    # print(q1,q2,q3,q4,q5)
    if q4 > (-2/3*pi) and q4 < (2/3*pi):
        Node_i = Node([q1,q2,q3,q4,q5])
        Graph1.put_node(Node_i)
        # print(len(Graph1.nodelist))
Graph1.connect_graph()
print(Graph1.connection_idx)
# plt.figure(1)
Graph1.visualizexyz()
# fig = plt.figure()
# ax = fig.gca(projection='3d')
# x = obstacle1.vertices[:,0]
# y = obstacle1.vertices[:,1]
# z = obstacle1.vertices[:,2]
#
# ax.plot_surface(x,y,z)
# plt.show(ax)

# from mpl_toolkits.mplot3d import Axes3D
# from mpl_toolkits.mplot3d.art3d import Poly3DCollection
# import numpy as np
# import matplotlib.pyplot as plt
#
# def cuboid_data2(o, size=(1,1,1)):
#     X = [[[0, 1, 0], [0, 0, 0], [1, 0, 0], [1, 1, 0]],
#          [[0, 0, 0], [0, 0, 1], [1, 0, 1], [1, 0, 0]],
#          [[1, 0, 1], [1, 0, 0], [1, 1, 0], [1, 1, 1]],
#          [[0, 0, 1], [0, 0, 0], [0, 1, 0], [0, 1, 1]],
#          [[0, 1, 0], [0, 1, 1], [1, 1, 1], [1, 1, 0]],
#          [[0, 1, 1], [0, 0, 1], [1, 0, 1], [1, 1, 1]]]
#     X = np.array(X).astype(float)
#     for i in range(3):
#         X[:,:,i] *= size[i]
#     X += np.array(o)
#     print(X)
#     return X
#
# def plotCubeAt2(positions,sizes=None,colors=None, **kwargs):
#     if not isinstance(colors,(list,np.ndarray)): colors=["C0"]*len(positions)
#     if not isinstance(sizes,(list,np.ndarray)): sizes=[(1,1,1)]*len(positions)
#     g = []
#     for p,s,c in zip(positions,sizes,colors):
#         g.append( cuboid_data2(p, size=s) )
#     return Poly3DCollection(np.concatenate(g),
#                             facecolors=np.repeat(colors,6), **kwargs)
#
#
# positions = [(-3,5,-2),(1,7,1)]
# sizes = [(4,5,3), (3,3,7)]
# colors = ["crimson","limegreen"]
#
# fig = plt.figure()
# ax = fig.gca(projection='3d')
# ax.set_aspect('equal')
#
# pc = plotCubeAt2(positions,sizes,colors=colors, edgecolor="k")
# ax.add_collection3d(pc)
#
# ax.set_xlim([-4,6])
# ax.set_ylim([4,13])
# ax.set_zlim([-3,9])
#
# plt.show()
#

# from mpl_toolkits.mplot3d import Axes3D
# from mpl_toolkits.mplot3d.art3d import Poly3DCollection
# import matplotlib.pyplot as plt
#
# fig = plt.figure()
# ax = Axes3D(fig)
# x = [0, 1, 1,0]#, 0]
# y = [0, 0, 1,1]#, 1]
# z = [0, 0, 0,0]#, 1]
# verts = [list(zip(x, y, z))]
#
# alpha=0.5
# fc = "C0"
#
# # This line fails to give a semitransparent artist
# pc = Poly3DCollection(verts, alpha = alpha, facecolors=fc, linewidths=1)
#
# ax.add_collection3d(pc)
# plt.show()
