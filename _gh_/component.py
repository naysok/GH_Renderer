### INPUT
### - POINT_IN (List Access)
### - LINE_IN (List Access)
### - MESH_IN (List Access)

### OUTPUT
### - POINT_RENDERED
### - LINE_RENDERED
### - MESH_RENDERED

########################################

from gh_renderer import renderer
reload(renderer)
rr = renderer.Renderer()

########################################

ghenv.Component.Message = 'RENDERER'

POINT_RENDERED = rr.render_points(POINT_IN)
LINE_RENDERED = rr.render_lines(LINE_IN)
MESH_RENDERED = rr.render_meshes(MESH_IN)