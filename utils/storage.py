import os
import json

DB_PATH = "database/user_data.json"

def cargar_datos_usuario():
    """Carga los datos de usuario desde el archivo JSON."""
    if os.path.exists(DB_PATH):
        with open(DB_PATH, "r") as f:
            return json.load(f)
    return {}

def guardar_datos_usuario(datos):
    """Guarda el diccionario completo de usuarios."""
    with open(DB_PATH, "w") as f:
        json.dump(datos, f, indent=4)

def registrar_usuario(username, password, phone, emergency):
    """Registra un nuevo usuario si no está duplicado."""
    datos = cargar_datos_usuario()

    if username in datos:
        return False, "Usuario ya registrado."

    datos[username] = {
        "username": username,
        "password": password,
        "telefono": phone,
        "emergencia": emergency
    }

    guardar_datos_usuario(datos)
    return True, "Registro exitoso. Puedes iniciar sesión."
