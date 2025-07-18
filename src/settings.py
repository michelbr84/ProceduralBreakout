# settings.py
# Configurações globais do Procedural Breakout

# Tela
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
FPS = 60

# Barra (Paddle)
PADDLE_WIDTH = 100
PADDLE_HEIGHT = 16
PADDLE_COLOR = (200, 200, 220)
PADDLE_SPEED = 8

# Bola
BALL_RADIUS = 10
BALL_COLOR = (255, 255, 255)
BALL_SPEED = 6

# Blocos
BLOCK_WIDTH = 60
BLOCK_HEIGHT = 24
BLOCK_GAP = 6  # Espaço entre blocos
BLOCK_ROWS_RANGE = (4, 8)
BLOCK_COLS_RANGE = (6, 12)
BLOCK_COLORS = [
    (220, 80, 80),   # Vermelho suave
    (80, 180, 220),  # Azul claro
    (80, 220, 120),  # Verde suave
    (240, 220, 80),  # Amarelo
    (180, 80, 220),  # Roxo
    (220, 160, 80),  # Laranja
]

# Fundo
BG_COLOR = (30, 30, 40)

# Score
SCORE_COLOR = (255, 255, 255)
SCORE_FONT_SIZE = 32

# Mensagens
MSG_COLOR = (255, 255, 255)
MSG_FONT_SIZE = 48 