import random

from src import settings
from src.block import BLOCK_HIT_COLORS


def generate_blocks(level=1):
    rows = random.randint(*settings.BLOCK_ROWS_RANGE)
    cols = random.randint(*settings.BLOCK_COLS_RANGE)
    grid = []
    max_hits = min(3 + (level - 1), len(BLOCK_HIT_COLORS))  # Level 1: até 3 hits, Level 2: até 4 hits, ...
    block_colors = [color for color, hits in BLOCK_HIT_COLORS if hits <= max_hits]
    for y in range(rows):
        row = []
        for x in range(cols):
            # 80% de chance de existir bloco nesta posição
            if random.random() < 0.8:
                color = random.choice(block_colors)
                row.append({'exists': True, 'color': color})
            else:
                row.append({'exists': False})
        grid.append(row)
    return grid
