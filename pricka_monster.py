import random
import time

WIDTH = 500
HEIGHT = 500

monster = Actor("monster")
monster.pos = 200, 200
monster_hit = False

def draw():
    screen.clear()
    monster.draw()
    if monster_hit:
        screen.draw.text("Träff",topleft=(10,10))
    else:
        screen.draw.text("Miss",topleft=(10,10))
    
def set_monster_hit():
    monster.image = 'blod_1'
    clock.schedule_unique(set_monster_normal, 1.0)

def set_monster_normal():
    monster.image = 'monster'

def on_mouse_down(pos):
    global monster_hit
    if monster.collidepoint(pos):
        monster_hit = True
        sounds.splatt.play()
        set_monster_hit()
    else:
        monster_hit = False
        sounds.skratt.play()
        monster.x = random.randint(0,WIDTH)
        monster.y = random.randint(0,HEIGHT)
