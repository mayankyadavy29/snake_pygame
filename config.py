import pygame as pg

vec = pg.math.Vector2

pg.init()

size = width, height = 640, 480
screen = pg.display.set_mode(size)
pg.display.set_caption("Snake Game")
clock = pg.time.Clock()

# Constants
BLOCK_SIZE = 40
BLOCKS_X = width//BLOCK_SIZE
BLOCKS_Y = height//BLOCK_SIZE


