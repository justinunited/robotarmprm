import pandas as pd
from collections import OrderedDict
import numpy as np
import heapq

#x1 = [3, 3, 3, 3, 3, 3, 3, 3, 2, 2, 2, 2, 2, 2, 2, 2, 1, 1, 1, 1, 1, 1, 1, 1, 3, 2, 4, 4, 4, 3]
#y1 = [3, 3, 2, 2, 2, 2, 1, 1, 3, 3, 3, 3, 1, 1, 1, 1, 3, 3, 2, 2, 2, 2, 1, 1, 2, 2, 2, 2, 4, 2]
#x2 = [3, 2, 3, 3, 2, 2, 3, 2, 3, 3, 1, 1, 3, 3, 1, 1, 2, 1, 3, 2, 2, 1, 2, 1, 2, 1, 3, 3, 3, 4]
#y2 = [2, 3, 3, 1, 3, 1, 1, 1, 3, 2, 3, 2, 2, 1, 2, 1, 3, 2, 1, 3, 1, 1, 1, 2, 2, 2, 2, 3, 1, 2]

#coord_pairs = pd.DataFrame(
#    OrderedDict((('x1', pd.Series(x1)), ('y1', pd.Series(y1)), ('x2', pd.Series(x2)), ('y2', pd.Series(y2)))))
#coord_pairs = coord_pairs.sort_values(['x1', 'y1'], ascending=[True, True])
#print(coord_pairs)

start = (q1,q2,q3,q4,q5)
goal = (q1,q2,q3,q4,q5)

#### A Star ####
def available_neighbours(current_x,current_y,current_z): ## find neighbours

    return list(zip(coord_pairs.loc[(coord_pairs.x1 == current_x) & (coord_pairs.y1 == current_y) & (coord_pairs.z1 == current_z)][["x2"]].x2,

coord_pairs.loc[(coord_pairs.x1 == current_x) & (coord_pairs.y1 == current_y) & (coord_pairs.z1 == current_z)][["y2"]].y2,

coord_pairs.loc[(coord_pairs.x1 == current_x) & (coord_pairs.y1 == current_y) & (coord_pairs.z1 == current_z)][["z2"]].z2))_pairs.loc[(coord_pairs.x1 == current_x) & (coord_pairs.y1 == current_y)][["y2"]].y2))



def heuristic(a, b):
    return np.sqrt((b[0] - a[0]) ** 2 + (b[1] - a[1]) ** 2 + (b[2] - a[2]) ** 2 + (b[3] - a[3]) ** 2 + (b[4] - a[4]) ** 2)


def astar(start, goal):
    close_set = set()
    came_from = {}
    gscore = {start: 0}
    fscore = {start: heuristic(start, goal)}
    oheap = []

    heapq.heappush(oheap, (fscore[start], start))

    while oheap:

        current = heapq.heappop(oheap)[4]
        print(current)
        neighbours = available_neighbours(current[0], current[1],current[2], current[3], current[4])

        if current == goal:
            data = []
            while current in came_from:
                data.append(current)
                current = came_from[current]
            return data

        close_set.add(current)
        for i, j, k, l, m in neighbours:
            neighbour = i, j, k, l, m
            tentative_g_score = gscore[current] + heuristic(current, neighbour)
            if neighbour in close_set and tentative_g_score >= gscore.get(neighbour, 0):
                continue

            if tentative_g_score < gscore.get(neighbour, 0) or neighbour not in [i[1] for i in oheap]:
                came_from[neighbour] = current
                gscore[neighbour] = tentative_g_score
                fscore[neighbour] = tentative_g_score + heuristic(neighbour, goal)
                heapq.heappush(oheap, (fscore[neighbour], neighbour))

    return False



route = astar(start, goal)
route = route + [start]
route = route[::-1]
print(route)