from vtk import *
from .Object3D import Object3D


class Box(Object3D):

    def __init__(self):
        Object3D.__init__(self)
        self._edges_actor = vtkActor()
        self._cube_source = vtkCubeSource()
        self._mapper.SetInputConnection(self._cube_source.GetOutputPort())
        ee = vtkExtractEdges()
        em = vtkPolyDataMapper()
        ee.SetInputConnection(self._cube_source.GetOutputPort())
        em.SetInputConnection(ee.GetOutputPort())
        self._edges_actor.SetMapper(em)
        self._edges_actor.GetProperty().SetColor(0, 0, 0)
        self._additional_actors.append(self._edges_actor)
        self._size = [1, 1, 1]
        self._position = [0, 0, 0]
        self._update()

    @property
    def position(self):
        return self._position

    @position.setter
    def position(self, p):
        assert len(p) == 3
        self._position = p
        self._update()

    @property
    def size(self):
        return self._size

    @size.setter
    def size(self, s):
        assert len(s) == 3
        self._size = s
        self._update()

    def _update(self):
        p1 = self._position[0]
        p2 = self._position[1]
        p3 = self._position[2]
        s1 = self._size[0]
        s2 = self._size[1]
        s3 = self._size[2]
        self._cube_source.SetBounds(p1, p1 + s1, p2, p2 + s2, p3, p3 + s3)
        self._cube_source.Modified()
