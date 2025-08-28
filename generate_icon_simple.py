#!/usr/bin/env python3
"""Generate a simple icon for Procedural Breakout using matplotlib"""

import os
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as patches

def create_icon():
    # Create figure
    fig, ax = plt.subplots(1, 1, figsize=(5.12, 5.12), dpi=100)
    ax.set_xlim(0, 100)
    ax.set_ylim(0, 100)
    ax.set_aspect('equal')
    
    # Dark background
    ax.add_patch(patches.Rectangle((0, 0), 100, 100, facecolor='#1e1e28'))
    
    # Draw blocks
    colors = ['#dc5050', '#50b4dc', '#50dc78', '#f0dc50', '#b450dc', '#dca050']
    block_width = 18
    block_height = 6
    gap = 2
    
    for row in range(3):
        for col in range(4):
            x = 10 + col * (block_width + gap)
            y = 70 - row * (block_height + gap)
            color = colors[(row * 4 + col) % len(colors)]
            ax.add_patch(patches.Rectangle((x, y), block_width, block_height, 
                                         facecolor=color, edgecolor='none'))
    
    # Draw ball
    ball = patches.Circle((50, 30), 4, facecolor='white', edgecolor='none')
    ax.add_patch(ball)
    
    # Draw paddle
    paddle = patches.Rectangle((40, 10), 20, 4, facecolor='#c8c8dc', edgecolor='none')
    ax.add_patch(paddle)
    
    # Remove axes
    ax.axis('off')
    
    # Create data directory if it doesn't exist
    if not os.path.exists('data'):
        os.makedirs('data')
    
    # Save icon
    plt.savefig('data/icon.png', bbox_inches='tight', pad_inches=0, transparent=True)
    plt.close()
    
    print("✅ Icon generated successfully!")
    print("  - data/icon.png (512x512)")

if __name__ == '__main__':
    try:
        create_icon()
    except ImportError as e:
        print(f"❌ Error: {e}")
        print("\nTo generate icon manually:")
        print("1. Create a 'data' directory")
        print("2. Add a PNG image named 'icon.png' (recommended size: 512x512)")
        print("3. The icon should represent a breakout game with blocks, ball, and paddle")