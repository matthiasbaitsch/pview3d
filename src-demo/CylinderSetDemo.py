#!/usr/bin/env python
# -*- coding: utf-8 -*-

import vtk
from random import *
from pview3d import CylinderSet


def rvec():
    return [random(), random(), random()]

# renderer
renderer = vtk.vtkRenderer()
cs = CylinderSet()
cs.color = 'blue'

n = 5000
for i in range(n):
    cs.add_cylinder(rvec(), rvec(), 0.01 * random())

cs._add_to_renderer(renderer)

# render window
renderWindow = vtk.vtkRenderWindow()
renderWindow.AddRenderer(renderer)
interactor = vtk.vtkRenderWindowInteractor()
interactor.SetRenderWindow(renderWindow)
renderWindow.Render()
interactor.Start()

