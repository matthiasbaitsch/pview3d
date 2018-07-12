from vtk import *
from .Object3D import Object3D


class CylinderSet(Object3D):

    def __init__(self):
        Object3D.__init__(self)
        self._cells = vtkCellArray()
        self._maxR = -1e10
        self._minR = 1e10
        self._points = vtkPoints()
        self._polyData = vtkPolyData()
        self._radii = vtkDoubleArray()
        self._tubeFilter = vtkTubeFilter()
        self._polyData.GetPointData().SetScalars(self._radii)
        self._polyData.SetPoints(self._points)
        self._polyData.SetLines(self._cells)
        self._tubeFilter.SetInputData(self._polyData)
        self.set_number_of_sides(10)
        self._tubeFilter.CappingOn()
        self._mapper.ScalarVisibilityOff()
        self._mapper.SetInputConnection(self._tubeFilter.GetOutputPort())

    def add_cylinder(self, p1, p2, radius):
        self._cells.InsertNextCell(2);
        self._cells.InsertCellPoint(self._points.InsertNextPoint(p1));
        self._cells.InsertCellPoint(self._points.InsertNextPoint(p2));
        self._radii.InsertNextValue(radius);
        self._radii.InsertNextValue(radius);
        if radius < self._minR:
            self._minR = radius
            self._adjust_r()
        if radius > self._maxR:
            self._maxR = radius
            self._adjust_r()

    def set_number_of_sides(self, n):
        self._tubeFilter.SetNumberOfSides(n)

    def clear(self):
        self._minR = 1e10
        self._maxR = -1e10
        self._polyData.Reset()

    def _adjust_r(self):
        if self._minR == self._maxR:
            self._tubeFilter.SetRadius(self._minR)
            self._tubeFilter.SetVaryRadiusToVaryRadiusOff()
        else:
            self._tubeFilter.SetRadius(self._minR)
            self._tubeFilter.SetRadiusFactor(self._maxR / self._minR)
            self._tubeFilter.SetVaryRadiusToVaryRadiusByScalar()
