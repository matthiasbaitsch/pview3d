from vtk import *
from .Object3D import Object3D


class MeshContourLines(Object3D):

    def __init__(self):
        Object3D.__init__(self)
        self._contourFilter = vtkContourFilter()
        self._mesh = None
        self.contour_range = None
        self.number_of_contours = 19
        self._mapper.SetInputConnection(self._contourFilter.GetOutputPort())
        self._mapper.SetResolveCoincidentTopologyToPolygonOffset()
        self._mapper.ScalarVisibilityOff()
        self._actor.GetProperty().SetColor(0, 0, 0)

    def create_contours(self):
        if self.contour_range:
            r = self.contour_range
        else:
            r = self._mesh.scalar_range
        self._contourFilter.GenerateValues(self.number_of_contours, r[0], r[1])

    def set_mesh(self, mesh):
        self._mesh = mesh
        self._contourFilter.SetInputConnection(self._mesh._surface_output_port)

