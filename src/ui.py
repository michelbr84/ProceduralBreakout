import pygame
from src import settings

score_font = None
msg_font = None

def init_fonts():
    global score_font, msg_font
    if score_font is None:
        score_font = pygame.font.SysFont(None, settings.SCORE_FONT_SIZE)
    if msg_font is None:
        msg_font = pygame.font.SysFont(None, settings.MSG_FONT_SIZE)

def draw_score(surface, score):
    init_fonts()
    score_surf = score_font.render(f"Score: {score}", True, settings.SCORE_COLOR)
    surface.blit(score_surf, (20, 10))

def draw_message(surface, msg, submsg=None):
    init_fonts()
    msg_surf = msg_font.render(msg, True, settings.MSG_COLOR)
    msg_rect = msg_surf.get_rect(center=(settings.SCREEN_WIDTH//2, settings.SCREEN_HEIGHT//2 - 30))
    surface.blit(msg_surf, msg_rect)
    if submsg:
        info_surf = score_font.render(submsg, True, settings.MSG_COLOR)
        info_rect = info_surf.get_rect(center=(settings.SCREEN_WIDTH//2, settings.SCREEN_HEIGHT//2 + 30))
        surface.blit(info_surf, info_rect) 