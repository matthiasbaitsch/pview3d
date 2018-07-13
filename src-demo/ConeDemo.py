#!/usr/bin/env python
# -*- coding: utf-8 -*-

from pview3d import *

# viewer
v = Viewer()

c1 = Cone()
c1.color = 'orange'
c2 = Cone()
c2.radius = 0.25
c2.height = 2
c2.center = [0, 0, 1]
c2.direction = [10, 0, 10]
c2.color = 'brown'

v.add_object(c1)
v.add_object(c2)

v.run()