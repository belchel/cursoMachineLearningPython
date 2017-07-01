import math
import numpy as np


v1 = [1.2, 2, 3.8, 4.5]
v2 = [0.5, 4.5, 9.6, 3.4]


def dist_eucl(v1,v2):
    v1, v2 = np.array(v1), np.array(v2)
    diff = v1 - v2
    quad_dist = np.dot(diff, diff)
    return math.sqrt(quad_dist)


print('%.2f' % dist_eucl(v1,v2))
