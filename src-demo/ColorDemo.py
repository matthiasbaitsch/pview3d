#!/usr/bin/env python
# -*- coding: utf-8 -*-

import vtk
import matplotlib
from pview3d import Box

print(matplotlib.colors.cnames.items())

# renderer
renderer = vtk.vtkRenderer()

# all named colors
x = 0
y = 0
for name, hex in matplotlib.colors.cnames.items():
    box = Box()
    box.position = [x, y, 0]
    box.color = name
    box._add_to_renderer(renderer)
    x += 1
    if x == 12:
        x = 0
        y += 1

# render window
renderWindow = vtk.vtkRenderWindow()
renderWindow.AddRenderer(renderer)
interactor = vtk.vtkRenderWindowInteractor()
interactor.SetRenderWindow(renderWindow)
renderWindow.Render()
interactor.Start()
