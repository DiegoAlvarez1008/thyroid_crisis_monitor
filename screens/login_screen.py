# screens/login_screen.py

from kivy.uix.screenmanager import Screen
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.label import Label

from utils.storage import iniciar_sesion

class LoginScreen(Screen):
    def __init__(self, **kwargs):
        super(LoginScreen, self).__init__(**kwargs)
        self.layout = BoxLayout(orientation='vertical', spacing=10, padding=20)

        self.dni_input = TextInput(hint_text="DNI (8 dígitos)", input_filter="int")
        self.password_input = TextInput(hint_text="Contraseña", password=True)

        self.msg_label = Label(text="", font_size=14)

        btn_login = Button(text="Iniciar sesión", on_press=self.iniciar_sesion)
        btn_volver = Button(text="Volver", on_press=self.volver_inicio)

        self.layout.add_widget(Label(text="Iniciar Sesión", font_size=20))
        self.layout.add_widget(self.dni_input)
        self.layout.add_widget(self.password_input)
        self.layout.add_widget(btn_login)
        self.layout.add_widget(btn_volver)
        self.layout.add_widget(self.msg_label)

        self.add_widget(self.layout)

    def iniciar_sesion(self, instance):
        dni = self.dni_input.text.strip()
        password = self.password_input.text.strip()

        if not dni or not password:
            self.msg_label.text = "Ingrese DNI y contraseña."
            return

        exito, mensaje = iniciar_sesion(dni, password)
        self.msg_label.text = mensaje
        if exito:
            # Aquí puedes dirigir a la pantalla de monitoreo
            self.manager.current = "monitor"

    def volver_inicio(self, instance):
        self.manager.current = "home"
