import PlayerController
from clge import *
from clge import Constants
from clge.Behaviour import Vector2

scr = Screen(30, 30, True)
scr.set_timeout(.1)
scr.auto_clear_objects_list_setter(True)

world = Behaviour.World()

a = Behaviour.Behaviour("Test Object", scr, world)
a.addComponent(Behaviour.Components.AsciiRenderer2D)
a.addComponent(Behaviour.Components.Collider2D)
a.addComponent(PlayerController.PlayerController)

# The Children of a Behaviour object are not working pretty so I don't advice you to use them
# c = Behaviour.Behaviour("Test Child Object", scr, world)
# c.addComponent(Behaviour.Components.AsciiRenderer2D)
# c.addComponent(Behaviour.Components.Collider2D)
# c.getComponentByType("transform2d").changePositionBy(Constants.TRANSFORM2D_MV_POS, 0, 1)
#
# a.addChild(c)

# The Physiqs module is currently being tested and is experimental.
# It may cause bugs and errors! Use it at your own risk
# a.addComponent(Behaviour.Components.Physiqs)
# a.getComponentByType("physiqs").addForce(Vector2(1, 0), 5)


b = Behaviour.Behaviour("Wall Object", scr, world)
b.addComponent(Behaviour.Components.AsciiRenderer2D)
b.getComponentByType("transform2d").changePositionBy(Constants.TRANSFORM2D_MV_POS, 2, 15)
b.getComponentByType("transform2d").setSize(24, 2)
b.addComponent(Behaviour.Components.Collider2D)

scr.Start()
