from vtk import *
import matplotlib


class Object3D:

    @staticmethod
    def set_color(a, c):
        if isinstance(c, str):
            Object3D.set_color(a, hex_to_rgb(matplotlib.colors.cnames[c]))
        else:
            a.GetProperty().SetColor(c)

    def __init__(self):
        self._mapper = vtkPolyDataMapper()
        self._actor = vtkActor()
        self._actor.SetMapper(self._mapper)
        self._additional_actors = []
        self.color = [1, 1, 1]

    @property
    def color(self):
        return self._actor.GetProperty().GetColor()

    @color.setter
    def color(self, c):
        Object3D.set_color(self._actor, c)

    @property
    def visible(self):
        return self._actor.IsVisible()

    @visible.setter
    def visible(self, v):
        self._actor.SetVisibility(v)

    @property
    def _actors(self):
        return [self._actor] + self._additional_actors

    def _add_to_renderer(self, r):
        for a in self._actors:
            r.AddActor(a)


def hex_to_rgb(value):
    value = value.lstrip('#')
    lv = len(value)
    return list(int(value[i:i + lv // 3], 16) / 255.0 for i in range(0, lv, lv // 3))

