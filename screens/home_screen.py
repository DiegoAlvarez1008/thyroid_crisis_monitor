from kivy.uix.screenmanager import Screen
from kivy.uix.label import Label

class HomeScreen(Screen):
    def __init__(self, **kwargs):
        super(HomeScreen, self).__init__(**kwargs)
        self.add_widget(Label(text="Bienvenido al Monitor de Crisis Tiroidea"))
