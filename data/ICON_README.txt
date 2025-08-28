ICON SETUP FOR PROCEDURAL BREAKOUT
==================================

To add a custom icon for the Android app:

1. Create or find a PNG image (recommended size: 512x512 pixels)
2. Name it "icon.png" 
3. Place it in this 'data' directory

Icon Design Suggestions:
- Include colorful blocks at the top
- A white ball in the middle
- A paddle at the bottom
- Dark background (matching the game's color scheme)

The icon is already configured in buildozer.spec and will be used automatically when building the APK.

Alternative: Use the provided Python scripts to generate an icon:
- generate_icon.py (requires Pillow/PIL)
- generate_icon_simple.py (requires matplotlib)