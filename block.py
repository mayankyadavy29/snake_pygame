from config import *

class Block:
    def __init__(self, pos, type):
        self.type = type  # 0 -> Snake , 1 -> Food
        self.pos = pos
        self.image = pg.Surface([BLOCK_SIZE, BLOCK_SIZE])
        self.image.fill('blue' if type else 'orange')
        self.rect = self.image.get_rect()
        self.rect.topleft = self.pos * BLOCK_SIZE

    def move(self, pos):
        self.pos[0] = pos[0] % BLOCKS_X
        self.pos[1] = pos[1] % BLOCKS_Y
        self.rect.topleft = self.pos*BLOCK_SIZE

    def draw(self):
        screen.blit(self.image, self.rect)
