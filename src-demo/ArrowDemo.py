#!/usr/bin/env python
# -*- coding: utf-8 -*-

from pview3d import *

# viewer
v = Viewer()

a1 = Arrow()
a1.point2 = [1, 0, 0]
a1.color = "red"
a2 = Arrow()
a2.point2 = [0, 2, 0]
a2.color = "green"
a3 = Arrow()
a3.point2 = [0, 0, 3]
a3.color = "blue"
a4 = Arrow()
a4.point1 = [1, 2, 3]
a4.point2 = [0, 0, 0]
a4.color = "orange"
a5 = Arrow(1, 2, 3, 1, 0, 0)
a6 = Arrow(1, 2, 3, 0, 2, 0)
a7 = Arrow(1, 2, 3, 0, 0, 3)

v.add_objects([a1, a2, a3, a4, a5, a6, a7])

v.run()