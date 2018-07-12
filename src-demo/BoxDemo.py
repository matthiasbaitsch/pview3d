#!/usr/bin/env python
# -*- coding: utf-8 -*-

import vtk
from random import *
from pview3d import Box

# renderer
renderer = vtk.vtkRenderer()

n = 30
for i in range(n):
    for j in range(n):
        box = Box()
        box.size = [1, 1, 5*random()]
        box.position = [i, j, 0]
        box.color = [random(), random(), random()]
        box._add_to_renderer(renderer)


# render window
renderWindow = vtk.vtkRenderWindow()
renderWindow.AddRenderer(renderer)
interactor = vtk.vtkRenderWindowInteractor()
interactor.SetRenderWindow(renderWindow)
renderWindow.Render()
interactor.Start()
