from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen
from screens.home_screen import HomeScreen

class ThyroidApp(App):
    def build(self):
        sm = ScreenManager()
        sm.add_widget(HomeScreen(name="home"))
        return sm

if __name__ == "__main__":
    ThyroidApp().run()
