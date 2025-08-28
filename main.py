import random

import pygame

from src import settings
from src.ball import Ball
from src.block import BLOCK_HIT_COLORS, Block
from src.level_generator import generate_blocks
from src.paddle import Paddle

pygame.init()
screen = pygame.display.set_mode((settings.SCREEN_WIDTH, settings.SCREEN_HEIGHT))
pygame.display.set_caption('Procedural Breakout')
clock = pygame.time.Clock()

state = 'menu'  # 'menu', 'jogo', 'pause', 'options'
sound_volume = 1.0
show_block_hits = True

# --- Som simples para eventos ---
def gen_beep(freq, ms):
    import numpy as np
    sample_rate = 44100
    t = np.linspace(0, ms/1000, int(sample_rate*ms/1000), False)
    tone = np.sin(freq * t * 2 * np.pi) * 32767
    tone = tone.astype(np.int16)
    stereo = np.column_stack([tone, tone])
    sound = pygame.sndarray.make_sound(stereo)
    sound.set_volume(sound_volume)
    return sound

beep = gen_beep(1000, 300)

# --- Estado do jogo ---
def novo_jogo():
    paddle = Paddle()
    ball = Ball()
    level = 1
    score = 0
    blocks = criar_blocos(level)
    vidas = 3
    return paddle, ball, blocks, level, score, vidas

def criar_blocos(level):
    grid = generate_blocks(level)
    blocks = []
    y0 = 60
    for row_idx, row in enumerate(grid):
        for col_idx, cell in enumerate(row):
            if cell.get('exists'):
                color = cell['color']
                x = 40 + col_idx * (settings.BLOCK_WIDTH + settings.BLOCK_GAP)
                y = y0 + row_idx * (settings.BLOCK_HEIGHT + settings.BLOCK_GAP)
                hits = [hits for c, hits in BLOCK_HIT_COLORS if c == color][0]
                block = Block(x, y, color, hits)
                blocks.append(block)
    return blocks

paddle, ball, blocks, level, score, vidas = novo_jogo()

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if state == 'menu' and event.key == pygame.K_SPACE:
                state = 'jogo'
                paddle, ball, blocks, level, score, vidas = novo_jogo()
            elif state == 'menu' and event.key == pygame.K_n:
                show_block_hits = not show_block_hits
            elif state == 'pause' and event.key == pygame.K_n:
                show_block_hits = not show_block_hits
            elif state == 'jogo' and event.key == pygame.K_ESCAPE:
                state = 'pause'
            elif state == 'jogo' and event.key == pygame.K_SPACE:
                ball.launch()
            elif state == 'jogo' and event.key == pygame.K_f:
                # Deixar apenas um bloco aleatório vivo
                vivos = [b for b in blocks if b.alive]
                if len(vivos) > 1:
                    keep = random.choice(vivos)
                    for b in blocks:
                        if b is not keep:
                            b.alive = False
            elif state == 'pause':
                if event.key == pygame.K_ESCAPE:
                    state = 'jogo'
                elif event.key == pygame.K_o:
                    state = 'options'
            elif state == 'options':
                if event.key == pygame.K_ESCAPE:
                    state = 'pause'
                elif event.key == pygame.K_UP:
                    sound_volume = min(1.0, sound_volume + 0.1)
                    beep.set_volume(sound_volume)
                elif event.key == pygame.K_DOWN:
                    sound_volume = max(0.0, sound_volume - 0.1)
                    beep.set_volume(sound_volume)
                elif event.key == pygame.K_SPACE:
                    beep.play()

    if state == 'menu':
        screen.fill((30, 30, 40))
        font = pygame.font.SysFont(None, 48)
        text = font.render('Procedural Breakout', True, (255,255,255))
        screen.blit(text, (180, 200))
        font2 = pygame.font.SysFont(None, 32)
        text2 = font2.render('Pressione ESPAÇO para começar', True, (200,200,200))
        screen.blit(text2, (200, 300))
        text3 = font2.render(f'N - {"Ocultar" if show_block_hits else "Mostrar"} Números nos Blocos', True, (180,255,180))
        screen.blit(text3, (180, 350))
    elif state == 'pause':
        screen.fill((30, 30, 40))
        font = pygame.font.SysFont(None, 48)
        text = font.render('PAUSA', True, (255,255,255))
        screen.blit(text, (320, 250))
        font2 = pygame.font.SysFont(None, 32)
        text2 = font2.render('ESC - Voltar ao jogo | O - Opções de Som', True, (200,200,200))
        screen.blit(text2, (140, 320))
        text3 = font2.render(f'N - {"Ocultar" if show_block_hits else "Mostrar"} Números nos Blocos', True, (180,255,180))
        screen.blit(text3, (180, 370))
    elif state == 'options':
        screen.fill((30, 30, 40))
        font = pygame.font.SysFont(None, 48)
        text = font.render('Opções de Som', True, (255,255,255))
        screen.blit(text, (250, 180))
        font2 = pygame.font.SysFont(None, 32)
        text2 = font2.render(f'Volume: {int(sound_volume*100)}% (Setas)', True, (200,200,200))
        screen.blit(text2, (220, 260))
        text3 = font2.render('ESPAÇO - Testar beep', True, (180,255,180))
        screen.blit(text3, (260, 320))
        text4 = font2.render('ESC - Voltar ao menu de pausa', True, (200,200,200))
        screen.blit(text4, (200, 380))
    elif state == 'jogo':
        screen.fill(settings.BG_COLOR)
        keys = pygame.key.get_pressed()
        paddle.update(keys)
        ball.update(paddle)
        # Colisão bola-bloco
        for block in blocks:
            if block.alive and block.collide_with_ball(ball):
                if not block.alive:
                    score += 100
                ball.vy *= -1
                beep.play()
                break
        # Bola fora da tela
        if ball.y - ball.radius > settings.SCREEN_HEIGHT:
            vidas -= 1
            if vidas > 0:
                ball.reset()
            else:
                state = 'menu'  # Reinicia para o menu
        # Próximo nível
        if all(not block.alive for block in blocks):
            level = min(level + 1, 10)
            blocks = criar_blocos(level)
            ball.reset()
        # Desenhar paddle, bola, blocos
        paddle.draw(screen)
        ball.draw(screen)
        for block in blocks:
            block.draw(screen, show_block_hits)
        # Score e vidas
        font = pygame.font.SysFont(None, 32)
        score_surf = font.render(f'Score: {score}', True, (255,255,255))
        screen.blit(score_surf, (20, 10))
        vidas_surf = font.render(f'Vidas: {vidas}', True, (255,255,255))
        screen.blit(vidas_surf, (700, 10))
    pygame.display.flip()
    clock.tick(settings.FPS)
pygame.quit()
