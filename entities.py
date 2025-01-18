import ursina
from ursina import *
from ursina.prefabs.first_person_controller import FirstPersonController
from ursina.shaders import lit_with_shadows_shader

class physical_object:
    def __init__(self, model, collider , scale, texture, texture_scale):
        self.model = model
        self.collider = collider
        self.scale = scale
        self.texture = texture
        self.texture_scale = texture_scale
        pass

class non_physical_object:
    def __init__(self, model, scale, texture, texture_scale):
        self.model = model
        self.scale = scale
        self.texture = texture
        self.texture_scale = texture_scale
        pass

ground = physical_object(Entity(model = 'plane', collider = 'box', scale = 64, texture = 'grass', texture_scale = (4,4)))

shotgun = non_physical_object(Entity(model='cube', parent=camera))
shotgun.muzzle_flash = non_physical_object(Entity(parent = shotgun, color = color.yellow, enabled=False))