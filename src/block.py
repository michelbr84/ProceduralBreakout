import pygame


def generate_hit_colors(max_hits=10):
    # Gera uma paleta de cores distintas para cada hit (do laranja ao azul escuro)
    import colorsys
    base_hue = 0.08  # Laranja
    end_hue = 0.6    # Azul escuro
    colors = []
    for i in range(max_hits, 0, -1):
        hue = base_hue + (end_hue - base_hue) * (max_hits - i) / (max_hits - 1)
        rgb = colorsys.hsv_to_rgb(hue, 0.7, 1.0)
        color = tuple(int(c * 255) for c in rgb)
        colors.append((color, i))
    return colors

MAX_HITS = 10
BLOCK_HIT_COLORS = generate_hit_colors(MAX_HITS)
BLOCK_COLOR_TO_HITS = {color: hits for color, hits in BLOCK_HIT_COLORS}
BLOCK_HITS_TO_COLOR = {hits: color for color, hits in BLOCK_HIT_COLORS}
BLOCK_COLOR_SCORES = {color: 20 + hits * 20 for color, hits in BLOCK_HIT_COLORS}  # Score cresce com hits

class Block:
    def __init__(self, x, y, color, hits=1):
        self.width = 60
        self.height = 24
        self.color = color
        self.rect = pygame.Rect(x, y, self.width, self.height)
        self.alive = True
        self.hits = hits

    def draw(self, surface, show_hits=True):
        if self.alive:
            pygame.draw.rect(surface, self.color, self.rect)
            if show_hits:
                font = pygame.font.SysFont(None, 28, bold=True)
                hits_str = str(self.hits)
                outline = font.render(hits_str, True, (255,255,255))
                outline_rect = outline.get_rect(center=self.rect.center)
                text = font.render(hits_str, True, (0,0,0))
                text_rect = text.get_rect(center=self.rect.center)
                for dx in [-1,0,1]:
                    for dy in [-1,0,1]:
                        if dx != 0 or dy != 0:
                            surface.blit(outline, outline_rect.move(dx,dy))
                surface.blit(text, text_rect)

    def collide_with_ball(self, ball):
        if self.alive and self.rect.colliderect(pygame.Rect(
            ball.x - ball.radius, ball.y - ball.radius, ball.radius * 2, ball.radius * 2)):
            self.hits -= 1
            if self.hits <= 0:
                self.alive = False
            else:
                # Atualiza cor conforme hits
                if self.hits in BLOCK_HITS_TO_COLOR:
                    self.color = BLOCK_HITS_TO_COLOR[self.hits]
            return True
        return False
