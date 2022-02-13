from kivy.app import App
from kivy.uix.label import Label
from kivy.core.window import Window
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
import os
os.environ['KIVY_GL_BACKEND'] = 'angle_sdl2'


Window.size = (1080, 1920)
Window.title = "App"


class Container(BoxLayout):
    pass


class MainApp(App):
    def build(self):
        return Container()


if __name__ == "__main__":
    MainApp().run()

