#This is the web page

import ursina
from ursina import *
from ursina.prefabs.first_person_controller import FirstPersonController
from ursina.shaders import lit_with_shadows_shader

Ground = Entity(model='plane', texture='texture_name')
Ground.color = rgb(.61, 117, 38)
    