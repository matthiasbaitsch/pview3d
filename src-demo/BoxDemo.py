#!/usr/bin/env python
# -*- coding: utf-8 -*-

from random import *
from pview3d import *

# viewer
v = Viewer()

n = 20
for i in range(n):
    for j in range(n):
        box = Box()
        box.size = [1, 1, 5*random()]
        box.position = [i, j, 0]
        box.color = [random(), random(), random()]
        v.add_object(box)

v.run()