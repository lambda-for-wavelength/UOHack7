import ursina
from ursina import *
from ursina.prefabs.first_person_controller import FirstPersonController
from ursina.shaders import lit_with_shadows_shader

Ground = Entity(model='plane', texture='texture_name', scale=(3,1,1))
Ground.color = rgb(.61, 117, 38)
Ground.position = Vec3(0,0,0)
Ground.rotation = (0,0,0)