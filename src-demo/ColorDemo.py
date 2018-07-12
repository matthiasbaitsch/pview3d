#!/usr/bin/env python
# -*- coding: utf-8 -*-

import vtk
import matplotlib
from pview3d import *

print(matplotlib.colors.cnames.items())

# viewer
v = Viewer()

# all named colors
x = 0
y = 0
for name, hex in matplotlib.colors.cnames.items():
    box = Box()
    box.position = [x, y, 0]
    box.color = name
    v.add_object(box)
    x += 1
    if x == 12:
        x = 0
        y += 1

# run
v.run()
