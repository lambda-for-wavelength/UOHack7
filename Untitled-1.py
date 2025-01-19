from ursina import *

app = Ursina()

'''
Loads an image sequence as a frame animation.
Consider using SpriteSheetAnimation instead if possible.
So if you have some frames named image_000.png, image_001.png, image_002.png and so on,
you can load it like this: Animation('image')

You can also load a .gif by including the file type: Animation('image.gif')
'''

a = Animation('muzzleflash.gif')

app.run()

