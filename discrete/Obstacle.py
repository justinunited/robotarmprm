import numpy as np
class Obstacle:
    def __init__(self,point1,point2):
        vertices = []
        point_min = (min(point1[0],point2[0]),min(point1[1],point2[1]),min(point1[2],point2[2]))
        point_max = (max(point1[0],point2[0]),max(point1[1],point2[1]),max(point1[2],point2[2]))
        self.twopoint = (point_min,point_max)
        list = point1 = [point1,point2]
        for a in range(len(list)):
            for b in range(len(list)):
                for c in range(len(list)):
                    vertices.append([list[a][0],list[b][1],list[c][2]])
        self.vertices = np.array(vertices)