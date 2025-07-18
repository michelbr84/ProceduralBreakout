import pygame
import numpy as np
import time

def gen_beep(freq, ms):
    sample_rate = 44100
    t = np.linspace(0, ms/1000, int(sample_rate*ms/1000), False)
    tone = np.sin(freq * t * 2 * np.pi) * 32767
    tone = tone.astype(np.int16)
    stereo = np.column_stack([tone, tone])
    sound = pygame.sndarray.make_sound(stereo)
    sound.set_volume(1.0)
    return sound

pygame.init()
pygame.mixer.init()
print('Antes de set_mode')
screen = pygame.display.set_mode((400, 200))
print('Depois de set_mode')
input('Pressione Enter para iniciar o loop e abrir a janela do Pygame...')
clock = pygame.time.Clock()
beep = gen_beep(1000, 300)

print('Loop iniciado. Pressione qualquer tecla na janela para ouvir beep. Feche a janela para sair.')
start_time = time.time()
running = True
while running:
    for event in pygame.event.get():
        print('Evento:', event)
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            print('Beep!')
            beep.stop()
            beep.play()
    if time.time() - start_time > 30:
        print('Tempo limite atingido, saindo...')
        running = False
    clock.tick(60)
pygame.quit() 