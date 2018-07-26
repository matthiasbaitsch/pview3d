from pview3d import *

v = Viewer()
ps = PolygonSet()

ps.insert_vertex(0, 0, 0, 0)
ps.insert_vertex(1, 0, 0, 1)
ps.insert_vertex(0, 1, 0, -1)
ps.polygon_complete()

ps.insert_vertex(1, 0, 0, 0)
ps.insert_vertex(2, 0, 0.2, 1)
ps.insert_vertex(2, 1, 0, 2)
ps.insert_vertex(1, 1, 0.2, 3)
ps.polygon_complete()

ps.smooth = True
ps.banded = True
ps.color_by_data = True
ps.outlines_visible = True
ps.contour_lines_visible = True
ps.create_colors()

v.add_object(ps)
v.run()