from ForwardKinematics import Px,Py,Pz
from Node import Node
import matplotlib.pyplot as plt
import numpy as np
from mpl_toolkits.mplot3d.art3d import Poly3DCollection,Line3DCollection
from mpl_toolkits.mplot3d import Axes3D
from math import sqrt




class Graph:
    def __init__(self):
        self.nodelist = []
        self.obstaclelist = []
        self.connection_idx = []

    def put_node(self,Node):
        (q1,q2,q3,q4,q5) = Node.config[0],Node.config[1],Node.config[2],Node.config[3],Node.config[4]
        x = Px(q1,q2,q3,q4,q5)
        y = Py(q1,q2,q3,q4,q5)
        z = Pz(q1,q2,q3,q4,q5)
        intersect = 0
        if z<0:
            intersect = 1
        if intersect == 0:
            for i in self.obstaclelist:
                if i.twopoint[0][0] < x and i.twopoint[1][0] > x and i.twopoint[0][1] < y and i.twopoint[1][1] > y and i.twopoint[0][2] < z and i.twopoint[1][2] > z:
                    intersect = 1
                    break
        if intersect == 0:
            self.nodelist.append(Node)

    def put_obstacle(self,obstacle):
        self.obstaclelist.append(obstacle)

    def visualize15z(self):
        pointlist = []
        for i in self.nodelist:
            (q1, q2, q3, q4, q5) = i.config[0], i.config[1], i.config[2], i.config[3], i.config[4]
            z = Pz(q1, q2, q3, q4, q5)
            pointlist.append([q1,q5,z])
        np_pointlist = np.array(pointlist)
        q1list = np_pointlist[:,0]
        q5list = np_pointlist[:,1]
        zlist = np_pointlist[:, 2]
        fig = plt.figure()
        ax = fig.gca(projection='3d')
        ax.scatter(q1list,q5list,zlist)
        for i in self.connection_idx:
            config_a = self.nodelist[i[0]].config
            config_b = self.nodelist[i[1]].config
            z_1 = Pz(config_a[0],config_a[1],config_a[2],config_a[3],config_a[4])
            z_2 = Pz(config_b[0],config_b[1],config_b[2],config_b[3],config_b[4])
            q1 = [config_a[0],config_b[0]]
            q5 = [config_a[4],config_b[4]]
            z = [z_1,z_2]
            ax.plot(q1,q5,z, color='red')
        plt.show(ax)

    def visualizexyz(self):
        xlist = []
        ylist = []
        zlist = []
        for i in self.nodelist:
            (q1, q2, q3, q4, q5) = i.config[0], i.config[1], i.config[2], i.config[3], i.config[4]
            x = Px(q1, q2, q3, q4, q5)
            y = Py(q1, q2, q3, q4, q5)
            z = Pz(q1, q2, q3, q4, q5)
            xlist.append(x)
            ylist.append(y)
            zlist.append(z)
        x_np = np.array(xlist)
        y_np = np.array(ylist)
        z_np = np.array(zlist)
        fig = plt.figure()
        ax = fig.gca(projection='3d')
        ax.scatter(x_np, y_np, z_np)

        for i in self.obstaclelist:
            xmin,ymin,zmin = i.twopoint[0]
            xmax,ymax,zmax = i.twopoint[1]
            sq1 = np.array([[xmin,ymin,zmin],[xmin,ymin,zmax],[xmax,ymin,zmax],[xmax,ymin,zmin]])
            sq2 = np.array([[xmin,ymin,zmin],[xmin,ymax,zmin],[xmax,ymax,zmin],[xmax,ymin,zmin]])
            sq3 = np.array([[xmin,ymin,zmin],[xmin,ymin,zmax],[xmin,ymax,zmax],[xmin,ymax,zmin]])
            sq4 = np.array([[xmin,ymin,zmax],[xmin,ymax,zmax],[xmax,ymax,zmax],[xmax,ymin,zmax]])
            sq5 = np.array([[xmax,ymin,zmin],[xmax,ymax,zmin],[xmax,ymax,zmax],[xmax,ymin,zmax]])
            sq6 = np.array([[xmin,ymax,zmin],[xmax,ymax,zmin],[xmax,ymax,zmax],[xmin,ymax,zmax]])
            squarelist = [sq1,sq2,sq3,sq4,sq5,sq6]
            for i in squarelist:
                x = i[:,0]
                y = i[:,1]
                z = i[:,2]
                verts = [list(zip(x,y,z))]
                pc = Poly3DCollection(verts,facecolors='g')
                line = Line3DCollection(verts, colors='k', linewidths=0.5)
                ax.add_collection3d(pc)
                ax.add_collection(line)
        for i in self.connection_idx:
            config_a = self.nodelist[i[0]].config
            config_b = self.nodelist[i[1]].config
            x_1 = Px(config_a[0],config_a[1],config_a[2],config_a[3],config_a[4])
            y_1 = Py(config_a[0],config_a[1],config_a[2],config_a[3],config_a[4])
            z_1 = Pz(config_a[0],config_a[1],config_a[2],config_a[3],config_a[4])
            x_2 = Px(config_b[0],config_b[1],config_b[2],config_b[3],config_b[4])
            y_2 = Py(config_b[0],config_b[1],config_b[2],config_b[3],config_b[4])
            z_2 = Pz(config_b[0],config_b[1],config_b[2],config_b[3],config_b[4])
            x = [x_1,x_2]
            y = [y_1,y_2]
            z = [z_1,z_2]
            ax.plot(x,y,z,color='red')
        plt.show(ax)

    def connect_graph(self):
        for a in range(len(self.nodelist)):
            for b in range(len(self.nodelist)):
                if self.nodelist[a] == self.nodelist[b] or (b,a) in self.connection_idx or (a,b) in self.connection_idx:
                    continue
                no_colission = True
                q1 = np.array(self.nodelist[a].config)
                q2 = np.array(self.nodelist[b].config)
                diff = q1-q2
                dis_s = np.square(diff)
                sum = np.sum(dis_s)
                dis = np.sqrt(sum)
                if dis > 7:
                    continue
                q0_1,q0_2,q0_3,q0_4,q0_5 = self.nodelist[a].config
                q1_1,q1_2,q1_3,q1_4,q1_5 = self.nodelist[b].config
                x0 = Px(q0_1,q0_2,q0_3,q0_4,q0_5)
                y0 = Py(q0_1,q0_2,q0_3,q0_4,q0_5)
                z0 = Pz(q0_1,q0_2,q0_3,q0_4,q0_5)
                x1 = Px(q1_1,q1_2,q1_3,q1_4,q1_5)
                y1 = Py(q1_1,q1_2,q1_3,q1_4,q1_5)
                z1 = Pz(q1_1,q1_2,q1_3,q1_4,q1_5)
                P0 = np.array([x0,y0,z0])
                P1 = np.array([x1,y1,z1])
                #check if line is parallel to any axis
                pdif = P1-P0
                non_zero = np.count_nonzero(pdif)
                if non_zero != 3:
                    continue
                for c in self.obstaclelist:
                    #find whether P0 or P1 is closer to the obstacle
                    dis0 = []
                    dis1 = []
                    for d in c.vertices:
                        dis_e = sqrt((P0[0]-d[0])**2 + (P0[1]-d[1])**2 +(P0[2]-d[2])**2)
                        dis_e1 = sqrt((P1[0]-d[0])**2 + (P1[1]-d[1])**2 +(P1[2]-d[2])**2)
                        dis0.append(dis_e)
                        dis1.append(dis_e1)
                    mindis0 = min(dis0)
                    mindis1 = min(dis1)

                    if mindis1<mindis0:
                        temp = P0
                        P0 = P1
                        P1 = temp
                        dis0 = dis1

                    #find the nearest and farthest vertices
                    idx_f0 = dis0.index(min(dis0))
                    idx_f1 = dis0.index(max(dis0))
                    f0 = c.vertices[idx_f0]
                    f1 = c.vertices[idx_f1]
                    print(f0,f1)
                    #find time representation of collision at each plane
                    t0_x = ((f0[0] - P0[0]) / (P1[0] - P0[0]))
                    t0_y = ((f0[1] - P0[1]) / (P1[1] - P0[1]))
                    t0_z = ((f0[2] - P0[2]) / (P1[2] - P0[2]))
                    t1_x = ((f1[0] - P0[0]) / (P1[0] - P0[0]))
                    t1_y = ((f1[1] - P0[1]) / (P1[1] - P0[1]))
                    t1_z = ((f1[2] - P0[2]) / (P1[2] - P0[2]))
                    t0list = [t0_x,t0_y,t0_z]
                    t1list = [t1_x,t1_y,t1_z]
                    t0 = max(t0list)
                    t1 = min(t1list)
                    if t0<=t1:
                        no_colission = False
                        break
                # print(no_colission)
                if no_colission == True:
                    self.connection_idx.append((a,b))
                    self.nodelist[a].connectedNode.append(b)
                    self.nodelist[b].connectedNode.append(a)
