from vtk import *
from .Object3D import Object3D
from .MeshContourLines import MeshContourLines


class AbstractMesh(Object3D):

    def __init__(self):
        Object3D.__init__(self)

        # other 3d objects
        self._contour_lines = MeshContourLines()

        # pipelines
        self._triangle_filter = vtkTriangleFilter()
        self._normals = vtkPolyDataNormals()
        self._normals.SetFeatureAngle(40)
        self._banded_contours = vtkBandedPolyDataContourFilter()
        self._banded_contours.SetScalarModeToValue()
        self._banded_contours.GenerateContourEdgesOff()
        self._edges_mapper = vtkPolyDataMapper()
        self._edges_mapper.ScalarVisibilityOff()
        self._edges_actor = vtkActor()
        self._edges_actor.SetMapper(self._edges_mapper)
        self._edges_actor.GetProperty().SetColor(0, 0, 0)

        # actors
        self._additional_actors.append(self._edges_actor)
        self._additional_actors.append(self._contour_lines._actor)

        # properties
        self._smooth = True
        self._banded = False
        self._scalar_range = None
        self.number_of_contours = 10
        self.color_by_data = False
        self.outlines_visible = True
        self.contour_lines_visible = False

    def _update_pipeline(self):

        # surface
        if self._smooth:
            if self._banded:
                self._banded_contours.SetInputConnection(self._surface_output_port)
                self._normals.SetInputConnection(self._banded_contours.GetOutputPort())
                self._triangle_filter.SetInputConnection(self._normals.GetOutputPort())
                self._mapper.SetInputConnection(self._triangle_filter.GetOutputPort())
            else:
                self._normals.SetInputConnection(self._surface_output_port)
                self._mapper.SetInputConnection(self._normals.GetOutputPort())
        else:
            if self._banded:
                self._banded_contours.SetInputConnection(self._surface_output_port)
                self._triangle_filter.SetInputConnection(self._banded_contours.GetOutputPort())
                self._mapper.SetInputConnection(self._triangle_filter.GetOutputPort())
            else:
                self._mapper.SetInputConnection(self._surface_output_port)

        # edges
        self._edges_mapper.SetInputConnection(self._edges_output_port)

        # tell mapper which data to use
        if self._banded:
            self._mapper.SetScalarModeToUseCellData()
        else:
            self._mapper.SetScalarModeToUsePointData()

    def _initialize(self):
        self._contour_lines.set_mesh(self)
        self._update_pipeline()

    @property
    def _edges_output_port(self):
        ee = vtkExtractEdges()
        ee.SetInputConnection(self._surface_output_port)
        return ee.GetOutputPort()

    @property
    def _poly_data(self):
        p = self._surface_output_port.GetProducer()
        p.Update()
        if isinstance(p, vtkProgrammableSource):
            return p.GetPolyDataOutput()
        elif isinstance(p, vtkPolyDataAlgorithm):
            return p.GetOutput()
        else:
            raise AssertionError()

    def create_colors(self):
        r = self.scalar_range
        if self._banded:
            self._banded_contours.GenerateValues(self.number_of_contours, r)
            self._mapper.SetScalarRange(r)
        else:
            self._mapper.SetScalarRange(r)
        self._contour_lines.create_contours()

    @property
    def scalar_range(self):
        if self._scalar_range:
            return self._scalar_range
        else:
            return self._poly_data.GetPointData().GetScalars().GetRange()

    @scalar_range.setter
    def scalar_range(self, r):
        self._scalar_range = r

    @property
    def smooth(self):
        return self._smooth

    @smooth.setter
    def smooth(self, s):
        self._smooth = s
        self._update_pipeline()

    @property
    def banded(self):
        return self._banded

    @banded.setter
    def banded(self, b):
        self._banded = b
        self._update_pipeline()

    @property
    def color_by_data(self):
        return self._mapper.GetScalarVisibility()

    @property
    def contour_lines_visible(self):
        return self._contour_lines.visible

    @contour_lines_visible.setter
    def contour_lines_visible(self, b):
        self._contour_lines.visible = b

    @property
    def contour_lines_color(self):
        return self._contour_lines.color

    @contour_lines_color.setter
    def contour_lines_color(self, c):
        self._contour_lines.color = c

    @property
    def number_of_contours(self):
        return self._contour_lines.number_of_contours

    @number_of_contours.setter
    def number_of_contours(self, nc):
        self._contour_lines.number_of_contours = nc

    @color_by_data.setter
    def color_by_data(self, c):
        self._mapper.SetScalarVisibility(c)
