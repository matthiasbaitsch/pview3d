from vtk import *
from .Object3D import Object3D


class UnstructuredMesh(Object3D):

    def __init__(self):
        Object3D.__init__(self)

        self._cells = vtkCellArray()
        self._doubleArray = vtkDoubleArray()
        self._points = vtkPoints()

