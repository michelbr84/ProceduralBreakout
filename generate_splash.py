#!/usr/bin/env python3
"""Generate a simple splash screen for Procedural Breakout"""

import os

def create_splash_svg():
    """Create a simple SVG splash screen"""
    
    svg_content = '''<?xml version="1.0" encoding="UTF-8"?>
<svg width="720" height="1280" viewBox="0 0 720 1280" xmlns="http://www.w3.org/2000/svg">
  <!-- Background -->
  <rect width="720" height="1280" fill="#1E1E28"/>
  
  <!-- Title -->
  <text x="360" y="500" font-family="Arial, sans-serif" font-size="60" font-weight="bold" text-anchor="middle" fill="white">
    PROCEDURAL
  </text>
  <text x="360" y="580" font-family="Arial, sans-serif" font-size="60" font-weight="bold" text-anchor="middle" fill="white">
    BREAKOUT
  </text>
  
  <!-- Decorative blocks -->
  <rect x="160" y="300" width="80" height="30" fill="#dc5050" rx="5"/>
  <rect x="260" y="300" width="80" height="30" fill="#50b4dc" rx="5"/>
  <rect x="360" y="300" width="80" height="30" fill="#50dc78" rx="5"/>
  <rect x="460" y="300" width="80" height="30" fill="#f0dc50" rx="5"/>
  
  <!-- Ball -->
  <circle cx="360" cy="700" r="20" fill="white"/>
  
  <!-- Paddle -->
  <rect x="300" y="780" width="120" height="20" fill="#c8c8dc" rx="10"/>
  
  <!-- Loading text -->
  <text x="360" y="1000" font-family="Arial, sans-serif" font-size="30" text-anchor="middle" fill="#888888">
    Loading...
  </text>
</svg>'''
    
    # Create data directory if it doesn't exist
    if not os.path.exists('data'):
        os.makedirs('data')
    
    # Save SVG file
    with open('data/presplash.svg', 'w') as f:
        f.write(svg_content)
    
    print("✅ Splash screen SVG generated successfully!")
    print("  - data/presplash.svg")
    print("\nNote: To convert to PNG, you can use:")
    print("  - Online converter: https://cloudconvert.com/svg-to-png")
    print("  - Command line: inkscape -w 720 -h 1280 data/presplash.svg -o data/presplash.png")
    print("  - Or any image editing software that supports SVG")

if __name__ == '__main__':
    create_splash_svg()