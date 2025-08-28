import pygame

from src import settings


class Paddle:
    def __init__(self):
        self.width = settings.PADDLE_WIDTH
        self.height = settings.PADDLE_HEIGHT
        self.color = settings.PADDLE_COLOR
        self.speed = settings.PADDLE_SPEED
        self.x = (settings.SCREEN_WIDTH - self.width) // 2
        self.y = settings.SCREEN_HEIGHT - self.height - 30
        self.rect = pygame.Rect(self.x, self.y, self.width, self.height)

    def move(self, direction):
        if direction == 'left':
            self.rect.x -= self.speed
        elif direction == 'right':
            self.rect.x += self.speed
        # Limita dentro da tela
        self.rect.x = max(0, min(self.rect.x, settings.SCREEN_WIDTH - self.width))

    def update(self, keys):
        if keys[pygame.K_LEFT]:
            self.move('left')
        if keys[pygame.K_RIGHT]:
            self.move('right')

    def draw(self, surface):
        pygame.draw.rect(surface, self.color, self.rect)
