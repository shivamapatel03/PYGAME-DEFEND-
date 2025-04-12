import pygame
import random

class GameEngine:
    def __init__(self, player):
        self.width = 640
        self.height = 480
        self.window = pygame.display.set_mode((self.width, self.height))
        self.player = player
        self.clock = pygame.time.Clock()
        self.falling_objects = []
        self.spawn_rate = 25
        self.score = 0

    def spawn_object(self):
        x = random.randint(0, self.width - 30)
        y = 0
        rect = pygame.Rect(x, y, 30, 30)
        self.falling_objects.append(rect)

    def update_objects(self):
        for obj in self.falling_objects:
            obj.y += 5
        self.falling_objects = [o for o in self.falling_objects if o.y < self.height]

    def check_collision(self):
        for obj in self.falling_objects:
            if self.player.rect.colliderect(obj):
                return True
        return False

    def draw_objects(self):
        for obj in self.falling_objects:
            pygame.draw.rect(self.window, (255, 0, 0), obj)

    def draw_score(self):
        font = pygame.font.SysFont(None, 30)
        score_text = font.render(f"Score: {self.score}", True, (255, 255, 255))
        self.window.blit(score_text, (10, 10))

    def run_frame(self, hand_x):
        self.window.fill((0, 0, 0))
        if hand_x:
            self.player.update(hand_x)
        self.player.draw(self.window)

        if pygame.time.get_ticks() % self.spawn_rate == 0:
            self.spawn_object()

        self.update_objects()
        self.draw_objects()
        self.draw_score()
        self.score += 1

        pygame.display.update()
        self.clock.tick(30)
        return not self.check_collision()
