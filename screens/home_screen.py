from kivy.uix.screenmanager import Screen
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.app import App

class HomeScreen(Screen):
    def __init__(self, **kwargs):
        super(HomeScreen, self).__init__(**kwargs)
        layout = BoxLayout(orientation='vertical', spacing=15, padding=30)

        label = Label(text="Monitor de Crisis Tiroidea", font_size=24, size_hint=(1, 0.2))

        btn_registro = Button(text="Registrarse", size_hint=(1, 0.2))
        btn_login = Button(text="Iniciar sesión", size_hint=(1, 0.2))
        btn_salir = Button(text="Salir de la aplicación", size_hint=(1, 0.2), on_press=self.salir_app)

        btn_registro.bind(on_press=self.ir_a_registro)
        btn_login.bind(on_press=self.ir_a_monitor)

        layout.add_widget(label)
        layout.add_widget(btn_registro)
        layout.add_widget(btn_login)
        layout.add_widget(btn_salir)

        self.add_widget(layout)

    def ir_a_monitor(self, instance):
        self.manager.current = "monitor"

    def salir_app(self, instance):
        App.get_running_app().stop()

    def no_implementado(self, instance):
        print("Funcionalidad de registro aún no implementada.")

    def ir_a_registro(self, instance):
        self.manager.current = "register"

