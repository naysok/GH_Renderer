import rhinoscriptsyntax as rs


#############################################
###                                       ###
###   Runnig on GHPython (IronPython 2)   ###
###                                       ###
#############################################


class Renderer():


    """

    ############################
    ####                     ###
    ####     Defined Type    ###
    ####                     ###
    ############################

    ### Point
    vert = [x0, y0, z0]

    ### Points
    verts = [vert, vert, , , , , ,  vert]
    verts = [[x0, y0, z0], [x1, y1, z1], , , , , , ,  [xn, yn, zn]]


    ### Line
    vert2 = [vert, vert]
    vert2 = [[x0, y0, z0], [x1, y1, z1]]

    ### Lines
    vert2s = [vert2, vert2, , , , , , vert2]
    vert2s = [[[x0, y0, z0], [x1, y1, z1]], , , , , , [[xm, ym, zm], [xn, yn, zn]]]


    ### Mesh
    vert3 = [[x0, y0, z0], [x1, y1, z1], [x2, y2, z2]]

    ### Meshes
    vert3s = [vert3, vert3, , , , , , vert3]
    vert3s = [[[x0, y0, z0], [x1, y1, z1], [x2, y2, z2]], , , , , , [[xk, yk, zk], [xm, ym, zm], [xn, yn, zn]]]


    """


    ################################################################################


    def add_point(self, vert):
        
        return rs.AddPoint(vert)


    def add_points(self, verts):

        pts = []

        for i in xrange(len(verts)):
            p = verts[i]
            pt = rs.AddPoint(p)
            pts.append(pt)
        
        return pts


    def render_points(self, points):

        ### Render Points (or Point)

        ### Segment Point / Points
        if points == None:
            rendered = None
        elif (len(points) == 3) and (type(points[0]) == float):
            rendered = self.add_point(points)
        else:
            rendered = self.add_points(points)
        
        return rendered


    ################################################################################


    def add_line(self, vert2):

        p0 = rs.AddPoint(vert2[0])
        p1 = rs.AddPoint(vert2[1])
        
        return rs.AddLine(p0, p1)
    

    def add_lines(self, vert2s):

        lines = []

        for i in xrange(len(vert2s)):
            vert2 = vert2s[i]
            line = self.add_line(vert2)
            lines.append(line)

        return lines


    def render_lines(self, lines):
        
        ### Render Lines (or Line)

        ### Segment Line / Lines
        if lines == None:
            rendered = None
        elif (len(lines) == 2) and (len(lines[0]) == 3):
            rendered = self.add_line(lines)
        else:
            rendered = self.add_lines(lines)

        return rendered


    ################################################################################


    def vert3_to_points(self, vert3):
                
        # print(vert3)

        points = []
        
        for i in xrange(len(vert3)):
            vert = vert3[i]
            # print(vert)
            p = rs.AddPoint(vert)
            points.append(p)
        
        points_geo = rs.coerce3dpointlist(points)
        
        return points_geo
    
    
    def add_mesh(self, verts3):
        
        ### Convert verts(Number-List) to Point
        
        points = self.vert3_to_points(verts3)
        # print(points)
        
        ### Create Mesh
        m = rs.AddMesh(points, [[0, 1, 2]])
        
        return m
    
    
    def add_meshes(self, meshes):
        
        render = []
        
        for i in xrange(len(meshes)):
            tmp = meshes[i]
            # print(tmp)
            m = self.add_mesh(tmp)
            render.append(m)
        
        return render


    def render_meshes(self, meshes):

        ### Render Meshes (or Mesh)

        ### Segment Mesh / Meshes
        if meshes == None:
            rendered = None
        elif (len(meshes) != 3) or (len(meshes[0]) != 1):
            rendered = self.add_meshes(meshes)
        else:
            rendered = self.add_mesh(meshes)

        return rendered