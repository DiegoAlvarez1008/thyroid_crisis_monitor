# utils/storage.py

import os
import json
import re

DB_PATH = "database/user_data.json"

EMAIL_REGEX = r"(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)"
PHONE_REGEX = r"^\+?\d{7,15}$"  # mínimo 7 dígitos, opcional '+' al inicio
DNI_REGEX   = r"^\d{8}$"         # asumiendo DNI de 8 dígitos (ajusta según tu país)

def cargar_usuarios():
    """Devuelve el diccionario completo de usuarios (clave = DNI)."""
    if os.path.exists(DB_PATH):
        with open(DB_PATH, "r") as f:
            try:
                return json.load(f)
            except json.JSONDecodeError:
                return {}
    return {}

def guardar_usuarios(usuarios: dict):
    """Guarda el diccionario completo de usuarios en JSON."""
    carpeta = os.path.dirname(DB_PATH)
    if carpeta and not os.path.exists(carpeta):
        os.makedirs(carpeta)
    with open(DB_PATH, "w") as f:
        json.dump(usuarios, f, indent=4)

def validar_dni(dni: str) -> bool:
    """Verifica formato de DNI (8 dígitos)."""
    return re.fullmatch(DNI_REGEX, dni) is not None

def validar_email(email: str) -> bool:
    """Verifica formato de email."""
    return re.fullmatch(EMAIL_REGEX, email) is not None

def validar_telefono(phone: str) -> bool:
    """Verifica formato de teléfono (7–15 dígitos, opcional '+')."""
    return re.fullmatch(PHONE_REGEX, phone) is not None

def registrar_usuario(dni: str, nombre: str, email: str, telefono: str, password: str) -> tuple[bool, str]:
    """
    Registra un usuario nuevo según DNI. 
    Devuelve (True, mensaje) o (False, mensaje_de_error).
    """

    usuarios = cargar_usuarios()

    # 1) Validar formato de DNI
    if not validar_dni(dni):
        return False, "DNI inválido (debe ser 8 dígitos)."

    # 2) Verificar si el DNI ya existe
    if dni in usuarios:
        return False, "Ya existe un usuario con ese DNI."

    # 3) Validar email y que no esté en uso
    if not validar_email(email):
        return False, "Formato de email inválido."
    # verificar unicidad del email
    for otra_dni, datos in usuarios.items():
        if datos.get("email", "").lower() == email.lower():
            return False, "El correo ya está en uso."

    # 4) Validar teléfono y que no esté en uso
    if not validar_telefono(telefono):
        return False, "Formato de teléfono inválido."
    for otra_dni, datos in usuarios.items():
        if datos.get("telefono", "") == telefono:
            return False, "El número de teléfono ya está en uso."

    # 5) Registrar el usuario
    usuarios[dni] = {
        "dni": dni,
        "nombre": nombre,
        "email": email,
        "telefono": telefono,
        "password": password
    }
    guardar_usuarios(usuarios)
    return True, "Registro exitoso. Ahora puede iniciar sesión con su DNI y contraseña."

def iniciar_sesion(dni: str, password: str) -> tuple[bool, str]:
    """
    Verifica que el DNI exista y que la contraseña coincida.
    Devuelve (True, mensaje_exito) o (False, mensaje_error).
    """
    usuarios = cargar_usuarios()

    # 1) Verificar existencia del DNI
    if dni not in usuarios:
        return False, "No existe usuario con ese DNI."

    datos = usuarios[dni]
    # 2) Verificar contraseña
    if datos.get("password") != password:
        return False, "Contraseña incorrecta."

    return True, f"Bienvenido, {datos.get('nombre')}!"
