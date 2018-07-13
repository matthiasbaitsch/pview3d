from vtk import *
from numpy import array
from numpy.linalg import norm

from .Object3D import Object3D


class Cone(Object3D):

    def __init__(self):
        Object3D.__init__(self)
        self._center = [0, 0, 0]
        self._direction = [0, 0, 1]
        self._coneSource = vtkConeSource()
        self._height = 1
        self._radius = 0.5
        self._mapper.SetInputConnection(self._coneSource.GetOutputPort())
        self.resolution = 40
        self._update()

    @property
    def center(self):
        return self._center

    @center.setter
    def center(self, c):
        self._center = c
        self._update()

    @property
    def direction(self):
        return self._direction

    @direction.setter
    def direction(self, d):
        self._direction = d
        self._update()

    @property
    def height(self):
        return self._height

    @height.setter
    def height(self, h):
        self._height = h
        self._update()

    @property
    def radius(self):
        return self._radius

    @radius.setter
    def radius(self, r):
        self._radius = r
        self._update()

    @property
    def resolution(self):
        return self._coneSource.GetResolution()

    @resolution.setter
    def resolution(self, r):
        self._coneSource.SetResolution(r)

    def _update(self):
        c = array(self._center)
        d = array(self._direction)
        cc = c + 0.5 * self._height / norm(self._direction) * d
        self._coneSource.SetRadius(self._radius)
        self._coneSource.SetHeight(self._height)
        self._coneSource.SetCenter(cc.tolist())
        self._coneSource.SetDirection(self._direction)
        self._coneSource.Modified();
