# Proyecto: Monitor de Crisis Tiroidea

Este proyecto es un prototipo funcional para detectar signos tempranos de crisis tiroidea en pacientes con hipertensión mediante sensores fisiológicos y evaluación cognitiva.

## Estructura del Proyecto

- `main.py`: punto de entrada de la app.
- `screens/`: contiene las pantallas de la app (UI).
- `utils/`: lógica médica, puntuación y procesamiento.
- `sensors/`: conexión con hardware (ESP32).
- `database/`: almacenamiento local (JSON o SQLite).
- `models/`: modelos ML entrenados (TFLite).
- `ml_training/`: notebooks para entrenar modelos.
- `assets/`: íconos, sonidos o imágenes.

## Requisitos

- Python 3.10+
- Kivy (`pip install kivy`)
