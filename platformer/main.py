from ursina import *
app = Ursina()

from ursina.prefabs.platformer_controller_2d import PlatformerController2d
player = PlatformerController2d(y=1, z=.01, scale_y=1, max_jumps=1)


# dont touch this part ok (scroll to the bottom if u wanna make ur own lvl)

quad = load_model('quad')
print('--------------', quad)
level_parent = Entity(model=Mesh(vertices=[], uvs=[]), texture='white_cube')
def make_level(texture):

    [destroy(c) for c in level_parent.children]

    for y in range(texture.height):
        collider = None
        for x in range(texture.width):
            col = texture.get_pixel(x,y)


            if col == color.black:
                level_parent.model.vertices += [Vec3(*e) + Vec3(x+.5,y+.5,0) for e in quad.vertices] 
                level_parent.model.uvs += quad.uvs
               
                if not collider:
                    collider = Entity(parent=level_parent, position=(x,y), model='quad', origin=(-.5,-.5), collider='box', visible=False)
                else:
                    
                    collider.scale_x += 1
            else:
                collider = None

           
            if col == color.green:
                player.start_position = (x, y)
                player.position = player.start_position

    level_parent.model.generate()






# edit the things below if u wanna make ur own version
make_level(load_texture('platformer_tutorial_level')) 

camera.orthographic = True
camera.position = (30/2,8)
camera.fov = 16



player.traverse_target = level_parent
enemy = Entity(model='cube',scale_x=4, collider='box', color=color.red, position=(17,5,-.1))
enemy2 = Entity(model='cube',scale_x=2, collider='box', color=color.red, position=(24,2,-.1))
goal = Entity(model='cube', collider='box', color=color.green, position=(27,6.5,-.1))
def update():
    if player.intersects(enemy).hit or player.intersects(enemy2).hit:
        player.position = player.start_position
    
    if player.intersects(goal).hit:
        txt = Text(text="U WIN :O", scale=2)

app.run()