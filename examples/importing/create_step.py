import gmsh
import math
gmsh.initialize()

spodek = gmsh.model.occ.addBox(0,0,0,5,15,5)
vrsek = gmsh.model.occ.addBox(0,0,5,5,10,2)
dira = gmsh.model.occ.addCylinder(2.5,12.5,0,0,0,5,r=2,angle=math.pi)

kus_tags, map = gmsh.model.occ.fuse(objectDimTags=[(3,spodek)],toolDimTags=[(3,vrsek)])
finale, map = gmsh.model.occ.cut(objectDimTags=kus_tags,toolDimTags=[(3,dira)])

gmsh.model.occ.synchronize()
gmsh.model.mesh.generate(3)
gmsh.write("step_files/component.step")
gmsh.write("step_files/component.msh")

gmsh.finalize()