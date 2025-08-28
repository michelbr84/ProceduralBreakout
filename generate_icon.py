#!/usr/bin/env python3
"""Generate a simple icon for Procedural Breakout"""

import os
from PIL import Image, ImageDraw, ImageFont

def create_icon():
    # Create a 512x512 icon (can be resized later)
    size = 512
    img = Image.new('RGBA', (size, size), (0, 0, 0, 0))
    draw = ImageDraw.Draw(img)
    
    # Background - dark blue gradient
    for y in range(size):
        color_value = int(30 + (y / size) * 20)
        draw.rectangle([(0, y), (size, y+1)], fill=(color_value, color_value, color_value+10, 255))
    
    # Draw paddle (white rectangle at bottom)
    paddle_width = size // 4
    paddle_height = size // 20
    paddle_x = (size - paddle_width) // 2
    paddle_y = size - size // 8
    draw.rectangle([paddle_x, paddle_y, paddle_x + paddle_width, paddle_y + paddle_height], 
                   fill=(200, 200, 220, 255))
    
    # Draw ball (white circle)
    ball_radius = size // 16
    ball_x = size // 2
    ball_y = paddle_y - ball_radius * 3
    draw.ellipse([ball_x - ball_radius, ball_y - ball_radius, 
                  ball_x + ball_radius, ball_y + ball_radius], 
                 fill=(255, 255, 255, 255))
    
    # Draw blocks (colorful rectangles)
    block_width = size // 8
    block_height = size // 24
    block_gap = size // 40
    colors = [
        (220, 80, 80, 255),   # Red
        (80, 180, 220, 255),  # Blue
        (80, 220, 120, 255),  # Green
        (240, 220, 80, 255),  # Yellow
        (180, 80, 220, 255),  # Purple
        (220, 160, 80, 255),  # Orange
    ]
    
    start_y = size // 8
    for row in range(3):
        for col in range(4):
            x = size // 8 + col * (block_width + block_gap)
            y = start_y + row * (block_height + block_gap)
            color = colors[(row * 4 + col) % len(colors)]
            draw.rectangle([x, y, x + block_width, y + block_height], fill=color)
    
    # Save the icon
    if not os.path.exists('data'):
        os.makedirs('data')
    
    # Save different sizes
    img.save('data/icon.png')
    img.resize((192, 192), Image.Resampling.LANCZOS).save('data/icon_192.png')
    img.resize((96, 96), Image.Resampling.LANCZOS).save('data/icon_96.png')
    img.resize((48, 48), Image.Resampling.LANCZOS).save('data/icon_48.png')
    
    print("✅ Icons generated successfully!")
    print("  - data/icon.png (512x512)")
    print("  - data/icon_192.png (192x192)")
    print("  - data/icon_96.png (96x96)")
    print("  - data/icon_48.png (48x48)")

if __name__ == '__main__':
    try:
        create_icon()
    except ImportError:
        print("❌ Error: Pillow library not installed!")
        print("To generate icons, install Pillow:")
        print("  pip install Pillow")
        print("\nAlternatively, you can add any PNG image as data/icon.png")