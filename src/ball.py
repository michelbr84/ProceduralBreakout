import pygame
from src import settings

class Ball:
    def __init__(self):
        self.radius = settings.BALL_RADIUS
        self.color = settings.BALL_COLOR
        self.speed = settings.BALL_SPEED
        self.reset()

    def reset(self):
        self.x = settings.SCREEN_WIDTH // 2
        self.y = settings.SCREEN_HEIGHT // 2
        self.vx = self.speed
        self.vy = -self.speed
        self.moving = False  # Só começa a mover após espaço

    def launch(self):
        if not self.moving:
            self.moving = True
            # Garante que a bola suba ao lançar
            self.vy = -abs(self.speed)
            # Pequena aleatoriedade para não travar
            import random
            self.vx = random.choice([-1, 1]) * abs(self.speed)

    def update(self, paddle):
        if not self.moving:
            # Bola acompanha a paddle antes do lançamento
            self.x = paddle.rect.centerx
            self.y = paddle.rect.top - self.radius
            return
        self.x += self.vx
        self.y += self.vy
        # Colisão com paredes
        if self.x - self.radius <= 0 or self.x + self.radius >= settings.SCREEN_WIDTH:
            self.vx *= -1
        if self.y - self.radius <= 0:
            self.vy *= -1
        # Colisão com paddle
        if paddle.rect.collidepoint(self.x, self.y + self.radius):
            self.vy = -abs(self.speed)
            # Ajuste de direção baseado no ponto de contato
            offset = (self.x - paddle.rect.centerx) / (paddle.width // 2)
            self.vx = self.speed * offset

    def draw(self, surface):
        pygame.draw.circle(surface, self.color, (int(self.x), int(self.y)), self.radius) 