from clge import *
from clge import Constants

scr = Screen(30, 30, True)
scr.set_timeout(.2)
scr.auto_clear_objects_list_setter(True)

world = Behaviour.World()

a = Behaviour.Behaviour("Test Object", scr, world)
a.addComponent(Behaviour.Components.AsciiRenderer2D)
a.addComponent(Behaviour.Components.Collider2D)


b = Behaviour.Behaviour("Wall Object", scr, world)
b.addComponent(Behaviour.Components.AsciiRenderer2D)
b.getComponentByType("transform2d").changePositionBy(Constants.TRANSFORM2D_MV_POS, 0, 15)
b.getComponentByType("transform2d").setSize(25, 1)
b.addComponent(Behaviour.Components.Collider2D)

scr.Start()