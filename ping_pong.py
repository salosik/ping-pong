from pygame import *    
from random import randint

WIDTH = 600
HEIGHT = 500
FPS = 60



bg = ((0,255,15))
window = display.set_mode((WIDTH,HEIGHT))
display.set_caption('ping-pong')
clock = time.Clock()

run = True 
while run :
    for e in event.get():
        if e.type == QUIT:
            run = False

    window.fill(bg)
    display.update()
    clock.tick(FPS)