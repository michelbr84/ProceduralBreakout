from kivy.app import App
from kivy.uix.label import Label


class ProceduralBreakoutApp(App):
    def build(self):
        return Label(text='Procedural Breakout - Android Test')

if __name__ == '__main__':
    ProceduralBreakoutApp().run()
