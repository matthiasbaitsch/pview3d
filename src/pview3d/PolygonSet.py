from vtk import *
from .AbstractMesh import AbstractMesh


class PolygonSet(AbstractMesh):

    MAX_VERTS = 500

    def __init__(self):
        AbstractMesh.__init__(self)
        self._currentVertex = 0
        self._points = vtkPoints()
        self._lines = vtkCellArray()
        self._polygons = vtkCellArray()
        self._scalars = vtkDoubleArray()
        self._surface_source = vtkProgrammableSource()
        self._edge_source = vtkProgrammableSource()

        # buffer
        self._vertices = []
        self._values = PolygonSet.MAX_VERTS * [0]
        for i in range(0, PolygonSet.MAX_VERTS):
            self._vertices.append([0, 0, 0])

        # set up
        self._scalars.SetNumberOfComponents(1)

        # get ready
        self._set_execute_method()
        self._initialize()

    def _set_execute_method(self):

        def us():
            pd = self._surface_source.GetPolyDataOutput()
            pd.SetPolys(self._polygons)
            pd.SetPoints(self._points)
            pd.GetPointData().SetScalars(self._scalars)

        def ue():
            pd = self._edge_source.GetPolyDataOutput()
            pd.SetLines(self._lines)
            pd.SetPoints(self._points)

        self._surface_source.SetExecuteMethod(us)
        self._edge_source.SetExecuteMethod(ue)

    @property
    def _edges_output_port(self):
        return self._edge_source.GetOutputPort()

    @property
    def _surface_output_port(self):
        return self._surface_source.GetOutputPort()

    def clear(self):
        self._points.Reset()
        self._scalars.Reset()
        self._polygons.Reset()
        self._lines.Reset()

    def insert_vertex(self, x, y, z, v):
        self._vertices[self._currentVertex][0] = x
        self._vertices[self._currentVertex][1] = y
        self._vertices[self._currentVertex][2] = z
        self._values[self._currentVertex] = v
        self._currentVertex = self._currentVertex + 1

    def polygon_complete(self):
        np = self._currentVertex

        # check
        if np < 3:
            raise AssertionError("Polygon must have at least three vertices")

        # insert cells
        self._polygons.InsertNextCell(np)
        self._lines.InsertNextCell(np + 1)

        # insert vertices
        for i in range(0, np):
            pt = self._vertices[i]

            # insert point and value
            idd = self._points.InsertNextPoint(pt[0], pt[1], pt[2])
            self._scalars.InsertNextValue(self._values[i])

            # insert cells
            self._polygons.InsertCellPoint(idd)
            self._lines.InsertCellPoint(idd)

            # remember first vertex id
            if i == 0:
                fidd = idd

        # close outline
        self._lines.InsertCellPoint(fidd)

        # touch
        self._surface_source.Modified()
        self._edge_source.Modified()

        # reset counter
        self._currentVertex = 0


