import pygame
import sys
from settings import *
from snake import Snake
from food import Food

class Game:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((WINDOW_SIZE, WINDOW_SIZE))
        pygame.display.set_caption("Змейка")
        self.clock = pygame.time.Clock()
        self.font = pygame.font.SysFont(None, 36)
        self.snake = Snake()
        self.food = Food()
        self.score = 0
        self.running = True

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                self.snake.change_direction(event.key)

    def check_wall_collision(self):
        head = self.snake.get_head_pos()
        return (head[0] < 0 or head[0] >= WINDOW_SIZE or
                head[1] < 0 or head[1] >= WINDOW_SIZE)

    def show_score(self):
        score_text = self.font.render(f"Счёт: {self.score}", True, WHITE)
        self.screen.blit(score_text, (10, 10))

    def game_over_screen(self):
        self.screen.fill(BLACK)
        msg1 = self.font.render("Игра окончена!", True, RED)
        msg2 = self.font.render(f"Итоговый счёт: {self.score}", True, WHITE)
        msg3 = self.font.render("R - перезапуск | Q - выход", True, WHITE)

        cx = WINDOW_SIZE // 2
        self.screen.blit(msg1, (cx - msg1.get_width()//2, cx - 40))
        self.screen.blit(msg2, (cx - msg2.get_width()//2, cx))
        self.screen.blit(msg3, (cx - msg3.get_width()//2, cx + 40))
        pygame.display.update()

        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_r:
                        return True  
                    if event.key == pygame.K_q:
                        pygame.quit()
                        sys.exit()

    def reset_game(self):
        self.snake.reset()
        self.food.spawn(self.snake.body)
        self.score = 0
        self.running = True

    def run(self):
        while True:
            self.reset_game()
            while self.running:
                self.handle_events()
                self.snake.move()

                if self.check_wall_collision() or self.snake.check_self_collision():
                    self.running = False
                    if self.game_over_screen():
                        continue
                    else:
                        return

                if self.food.is_eaten(self.snake.get_head_pos()):
                    self.score += 1
                    self.snake.grow_next_frame = True
                    self.food.spawn(self.snake.body)

                self.screen.fill(BLACK)
                self.food.draw(self.screen)
                self.snake.draw(self.screen)
                self.show_score()
                pygame.display.update()
                self.clock.tick(FPS)
