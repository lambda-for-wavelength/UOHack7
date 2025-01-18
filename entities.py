import ursina
from ursina import *
from ursina.prefabs.first_person_controller import FirstPersonController
from ursina.shaders import lit_with_shadows_shader

class physical_Entity(Entity):
    def __init_(self):
        super.__init__(self)
        self.collider = 'box'

class non_physical_Entity(Entity):
    pass

class living_Entity(Entity):
    pass

#ground = physical_Entity(Entity(model = 'plane', collider = 'box', scale = 64, texture = 'grass', texture_scale = (4,4)))

#shotgun = non_physical_Entity(Entity(model='cube', parent=camera))
#shotgun.muzzle_flash = non_physical_Entity(Entity(parent = shotgun, color = color.yellow, enabled=False))