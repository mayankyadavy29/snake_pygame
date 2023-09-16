import random

from config import *
from snake import Snake
from block import Block

def main():
    bg = pg.transform.scale(pg.image.load("assets/images/background.png"), (width, height))
    snake = Snake()
    snake.init()
    dead = pg.font.Font("assets/fonts/Slow Death.ttf", 60).render("YOU DIED !!", True, "brown")
    dead_rect = dead.get_rect().move(((width - dead.get_width()) // 2, (height - dead.get_height()) // 2))
    restart = pg.font.Font("assets/fonts/Quick Starter.ttf", 50).render("RESTART", True, "blue")
    restart_rect = restart.get_rect(midtop=(dead_rect.centerx, dead_rect.bottom + 40))
    restart_border_rect = pg.Rect(restart_rect)
    restart_border_rect = restart_border_rect.inflate(10, 20)
    food = Block(vec(random.randint(0, BLOCKS_X-1), random.randint(0, BLOCKS_Y-1)), 2)
    running = True
    while running:
        screen.blit(bg, (0, 0))
        for event in pg.event.get():
            if event.type == pg.QUIT:
                running = False
            if event.type == pg.MOUSEBUTTONUP:
                if restart_rect.collidepoint(event.pos):
                    snake = Snake()
                    snake.init()
        # Keys pressed action
        keys = pg.key.get_pressed()
        if keys[pg.K_w] and (snake.dir == "LEFT" or snake.dir == "RIGHT"):
            snake.dir = "UP"
        if keys[pg.K_s] and (snake.dir == "LEFT" or snake.dir == "RIGHT"):
            snake.dir = "DOWN"
        if keys[pg.K_a] and (snake.dir == "UP" or snake.dir == "DOWN"):
            snake.dir = "LEFT"
        if keys[pg.K_d] and (snake.dir == "UP" or snake.dir == "DOWN"):
            snake.dir = "RIGHT"

        if snake.eat:
            food = Block(vec(random.randint(0, BLOCKS_X-1), random.randint(0, BLOCKS_Y-1)), food_list[random.randint(0, 4)])
            snake.eat = False
        if not snake.dead:
            food.draw()
            score = pg.font.SysFont("comicsans", 30).render(str(snake.score), True, "yellow")
            screen.blit(score, (0, 0))
        snake.move(food)
        if snake.dead:
            screen.blit(dead, dead_rect)
            screen.blit(restart, restart_rect)
            dead_score = pg.font.Font("assets/fonts/GaelleNumber4.ttf", 80).render(str(snake.score), True, "brown")
            dead_score_rect = dead_score.get_rect().move((dead_rect.left + dead.get_width() // 2 - dead_score.get_width()//2),
                                                         (dead_rect.top - dead_score.get_height() - 20))
            screen.blit(dead_score, dead_score_rect)
            pg.draw.rect(screen, "blue", restart_border_rect, 5, 5)
        if not snake.dead:
            food.draw()
            score = pg.font.SysFont("comicsans", 30).render(str(snake.score), True, "yellow")
            screen.blit(score, (0, 0))
        pg.display.update()
        clock.tick(10)

    pg.quit()

if __name__ == "__main__":
    main()