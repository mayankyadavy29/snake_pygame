from config import *

class Block:
    def __init__(self, pos, type):
        self.type = type  # 0 -> SnakeHead , 1 -> SnakBody, 2 -> Food, 5 -> SuperFood
        self.pos = pos
        if type == 0:
            self.image = pg.transform.scale(pg.image.load("assets/images/snakehead.png"), (BLOCK_SIZE, BLOCK_SIZE))
        elif type == 1:
            self.image = pg.transform.scale(pg.image.load("assets/images/snakebody.png"), (BLOCK_SIZE, BLOCK_SIZE))
        elif type == 2:
            self.image = pg.transform.scale(pg.image.load("assets/images/food.png"), (BLOCK_SIZE, BLOCK_SIZE))
        elif type == 5:
            self.image = pg.transform.scale(pg.image.load("assets/images/superfood.png"), (BLOCK_SIZE, BLOCK_SIZE))
        self.rect = self.image.get_rect()
        self.rect.topleft = self.pos * BLOCK_SIZE

    def move(self, pos):
        self.pos[0] = pos[0] % BLOCKS_X
        self.pos[1] = pos[1] % BLOCKS_Y
        self.rect.topleft = self.pos*BLOCK_SIZE

    def draw(self):
        screen.blit(self.image, self.rect)
