import random

def random_powerup():
    powerups = [
        'expand_paddle',  # Aumenta a barra
        'slow_ball',      # Bola mais lenta
    ]
    # 20% de chance de dropar um power-up
    if random.random() < 0.2:
        return random.choice(powerups)
    return None 