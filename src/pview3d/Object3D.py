from vtk import *
import matplotlib


class Object3D:

    def __init__(self):
        self._mapper = vtkPolyDataMapper()
        self._actor = vtkActor()
        self._actor.SetMapper(self._mapper)
        self._additional_actors = []
        self.color = [1, 1, 1]

    @property
    def _actors(self):
        return [self._actor] + self._additional_actors

    @property
    def color(self):
        return self._actor.GetProperty().GetColor()

    @color.setter
    def color(self, c):
        if isinstance(c, str):
            self._actor.GetProperty().SetColor(hex_to_rgb(matplotlib.colors.cnames[c]))
        else:
            self._actor.GetProperty().SetColor(c)

    def _add_to_renderer(self, r):
        """
        Add this Object3D to the specified renderer.
        :type r: vtkRenderer
        """
        for a in self._actors:
            r.AddActor(a)




def hex_to_rgb(value):
    value = value.lstrip('#')
    lv = len(value)
    return list(int(value[i:i + lv // 3], 16) / 255.0 for i in range(0, lv, lv // 3))

