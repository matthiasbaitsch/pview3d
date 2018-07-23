from math import sqrt
from numpy import zeros
from numpy.linalg import norm


class Extrusion:

    @staticmethod
    def compute_transformation_matrix(p1, p2):
        t = zeros((3, 3))
        l = norm(p2 - p1)
        c = (p2 - p1) / l
        cx = c[0]
        cy = c[1]
        cz = c[2]
        d = sqrt(cx**2 + cy**2)

        if l < 1e-10:
            return None
        elif d < 1e-10:
            if c[2] < 0:
                cz = -1
            else:
                cz = 1
            t[0][2] = cz
            t[1][1] = 1
            t[2][0] = -cz
        else:
            t[0][0] = cx
            t[0][1] = cy
            t[0][2] = cz
            t[1][0] = -cy / d
            t[1][1] = cx / d
            t[1][2] = 0
            t[2][0] = -cx * cz / d
            t[2][1] = -cy * cz / d
            t[2][2] = d

        return t
