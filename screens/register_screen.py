from kivy.uix.screenmanager import Screen
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.label import Label
from utils.storage import registrar_usuario
import json
import os

class RegisterScreen(Screen):
    def __init__(self, **kwargs):
        super(RegisterScreen, self).__init__(**kwargs)
        self.layout = BoxLayout(orientation='vertical', spacing=10, padding=20)

        self.username_input = TextInput(hint_text="Nombre de usuario")
        self.password_input = TextInput(hint_text="Contraseña", password=True)
        self.phone_input = TextInput(hint_text="Teléfono del usuario")
        self.emergency_input = TextInput(hint_text="Teléfono de contacto de emergencia")

        self.msg_label = Label(text="", font_size=14)

        btn_registrar = Button(text="Registrar", on_press=self.registrar_usuario)
        btn_volver = Button(text="Volver", on_press=self.volver_inicio)

        self.layout.add_widget(Label(text="Registro de Usuario", font_size=20))
        self.layout.add_widget(self.username_input)
        self.layout.add_widget(self.password_input)
        self.layout.add_widget(self.phone_input)
        self.layout.add_widget(self.emergency_input)
        self.layout.add_widget(btn_registrar)
        self.layout.add_widget(btn_volver)
        self.layout.add_widget(self.msg_label)

        self.add_widget(self.layout)

    def registrar_usuario(self, instance):
        username = self.username_input.text.strip()
        password = self.password_input.text.strip()
        phone = self.phone_input.text.strip()
        emergency = self.emergency_input.text.strip()

        if not all([username, password, phone, emergency]):
            self.msg_label.text = "Completa todos los campos."
            return

        user_data = {
            "username": username,
            "password": password,
            "telefono": phone,
            "emergencia": emergency
        }

        exito, mensaje = registrar_usuario(username, password, phone, emergency)
        self.msg_label.text = mensaje
        if exito:
            self.username_input.text = ""
            self.password_input.text = ""
            self.phone_input.text = ""
            self.emergency_input.text = ""

        

    def volver_inicio(self, instance):
        self.manager.current = "home"
