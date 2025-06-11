from kivy.uix.screenmanager import Screen
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.togglebutton import ToggleButton
import json
import os
import re

DATA_FILE = "data/users.json"

class RegisterScreen(Screen):
    def __init__(self, **kwargs):
        super(RegisterScreen, self).__init__(**kwargs)
        self.layout = BoxLayout(orientation="vertical", spacing=10, padding=20)

        self.msg_error = Label(text="", color=(1, 0, 0, 1), font_size=14)

        self.input_dni = TextInput(hint_text="DNI (8 dígitos)", input_filter='int', multiline=False)
        self.input_nombre = TextInput(hint_text="Nombre completo", multiline=False)
        self.input_correo = TextInput(hint_text="Correo electrónico", multiline=False)
        self.input_telefono = TextInput(hint_text="Número de celular", input_filter='int', multiline=False)
        
        self.input_password = TextInput(hint_text="Contraseña", password=True, multiline=False)
        self.input_repetir_password = TextInput(hint_text="Repetir contraseña", password=True, multiline=False)

        self.toggle_password = ToggleButton(text="Mostrar contraseña", size_hint_y=None, height=40)
        self.toggle_password.bind(on_press=self.toggle_password_visibility)

        self.btn_registrar = Button(text="Registrarse", on_press=self.registrar_usuario)
        btn_volver = Button(text="Volver", on_press=self.volver_inicio)

        self.layout.add_widget(self.input_dni)
        self.layout.add_widget(self.input_nombre)
        self.layout.add_widget(self.input_correo)
        self.layout.add_widget(self.input_telefono)
        self.layout.add_widget(self.input_password)
        self.layout.add_widget(self.input_repetir_password)
        self.layout.add_widget(self.toggle_password)
        self.layout.add_widget(self.btn_registrar)
        self.layout.add_widget(btn_volver)
        self.layout.add_widget(self.msg_error)

        self.add_widget(self.layout)

    def toggle_password_visibility(self, instance):
    # Invertir visibilidad
        current_state = self.input_password.password
        self.input_password.password = not current_state
        self.input_repetir_password.password = not current_state
        instance.text = "Ocultar contraseña" if not current_state else "Mostrar contraseña"


    def registrar_usuario(self, instance):
        dni = self.input_dni.text.strip()
        nombre = self.input_nombre.text.strip()
        correo = self.input_correo.text.strip()
        telefono = self.input_telefono.text.strip()
        password = self.input_password.text.strip()
        repetir_password = self.input_repetir_password.text.strip()

        # Validaciones de campos
        if len(dni) != 8 or not dni.isdigit():
            self.msg_error.text = "El DNI debe tener 8 dígitos."
            return
        if len(telefono) != 9 or not telefono.isdigit():
            self.msg_error.text = "El número de celular debe tener 9 dígitos."
            return
        if not re.match(r"[^@]+@[^@]+\.[^@]+", correo):
            self.msg_error.text = "Correo electrónico inválido."
            return
        if password != repetir_password:
            self.msg_error.text = "Las contraseñas no coinciden."
            return
        if not self.validar_password(password):
            self.msg_error.text = "La contraseña debe tener mayúscula, minúscula y número."
            return

        # Cargar datos actuales
        if os.path.exists(DATA_FILE):
            with open(DATA_FILE, "r") as f:
                try:
                    usuarios = json.load(f)
                except json.JSONDecodeError:
                    usuarios = []
        else:
            usuarios = []

        # Validar si ya existe el DNI, correo o celular
        for usuario in usuarios:
            if usuario["dni"] == dni:
                self.msg_error.text = "El DNI ya está registrado."
                return
            if usuario["correo"] == correo:
                self.msg_error.text = "El correo ya está en uso."
                return
            if usuario["telefono"] == telefono:
                self.msg_error.text = "El número de celular ya está en uso."
                return

        # Guardar nuevo usuario
        usuarios.append({
            "dni": dni,
            "nombre": nombre,
            "correo": correo,
            "telefono": telefono,
            "password": password
        })

        os.makedirs(os.path.dirname(DATA_FILE), exist_ok=True)

        with open(DATA_FILE, "w") as f:
            json.dump(usuarios, f, indent=4)

        self.msg_error.color = (0, 1, 0, 1)
        self.msg_error.text = "Registro exitoso. Puedes iniciar sesión."
        self.limpiar_campos()

    def limpiar_campos(self):
        self.input_dni.text = ""
        self.input_nombre.text = ""
        self.input_correo.text = ""
        self.input_telefono.text = ""
        self.input_password.text = ""
        self.input_repetir_password.text = ""

    def validar_password(self, password):
        return (
            len(password) >= 8 and
            re.search(r"[A-Z]", password) and
            re.search(r"[a-z]", password) and
            re.search(r"\d", password)
        )
    
    def volver_inicio(self, instance):
        self.manager.current = "home"
        self.limpiar_campos()   # Se limpian los cuadros de texto al volver a la pantalla de inicio

