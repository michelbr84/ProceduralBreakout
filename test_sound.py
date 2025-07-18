import pygame
import numpy as np
import time

def gen_beep(freq, ms):
    sample_rate = 44100
    t = np.linspace(0, ms/1000, int(sample_rate*ms/1000), False)
    tone = np.sin(freq * t * 2 * np.pi) * 32767
    tone = tone.astype(np.int16)
    stereo = np.column_stack([tone, tone])  # Corrigir para estéreo
    sound = pygame.sndarray.make_sound(stereo)
    return sound

pygame.init()
pygame.mixer.init()
print('Tocando beep de teste...')
sound = gen_beep(800, 500)
sound.play()
time.sleep(1)
print('Teste finalizado.') 