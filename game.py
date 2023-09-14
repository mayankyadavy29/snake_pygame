import random

from config import *
from snake import Snake
from block import Block

def main():
    snake = Snake()
    snake.init()
    # for i in range(7):
    #     snake.add(1, BLOCKS_Y//2-i)
    dead = pg.font.SysFont("comicsans", 40).render("YOU DIED !!", True, "brown")
    dead_rect = dead.get_rect().move(((width - dead.get_width()) // 2, (height - dead.get_height()) // 2))
    restart = pg.font.SysFont("comicsans", 40).render("Restart", True, "green")
    restart_rect = restart.get_rect().move((dead_rect.left + 20, dead_rect.bottom + 20))
    food = Block(vec(random.randint(0, BLOCKS_X-1), random.randint(0, BLOCKS_Y-1)), 1)
    running = True
    while running:
        screen.fill("black")
        for event in pg.event.get():
            if event.type == pg.QUIT:
                running = False
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_w and (snake.dir == "LEFT" or snake.dir == "RIGHT"):
                    snake.dir = "UP"
                if event.key == pg.K_a and (snake.dir == "UP" or snake.dir == "DOWN"):
                    snake.dir = "LEFT"
                if event.key == pg.K_d and (snake.dir == "UP" or snake.dir == "DOWN"):
                    snake.dir = "RIGHT"
                if event.key == pg.K_s and (snake.dir == "LEFT" or snake.dir == "RIGHT"):
                    snake.dir = "DOWN"
            if event.type == pg.MOUSEBUTTONUP:
                if restart_rect.collidepoint(event.pos):
                    snake = Snake()
                    snake.init()
        if snake.eat:
            food = Block(vec(random.randint(0, BLOCKS_X-1), random.randint(0, BLOCKS_Y-1)), 1)
            snake.eat = False
        if not snake.dead:
            food.draw()
            score = pg.font.SysFont("comicsans", 30).render(str(len(snake.blocks)-5), True, "yellow")
            screen.blit(score, (0, 0))
        snake.move(food)
        if snake.dead:
            screen.blit(dead, dead_rect)
            screen.blit(restart, restart_rect)
        pg.display.update()
        clock.tick(10)
    pg.quit()

if __name__ == "__main__":
    main()