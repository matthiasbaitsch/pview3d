#!/usr/bin/env python
# -*- coding: utf-8 -*-

from random import *
from pview3d import *

def rvec():
    return [random(), random(), random()]

# renderer
v = Viewer()
cs = CylinderSet()
cs.color = 'antiquewhite'

# cylinders
for i in range(10000):
    cs.add_cylinder( rvec(), rvec(), 0.01 * random())
v.add_object(cs)

# run
v.run()

