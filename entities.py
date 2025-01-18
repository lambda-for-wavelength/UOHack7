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

shotgun = non_physical_object(Entity(model='cube', parent=camera))
shotgun.muzzle_flash = non_physical_object(Entity(parent = shotgun, color = color.yellow, enabled=False))




### ENEMIES
spawn_interval = 5
spawn_timer = 0

def length(vec):
    pass

class enemyrun(Entity):
    def __init__(self):
        super().__init__()

        self.health = 10
        self.speed = 2
        self.color = color.red
        self.model = 'cube'
        self.position = Vec3(random.randint(5, 10), 0, random.randint(5, 10)) 
        self.target = Vec3(0, 0, 0)

    def update(self):
        mouvment = self.target - self.position 
        self.position = self.position + mouvment * self.speed * time.dt
        
# List to keep track of enemies
enemylist = []        

def spawn_enemy():
    # Create and add a new enemy to the list
    e = enemyrun()
    enemylist.append(e)

def update():
    global spawn_timer

    # Update the spawn timer
    spawn_timer += time.dt

    # Check if the timer exceeds the spawn interval
    if spawn_timer >= spawn_interval:
        spawn_enemy()  # Spawn a new enemy
        spawn_timer = 0  # Reset the timer

    # Update all enemies in the enemy list
    for enemy in enemylist:
        if hasattr(enemy, 'update'):
            enemy.update()
