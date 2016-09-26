from teaser.project import Project
from teaser.logic.buildingobjects.buildingphysics.outerwall import OuterWall
import uuid
import teaser.data.output.buildingelement_output as be
print(uuid.uuid1())
print(type(str(uuid.uuid1())))

from teaser.data.dataclass import DataClass
from teaser.logic.buildingobjects.buildingphysics.material import Material

dc = DataClass()

material_list = []

for pyxb_wall in dc.element_bind.OuterWall:
    for pyxb_layer in pyxb_wall.Layers.layer:
        Material(parent=None)
        mat.save_material_template(data_class=dc)

prj = Project()

for out_wall in prj.data.element_bind.OuterWall:
    print(out_wall)
    for pyxb_layer in out_wall.Layers.layer:
        print(pyxb_layer.material.material_id)

for mat in prj.data.material_bind.Material:
    print(mat.material_id)


out = OuterWall(parent=None)

out.load_type_element(1900, 'heavy', prj.data)
be.delete_type_element(prj.data, out)
