from kivy.app import App
from kivy.uix.label import *
from kivy.core.window import Window
from kivy.uix.boxlayout import BoxLayout


Window.size = (1080, 1920)
Window.title = "App"


class schoolApp(App):
    def build(self):
        box = BoxLayout()
        label = Label("bruh")

        return label


if __name__ == "__main__":
    schoolApp().run()