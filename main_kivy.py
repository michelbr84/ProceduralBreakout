import random

from kivy.app import App
from kivy.clock import Clock
from kivy.core.window import Window
from kivy.graphics import Color, Ellipse, Rectangle
from kivy.uix.widget import Widget

# Configurações do jogo
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
FPS = 60

# Cores
BG_COLOR = (0.12, 0.12, 0.16, 1)
PADDLE_COLOR = (0.78, 0.78, 0.86, 1)
BALL_COLOR = (1, 1, 1, 1)
TEXT_COLOR = (1, 1, 1, 1)

# Configurações dos elementos
PADDLE_WIDTH = 100
PADDLE_HEIGHT = 16
BALL_RADIUS = 10
BALL_SPEED = 6
PADDLE_SPEED = 8

# Estados do jogo
STATE_MENU = 'menu'
STATE_PLAYING = 'playing'
STATE_PAUSE = 'pause'
STATE_GAME_OVER = 'game_over'
STATE_WIN = 'win'

class GameWidget(Widget):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.state = STATE_MENU
        self.score = 0
        self.lives = 3
        self.level = 1
        self.sound_volume = 1.0
        self.show_block_hits = True

        # Elementos do jogo
        self.paddle = None
        self.ball = None
        self.blocks = []

        # Controles touch
        self.touch_start_x = 0
        self.paddle_start_x = 0

        # Inicializar jogo
        self.init_game()

        # Configurar clock para atualização
        Clock.schedule_interval(self.update, 1.0 / FPS)

    def init_game(self):
        """Inicializar elementos do jogo"""
        # Paddle
        self.paddle = {
            'x': (SCREEN_WIDTH - PADDLE_WIDTH) // 2,
            'y': SCREEN_HEIGHT - PADDLE_HEIGHT - 30,
            'width': PADDLE_WIDTH,
            'height': PADDLE_HEIGHT
        }

        # Ball
        self.ball = {
            'x': SCREEN_WIDTH // 2,
            'y': SCREEN_HEIGHT // 2,
            'vx': BALL_SPEED,
            'vy': -BALL_SPEED,
            'radius': BALL_RADIUS,
            'moving': False
        }

        # Gerar blocos
        self.generate_blocks()

    def generate_blocks(self):
        """Gerar blocos proceduralmente"""
        self.blocks = []
        rows = random.randint(4, 8)
        cols = random.randint(6, 12)

        # Cores dos blocos (RGB)
        colors = [
            (0.86, 0.31, 0.31),  # Vermelho
            (0.31, 0.71, 0.86),  # Azul
            (0.31, 0.86, 0.47),  # Verde
            (0.94, 0.86, 0.31),  # Amarelo
            (0.71, 0.31, 0.86),  # Roxo
            (0.86, 0.63, 0.31),  # Laranja
        ]

        y0 = 60
        for row in range(rows):
            for col in range(cols):
                if random.random() < 0.8:  # 80% chance de bloco existir
                    color = random.choice(colors)
                    hits = random.randint(1, min(3 + self.level, 10))
                    x = 40 + col * 66  # 60 + 6 gap
                    y = y0 + row * 30   # 24 + 6 gap

                    self.blocks.append({
                        'x': x, 'y': y, 'width': 60, 'height': 24,
                        'color': color, 'hits': hits, 'alive': True
                    })

    def update(self, dt):
        """Atualizar lógica do jogo"""
        if self.state == STATE_PLAYING:
            self.update_ball()
            self.check_collisions()
            self.check_win_lose()

    def update_ball(self):
        """Atualizar posição da bola"""
        if not self.ball['moving']:
            # Bola segue o paddle antes do lançamento
            self.ball['x'] = self.paddle['x'] + self.paddle['width'] // 2
            self.ball['y'] = self.paddle['y'] - self.ball['radius']
            return

        # Mover bola
        self.ball['x'] += self.ball['vx']
        self.ball['y'] += self.ball['vy']

        # Colisão com paredes
        if self.ball['x'] - self.ball['radius'] <= 0 or self.ball['x'] + self.ball['radius'] >= SCREEN_WIDTH:
            self.ball['vx'] *= -1

        if self.ball['y'] - self.ball['radius'] <= 0:
            self.ball['vy'] *= -1

    def check_collisions(self):
        """Verificar colisões"""
        # Colisão bola-paddle
        if (self.ball['y'] + self.ball['radius'] >= self.paddle['y'] and
            self.ball['y'] - self.ball['radius'] <= self.paddle['y'] + self.paddle['height'] and
            self.ball['x'] >= self.paddle['x'] and self.ball['x'] <= self.paddle['x'] + self.paddle['width']):

            if self.ball['vy'] > 0:  # Bola descendo
                self.ball['vy'] = -abs(BALL_SPEED)
                # Ajustar direção baseado no ponto de contato
                offset = (self.ball['x'] - (self.paddle['x'] + self.paddle['width'] // 2)) / (self.paddle['width'] // 2)
                self.ball['vx'] = BALL_SPEED * offset

        # Colisão bola-blocos
        for block in self.blocks:
            if not block['alive']:
                continue

            if (self.ball['x'] >= block['x'] and self.ball['x'] <= block['x'] + block['width'] and
                self.ball['y'] >= block['y'] and self.ball['y'] <= block['y'] + block['height']):

                block['hits'] -= 1
                if block['hits'] <= 0:
                    block['alive'] = False
                    self.score += 100

                # Reverter direção da bola
                self.ball['vy'] *= -1
                break

    def check_win_lose(self):
        """Verificar condições de vitória/derrota"""
        # Bola saiu da tela
        if self.ball['y'] - self.ball['radius'] > SCREEN_HEIGHT:
            self.lives -= 1
            if self.lives > 0:
                self.ball['moving'] = False
                self.ball['x'] = self.paddle['x'] + self.paddle['width'] // 2
                self.ball['y'] = self.paddle['y'] - self.ball['radius']
            else:
                self.state = STATE_GAME_OVER

        # Todos os blocos destruídos
        if all(not block['alive'] for block in self.blocks):
            self.level = min(self.level + 1, 10)
            self.generate_blocks()
            self.ball['moving'] = False
            self.ball['x'] = self.paddle['x'] + self.paddle['width'] // 2
            self.ball['y'] = self.paddle['y'] - self.ball['radius']

    def launch_ball(self):
        """Lançar a bola"""
        if not self.ball['moving']:
            self.ball['moving'] = True
            self.ball['vy'] = -abs(BALL_SPEED)
            self.ball['vx'] = random.choice([-1, 1]) * abs(BALL_SPEED)

    def move_paddle(self, direction):
        """Mover paddle"""
        if direction == 'left':
            self.paddle['x'] = max(0, self.paddle['x'] - PADDLE_SPEED)
        elif direction == 'right':
            self.paddle['x'] = min(SCREEN_WIDTH - self.paddle['width'], self.paddle['x'] + PADDLE_SPEED)

    def on_touch_down(self, touch):
        """Evento de toque na tela"""
        if self.state == STATE_MENU:
            self.state = STATE_PLAYING
            self.init_game()
        elif self.state == STATE_PLAYING:
            self.touch_start_x = touch.x
            self.paddle_start_x = self.paddle['x']
            self.launch_ball()
        elif self.state == STATE_GAME_OVER or self.state == STATE_WIN:
            self.state = STATE_MENU

    def on_touch_move(self, touch):
        """Evento de movimento do toque"""
        if self.state == STATE_PLAYING:
            # Mover paddle baseado no movimento do toque
            delta_x = touch.x - self.touch_start_x
            new_x = self.paddle_start_x + delta_x
            self.paddle['x'] = max(0, min(SCREEN_WIDTH - self.paddle['width'], new_x))

    def draw(self):
        """Desenhar elementos do jogo"""
        self.canvas.clear()

        with self.canvas:
            # Fundo
            Color(*BG_COLOR)
            Rectangle(pos=self.pos, size=self.size)

            if self.state == STATE_MENU:
                self.draw_menu()
            elif self.state == STATE_PLAYING:
                self.draw_game()
            elif self.state == STATE_PAUSE:
                self.draw_pause()
            elif self.state == STATE_GAME_OVER:
                self.draw_game_over()
            elif self.state == STATE_WIN:
                self.draw_win()

    def draw_menu(self):
        """Desenhar menu principal"""
        # Título
        Color(*TEXT_COLOR)
        # Simular texto com retângulos
        title_width = 300
        title_height = 50
        Rectangle(pos=(SCREEN_WIDTH//2 - title_width//2, SCREEN_HEIGHT//2 + 50),
                 size=(title_width, title_height))

        # Instruções
        inst_width = 400
        inst_height = 30
        Rectangle(pos=(SCREEN_WIDTH//2 - inst_width//2, SCREEN_HEIGHT//2 - 50),
                 size=(inst_width, inst_height))

    def draw_game(self):
        """Desenhar elementos do jogo"""
        # Paddle
        Color(*PADDLE_COLOR)
        Rectangle(pos=(self.paddle['x'], self.paddle['y']),
                 size=(self.paddle['width'], self.paddle['height']))

        # Ball
        Color(*BALL_COLOR)
        Ellipse(pos=(self.ball['x'] - self.ball['radius'], self.ball['y'] - self.ball['radius']),
                size=(self.ball['radius'] * 2, self.ball['radius'] * 2))

        # Blocks
        for block in self.blocks:
            if block['alive']:
                Color(*block['color'])
                Rectangle(pos=(block['x'], block['y']),
                         size=(block['width'], block['height']))

        # HUD
        Color(*TEXT_COLOR)
        # Score
        Rectangle(pos=(20, SCREEN_HEIGHT - 40), size=(100, 30))
        # Lives
        Rectangle(pos=(SCREEN_WIDTH - 120, SCREEN_HEIGHT - 40), size=(100, 30))
        # Level
        Rectangle(pos=(SCREEN_WIDTH//2 - 50, SCREEN_HEIGHT - 40), size=(100, 30))

    def draw_pause(self):
        """Desenhar tela de pausa"""
        Color(*TEXT_COLOR)
        pause_width = 200
        pause_height = 50
        Rectangle(pos=(SCREEN_WIDTH//2 - pause_width//2, SCREEN_HEIGHT//2),
                 size=(pause_width, pause_height))

    def draw_game_over(self):
        """Desenhar tela de game over"""
        Color(*TEXT_COLOR)
        go_width = 200
        go_height = 50
        Rectangle(pos=(SCREEN_WIDTH//2 - go_width//2, SCREEN_HEIGHT//2),
                 size=(go_width, go_height))

    def draw_win(self):
        """Desenhar tela de vitória"""
        Color(*TEXT_COLOR)
        win_width = 200
        win_height = 50
        Rectangle(pos=(SCREEN_WIDTH//2 - win_width//2, SCREEN_HEIGHT//2),
                 size=(win_width, win_height))

class ProceduralBreakoutApp(App):
    def build(self):
        # Configurar tamanho da janela
        Window.size = (SCREEN_WIDTH, SCREEN_HEIGHT)
        Window.clearcolor = BG_COLOR

        # Criar widget principal
        game = GameWidget()

        # Configurar callback para desenho
        def redraw_callback(dt):
            game.draw()

        Clock.schedule_interval(redraw_callback, 1.0 / FPS)

        return game

if __name__ == '__main__':
    ProceduralBreakoutApp().run()
