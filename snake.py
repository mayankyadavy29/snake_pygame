import copy

from block import Block
from config import *

class Snake:
    def __init__(self):
        self.dir = None
        self.blocks = list()
        self.dead = False
        self.eat = False

    def init(self):
        self.dir = "RIGHT"
        for i in range(5):
            self.add(5-i, BLOCKS_Y//2)

    def add(self, x, y):
        self.blocks.append(Block(vec(x, y), 0))

    def move(self, food):
        if not self.dead:
            prev = copy.deepcopy(self.blocks[0].pos)
            if self.dir == "UP":
                new_pos = prev + vec(0, -1)
                self.__move_blocks(new_pos, prev, food)
            if self.dir == "DOWN":
                new_pos = prev + vec(0, 1)
                self.__move_blocks(new_pos, prev, food)
            if self.dir == "LEFT":
                new_pos = prev + vec(-1, 0)
                self.__move_blocks(new_pos, prev, food)
            if self.dir == "RIGHT":
                new_pos = prev + vec(1, 0)
                self.__move_blocks(new_pos, prev, food)

    def __move_blocks(self, new_pos, prev, food):
        self.blocks[0].move(new_pos)
        self.blocks[0].draw()
        self.check_for_dead(new_pos)
        self.check_for_food(self.blocks[0], food)
        for i in range(1, len(self.blocks)):
            cur, prev = prev, copy.deepcopy(self.blocks[i].pos)
            self.blocks[i].move(cur)
            self.check_for_food(self.blocks[i], food)
            self.blocks[i].draw()
            
    def check_for_dead(self, pos):
        pos_times = 0
        for b in self.blocks:
            if b.pos == pos:
                pos_times += 1
                if pos_times > 1:
                    self.dead = True
                    return

    def check_for_food(self, block, food):
        if block.rect.colliderect(food):
            self.eat = True
            self.blocks.append(copy.deepcopy(self.blocks[-1]))
            return True