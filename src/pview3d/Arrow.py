from vtk import *
from numpy import array
from numpy.linalg import norm

from .Object3D import Object3D
from .Extrusion import Extrusion


class Arrow(Object3D):

    _R_SHAFT = 1
    _R_TIP = 2.5

    def __init__(self, p1x = 0, p1y = 0, p1z = 0, p2x = 1, p2y = 0, p2z = 0):
        Object3D.__init__(self)
        self._arrowSource = vtkArrowSource()
        self._matrix4x4 = vtkMatrix4x4()
        self._point1 = [p1x, p1y, p1z]
        self._point2 = [p2x, p2y, p2z]
        self._radius = 0.03
        self._was_too_short = False
        t1 = vtkTransformPolyDataFilter()
        t2 = vtkMatrixToHomogeneousTransform()
        self._arrowSource.SetTipResolution(15)
        self._arrowSource.SetShaftResolution(15)
        self._arrowSource.SetShaftRadius(Arrow._R_SHAFT)
        self._arrowSource.SetTipRadius(Arrow._R_TIP)
        t2.SetInput(self._matrix4x4)
        t1.SetTransform(t2)
        t1.SetInputConnection(self._arrowSource.GetOutputPort())
        spdf = vtkSmoothPolyDataFilter()
        spdf.SetInputConnection(t1.GetOutputPort())
        self._mapper.SetInputConnection(t1.GetOutputPort())
        self._update()

    @property
    def point1(self):
        return self._point1

    @point1.setter
    def point1(self, c):
        self._point1 = c
        self._update()

    @property
    def point2(self):
        return self._point2

    @point2.setter
    def point2(self, c):
        self._point2 = c
        self._update()

    @property
    def radius(self):
        return self._radius

    @radius.setter
    def radius(self, r):
        self._radius = r
        self._update()

    def _update(self):
        p1 = array(self._point1)
        p2 = array(self._point2)
        t = Extrusion.compute_transformation_matrix(p1, p2)
        l = norm(p2 - p1)

        if l < 1e-5:
            if self.visible:
                self.visible = False
                self._was_too_short = True
            return

        if self._was_too_short:
            self.visible = True
            self._was_too_short = False

        if ~(t is None):
            for i in range(0, 3):
                for j in range(0, 3):
                    if j == 0:
                        s = l
                    else:
                        s = self._radius
                    self._matrix4x4.SetElement(i, j, s * t[j, i])
        else:
            self._matrix4x4.Identity()

        for i in range(0, 3):
            self._matrix4x4.SetElement(i, 3, self._point1[i])

        self._arrowSource.SetTipLength(4 * Arrow._R_TIP * self._radius / l)