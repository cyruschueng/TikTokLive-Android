class Models:
    from kivy.app import App
    from kivymd.app import MDApp
    Liveapp = MDApp
    from kivy.uix.boxlayout import BoxLayout
    from kivy.lang.builder import Builder
    from kivy.core.window import Window
    from kivy.animation import Animation
    from kivy.metrics import sp
    from kivy.uix.widget import Widget
    from kivy.clock import Clock

class ConfigMyapp:
    def size_myscreen(   
        self
    ):
        models = Models()
        models.Window.size = (480*0.5, 800*0.5)