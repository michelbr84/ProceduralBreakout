import pygame
import sys
from src.paddle import Paddle
from src.ball import Ball
from src.block import Block, BLOCK_COLOR_SCORES
from src import level_generator
from src import settings
from src import ui
from src import utils
import time

# Inicialização do Pygame
pygame.init()
pygame.mixer.init()

# Sons do sistema (tons simples)
def gen_beep(freq, ms):
    import numpy as np
    sample_rate = 44100
    t = np.linspace(0, ms/1000, int(sample_rate*ms/1000), False)
    tone = np.sin(freq * t * 2 * np.pi) * 32767
    tone = tone.astype(np.int16)
    sound = pygame.sndarray.make_sound(tone)
    return sound

try:
    import numpy as np
    sound_paddle = gen_beep(800, 60)
    sound_wall = gen_beep(400, 60)
    sound_life = gen_beep(200, 300)
    sound_block_hit = gen_beep(1200, 40)
    sound_block_destroy = gen_beep(1600, 80)
except Exception:
    sound_paddle = sound_wall = sound_life = sound_block_hit = sound_block_destroy = None

# Configurações iniciais
SCREEN_WIDTH = settings.SCREEN_WIDTH
SCREEN_HEIGHT = settings.SCREEN_HEIGHT
FPS = settings.FPS
LIVES_INIT = 3

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption('Procedural Breakout')
clock = pygame.time.Clock()

sound_last_played = {
    'block_destroy': 0,
    'block_hit': 0,
    'paddle': 0,
    'wall': 0,
    'life': 0,
    'powerup': 0,
}
SOUND_COOLDOWN = 0.2  # segundos

def create_blocks(level):
    grid = level_generator.generate_blocks(level=level)
    blocks = []
    y0 = 60  # Margem superior
    for row_idx, row in enumerate(grid):
        x0 = 40  # Margem esquerda
        for col_idx, cell in enumerate(row):
            if cell.get('exists'):
                x = x0 + col_idx * (settings.BLOCK_WIDTH + settings.BLOCK_GAP)
                y = y0 + row_idx * (settings.BLOCK_HEIGHT + settings.BLOCK_GAP)
                blocks.append(Block(x, y, cell['color']))
    return blocks

def reset_game(full_reset=True, blocks=None, level=1):
    paddle = Paddle()
    ball = Ball()
    if full_reset or blocks is None:
        blocks = create_blocks(level)
        score = 0
        lives = LIVES_INIT
    else:
        score = None  # Não altera
        lives = None  # Não altera
    return paddle, ball, blocks, score, lives, False  # False = not game over

# Estados do jogo
game_state = 'menu'  # 'menu', 'playing', 'gameover', 'win'
paddle = ball = blocks = score = game_over = win = lives = None
level = 1

sound_flags = {'block_destroy': False, 'block_hit': False, 'paddle': False, 'wall': False, 'life': False, 'powerup': False}
# Variáveis globais para power-ups
powerups_on_screen = []
powerup_active = None
powerup_timer = 0

# Loop principal
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            # running = False (removido para debug ESC)
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
    pass
                # running = False (removido para debug ESC)
            if game_state == 'menu' and event.key == pygame.K_SPACE:
                level = 1
                paddle, ball, blocks, score, lives, game_over = reset_game(full_reset=True, level=level)
                win = False
                game_state = 'playing'
            elif game_state in ('gameover', 'win') and event.key == pygame.K_r:
                game_state = 'menu'
            elif game_state == 'playing':
                if event.key == pygame.K_SPACE and not game_over:
                    ball.launch()
                if event.key == pygame.K_r:
                    game_state = 'menu'
                if event.key == pygame.K_f:
                    # Deixar apenas um bloco aleatório vivo
                    vivos = [b for b in blocks if b.alive]
                    if len(vivos) > 1:
                        import random
                        keep = random.choice(vivos)
                        for b in blocks:
                            if b is not keep:
                                b.alive = False

    screen.fill(settings.BG_COLOR)

    if game_state == 'menu':
        ui.draw_message(screen, "Procedural Breakout", "Pressione ESPAÇO para começar")
        font = pygame.font.SysFont(None, 28)
        instructions = [
            "← → : mover barra",
            "ESPAÇO: lançar bola",
            "R: reiniciar partida",
            "ESC: sair do jogo"
        ]
        for i, text in enumerate(instructions):
            surf = font.render(text, True, (180, 180, 200))
            rect = surf.get_rect(center=(SCREEN_WIDTH//2, SCREEN_HEIGHT//2 + 80 + i*30))
            screen.blit(surf, rect)

    elif game_state == 'playing':
        if not game_over:
            keys = pygame.key.get_pressed()
            paddle.update(keys)
            prev_x, prev_y = ball.x, ball.y
            prev_vx, prev_vy = ball.vx, ball.vy
            ball.update(paddle)

            # Colisão bola-blocos
            for block in blocks:
                collided = False
                hit, block_score, block_event = block.collide_with_ball(ball)
                now = time.time()
                if hit and now - sound_last_played['block_destroy'] > SOUND_COOLDOWN:
                    ball.vy *= -1
                    score += block_score
                    if sound_block_destroy:
                        print('Som: bloco destruído')
                        sound_block_destroy.stop()
                        sound_block_destroy.set_volume(1.0); sound_block_destroy.play()
                    sound_last_played['block_destroy'] = now
                    # Power-up drop
                    pu = utils.random_powerup()
                    if pu:
                        powerups_on_screen.append({'type': pu, 'x': block.rect.centerx, 'y': block.rect.centery, 'active': True})
                    collided = True
                elif block.alive and block.rect.colliderect(pygame.Rect(
                    ball.x - ball.radius, ball.y - ball.radius, ball.radius * 2, ball.radius * 2)):
                    ball.vy *= -1
                    if sound_block_hit:
                        sound_block_hit.stop()
                        sound_block_hit.set_volume(1.0); sound_block_hit.play()
                    collided = True
                if collided:
                    break

            # Colisão bola-paddle (apenas se mudou de direção vertical e estava acima da paddle)
            if prev_vy > 0 and ball.vy < 0 and prev_y < paddle.rect.top and ball.y >= paddle.rect.top:
                if sound_paddle:
                    sound_paddle.stop()
                    sound_paddle.set_volume(1.0); sound_paddle.play()
            # Colisão bola-parede (apenas se mudou de direção horizontal ou bateu no topo)
            if (prev_vx != ball.vx) or (prev_vy != ball.vy and ball.y - ball.radius <= 0):
                if sound_wall:
                    sound_wall.stop()
                    sound_wall.set_volume(1.0); sound_wall.play()

            # Se a bola cair abaixo da tela, perde vida ou game over
            if ball.y - ball.radius > SCREEN_HEIGHT:
                lives -= 1
                if sound_life:
                    sound_life.stop()
                    sound_life.set_volume(1.0); sound_life.play()
                if lives > 0:
                    paddle = Paddle()
                    ball = Ball()
                else:
                    game_over = True
                    win = False

            # Vitória: todos blocos destruídos
            if all(not block.alive for block in blocks):
                win = True
                if level < 10:
                    level += 1
                    paddle, ball, blocks, score, lives, game_over = reset_game(full_reset=True, level=level)
                    game_state = 'playing'
                else:
                    game_state = 'win'

        paddle.draw(screen)
        ball.draw(screen)
        for block in blocks:
            block.draw(screen)
        ui.draw_score(screen, score)
        # Exibir vidas
        font = pygame.font.SysFont(None, 28)
        lives_surf = font.render(f"Vidas: {lives}", True, (255, 200, 80))
        screen.blit(lives_surf, (SCREEN_WIDTH - 120, 10))
        # Exibir level
        level_surf = font.render(f"Fase: {level}", True, (180, 220, 255))
        screen.blit(level_surf, (SCREEN_WIDTH//2 - 40, 10))
        # Exibir número de blocos restantes
        blocos_vivos = sum(1 for b in blocks if b.alive)
        blocos_surf = font.render(f"Blocos: {blocos_vivos}", True, (200, 255, 200))
        screen.blit(blocos_surf, (SCREEN_WIDTH//2 + 60, 10))

        if game_over:
            game_state = 'gameover'

    elif game_state == 'win':
        ui.draw_message(screen, "Vitória! (Fase 10)", "Pressione R para voltar ao menu")

    elif game_state == 'gameover':
        ui.draw_message(screen, "Game Over", "Pressione R para voltar ao menu")

    pygame.display.flip()
    clock.tick(FPS)

pygame.quit()
sys.exit() 
sound_flags = {'block_destroy': False, 'block_hit': False, 'paddle': False, 'wall': False, 'life': False, 'powerup': False}
menu_state = None  # None, 'pause', 'options'
sound_volume = 1.0

def set_all_volumes(vol):
    if sound_paddle: sound_paddle.set_volume(vol)
    if sound_wall: sound_wall.set_volume(vol)
    if sound_life: sound_life.set_volume(vol)
    if sound_block_hit: sound_block_hit.set_volume(vol)
    if sound_block_destroy: sound_block_destroy.set_volume(vol)
    if sound_powerup: sound_powerup.set_volume(vol)

set_all_volumes(sound_volume)
