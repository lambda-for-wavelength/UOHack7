from ursina import *
from ursina.prefabs.first_person_controller import FirstPersonController
from ursina.shaders import lit_with_shadows_shader

app = Ursina(borderless=True)

application.target_fps = 120  # Increase the target FPS to 120

class Bullet(Entity):
    def __init__(self, creator, direction, **kwargs):
        super().__init__(model='sphere', scale=0.05, color=color.black, collider='box', **kwargs)
        self.creator = creator
        self.direction = direction
        self.speed = 200  # Adjusted speed
        self.life_span = 2
        self.start_time = time.time()

    def update(self):
        step = self.direction * self.speed * time.dt
        num_steps = 5  # Subdivide movement into smaller steps
        for i in range(num_steps):
            self.position += step / num_steps
            hit_info = self.intersects()
            if hit_info.hit:
                if isinstance(hit_info.entity, Enemy):
                    hit_info.entity.hp -= 1  # Decrease enemy health
                    destroy(self)  # Destroy bullet upon hit
                    return
        # Destroy the bullet after its lifespan
        if time.time() - self.start_time > self.life_span:
            destroy(self)

class Enemy(Entity):
    def __init__(self, **kwargs):
        super().__init__(parent=shootables_parent, model='sphere', scale_y=2, origin_y=-.5, color=color.light_gray, collider='box', **kwargs)
        self.health_bar = Entity(parent=self, y=1.2, model='cube', color=color.red, world_scale=(1.5, .1, .1))
        self.max_hp = 5
        self.hp = self.max_hp

    def update(self):
        dist = distance_xz(player.position, self.position)
        if dist > 40:
            return

        self.look_at_2d(player.position, 'y')

    @property
    def hp(self):
        return self._hp

    @hp.setter
    def hp(self, value):
        self._hp = value
        if value <= 0:
            destroy(self)
            return
        self.health_bar.world_scale_x = self.hp / self.max_hp * 1.5

random.seed(0)
Entity.default_shader = lit_with_shadows_shader

ground = Entity(model='plane', collider='box', scale=512, texture='grass', texture_scale=(4, 4))
editor_camera = EditorCamera(enabled=False, ignore_paused=True)
player = FirstPersonController(model='cube', z=-10, color=color.hsv(0,0,0,0), origin_y=-.2, speed=14, collider='box')
player.collider = BoxCollider(player, Vec3(0, 1, 0), Vec3(1, 2, 1))

shotgun = Entity(model='trishotgun.obj', parent=camera, position=(0, -.3, .3), scale=(.2, .2, .2), origin_z=-.5, color=color.red, on_cooldown=False)
shotgun.muzzle_flash = Entity(parent=shotgun, z=1, world_scale=.5, model='quad', color=color.yellow, enabled=False)

shootables_parent = Entity()
mouse.traverse_target = shootables_parent

enemies = [Enemy(x=x * 4) for x in range(30)]

def shoot():
    if not shotgun.on_cooldown:
        shotgun.on_cooldown = True
        shotgun.muzzle_flash.enabled = True
        from ursina.prefabs.ursfx import ursfx

        # Create 8 bullets with a random spray pattern
        for i in range(16):
            random_direction = Vec3(
                player.forward.x + random.uniform(-0.1, 0.1),
                player.forward.y + random.uniform(-0.05, 0.05),
                player.forward.z + random.uniform(-0.05, 0.05)
            ).normalized()
            Bullet(
                creator=player,  # Pass the player as the creator
                position=player.position + player.forward * .3,  # Spawn in front of the player
                direction=random_direction
            )

        # Add sound and visual effects
        ursfx([(0.0, 0.0), (0.1, 0.9), (0.15, 0.75), (0.3, 0.14), (0.6, 0.0)],
              volume=0.5, wave='noise', pitch=random.uniform(-13, -12), pitch_change=-12, speed=3.0)
        invoke(shotgun.muzzle_flash.disable, delay=.05)
        invoke(setattr, shotgun, 'on_cooldown', False, delay=1)  # Set cooldown to 1 second

def update():
    if held_keys['left mouse']:
        shoot()

def pause_input(key):
    if key == 'tab':  # press tab to toggle edit/play mode
        editor_camera.enabled = not editor_camera.enabled
        player.visible_self = editor_camera.enabled
        player.cursor.enabled = not editor_camera.enabled
        shotgun.enabled = not editor_camera.enabled
        mouse.locked = not editor_camera.enabled
        editor_camera.position = player.position
        application.paused = editor_camera.enabled

pause_handler = Entity(ignore_paused=True, input=pause_input)

sun = DirectionalLight()
sun.look_at(Vec3(1, -1, -1))
Sky()

app.run()