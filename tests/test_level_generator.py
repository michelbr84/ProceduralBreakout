import os
import sys
import unittest

# Adiciona o diretório raiz ao sys.path para importação dos módulos src
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from src import level_generator, settings


class TestLevelGenerator(unittest.TestCase):
    def test_generate_blocks(self):
        for _ in range(10):  # Testa múltiplas gerações
            grid = level_generator.generate_blocks()
            self.assertTrue(settings.BLOCK_ROWS_RANGE[0] <= len(grid) <= settings.BLOCK_ROWS_RANGE[1])
            self.assertTrue(all(settings.BLOCK_COLS_RANGE[0] <= len(row) <= settings.BLOCK_COLS_RANGE[1] for row in grid))
            for row in grid:
                for block in row:
                    self.assertIn('exists', block)
                    if block['exists']:
                        self.assertIn('color', block)
                        self.assertIn(block['color'], settings.BLOCK_COLORS)

if __name__ == '__main__':
    unittest.main()
