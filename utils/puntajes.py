# utils/puntajes.py
def evaluar_estado(puntuacion):
    """Evalúa el estado del paciente en función de los parámetros."""
    if puntuacion >= 45:
        return "critico" # Estado crítico porque se el puntaje comienza con una puntuación de 30 en la escala
    elif puntuacion >= 26 and puntuacion <= 44:
        return "preocupante"
    else:
        return "normal"


def calcular_puntaje_temp(temp):
    if 37.2 <= temp <= 37.7:
        return 5
    elif 37.8 <= temp <= 38.2:
        return 10
    elif 38.3 <= temp <= 38.8:
        return 15
    elif 38.9 <= temp <= 39.3:
        return 20
    elif 39.4 <= temp <= 39.9:
        return 25
    elif temp >= 40.0:
        return 30
    else:
        return 0


def calcular_puntaje_fc(fc):
    if 90 <= fc <= 99:
        return 5
    elif 100 <= fc <= 109:
        return 10
    elif 110 <= fc <= 119:
        return 15
    elif 120 <= fc <= 129:
        return 20
    elif 130 <= fc <= 139:
        return 25
    elif fc >= 140:
        return 30
    else:
        return 0


def calcular_puntaje_test(tiempo_respuesta, respuesta_correcta):
    if not respuesta_correcta:
        return 10  # Penalización por error

    if tiempo_respuesta < 3:
        return 0
    elif tiempo_respuesta < 6:
        return 5
    else:
        return 10


def calcular_puntaje_total(temp, fc, tiempo_respuesta, respuesta_correcta):
    puntaje_temp = calcular_puntaje_temp(temp)
    puntaje_fc = calcular_puntaje_fc(fc)
    puntaje_test = calcular_puntaje_test(tiempo_respuesta, respuesta_correcta)
    return puntaje_temp + puntaje_fc + puntaje_test
