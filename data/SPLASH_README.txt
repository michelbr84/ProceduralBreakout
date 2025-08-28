SPLASH SCREEN SETUP FOR PROCEDURAL BREAKOUT
===========================================

To add a splash screen for the Android app:

1. Convert the provided presplash.svg to PNG format:
   - Recommended size: 720x1280 pixels (9:16 aspect ratio)
   - Name it "presplash.png"
   - Place it in this 'data' directory

2. The splash screen is already configured in buildozer.spec with:
   - Background color: #1E1E28 (dark gray matching the game)
   - Image file: data/presplash.png

Splash Screen Design (in presplash.svg):
- Game title: "PROCEDURAL BREAKOUT"
- Colorful blocks decoration
- White ball
- Gray paddle
- "Loading..." text
- Dark background

To convert SVG to PNG:
- Online: https://cloudconvert.com/svg-to-png
- Command line: inkscape -w 720 -h 1280 presplash.svg -o presplash.png
- Any image editor that supports SVG (GIMP, Photoshop, etc.)

The splash screen will be displayed automatically when the app starts on Android.