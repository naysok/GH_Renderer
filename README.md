# GH_Renderer  


数値計算の結果をライノへ描画するためのライブラリ。  

座標のまとまりをリストで渡す。ひとまず Point, Line, Mesh を描画可。定義は以下の通り。  


```python

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

```