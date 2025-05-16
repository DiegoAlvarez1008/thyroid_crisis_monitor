from kivy.app import App
from kivy.uix.screenmanager import ScreenManager
from screens.home_screen import HomeScreen
from screens.monitor_screen import MonitorScreen
from screens.test_cognitive_screen import TestCognitiveScreen
from screens.register_screen import RegisterScreen

class ThyroidApp(App):
    def build(self):
        sm = ScreenManager()
        sm.add_widget(HomeScreen(name="home"))
        sm.add_widget(MonitorScreen(name="monitor"))
        sm.add_widget(TestCognitiveScreen(name="test"))
        sm.add_widget(RegisterScreen(name="register"))
        return sm

if __name__ == "__main__":
    ThyroidApp().run()

