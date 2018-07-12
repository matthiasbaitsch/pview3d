import sys
import vtk
from PyQt5.QtWidgets import *
from vtk.qt.QVTKRenderWindowInteractor import QVTKRenderWindowInteractor


class Viewer(QMainWindow):

    def __init__(self, parent = None):
        self.app = QApplication(sys.argv)
        QMainWindow.__init__(self, parent)
        self.frame = QFrame()
        self.vl = QVBoxLayout()
        self.interactor = QVTKRenderWindowInteractor(self.frame)
        self.vl.addWidget(self.interactor)
        self.ren = vtk.vtkRenderer()
        self.ren.SetBackground(1, 1, 1)
        self.interactor.GetRenderWindow().AddRenderer(self.ren)
        self.iren = self.interactor.GetRenderWindow().GetInteractor()
        self.iren.SetInteractorStyle(vtk.vtkInteractorStyleTrackballCamera())
        self.frame.setLayout(self.vl)
        self.setCentralWidget(self.frame)
        self.iren.Initialize()

    def add_object(self, o):
        o._add_to_renderer(self.ren)
        self.ren.ResetCamera()

    def run(self):
        self.show()
        sys.exit(self.app.exec_())



 
